# -*- coding: utf-8 -*-
"""
Distance IR Plugin
Copyright (C) 2011-2012 Olaf Lüke <olaf@tinkerforge.com>
Copyright (C) 2014 Matthias Bolte <matthias@tinkerforge.com>

distance.py: Distance IR Plugin Implementation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from brickv.plugin_system.plugin_base import PluginBase
from brickv.plot_widget import PlotWidget
from brickv.bindings import ip_connection
from brickv.bindings.bricklet_distance_ir import BrickletDistanceIR
from brickv.async_call import async_call
from brickv.utils import get_main_window

from PyQt4.QtGui import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QApplication, QPolygonF, QMessageBox
from PyQt4.QtCore import pyqtSignal, Qt, QPointF
from PyQt4.Qwt5 import QwtSpline

import os
import sys

class AnalogLabel(QLabel):
    def setText(self, text):
        text = "Analog value: " + text
        super(AnalogLabel, self).setText(text)

class DistanceLabel(QLabel):
    def setText(self, text):
        text = "Distance: " + text + " cm"
        super(DistanceLabel, self).setText(text)

class DistanceIR(PluginBase):
    NUM_VALUES = 128
    DIVIDER = 2**12/NUM_VALUES

    qtcb_distance = pyqtSignal(int)
    qtcb_analog = pyqtSignal(int)

    def __init__(self, *args):
        PluginBase.__init__(self, 'Distance IR Bricklet', BrickletDistanceIR, *args)

        self.dist = self.device

        self.qtcb_distance.connect(self.cb_distance)
        self.dist.register_callback(self.dist.CALLBACK_DISTANCE,
                                    self.qtcb_distance.emit)

        self.qtcb_analog.connect(self.cb_analog)
        self.dist.register_callback(self.dist.CALLBACK_ANALOG_VALUE,
                                    self.qtcb_analog.emit)

        self.analog_value = 0

        self.distance_label = DistanceLabel('Distance: ')
        self.analog_label = AnalogLabel('Analog value: ')
        self.sample_layout = QHBoxLayout()
        self.sample_label = QLabel('Sample Points:')
        self.sample_edit = QLineEdit()
        self.sample_file = QPushButton("File...")
        self.sample_save = QPushButton("Save")

        self.sample_file.clicked.connect(self.sample_file_clicked)
        self.sample_save.clicked.connect(self.sample_save_clicked)

        self.sample_layout.addWidget(self.sample_label)
        self.sample_layout.addWidget(self.sample_edit)
        self.sample_layout.addWidget(self.sample_file)
        self.sample_layout.addWidget(self.sample_save)

        self.current_value = None

        plot_list = [['', Qt.red, self.get_current_value]]
        self.plot_widget = PlotWidget('Distance [cm]', plot_list)

        layout_h1 = QHBoxLayout()
        layout_h1.addStretch()
        layout_h1.addWidget(self.distance_label)
        layout_h1.addStretch()

        layout_h2 = QHBoxLayout()
        layout_h2.addStretch()
        layout_h2.addWidget(self.analog_label)
        layout_h2.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(layout_h1)
        layout.addLayout(layout_h2)
        layout.addWidget(self.plot_widget)
        layout.addLayout(self.sample_layout)

    def start(self):
        async_call(self.dist.get_distance, None, self.cb_distance, self.increase_error_count)
        async_call(self.dist.set_distance_callback_period, 100, None, self.increase_error_count)
        async_call(self.dist.set_analog_value_callback_period, 100, None, self.increase_error_count)

        self.plot_widget.stop = False

    def stop(self):
        async_call(self.dist.set_distance_callback_period, 0, None, self.increase_error_count)
        async_call(self.dist.set_analog_value_callback_period, 0, None, self.increase_error_count)

        self.plot_widget.stop = True

    def destroy(self):
        pass

    def get_url_part(self):
        return 'distance_ir'

    @staticmethod
    def has_device_identifier(device_identifier):
        return device_identifier == BrickletDistanceIR.DEVICE_IDENTIFIER

    def sample_file_clicked(self):
        last_dir = ''
        if len(self.sample_edit.text()) > 0:
            last_dir = os.path.dirname(os.path.realpath(unicode(self.sample_edit.text().toUtf8(), 'utf-8')))
        file_name = QFileDialog.getOpenFileName(self,
                                                "Open Sample Point file",
                                                last_dir,
                                                "")
        if len(file_name) > 0:
            self.sample_edit.setText(file_name)

    def sample_interpolate(self, x, y):
        spline = QwtSpline()
        points = QPolygonF()

        for point in zip(x, y):
            points.append(QPointF(*point))

        spline.setSplineType(QwtSpline.Natural)
        spline.setPoints(points)

        px = range(0, 2**12, DistanceIR.DIVIDER)
        py = []

        for X in px:
            py.append(spline.value(X))

        for i in range(x[0]/DistanceIR.DIVIDER):
            py[i] = y[0]

        for i in range(x[-1]/DistanceIR.DIVIDER, 2**12/DistanceIR.DIVIDER):
            py[i] = y[-1]

        for i in range(len(py)):
            if py[i] > y[0]:
                py[i] = y[0]
            if py[i] < y[-1]:
                py[i] = y[-1]

        try:
            old_text = self.sample_edit.text()
            for i in range(DistanceIR.NUM_VALUES):
                value = int(round(py[i]*100))
                self.dist.set_sampling_point(i, value)
                self.sample_edit.setText("Writing sample point, value: " +  str((i, value)))

                QApplication.processEvents()
            self.sample_edit.setText(old_text)
        except ip_connection.Error:
            return

    def sample_save_clicked(self):
        x = []
        y = []
        text = self.sample_edit.text()
        text = unicode(text.toUtf8(), 'utf-8').encode(sys.getfilesystemencoding())

        with open(text, 'rb') as f:
            for line in f:
                c = line.find('#')
                if c != -1:
                    line = line[:c]

                line = line.strip()

                if line.startswith('\xEF\xBB\xBF'): # strip UTF-8 BOM, Internet Explorer adds it to text files
                    line = line[3:]

                if len(line) == 0:
                    continue

                if ':' not in line:
                    QMessageBox.critical(get_main_window(), "Sample points",
                                         "Sample points file is malformed (error code 1)",
                                         QMessageBox.Ok)
                    return

                s = line.split(':')

                if len(s) != 2:
                    QMessageBox.critical(get_main_window(), "Sample points",
                                         "Sample points file is malformed (error code 2)",
                                         QMessageBox.Ok)
                    return

                try:
                    x.append(int(s[1]))
                    y.append(int(s[0]))
                except:
                    QMessageBox.critical(get_main_window(), "Sample points",
                                         "Sample points file is malformed (error code 3)",
                                         QMessageBox.Ok)
                    return

        self.sample_interpolate(x, y)

    def get_current_value(self):
        return self.current_value

    def cb_distance(self, distance):
        self.current_value = distance/10.0
        self.distance_label.setText(str(distance/10.0))

    def cb_analog(self, value):
        self.analog_value = value
        self.analog_label.setText(str(self.analog_value))
