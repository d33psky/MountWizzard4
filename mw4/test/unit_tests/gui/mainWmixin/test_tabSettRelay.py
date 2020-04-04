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
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import pyqtSignal
from mw4.gui.mainWmixin.tabSettRelay import SettRelay

# local import
from mw4.powerswitch.kmRelay import KMRelay
from mw4.gui.widgets.main_ui import Ui_MainWindow
from mw4.gui.widget import MWidget


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown(qtbot):
    global ui, widget, Test, app

    class Test(QObject):
        config = {'mainW': {}}
        threadPool = QThreadPool()
        update1s = pyqtSignal()
        message = pyqtSignal(str, int)
        relay = KMRelay()

    widget = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)

    app = SettRelay(app=Test(), ui=ui,
                    clickable=MWidget().clickable)

    app.changeStyleDynamic = MWidget().changeStyleDynamic
    app.close = MWidget().close

    app.deleteLater = MWidget().deleteLater
    qtbot.addWidget(app)

    yield

    del widget, ui, Test, app


def test_initConfig_1():
    app.app.config['mainW'] = {}
    suc = app.initConfig()
    assert suc


def test_storeConfig_1():
    app.ui.relayDevice.setCurrentIndex(0)
    app.storeConfig()


def test_setupRelayGui(qtbot):
    assert 8 == len(app.relayDropDowns)
    assert 8 == len(app.relayButtonTexts)
    assert 8 == len(app.relayButtons)
    for dropDown in app.relayDropDowns:
        val = dropDown.count()
        assert 2 == val


def test_toggleRelay_1(qtbot):
    def Sender():
        return ui.relayButton0
    app.sender = Sender

    app.ui.relayDevice.setCurrentIndex(0)
    with qtbot.waitSignal(app.app.message) as blocker:
        suc = app.relayButtonPressed()
        assert not suc
    assert ['Relay action cannot be performed', 2] == blocker.args


def test_toggleRelay_2(qtbot):
    def Sender():
        return ui.relayButton0
    app.sender = Sender
    app.ui.relayDevice.setCurrentIndex(1)
    with mock.patch.object(app.app.relay,
                           'switch',
                           return_value=False):
        with qtbot.waitSignal(app.app.message) as blocker:
            suc = app.relayButtonPressed()
            assert not suc
        assert ['Relay action cannot be performed', 2] == blocker.args


def test_relayHost():
    app.ui.relayHost.setText('test')
    app.relayHost()

    assert app.app.relay.host == ('test', 80)


def test_relayUser():
    app.ui.relayUser.setText('test')
    app.relayUser()

    assert app.app.relay.user == 'test'


def test_relayPassword():
    app.ui.relayPassword.setText('test')
    app.relayPassword()

    assert app.app.relay.password == 'test'


def test_doRelayAction_1(qtbot):
    app.relayDropDowns[7].setCurrentIndex(0)
    with mock.patch.object(app.app.relay,
                           'switch',
                           return_value=False):
        suc = app.doRelayAction(7)
        assert not suc


def test_doRelayAction_2(qtbot):
    app.relayDropDowns[7].setCurrentIndex(0)
    with mock.patch.object(app.app.relay,
                           'switch',
                           return_value=True):
        suc = app.doRelayAction(7)
        assert suc


def test_doRelayAction_3(qtbot):
    app.relayDropDowns[7].setCurrentIndex(2)
    suc = app.doRelayAction(7)
    assert not suc


def test_doRelayAction_4(qtbot):
    app.relayDropDowns[7].setCurrentIndex(1)
    with mock.patch.object(app.app.relay,
                           'pulse',
                           return_value=False):
        suc = app.doRelayAction(7)
        assert not suc


def test_doRelayAction_5(qtbot):
    app.relayDropDowns[7].setCurrentIndex(1)
    with mock.patch.object(app.app.relay,
                           'pulse',
                           return_value=True):
        suc = app.doRelayAction(7)
        assert suc


def test_relayButtonPressed_1(qtbot):
    def Sender():
        return ui.relayButton0
    app.sender = Sender

    with mock.patch.object(app,
                           'doRelayAction',
                           return_value=False):
        suc = app.relayButtonPressed()
        assert not suc


def test_relayButtonPressed_2(qtbot):
    def Sender():
        return ui.relayButton0
    app.sender = Sender

    with mock.patch.object(app,
                           'doRelayAction',
                           return_value=True):
        suc = app.relayButtonPressed()
        assert suc
