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
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.uic
import PyQt5.QtTest
import PyQt5.QtCore
# local import
from mw4.test.test_units.setupQt import setupQt


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test
    app, spy, mwGlob, test = setupQt()
    app.mainW.deviceStat['mount'] = True
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
    suc = app.storeConfig()
    assert suc


def test_setupIcons():
    suc = app.mainW.setupIcons()
    assert suc


def test_updatePointGui_alt():
    value = '45'
    app.mount.obsSite.Alt = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '45.00' == app.mainW.ui.ALT.text()
    value = None
    app.mount.obsSite.Alt = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.ALT.text()


def test_updatePointGui_az():
    value = '45'
    app.mount.obsSite.Az = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '45.00' == app.mainW.ui.AZ.text()
    value = None
    app.mount.obsSite.Az = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.AZ.text()


def test_updatePointGui_ra():
    value = '45'
    app.mount.obsSite.raJNow = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '45:00:00' == app.mainW.ui.RA.text()
    value = None
    app.mount.obsSite.raJNow = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.RA.text()


def test_updatePointGui_dec():
    value = '45'
    app.mount.obsSite.decJNow = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '+45:00:00' == app.mainW.ui.DEC.text()
    value = None
    app.mount.obsSite.decJNow = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.DEC.text()


def test_updatePointGui_pierside():
    value = 'W'
    app.mount.obsSite.pierside = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert 'WEST' == app.mainW.ui.pierside.text()
    value = None
    app.mount.obsSite.pierside = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.pierside.text()


def test_updatePointGui_ha():
    value = '12'
    app.mount.obsSite.raJNow = value
    app.mount.obsSite.timeSidereal = '00:00:00'
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '12:00:00' == app.mainW.ui.HA.text()
    value = None
    app.mount.obsSite.timeSidereal = '00:00:00'
    app.mount.obsSite.raJNow = value
    app.mainW.updatePointGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.HA.text()


def test_updateTimeGui_sidereal():
    value = '45:45:45'
    app.mount.obsSite.timeSidereal = value
    app.mainW.updateTimeGUI(app.mount.obsSite)
    assert '45:45:45' == app.mainW.ui.timeSidereal.text()
    value = None
    app.mount.obsSite.timeSidereal = value
    app.mainW.updateTimeGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.timeSidereal.text()


def test_updateStatusGui_statusText():
    app.mount.obsSite.status = 6
    app.mainW.updateStatusGUI(app.mount.obsSite)
    assert 'Slewing or going to stop' == app.mainW.ui.statusText.text()
    app.mount.obsSite.status = None
    app.mainW.updateStatusGUI(app.mount.obsSite)
    assert '-' == app.mainW.ui.statusText.text()


def test_updateSetting_slewRate():
    value = '15'
    app.mount.setting.slewRate = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '15' == app.mainW.ui.slewRate.text()
    value = None
    app.mount.setting.slewRate = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.slewRate.text()


def test_updateSetting_timeToFlip():
    value = '15'
    app.mount.setting.timeToFlip = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert ' 15' == app.mainW.ui.timeToFlip.text()
    value = None
    app.mount.setting.timeToFlip = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.timeToFlip.text()


def test_updateSettingExt_UTCExpire():
    value = '2020-10-05'
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert value == app.mainW.ui.UTCExpire.text()
    value = None
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert '-' == app.mainW.ui.UTCExpire.text()


def test_updateSettingExt_UTCExpire1():
    value = '2016-10-05'
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert value == app.mainW.ui.UTCExpire.text()
    value = None
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert '-' == app.mainW.ui.UTCExpire.text()


def test_updateSettingExt_UTCExpire2():
    value = '2018-10-05'
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert value == app.mainW.ui.UTCExpire.text()
    value = None
    app.mount.setting.UTCExpire = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert '-' == app.mainW.ui.UTCExpire.text()


