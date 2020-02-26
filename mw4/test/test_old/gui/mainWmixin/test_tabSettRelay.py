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
import unittest.mock as mock
import pytest
# external packages
# local import
from mw4.test.test_old.setupQt import setupQt


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test
    app, spy, mwGlob, test = setupQt()
    yield


def test_initConfig_1():
    app.config['mainW'] = {}
    suc = app.mainW.initConfig()
    assert suc


def test_initConfig_2():
    del app.config['mainW']
    suc = app.mainW.initConfig()
    assert suc


def test_storeConfig_1():
    app.mainW.ui.relayDevice.setCurrentIndex(0)
    app.mainW.storeConfig()


def test_setupIcons():
    suc = app.mainW.setupIcons()
    assert suc


def test_setupRelayGui(qtbot):
    assert 8 == len(app.mainW.relayDropDowns)
    assert 8 == len(app.mainW.relayButtonTexts)
    assert 8 == len(app.mainW.relayButtons)
    for dropDown in app.mainW.relayDropDowns:
        val = dropDown.count()
        assert 2 == val


def test_toggleRelay_1(qtbot):
    app.mainW.ui.relayDevice.setCurrentIndex(0)
    with qtbot.waitSignal(app.message) as blocker:
        suc = app.mainW.relayButtonPressed()
        assert not suc
    assert ['Relay action cannot be performed', 2] == blocker.args


def test_toggleRelay_2(qtbot):
    app.mainW.ui.relayDevice.setCurrentIndex(1)
    with mock.patch.object(app.relay,
                           'switch',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.relayButtonPressed()
            assert not suc
        assert ['Relay action cannot be performed', 2] == blocker.args


def test_relayHost():
    app.mainW.ui.relayHost.setText('test')
    app.mainW.relayHost()

    assert app.relay.host == ('test', 80)


def test_relayUser():
    app.mainW.ui.relayUser.setText('test')
    app.mainW.relayUser()

    assert app.relay.user == 'test'


def test_relayPassword():
    app.mainW.ui.relayPassword.setText('test')
    app.mainW.relayPassword()

    assert app.relay.password == 'test'


def test_doRelayAction_1(qtbot):
    app.mainW.relayDropDowns[7].setCurrentIndex(0)
    with mock.patch.object(app.relay,
                           'switch',
                           return_value=False):
        suc = app.mainW.doRelayAction(7)
        assert not suc


def test_doRelayAction_2(qtbot):
    app.mainW.relayDropDowns[7].setCurrentIndex(0)
    with mock.patch.object(app.relay,
                           'switch',
                           return_value=True):
        suc = app.mainW.doRelayAction(7)
        assert suc


def test_doRelayAction_3(qtbot):
    app.mainW.relayDropDowns[7].setCurrentIndex(2)
    suc = app.mainW.doRelayAction(7)
    assert not suc


def test_doRelayAction_4(qtbot):
    app.mainW.relayDropDowns[7].setCurrentIndex(1)
    with mock.patch.object(app.relay,
                           'pulse',
                           return_value=False):
        suc = app.mainW.doRelayAction(7)
        assert not suc


def test_doRelayAction_5(qtbot):
    app.mainW.relayDropDowns[7].setCurrentIndex(1)
    with mock.patch.object(app.relay,
                           'pulse',
                           return_value=True):
        suc = app.mainW.doRelayAction(7)
        assert suc
