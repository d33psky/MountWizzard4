############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Python-based Tool for interaction with the 10micron mounts
# GUI with PyQT5 for python
#
# written in python3, (c) 2019-2021 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries
import sys
import unittest.mock as mock
import glob
import os

# external packages
import pytest
import PyQt5
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

# local import
from mw4 import loader


def test_main_1():
    class App:

        @staticmethod
        def installEventFilter(a):
            return

        @staticmethod
        def exec_():
            return 0

        @staticmethod
        def setWindowIcon(a):
            return 0

    class Splash:

        @staticmethod
        def showMessage(a):
            return

        @staticmethod
        def setValue(a):
            return

        @staticmethod
        def close():
            return

    files = glob.glob('tests/config/*.cfg')
    for f in files:
        os.remove(f)

    mwGlob = {'configDir': 'tests/config',
              'dataDir': 'tests/data',
              'tempDir': 'tests/temp',
              'imageDir': 'tests/image',
              'modelDir': 'tests/model',
              'workDir': 'mw4/test',
              'modeldata': '4.0',
              }
    with mock.patch.object(PyQt5.QtCore.QBasicTimer,
                           'start'):
        with mock.patch.object(PyQt5.QtCore.QTimer,
                               'start'):
            with mock.patch.object(loader,
                                   'QIcon'):
                with mock.patch.object(loader,
                                       'MyApp',
                                       return_value=App()):
                    with mock.patch.object(loader,
                                           'SplashScreen',
                                           return_value=Splash()):
                        with mock.patch.object(loader,
                                               'MountWizzard4'):
                            with mock.patch.object(loader,
                                                   'setupWorkDirs',
                                                   return_value=mwGlob):
                                with mock.patch.object(sys,
                                                       'exit'):
                                    with mock.patch.object(sys,
                                                           'excepthook'):
                                        with mock.patch.object(loader,
                                                               'QAwesomeTooltipEventFilter'):
                                            loader.main()