def test_updateSetting_statusUnattendedFlip():
    value = '1'
    app.mount.setting.statusUnattendedFlip = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'ON' == app.mainW.ui.statusUnattendedFlip.text()
    value = None
    app.mount.setting.statusUnattendedFlip = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'OFF' == app.mainW.ui.statusUnattendedFlip.text()


def test_updateSetting_statusDualAxisTracking():
    value = '1'
    app.mount.setting.statusDualAxisTracking = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'ON' == app.mainW.ui.statusDualAxisTracking.text()
    value = None
    app.mount.setting.statusDualAxisTracking = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'OFF' == app.mainW.ui.statusDualAxisTracking.text()


def test_updateSetting_statusRefraction():
    value = '1'
    app.mount.setting.statusRefraction = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'ON' == app.mainW.ui.statusRefraction.text()
    value = None
    app.mount.setting.statusRefraction = value
    app.mainW.updateSetStatGUI(app.mount.setting)
    assert 'OFF' == app.mainW.ui.statusRefraction.text()


def test_updateSetting_statusGPSSynced_1():
    value = True
    app.mount.setting.gpsSynced = value
    app.mainW.updateSetSyncGUI(app.mount.setting)
    assert app.mainW.ui.statusGPSSynced.text() == 'YES'


def test_updateSetting_statusGPSSynced_2():
    value = None
    app.mount.setting.gpsSynced = value
    app.mainW.updateSetSyncGUI(app.mount.setting)
    assert app.mainW.ui.statusGPSSynced.text() == 'NO'


def test_updateSetting_statusGPSSynced_3():
    value = False
    app.mount.setting.gpsSynced = value
    app.mainW.updateSetSyncGUI(app.mount.setting)
    assert app.mainW.ui.statusGPSSynced.text() == 'NO'


def test_tracking_speed1():
    with mock.patch.object(app.mount.obsSite,
                           'checkRateLunar',
                           return_value=True):
        suc = app.mainW.updateTrackingGui(app.mount.obsSite)
        assert suc


def test_tracking_speed2():
    with mock.patch.object(app.mount.obsSite,
                           'checkRateSidereal',
                           return_value=True):
        suc = app.mainW.updateTrackingGui(app.mount.obsSite)
        assert suc


def test_tracking_speed3():
    with mock.patch.object(app.mount.obsSite,
                           'checkRateSolar',
                           return_value=True):
        suc = app.mainW.updateTrackingGui(app.mount.obsSite)
        assert suc


