# -*- coding: utf-8 -*-
"""
RED Plugin
Copyright (C) 2014-2015 Matthias Bolte <matthias@tinkerforge.com>

program_info_c_compile.py: Program C/C++ Compile Info Widget

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

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog
from brickv.plugin_system.plugins.red.ui_program_info_c_compile import Ui_ProgramInfoCCompile
import posixpath

class ProgramInfoCCompile(QDialog, Ui_ProgramInfoCCompile):
    def __init__(self, parent, script_manager, program):
        QDialog.__init__(self, parent)

        self.setupUi(self)
        self.setModal(True)

        self.script_manager  = script_manager
        self.program         = program
        self.script_instance = None

        self.rejected.connect(self.cancel_make_execution)
        self.button_make.clicked.connect(lambda: self.execute_make(None))
        self.button_clean.clicked.connect(lambda: self.execute_make('clean'))
        self.button_cancel.clicked.connect(self.cancel_make_execution)
        self.button_close.clicked.connect(self.reject)

        self.button_cancel.setEnabled(False)

    def log(self, message, bold=False, pre=False):
        if bold:
            self.edit_log.appendHtml(u'<b>{0}</b>'.format(Qt.escape(message)))
        elif pre:
            self.edit_log.appendHtml(u'<pre>{0}</pre>'.format(message))
        else:
            self.edit_log.appendPlainText(message)

        self.edit_log.verticalScrollBar().setValue(self.edit_log.verticalScrollBar().maximum())

    def execute_make(self, target): # target = None for default
        self.button_make.setEnabled(False)
        self.button_clean.setEnabled(False)
        self.button_cancel.setEnabled(True)

        # FIXME: it would be better to read the output incremental instead of
        #        waiting for make to exit and then display it in a burst
        def cb_make_helper(result):
            aborted = self.script_instance.abort
            self.script_instance = None

            if result != None:
                for s in result.stdout.rstrip().split('\n'):
                    self.log(s, pre=True)

                if result.exit_code != 0:
                    self.log('...error', bold=True)
                else:
                    self.log('...done')
            elif aborted:
                self.log('...canceled', bold=True)
            else:
                self.log('...error', bold=True)

            self.button_make.setEnabled(True)
            self.button_clean.setEnabled(True)
            self.button_cancel.setEnabled(False)

        if target != None:
            self.log('Executing make {0}...'.format(target))
        else:
            self.log('Executing make...')

        make_options      = self.program.cast_custom_option_value_list('c.make_options', unicode, [])
        working_directory = posixpath.join(self.program.root_directory, 'bin', self.program.working_directory)

        if target != None:
            make_options.append(target)

        self.script_instance = self.script_manager.execute_script('make_helper', cb_make_helper, [working_directory] + make_options,
                                                                  max_length=1024*1024, redirect_stderr_to_stdout=True,
                                                                  execute_as_user=True)

    def cancel_make_execution(self):
        script_instance = self.script_instance

        if script_instance == None:
            return

        self.button_make.setEnabled(True)
        self.button_clean.setEnabled(True)
        self.button_cancel.setEnabled(False)

        self.script_manager.abort_script(script_instance)
