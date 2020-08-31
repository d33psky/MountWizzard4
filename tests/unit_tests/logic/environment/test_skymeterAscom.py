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
# written in python3 , (c) 2019, 2020 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries
import pytest
import platform

# external packages
from PyQt5.QtCore import QThreadPool, QObject, pyqtSignal

# local import
from logic.environment.skymeterAscom import SkymeterAscom
from logic.environment.skymeter import SkymeterSignals

if not platform.system() == 'Windows':
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    class Test1:
        Name = 'test'
        DriverVersion = '1'
        DriverInfo = 'test1'
        temperature = 10
        skyquality = 21.00

    class Test(QObject):
        threadPool = QThreadPool()
        message = pyqtSignal(str, int)

    global app

    app = SkymeterAscom(app=Test(), signals=SkymeterSignals(), data={})
    app.client = Test1()
    yield


def test_getInitialConfig_1():
    suc = app.getInitialConfig()
    assert suc


def test_workerPollData_1():
    app.deviceConnected = False
    suc = app.workerPollData()
    assert not suc


def test_workerPollData_2():
    app.deviceConnected = True
    suc = app.workerPollData()
    assert suc
