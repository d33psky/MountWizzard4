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

# external packages
from PyQt5.QtCore import QThreadPool, QObject, pyqtSignal
from indibase.indiBase import Device, Client

# local import
from logic.cover.coverIndi import CoverIndi
from logic.cover.cover import CoverSignals


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    class Test(QObject):
        threadPool = QThreadPool()
        message = pyqtSignal(str, int)
    global app
    app = CoverIndi(app=Test(), signals=CoverSignals(), data={})

    yield


def test_setUpdateConfig_1():
    app.deviceName = ''
    suc = app.setUpdateConfig('test')
    assert not suc


def test_setUpdateConfig_2():
    app.deviceName = 'test'
    app.device = None
    suc = app.setUpdateConfig('test')
    assert not suc


def test_setUpdateConfig_3():
    app.deviceName = 'test'
    app.device = Device()
    with mock.patch.object(app.device,
                           'getNumber',
                           return_value={'Test': 1}):
        suc = app.setUpdateConfig('test')
        assert not suc


def test_setUpdateConfig_4():
    app.deviceName = 'test'
    app.device = Device()
    app.UPDATE_RATE = 1
    with mock.patch.object(app.device,
                           'getNumber',
                           return_value={'PERIOD': 1}):
        suc = app.setUpdateConfig('test')
        assert suc


def test_setUpdateConfig_5():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getNumber',
                           return_value={'PERIOD': 1}):
        with mock.patch.object(app.client,
                               'sendNewNumber',
                               return_value=False):
            suc = app.setUpdateConfig('test')
            assert not suc


def test_setUpdateConfig_6():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getNumber',
                           return_value={'PERIOD': 1}):
        with mock.patch.object(app.client,
                               'sendNewNumber',
                               return_value=True):
            suc = app.setUpdateConfig('test')
            assert suc


def test_updateText_1():
    app.device = None
    suc = app.updateText('test', 'test')
    assert not suc


def test_updateText_2():
    app.device = Device()
    app.deviceName = 'test'
    with mock.patch.object(app.device,
                           'getText',
                           return_value={'Cover': 'OPEN'}):
        suc = app.updateText('test', 'CAP_PARK')
        assert suc


def test_updateText_3():
    app.device = Device()
    app.deviceName = 'test'
    with mock.patch.object(app.device,
                           'getText',
                           return_value={'Cover': 'CLOSED'}):
        suc = app.updateText('test', 'CAP_PARK')
        assert suc


def test_updateText_4():
    app.device = Device()
    app.deviceName = 'test'
    with mock.patch.object(app.device,
                           'getText',
                           return_value={'Cover': 'test'}):
        suc = app.updateText('test', 'CAP_PARK')
        assert suc


def test_closeCover_1():
    app.deviceName = 'test'
    app.device = None
    suc = app.closeCover()
    assert not suc


def test_closeCover_2():
    app.deviceName = 'test'
    app.device = Device()
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'Test': 1}):
        suc = app.closeCover()
        assert not suc


def test_closeCover_3():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'On',
                                         'UNPARK': 'Off'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=False):
            suc = app.closeCover()
            assert not suc


def test_closeCover_4():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'On',
                                         '': 'Off'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=False):
            suc = app.closeCover()
            assert not suc


def test_closeCover_5():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'Off',
                                         'UNPARK': 'On'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=True):
            suc = app.closeCover()
            assert suc


def test_openCover_1():
    app.deviceName = 'test'
    app.device = None
    suc = app.openCover()
    assert not suc


def test_openCover_2():
    app.deviceName = 'test'
    app.device = Device()
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'Test': 1}):
        suc = app.openCover()
        assert not suc


def test_openCover_3():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'On',
                                         'UNPARK': 'Off'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=False):
            suc = app.openCover()
            assert not suc


def test_openCover_4():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'On',
                                         '': 'Off'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=False):
            suc = app.openCover()
            assert not suc


def test_openCover_5():
    app.deviceName = 'test'
    app.device = Device()
    app.client = Client()
    app.UPDATE_RATE = 0
    with mock.patch.object(app.device,
                           'getSwitch',
                           return_value={'PARK': 'Off',
                                         'UNPARK': 'On'}):
        with mock.patch.object(app.client,
                               'sendNewSwitch',
                               return_value=True):
            suc = app.openCover()
            assert suc


def test_haltCover_1():
    app.deviceName = 'test'
    app.device = None
    suc = app.haltCover()
    assert not suc
