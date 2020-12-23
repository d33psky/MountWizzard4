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
import unittest.mock as mock
import pytest
import datetime

# external packages
import PyQt5
from PyQt5.QtWidgets import QWidget
from skyfield.api import Angle, Topos

# local import
from tests.baseTestSetupMixins import App
from gui.utilities.toolsQtWidget import MWidget
from gui.widgets.main_ui import Ui_MainWindow
from gui.mainWmixin.tabMount import Mount


@pytest.fixture(autouse=True, scope='module')
def module(qapp):
    yield


@pytest.fixture(autouse=True, scope='function')
def function(module):

    class Mixin(MWidget, Mount):
        def __init__(self):
            super().__init__()
            self.app = App()
            self.deviceStat = self.app.deviceStat
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            Mount.__init__(self)

    window = Mixin()
    yield window


def test_initConfig_1(function):
    function.app.config['mainW'] = {}
    suc = function.initConfig()
    assert suc


def test_initConfig_2(function):
    del function.app.config['mainW']
    suc = function.initConfig()
    assert suc


def test_storeConfig_1(function):
    function.app.config['mainW'] = {}
    suc = function.storeConfig()
    assert suc


def test_updatePointGui_alt(function):
    value = Angle(degrees=45)
    function.app.mount.obsSite.Alt = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '45.00' == function.ui.ALT.text()
    value = None
    function.app.mount.obsSite.Alt = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.ALT.text()


def test_updatePointGui_az(function):
    value = Angle(degrees=45)
    function.app.mount.obsSite.Az = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '45.00' == function.ui.AZ.text()
    value = None
    function.app.mount.obsSite.Az = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.AZ.text()


def test_updatePointGui_ra(function):
    value = Angle(hours=45)
    function.app.mount.obsSite.raJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '45 00 00' == function.ui.RA.text()
    value = None
    function.app.mount.obsSite.raJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.RA.text()


def test_updatePointGui_dec_1(function):
    function.ui.checkJ2000.setChecked(False)
    value = Angle(degrees=45)
    function.app.mount.obsSite.decJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '+45 00 00' == function.ui.DEC.text()


def test_updatePointGui_dec_2(function):
    value = None
    function.app.mount.obsSite.decJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.DEC.text()


def test_updatePointGui_pierside(function):
    value = 'W'
    function.app.mount.obsSite.pierside = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert 'WEST' == function.ui.pierside.text()
    value = None
    function.app.mount.obsSite.pierside = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.pierside.text()


def test_updatePointGui_ha_1(function):
    value = Angle(hours=12)
    function.app.mount.obsSite.haJNow = value
    function.app.mount.obsSite.timeSidereal = '00:00:00'
    function.updatePointGUI(function.app.mount.obsSite)
    assert '12 00 00' == function.ui.HA.text()


def test_updatePointGui_ha_2(function):
    value = None
    function.app.mount.obsSite.timeSidereal = '00:00:00'
    function.app.mount.obsSite.haJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
    assert '-' == function.ui.HA.text()


def test_updateTimeGui_sidereal_1(function):
    value = Angle(hours=12)
    function.app.mount.obsSite.timeSidereal = value
    function.updateTimeGUI(function.app.mount.obsSite)
    assert '12:00:00' == function.ui.timeSidereal.text()


def test_updateTimeGui_sidereal_2(function):
    value = None
    function.app.mount.obsSite.timeSidereal = value
    function.updateTimeGUI(function.app.mount.obsSite)
    assert '-' == function.ui.timeSidereal.text()


def test_updateSetting_slewRate(function):
    value = 15
    function.app.mount.setting.slewRate = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '15' == function.ui.slewRate.text()
    value = None
    function.app.mount.setting.slewRate = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.slewRate.text()