def test_changeTracking_ok1(qtbot):
    app.mount.obsSite.status = 0
    with mock.patch.object(app.mount.obsSite,
                           'stopTracking',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changeTracking()
            assert suc
        assert ['Cannot stop tracking', 2] == blocker.args


def test_changeTracking_ok2(qtbot):
    app.mount.obsSite.status = 0
    with mock.patch.object(app.mount.obsSite,
                           'stopTracking',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changeTracking()
            assert suc
        assert ['Stopped tracking', 0] == blocker.args


def test_changeTracking_ok3(qtbot):
    app.mount.obsSite.status = 1
    with mock.patch.object(app.mount.obsSite,
                           'startTracking',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changeTracking()
            assert suc
        assert ['Cannot start tracking', 2] == blocker.args


def test_changeTracking_ok4(qtbot):
    app.mount.obsSite.status = 1
    with mock.patch.object(app.mount.obsSite,
                           'startTracking',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changeTracking()
            assert suc
        assert ['Started tracking', 0] == blocker.args


def test_changePark_ok1(qtbot):
    app.mount.obsSite.status = 5
    with mock.patch.object(app.mount.obsSite,
                           'unpark',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changePark()
            assert suc
        assert ['Cannot unpark mount', 2] == blocker.args


def test_changePark_ok2(qtbot):
    app.mount.obsSite.status = 5
    with mock.patch.object(app.mount.obsSite,
                           'unpark',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changePark()
            assert suc
        assert ['Mount unparked', 0] == blocker.args


def test_changePark_ok3(qtbot):
    app.mount.obsSite.status = 1
    with mock.patch.object(app.mount.obsSite,
                           'park',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changePark()
            assert suc
        assert ['Cannot park mount', 2] == blocker.args


def test_changePark_ok4(qtbot):
    app.mount.obsSite.status = 1
    with mock.patch.object(app.mount.obsSite,
                           'park',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.changePark()
            assert suc
        assert ['Mount parked', 0] == blocker.args


def test_setLunarTracking1(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setLunarTracking',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setLunarTracking()
            assert suc
        assert ['Tracking set to Lunar', 0] == blocker.args


def test_setLunarTracking2(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setLunarTracking',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setLunarTracking()
            assert not suc
        assert ['Cannot set tracking to Lunar', 2] == blocker.args


def test_setSiderealTracking1(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setSiderealTracking',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setSiderealTracking()
            assert suc
        assert ['Tracking set to Sidereal', 0] == blocker.args


def test_setSiderealTracking2(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setSiderealTracking',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setSiderealTracking()
            assert not suc
        assert ['Cannot set tracking to Sidereal', 2] == blocker.args


def test_setSolarTracking1(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setSolarTracking',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setSolarTracking()
            assert suc
        assert ['Tracking set to Solar', 0] == blocker.args


def test_setSolarTracking2(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'setSolarTracking',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.setSolarTracking()
            assert not suc
        assert ['Cannot set tracking to Solar', 2] == blocker.args


def test_stop1(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'stop',
                           return_value=True):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.stop()
            assert suc
        assert ['Mount stopped', 0] == blocker.args


def test_stop2(qtbot):
    with mock.patch.object(app.mount.obsSite,
                           'stop',
                           return_value=False):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.stop()
            assert not suc
        assert ['Cannot stop mount', 2] == blocker.args


def test_updateSetting_slewRate():
    value = '5'
    app.mount.setting.slewRate = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert app.mainW.ui.slewRate.text() == ' 5'
    value = None
    app.mount.setting.slewRate = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.slewRate.text()


def test_updateSetting_timeToFlip():
    value = '5'
    app.mount.setting.timeToFlip = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert app.mainW.ui.timeToFlip.text() == '  5'
    value = None
    app.mount.setting.timeToFlip = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.timeToFlip.text()


def test_updateSetting_timeToMeridian():
    value = '5'
    app.mount.setting.timeToMeridian = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert app.mainW.ui.timeToMeridian.text() == '  5'
    value = None
    app.mount.setting.timeToMeridian = value
    app.mainW.updateSettingGUI(app.mount.sett)
    assert '-' == app.mainW.ui.timeToMeridian.text()


def test_updateSetting_refractionTemp():
    value = '15'
    app.mount.setting.refractionTemp = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '+15.0' == app.mainW.ui.refractionTemp.text()
    assert '+15.0' == app.mainW.ui.refractionTemp1.text()
    value = None
    app.mount.setting.refractionTemp = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.refractionTemp.text()
    assert '-' == app.mainW.ui.refractionTemp1.text()


def test_updateSetting_refractionPress():
    value = '1050.0'
    app.mount.setting.refractionPress = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert value == app.mainW.ui.refractionPress.text()
    assert value == app.mainW.ui.refractionPress1.text()
    value = None
    app.mount.setting.refractionPress = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.refractionPress.text()
    assert '-' == app.mainW.ui.refractionPress1.text()


def test_updateSetting_meridianLimitTrack_1():
    value = '15'
    app.mount.setting.meridianLimitTrack = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '15.0' == app.mainW.ui.meridianLimitTrack.text()
    value = None
    app.mount.setting.meridianLimitTrack = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.meridianLimitTrack.text()


def test_updateSetting_meridianLimitSlew():
    value = '15'
    app.mount.setting.meridianLimitSlew = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '15.0' == app.mainW.ui.meridianLimitSlew.text()
    value = None
    app.mount.setting.meridianLimitSlew = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.meridianLimitSlew.text()


def test_updateSetting_horizonLimitLow():
    value = '0'
    app.mount.setting.horizonLimitLow = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '0.0' == app.mainW.ui.horizonLimitLow.text()
    value = None
    app.mount.setting.horizonLimitLow = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.horizonLimitLow.text()


def test_updateSetting_horizonLimitHigh():
    value = '50'
    app.mount.setting.horizonLimitHigh = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '50.0' == app.mainW.ui.horizonLimitHigh.text()
    value = None
    app.mount.setting.horizonLimitHigh = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.horizonLimitHigh.text()


def test_updateSetting_timeToMeridian():
    app.mount.setting.timeToFlip = '100'
    app.mount.setting.meridianLimitTrack = '15'

    app.mainW.updateSettingGUI(app.mount.setting)
    assert ' 40' == app.mainW.ui.timeToMeridian.text()
    value = None
    app.mount.setting.timeToFlip = value
    app.mount.setting.meridianLimitTrack = value
    app.mainW.updateSettingGUI(app.mount.setting)
    assert '-' == app.mainW.ui.timeToMeridian.text()


def test_updateSettingExt_location():
    app.mount.obsSite.location = ['49:00:00', '11:00:00', '500']
    app.mainW.updateLocGUI(app.mount.obsSite)
    assert '11 00\' 00.0\"' == app.mainW.ui.siteLongitude.text()
    assert '49 00\' 00.0\"' == app.mainW.ui.siteLatitude.text()
    assert '500.0' == app.mainW.ui.siteElevation.text()
    app.mount.obsSite.location = None
    app.mainW.updateLocGUI(app.mount.obsSite)
    assert '11 00\' 00.0\"' == app.mainW.ui.siteLongitude.text()
    assert '49 00\' 00.0\"' == app.mainW.ui.siteLatitude.text()
    assert '500.0' == app.mainW.ui.siteElevation.text()


def test_setMeridianLimitTrack1(qtbot):
    app.mainW.deviceStat['mount'] = False
    app.mount.setting.meridianLimitTrack = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setMeridianLimitTrack()
        assert not suc


def test_setMeridianLimitTrack3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.meridianLimitTrack = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = app.mainW.setMeridianLimitTrack()
        assert not suc


def test_setMeridianLimitTrack4(qtbot):
    app.mount.setting.meridianLimitTrack = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.setting,
                               'setMeridianLimitTrack',
                               return_value=True):
            suc = app.mainW.setMeridianLimitTrack()
            assert suc


def test_setMeridianLimitSlew1(qtbot):
    app.mainW.deviceStat['mount'] = False
    app.mount.setting.meridianLimitSlew = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setMeridianLimitSlew()
        assert not suc


def test_setMeridianLimitSlew3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.meridianLimitSlew = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = app.mainW.setMeridianLimitSlew()
        assert not suc


def test_setMeridianLimitSlew4(qtbot):
    app.mount.setting.meridianLimitSlew = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.setting,
                               'setMeridianLimitSlew',
                               return_value=True):
            suc = app.mainW.setMeridianLimitSlew()
            assert suc


def test_setHorizonLimitHigh1(qtbot):
    app.mainW.deviceStat['mount'] = False
    app.mount.setting.horizonLimitHigh = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setHorizonLimitHigh()
        assert not suc


def test_setHorizonLimitHigh3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.horizonLimitHigh = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = app.mainW.setHorizonLimitHigh()
        assert not suc


def test_setHorizonLimitHigh4(qtbot):
    app.mount.setting.horizonLimitHigh = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.setting,
                               'setHorizonLimitHigh',
                               return_value=True):
            suc = app.mainW.setHorizonLimitHigh()
            assert suc


def test_setHorizonLimitLow1(qtbot):
    app.mainW.deviceStat['mount'] = False
    app.mount.setting.horizonLimitLow = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setHorizonLimitLow()
        assert not suc


def test_setHorizonLimitLow3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.horizonLimitLow = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = app.mainW.setHorizonLimitLow()
        assert not suc


def test_setHorizonLimitLow4(qtbot):
    app.mount.setting.horizonLimitLow = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.setting,
                               'setHorizonLimitLow',
                               return_value=True):
            suc = app.mainW.setHorizonLimitLow()
            assert suc


def test_setSlewRate1(qtbot):
    app.mainW.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setSlewRate()
        assert not suc


def test_setSlewRate3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.slewRate = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, False)):
        suc = app.mainW.setSlewRate()
        assert not suc


def test_setSlewRate4(qtbot):
    app.mount.setting.slewRate = 10
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getInt',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.setting,
                               'setSlewRate',
                               return_value=True):
            suc = app.mainW.setSlewRate()
            assert suc


def test_setLongitude1(qtbot):
    app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setLongitude()
        assert not suc


def test_setLongitude2(qtbot):
    app.mainW.deviceStat['mount'] = False
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, True)):
        suc = app.mainW.setLongitude()
        assert not suc


def test_setLongitude3(qtbot):
    app.mainW.deviceStat['mount'] = True
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, False)):
        suc = app.mainW.setLongitude()
        assert not suc


def test_setLongitude4(qtbot):
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.obsSite,
                               'setLongitude',
                               return_value=True):
            suc = app.mainW.setLongitude()
            assert suc


def test_setLatitude1(qtbot):
    app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setLatitude()
        assert not suc


def test_setLatitude2(qtbot):
    app.mainW.deviceStat['mount'] = True
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, True)):
        suc = app.mainW.setLatitude()
        assert not suc


