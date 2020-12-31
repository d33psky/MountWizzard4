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
# Licence APL2.0
#
###########################################################
# standard libraries
import pytest
import unittest.mock as mock
import platform

# external packages
import PyQt5
from PyQt5.QtCore import QThreadPool, QObject, pyqtSignal

# local import
from logic.cover.coverAscom import CoverAscom
from logic.cover.cover import CoverSignals

if not platform.system() == 'Windows':
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    class Test1:
        Name = 'test'
        DriverVersion = '1'
        DriverInfo = 'test1'
        CoverState = 1

        @staticmethod
        def CloseCover():
            return True

        @staticmethod
        def OpenCover():
            return True

        @staticmethod
        def HaltCover():
            return True

    class Test(QObject):
        threadPool = QThreadPool()
        message = pyqtSignal(str, int)

    global app
    with mock.patch.object(PyQt5.QtCore.QTimer,
                           'start'):
        app = CoverAscom(app=Test(), signals=CoverSignals(), data={})
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


def test_workerPollData_3():
    app.deviceConnected = True
    app.client.coverstate = 1
    suc = app.workerPollData()
    assert suc


def test_workerPollData_4():
    app.deviceConnected = True
    app.client.coverstate = 0
    suc = app.workerPollData()
    assert suc


def test_closeCover_1():
    app.deviceConnected = False
    suc = app.closeCover()
    assert not suc


def test_closeCover_2():
    app.deviceConnected = True
    suc = app.closeCover()
    assert suc


def test_closeCover_3():
    app.deviceConnected = True
    suc = app.closeCover()
    assert suc


def test_openCover_1():
    app.deviceConnected = False
    suc = app.openCover()
    assert not suc


def test_openCover_2():
    app.deviceConnected = True
    suc = app.openCover()
    assert suc


def test_openCover_3():
    app.deviceConnected = True
    suc = app.openCover()
    assert suc


def test_haltCover_1():
    app.deviceConnected = False
    suc = app.haltCover()
    assert not suc


def test_haltCover_2():
    app.deviceConnected = True
    suc = app.haltCover()
    assert suc


def test_haltCover_3():
    app.deviceConnected = True
    suc = app.haltCover()
    assert suc