def test_updateSetting_timeToFlip(function):
    value = 15
    function.app.mount.setting.timeToFlip = value
    function.updateSettingGUI(function.app.mount.setting)
    assert ' 15' == function.ui.timeToFlip.text()
    value = None
    function.app.mount.setting.timeToFlip = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.timeToFlip.text()


def test_updateSettingExt_UTCExpire(function):
    value = '2020-10-05'
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert value == function.ui.UTCExpire.text()
    value = None
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.UTCExpire.text()


def test_updateSettingExt_UTCExpire_1(function):
    value = '2016-10-05'
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert value == function.ui.UTCExpire.text()
    value = None
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.UTCExpire.text()


def test_updateSettingExt_UTCExpire_2(function):
    tomorrow = datetime.date.today() + datetime.timedelta(days=15)
    value = tomorrow.strftime('%Y-%m-%d')
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert value == function.ui.UTCExpire.text()
    value = None
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.UTCExpire.text()


def test_updateSettingExt_UTCExpire_3(function):
    tomorrow = datetime.date.today() + datetime.timedelta(days=40)
    value = tomorrow.strftime('%Y-%m-%d')
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert value == function.ui.UTCExpire.text()
    value = None
    function.app.mount.setting.UTCExpire = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.UTCExpire.text()


def test_updateSetting_statusUnattendedFlip(function):
    value = True
    function.app.mount.setting.statusUnattendedFlip = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert 'ON' == function.ui.statusUnattendedFlip.text()
    value = None
    function.app.mount.setting.statusUnattendedFlip = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.statusUnattendedFlip.text()


def test_updateSetting_statusDualAxisTracking(function):
    value = True
    function.app.mount.setting.statusDualAxisTracking = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert 'ON' == function.ui.statusDualAxisTracking.text()
    value = None
    function.app.mount.setting.statusDualAxisTracking = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.statusDualAxisTracking.text()


def test_updateSetting_statusRefraction(function):
    value = True
    function.app.mount.setting.statusRefraction = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert 'ON' == function.ui.statusRefraction.text()
    value = None
    function.app.mount.setting.statusRefraction = value
    function.updateSetStatGUI(function.app.mount.setting)
    assert '-' == function.ui.statusRefraction.text()


def test_updateSetSyncGUI_1(function):
    function.app.mount.setting.gpsSynced = True
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert function.ui.statusGPSSynced.text() == 'YES'
    assert suc


def test_updateSetSyncGUI_2(function):
    function.app.mount.setting.gpsSynced = False
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert function.ui.statusGPSSynced.text() == 'NO'
    assert suc


def test_updateSetSyncGUI_3(function):
    function.app.mount.setting.gpsSynced = None
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert function.ui.statusGPSSynced.text() == '-'
    assert suc


def test_updateSetSyncGUI_4(function):
    function.app.mount.setting.typeConnection = None
    function.app.mount.setting.wakeOnLan = 'ON'
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert suc


def test_updateSetSyncGUI_5(function):
    function.app.mount.setting.typeConnection = 1
    function.app.mount.setting.wakeOnLan = None
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert suc


def test_updateSetSyncGUI_6(function):
    function.app.mount.setting.typeConnection = 1
    function.app.mount.setting.wakeOnLan = 'OFF'
    suc = function.updateSetSyncGUI(function.app.mount.setting)
    assert suc