def test_setLatitude3(qtbot):
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, False)):
        suc = app.mainW.setLatitude()
        assert not suc


def test_setLatitude4(qtbot):
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.obsSite,
                               'setLatitude',
                               return_value=True):
            suc = app.mainW.setLatitude()
            assert suc


def test_setElevation1(qtbot):
    app.mount.obsSite.location = None
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setElevation()
        assert not suc


def test_setElevation3(qtbot):
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, False)):
        suc = app.mainW.setElevation()
        assert not suc


def test_setElevation4(qtbot):
    elev = '999.9'
    lon = '+160*30:45.5'
    lat = '+45*30:45.5'
    app.mount.obsSite.location = lat, lon, elev
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getDouble',
                           return_value=(10, True)):
        with mock.patch.object(app.mount.obsSite,
                               'setElevation',
                               return_value=True):
            suc = app.mainW.setElevation()
            assert suc


def test_setUnattendedFlip1(qtbot):
    app.mainW.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setUnattendedFlip()
        assert not suc


def test_setUnattendedFlip3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.statusUnattendedFlip = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = app.mainW.setUnattendedFlip()
        assert not suc


def test_setUnattendedFlip4(qtbot):
    app.mount.setting.statusUnattendedFlip = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(app.mount.setting,
                               'setUnattendedFlip',
                               return_value=True):
            suc = app.mainW.setUnattendedFlip()
            assert suc


def test_setDualAxisTracking1(qtbot):
    app.mainW.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setDualAxisTracking()
        assert not suc


def test_setDualAxisTracking3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = app.mainW.setDualAxisTracking()
        assert not suc


def test_setDualAxisTracking4(qtbot):
    app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(app.mount.setting,
                               'setDualAxisTracking',
                               return_value=True):
            suc = app.mainW.setDualAxisTracking()
            assert suc


def test_setRefraction1(qtbot):
    app.mainW.deviceStat['mount'] = False
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'critical',
                           return_value=True):
        suc = app.mainW.setRefraction()
        assert not suc


def test_setRefraction3(qtbot):
    app.mainW.deviceStat['mount'] = True
    app.mount.setting.statusRefraction = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', False)):
        suc = app.mainW.setRefraction()
        assert not suc


def test_setRefraction4(qtbot):
    app.mount.setting.statusRefraction = True
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getItem',
                           return_value=('ON', True)):
        with mock.patch.object(app.mount.setting,
                               'setRefraction',
                               return_value=True):
            suc = app.mainW.setRefraction()
            assert suc
