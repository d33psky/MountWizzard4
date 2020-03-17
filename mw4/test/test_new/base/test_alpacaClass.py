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
# Python  v3.7.5
#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
# standard libraries
from unittest import mock

# external packages
import pytest
import requests
import requests.exceptions as req
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

# local import
from mw4.base.alpacaClass import AlpacaClass


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    class Test(QObject):
        threadPool = QThreadPool()
        message = pyqtSignal(str, int)
    global app
    app = AlpacaClass(app=Test())

    yield

    app.threadPool.waitForDone(1000)
    del app


def test_properties_1():
    app.host = ('localhost', 11111)
    app.name = 'test'
    app.name = 'test:2'
    app.apiVersion = 1
    app.protocol = 1


def test_properties_2():
    host = app.host
    assert host == ('localhost', 11111)
    assert app.name == ''
    assert app.apiVersion == 1
    assert app.protocol == 'http'


def test_getInitialConfig_1():
    with mock.patch.object(app.client,
                           'connected',
                           return_value=False):
        suc = app.getInitialConfig()
        assert not suc


def test_getInitialConfig_2():
    app.serverConnected = False
    app.deviceConnected = False
    with mock.patch.object(app.client,
                           'connected',
                           return_value=True):
        suc = app.getInitialConfig()
        assert suc
        assert app.serverConnected
        assert app.deviceConnected
        assert app.data['DRIVER_INFO.DRIVER_NAME'] is None
        assert app.data['DRIVER_INFO.DRIVER_VERSION'] is None
        assert app.data['DRIVER_INFO.DRIVER_EXEC'] == ''


def test_startTimer():
    suc = app.startTimer()
    assert suc
    app.cycleData.stop()
    app.cycleDevice.stop()


def test_stopTimer():
    suc = app.stopTimer()
    assert suc


def test_dataEntry_1():
    app.data = {'YES': 0}

    res = app.dataEntry(None, 'YES')
    assert res
    assert 'YES' not in app.data


def test_dataEntry_2():
    app.data = {'YES': 0,
                'NO': 0}

    res = app.dataEntry(None, 'YES', 'NO')
    assert res
    assert 'YES' not in app.data
    assert 'NO' not in app.data


def test_dataEntry_3():
    app.data = {'YES': 0,
                'NO': 0}

    res = app.dataEntry(10, 'YES', 'NO')
    assert not res
    assert 'YES' in app.data
    assert 'NO' in app.data


def test_pollStatus_1():
    app.deviceConnected = True
    with mock.patch.object(app.client,
                           'connected',
                           return_value=False):
        suc = app.pollStatus()
        assert not suc
        assert not app.deviceConnected


def test_pollStatus_2():
    app.deviceConnected = False
    with mock.patch.object(app.client,
                           'connected',
                           return_value=True):
        suc = app.pollStatus()
        assert suc
        assert app.deviceConnected


def test_pollStatus_3():
    app.deviceConnected = True
    with mock.patch.object(app.client,
                           'connected',
                           return_value=True):
        suc = app.pollStatus()
        assert suc
        assert app.deviceConnected


def test_pollStatus_4():
    app.deviceConnected = False
    with mock.patch.object(app.client,
                           'connected',
                           return_value=False):
        suc = app.pollStatus()
        assert not suc
        assert not app.deviceConnected


def test_emitData():
    app.emitData()


def test_workerPollData():
    app.workerPollData()


def test_pollData_1():
    app.deviceConnected = False
    suc = app.pollData()
    assert not suc


def test_pollData_2():
    app.deviceConnected = True
    suc = app.pollData()
    assert suc


def test_startPollStatus():
    suc = app.startPollStatus()
    assert suc


def test_startCommunication():
    suc = app.startCommunication()
    assert suc


def test_stopCommunication():
    app.deviceConnected = True
    app.serverConnected = True
    suc = app.stopCommunication()
    assert suc
    assert not app.serverConnected
    assert not app.deviceConnected