def test_tracking_speed1(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateLunar',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_tracking_speed2(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateSidereal',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_tracking_speed3(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateSolar',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_setLunarTracking1(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setLunarTracking',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setLunarTracking()
            assert suc
        assert ['Tracking set to Lunar', 0] == blocker.args


def test_setLunarTracking2(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setLunarTracking',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setLunarTracking()
            assert not suc
        assert ['Cannot set tracking to Lunar', 2] == blocker.args


def test_setSiderealTracking1(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setSiderealTracking',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setSiderealTracking()
            assert suc
        assert ['Tracking set to Sidereal', 0] == blocker.args


def test_setSiderealTracking2(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setSiderealTracking',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setSiderealTracking()
            assert not suc
        assert ['Cannot set tracking to Sidereal', 2] == blocker.args


def test_setSolarTracking1(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setSolarTracking',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setSolarTracking()
            assert suc
        assert ['Tracking set to Solar', 0] == blocker.args


def test_setSolarTracking2(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'setSolarTracking',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.setSolarTracking()
            assert not suc
        assert ['Cannot set tracking to Solar', 2] == blocker.args


def test_flipMount_1(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'flip',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.flipMount()
            assert not suc
        assert ['Cannot flip mount', 2] == blocker.args


def test_flipMount_2(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'flip',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.flipMount()
            assert suc
        assert ['Mount flipped', 0] == blocker.args


def test_stop1(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'stop',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.stop()
            assert suc
        assert ['Mount stopped', 0] == blocker.args


def test_stop2(function, qtbot):
    with mock.patch.object(function.app.mount.obsSite,
                           'stop',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.stop()
            assert not suc
        assert ['Cannot stop mount', 2] == blocker.args


def test_updateSetting_slewRate_1(function):
    value = 5
    function.app.mount.setting.slewRate = value
    function.updateSettingGUI(function.app.mount.setting)
    assert function.ui.slewRate.text() == ' 5'
    value = None
    function.app.mount.setting.slewRate = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.slewRate.text()


def test_updateSetting_timeToFlip_1(function):
    value = 5
    function.app.mount.setting.timeToFlip = value
    function.updateSettingGUI(function.app.mount.setting)
    assert function.ui.timeToFlip.text() == '  5'
    value = None
    function.app.mount.setting.timeToFlip = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.timeToFlip.text()


def test_updateSetting_timeToMeridian_1(function):
    function.app.mount.setting.timeToFlip = 5
    function.app.mount.setting.meridianLimitTrack = 0

    function.updateSettingGUI(function.app.mount.setting)
    assert function.ui.timeToMeridian.text() == '  0'

    function.app.mount.setting.timeToFlip = None
    function.app.mount.setting.meridianLimitTrack = None

    function.updateSettingGUI(function.app.mount.setting)
    assert '  0' == function.ui.timeToMeridian.text()


def test_updateSetting_refractionTemp(function):
    value = 15
    function.app.mount.setting.refractionTemp = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '+15.0' == function.ui.refractionTemp.text()
    assert '+15.0' == function.ui.refractionTemp1.text()
    value = None
    function.app.mount.setting.refractionTemp = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.refractionTemp.text()
    assert '-' == function.ui.refractionTemp1.text()


def test_updateSetting_refractionPress(function):
    value = 1050.0
    function.app.mount.setting.refractionPress = value
    function.updateSettingGUI(function.app.mount.setting)
    assert str(value) == function.ui.refractionPress.text()
    assert str(value) == function.ui.refractionPress1.text()
    value = None
    function.app.mount.setting.refractionPress = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.refractionPress.text()
    assert '-' == function.ui.refractionPress1.text()


def test_updateSetting_meridianLimitTrack_1(function):
    value = 15
    function.app.mount.setting.meridianLimitTrack = value
    function.updateSettingGUI(function.app.mount.setting)
    assert ' 15' == function.ui.meridianLimitTrack.text()
    value = None
    function.app.mount.setting.meridianLimitTrack = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.meridianLimitTrack.text()


def test_updateSetting_meridianLimitSlew(function):
    value = 15
    function.app.mount.setting.meridianLimitSlew = value
    function.updateSettingGUI(function.app.mount.setting)
    assert ' 15' == function.ui.meridianLimitSlew.text()
    value = None
    function.app.mount.setting.meridianLimitSlew = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.meridianLimitSlew.text()


def test_updateSetting_horizonLimitLow(function):
    value = 0
    function.app.mount.setting.horizonLimitLow = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '  0' == function.ui.horizonLimitLow.text()
    value = None
    function.app.mount.setting.horizonLimitLow = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.horizonLimitLow.text()


def test_updateSetting_horizonLimitHigh(function):
    value = 50
    function.app.mount.setting.horizonLimitHigh = value
    function.updateSettingGUI(function.app.mount.setting)
    assert ' 50' == function.ui.horizonLimitHigh.text()
    value = None
    function.app.mount.setting.horizonLimitHigh = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '-' == function.ui.horizonLimitHigh.text()


def test_updateSetting_timeToMeridian(function):
    function.app.mount.setting.timeToFlip = 100
    function.app.mount.setting.meridianLimitTrack = 15

    function.updateSettingGUI(function.app.mount.setting)
    assert '  0' == function.ui.timeToMeridian.text()
    value = None
    function.app.mount.setting.timeToFlip = value
    function.app.mount.setting.meridianLimitTrack = value
    function.updateSettingGUI(function.app.mount.setting)
    assert '  0' == function.ui.timeToMeridian.text()


def test_updateLocGUI_1(function):
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    function.updateLocGUI(function.app.mount.obsSite)
    assert '11E 00 00' == function.ui.siteLongitude.text()
    assert '49N 00 00' == function.ui.siteLatitude.text()
    assert '500.0' == function.ui.siteElevation.text()


def test_updateLocGUI_2(function):
    function.app.mount.obsSite.location = None
    suc = function.updateLocGUI(function.app.mount.obsSite)
    assert not suc


def test_updateLocGUI_3(function):
    function.app.mount.obsSite.location = ['49:00:00', '11:00:00', '500']
    suc = function.updateLocGUI(None)
    assert not suc


def test_updateTrackingGui_1(function):
    suc = function.updateTrackingGui(None)
    assert not suc


def test_updateTrackingGui_2(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateLunar',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_updateTrackingGui_3(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateSolar',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_updateTrackingGui_4(function):
    with mock.patch.object(function.app.mount.obsSite,
                           'checkRateSidereal',
                           return_value=True):
        suc = function.updateTrackingGui(function.app.mount.obsSite)
        assert suc


def test_changeTracking_ok1(function, qtbot):
    function.app.mount.obsSite.status = 0
    with mock.patch.object(function.app.mount.obsSite,
                           'stopTracking',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changeTracking()
            assert suc
        assert ['Cannot stop tracking', 2] == blocker.args


def test_changeTracking_ok2(function, qtbot):
    function.app.mount.obsSite.status = 0
    with mock.patch.object(function.app.mount.obsSite,
                           'stopTracking',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changeTracking()
            assert suc
        assert ['Stopped tracking', 0] == blocker.args


def test_changeTracking_ok3(function, qtbot):
    function.app.mount.obsSite.status = 1
    with mock.patch.object(function.app.mount.obsSite,
                           'startTracking',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changeTracking()
            assert suc
        assert ['Cannot start tracking', 2] == blocker.args


def test_changeTracking_ok4(function, qtbot):
    function.app.mount.obsSite.status = 1
    with mock.patch.object(function.app.mount.obsSite,
                           'startTracking',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changeTracking()
            assert suc
        assert ['Started tracking', 0] == blocker.args


def test_changePark_ok1(function, qtbot):
    function.app.mount.obsSite.status = 5
    with mock.patch.object(function.app.mount.obsSite,
                           'unpark',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changePark()
            assert suc
        assert ['Cannot unpark mount', 2] == blocker.args


def test_changePark_ok2(function, qtbot):
    function.app.mount.obsSite.status = 5
    with mock.patch.object(function.app.mount.obsSite,
                           'unpark',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changePark()
            assert suc
        assert ['Mount unparked', 0] == blocker.args


def test_changePark_ok3(function, qtbot):
    function.app.mount.obsSite.status = 1
    with mock.patch.object(function.app.mount.obsSite,
                           'park',
                           return_value=False):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changePark()
            assert suc
        assert ['Cannot park mount', 2] == blocker.args


def test_changePark_ok4(function, qtbot):
    function.app.mount.obsSite.status = 1
    with mock.patch.object(function.app.mount.obsSite,
                           'park',
                           return_value=True):
        with qtbot.waitSignal(function.app.message) as blocker:
            suc = function.changePark()
            assert suc
        assert ['Mount parked', 0] == blocker.args


def test_setMeridianLimitTrack_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.setting.meridianLimitTrack = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setMeridianLimitTrack()
        assert not suc


def test_setMeridianLimitTrack_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitTrack = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = function.setMeridianLimitTrack()
        assert not suc


def test_setMeridianLimitTrack_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitTrack = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setMeridianLimitTrack',
                               return_value=False):
            suc = function.setMeridianLimitTrack()
            assert not suc


def test_setMeridianLimitTrack_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitTrack = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setMeridianLimitTrack',
                               return_value=True):
            suc = function.setMeridianLimitTrack()
            assert suc


def test_setMeridianLimitSlew_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.setting.meridianLimitSlew = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setMeridianLimitSlew()
        assert not suc


def test_setMeridianLimitSlew_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitSlew = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = function.setMeridianLimitSlew()
        assert not suc


def test_setMeridianLimitSlew_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitSlew = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setMeridianLimitSlew',
                               return_value=False):
            suc = function.setMeridianLimitSlew()
            assert not suc


def test_setMeridianLimitSlew_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.meridianLimitSlew = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setMeridianLimitSlew',
                               return_value=True):
            suc = function.setMeridianLimitSlew()
            assert suc


def test_setHorizonLimitHigh_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.setting.horizonLimitHigh = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setHorizonLimitHigh()
        assert not suc


def test_setHorizonLimitHigh_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitHigh = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = function.setHorizonLimitHigh()
        assert not suc


def test_setHorizonLimitHigh_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitHigh = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setHorizonLimitHigh',
                               return_value=False):
            suc = function.setHorizonLimitHigh()
            assert not suc


def test_setHorizonLimitHigh_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitHigh = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setHorizonLimitHigh',
                               return_value=True):
            suc = function.setHorizonLimitHigh()
            assert suc


def test_setHorizonLimitLow_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.setting.horizonLimitLow = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setHorizonLimitLow()
        assert not suc


def test_setHorizonLimitLow_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitLow = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = function.setHorizonLimitLow()
        assert not suc


def test_setHorizonLimitLow_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitLow = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setHorizonLimitLow',
                               return_value=False):
            suc = function.setHorizonLimitLow()
            assert not suc


def test_setHorizonLimitLow_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.horizonLimitLow = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setHorizonLimitLow',
                               return_value=True):
            suc = function.setHorizonLimitLow()
            assert suc


def test_setSlewRate_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setSlewRate()
        assert not suc


def test_setSlewRate_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.slewRate = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = function.setSlewRate()
        assert not suc


def test_setSlewRate_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.slewRate = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setSlewRate',
                               return_value=False):
            suc = function.setSlewRate()
            assert not suc


def test_setSlewRate_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.slewRate = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.setting,
                               'setSlewRate',
                               return_value=True):
            suc = function.setSlewRate()
            assert suc


def test_setLongitude_1(function, qtbot):
    function.app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setLongitude()
        assert not suc


def test_setLongitude_2(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+160*30:45.5', True)):
        suc = function.setLongitude()
        assert not suc


def test_setLongitude_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+160*30:45.5', False)):
        suc = function.setLongitude()
        assert not suc


def test_setLongitude_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+160*30:45.5', True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setLongitude',
                               return_value=False):
            suc = function.setLongitude()
            assert not suc


def test_setLongitude_5(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('11E 30 45.5', True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setLongitude',
                               return_value=True):
            suc = function.setLongitude()
            assert suc


def test_setLongitude_6(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(None, True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setLongitude',
                               return_value=True):
            suc = function.setLongitude()
            assert not suc


def test_setLatitude_1(function, qtbot):
    function.app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setLatitude()
        assert not suc


def test_setLatitude_2(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+45*30:45.5', True)):
        suc = function.setLatitude()
        assert not suc


def test_setLatitude_3(function, qtbot):
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+45*30:45.5', False)):
        suc = function.setLatitude()
        assert not suc


def test_setLatitude_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('+45*30:45.5', True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setLatitude',
                               return_value=False):
            suc = function.setLatitude()
            assert not suc


def test_setLatitude_5(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('45N 30 45.5', True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setLatitude',
                               return_value=True):
            suc = function.setLatitude()
            assert suc


def test_setLatitude_6(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(None, True)):
        suc = function.setLatitude()
        assert not suc


def test_setElevation_1(function, qtbot):
    function.app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setElevation()
        assert not suc


def test_setElevation_2(function, qtbot):
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, False)):
        suc = function.setElevation()
        assert not suc


def test_setElevation_3(function, qtbot):
    function.app.deviceStat['mount'] = False
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, True)):
        suc = function.setElevation()
        assert not suc


def test_setElevation_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setElevation',
                               return_value=False):
            suc = function.setElevation()
            assert not suc


def test_setElevation_5(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.obsSite.location = Topos(longitude_degrees=11,
                                                latitude_degrees=49,
                                                elevation_m=500)
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, True)):
        with mock.patch.object(function.app.mount.obsSite,
                               'setElevation',
                               return_value=True):
            suc = function.setElevation()
            assert suc


def test_setUnattendedFlip_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setUnattendedFlip()
        assert not suc


def test_setUnattendedFlip_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusUnattendedFlip = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = function.setUnattendedFlip()
        assert not suc


def test_setUnattendedFlip_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusUnattendedFlip = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setUnattendedFlip',
                               return_value=False):
            suc = function.setUnattendedFlip()
            assert not suc


def test_setUnattendedFlip_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusUnattendedFlip = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setUnattendedFlip',
                               return_value=True):
            suc = function.setUnattendedFlip()
            assert suc


def test_setDualAxisTracking_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setDualAxisTracking()
        assert not suc


def test_setDualAxisTracking_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = function.setDualAxisTracking()
        assert not suc


def test_setDualAxisTracking_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setDualAxisTracking',
                               return_value=False):
            suc = function.setDualAxisTracking()
            assert not suc


def test_setDualAxisTracking_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setDualAxisTracking',
                               return_value=True):
            suc = function.setDualAxisTracking()
            assert suc


def test_setRefraction_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setRefraction()
        assert not suc


def test_setRefraction_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusRefraction = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = function.setRefraction()
        assert not suc


def test_setRefraction_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusRefraction = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setRefraction',
                               return_value=False):
            suc = function.setRefraction()
            assert not suc


def test_setRefraction_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusRefraction = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setRefraction',
                               return_value=True):
            suc = function.setRefraction()
            assert suc


def test_setWOL_1(function, qtbot):
    function.app.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = function.setWOL()
        assert not suc


def test_setWOL_2(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusWOL = '0'
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = function.setWOL()
        assert not suc


def test_setWOL_3(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusWOL = '0'
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setWOL',
                               return_value=False):
            suc = function.setWOL()
            assert not suc


def test_setWOL_4(function, qtbot):
    function.app.deviceStat['mount'] = True
    function.app.mount.setting.statusWOL = '0'
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(function.app.mount.setting,
                               'setWOL',
                               return_value=True):
            suc = function.setWOL()
            assert suc


def test_updatePointGui_ra_j2000(function):
    function.ui.checkJ2000.setChecked(True)
    value = Angle(hours=45)
    function.app.mount.obsSite.raJNow = value
    value = Angle(degrees=45)
    function.app.mount.obsSite.decJNow = value
    function.updatePointGUI(function.app.mount.obsSite)
