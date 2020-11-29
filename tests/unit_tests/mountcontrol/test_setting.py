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
# Python  v3.7.4

#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
# standard libraries
import unittest
import unittest.mock as mock
# external packages
# local imports
from mountcontrol.setting import Setting


class TestConfigData(unittest.TestCase):

    def setUp(self):
        pass

    #
    #
    # testing the class Setting and it's attribute
    #
    #

    def test_Setting_slewRate(self):
        sett = Setting()
        sett.slewRate = '67'
        self.assertEqual(67, sett.slewRate)
        self.assertEqual(67, sett._slewRate)

    def test_Setting_timeToFlip(self):
        sett = Setting()
        sett.timeToFlip = '67'
        self.assertEqual(67, sett.timeToFlip)
        self.assertEqual(67, sett._timeToFlip)

    def test_Setting_meridianLimitTrack(self):
        sett = Setting()
        sett.meridianLimitTrack = '67'
        self.assertEqual(67, sett.meridianLimitTrack)
        self.assertEqual(67, sett._meridianLimitTrack)

    def test_Setting_meridianLimitSlew(self):
        sett = Setting()
        sett.meridianLimitSlew = '67'
        self.assertEqual(67, sett.meridianLimitSlew)
        self.assertEqual(67, sett._meridianLimitSlew)

    def test_Setting_timeToMeridian(self):
        sett = Setting()
        sett.timeToFlip = '10'
        sett.meridianLimitTrack = '5'
        self.assertEqual(-10, sett.timeToMeridian())

    def test_Setting_refractionTemp(self):
        sett = Setting()
        sett.refractionTemp = '67'
        self.assertEqual(67, sett.refractionTemp)
        self.assertEqual(67, sett._refractionTemp)

    def test_Setting_refractionPress(self):
        sett = Setting()
        sett.refractionPress = '67'
        self.assertEqual(67, sett.refractionPress)
        self.assertEqual(67, sett._refractionPress)

    def test_Setting_telescopeTempDEC(self):
        sett = Setting()
        sett.telescopeTempDEC = '67'
        self.assertEqual(67, sett.telescopeTempDEC)

    def test_Setting_statusRefraction(self):
        sett = Setting()
        sett.statusRefraction = 1
        self.assertEqual(True, sett.statusRefraction)
        self.assertEqual(True, sett._statusRefraction)

    def test_Setting_statusUnattendedFlip(self):
        sett = Setting()
        sett.statusUnattendedFlip = 1
        self.assertEqual(True, sett.statusUnattendedFlip)
        self.assertEqual(True, sett._statusUnattendedFlip)

    def test_Setting_statusDualAxisTracking(self):
        sett = Setting()
        sett.statusDualAxisTracking = 1
        self.assertEqual(True, sett.statusDualAxisTracking)
        self.assertEqual(True, sett._statusDualAxisTracking)

    def test_Setting_horizonLimitHigh(self):
        sett = Setting()
        sett.horizonLimitHigh = '67'
        self.assertEqual(67, sett.horizonLimitHigh)
        self.assertEqual(67, sett._horizonLimitHigh)

    def test_Setting_horizonLimitLow(self):
        sett = Setting()
        sett.horizonLimitLow = '67'
        self.assertEqual(67, sett.horizonLimitLow)
        self.assertEqual(67, sett._horizonLimitLow)

    def test_Setting_UTCValid(self):
        sett = Setting()
        sett.UTCValid = 1
        self.assertEqual(True, sett.UTCValid)
        self.assertEqual(True, sett._UTCValid)

    def test_Setting_UTCExpire(self):
        sett = Setting()
        sett.UTCExpire = '67'
        self.assertEqual('67', sett.UTCExpire)
        self.assertEqual('67', sett._UTCExpire)

    def test_Setting_UTCExpire1(self):
        sett = Setting()
        sett.UTCExpire = 67
        self.assertEqual(None, sett.UTCExpire)
        self.assertEqual(None, sett._UTCExpire)

    def test_Setting_typeConnection_1(self):
        sett = Setting()
        sett.typeConnection = 5
        self.assertEqual(None, sett.typeConnection)
        self.assertEqual(None, sett._typeConnection)

    def test_Setting_typeConnection_2(self):
        sett = Setting()
        sett.typeConnection = 3
        self.assertEqual(3, sett.typeConnection)
        self.assertEqual(3, sett._typeConnection)

    def test_Setting_gpsSynced_1(self):
        sett = Setting()
        sett.gpsSynced = 5
        self.assertEqual(True, sett.gpsSynced)
        self.assertEqual(True, sett._gpsSynced)

    def test_Setting_gpsSynced_2(self):
        sett = Setting()
        sett.gpsSynced = 0
        self.assertEqual(False, sett.gpsSynced)
        self.assertEqual(False, sett._gpsSynced)

    def test_Setting_addressLanMAC_1(self):
        sett = Setting()
        value = '00:00:00:00:00:00'
        sett.addressLanMAC = '00:00:00:00:00:00'
        self.assertEqual(value, sett.addressLanMAC)
        self.assertEqual(value, sett._addressLanMAC)

    def test_Setting_addressWirelessMAC_1(self):
        sett = Setting()
        value = '00:00:00:00:00:00'
        sett.addressWirelessMAC = '00:00:00:00:00:00'
        self.assertEqual(value, sett.addressWirelessMAC)
        self.assertEqual(value, sett._addressWirelessMAC)

    #
    #
    # testing pollSetting med
    #
    #

    def test_Setting_parse_ok(self):
        sett = Setting()
        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*',
                    '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']
        suc = sett.parseSetting(response,  21)
        self.assertEqual(True, suc)

    def test_Setting_parse_not_ok1(self):
        sett = Setting()
        response = ['15', '1', '20', '0426', '05', '+010.0', '0EEE.0', '60.2', '+033.0',
                    '101+90*',
                    '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']
        suc = sett.parseSetting(response,  21)
        self.assertEqual(True, suc)

    def test_Setting_parse_not_ok2(self):
        sett = Setting()
        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '+90*',
                    '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']
        suc = sett.parseSetting(response,  21)
        self.assertEqual(True, suc)

    def test_Setting_parse_not_ok3(self):
        sett = Setting()
        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*',
                    '+00', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        suc = sett.parseSetting(response,  21)
        self.assertEqual(True, suc)

    def test_Setting_parse_not_ok4(self):
        sett = Setting(
                       )
        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*',
                    '+00*', ',2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        suc = sett.parseSetting(response,  21)

        self.assertEqual(True, suc)

    def test_Setting_poll_ok1(self):
        sett = Setting()

        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*', '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response,  21
            suc = sett.pollSetting()
            self.assertEqual(True, suc)

    def test_Setting_poll_ok2(self):
        sett = Setting()

        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*', '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response,  21
            suc = sett.pollSetting()
            self.assertEqual(True, suc)

    def test_Setting_poll_not_ok1(self):
        sett = Setting()

        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*', '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response,  21
            suc = sett.pollSetting()
            self.assertEqual(False, suc)

    def test_Setting_poll_not_ok2(self):
        sett = Setting()

        response = ['15', '1', '20', '0426', '05', '+010.0', '0950.0', '60.2', '+033.0',
                    '101+90*', '+00*', 'E,2018-08-11', '1', '0', '00:00:00:00:00:00', 'N',
                    '0', '987.0', '+20,5', '90.4', '-13,5']

        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 6
            suc = sett.pollSetting()
            self.assertEqual(False, suc)

    #
    #
    # testing setDualAxisTracking
    #
    #

    def test_Setting_setDualAxisTracking_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDualAxisTracking(1)
            self.assertEqual(True, suc)

    def test_Setting_setDualAxisTracking_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDualAxisTracking(1)
            self.assertEqual(False, suc)

    def test_Setting_setDualAxisTracking_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setDualAxisTracking(1)
            self.assertEqual(False, suc)

    #
    #
    # testing setMeridianLimitTrack
    #
    #

    def test_Setting_setMeridianLimitTrack_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitTrack(2)
            self.assertEqual(True, suc)

    def test_Setting_setMeridianLimitTrack_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitTrack(0)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitTrack_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setMeridianLimitTrack(0)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitTrack_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitTrack(40)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitTrack_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitTrack(-30)
            self.assertEqual(False, suc)

    #
    #
    # testing setMeridianLimitSlew
    #
    #

    def test_Setting_setMeridianLimitSlew_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitSlew(0)
            self.assertEqual(True, suc)

    def test_Setting_setMeridianLimitSlew_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitSlew(0)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitSlew_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setMeridianLimitSlew(0)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitSlew_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitSlew(40)
            self.assertEqual(False, suc)

    def test_Setting_setMeridianLimitSlew_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setMeridianLimitSlew(-30)
            self.assertEqual(False, suc)

    #
    #
    # testing setHorizonLimitLow
    #
    #

    def test_Setting_setHorizonLimitLow_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitLow(0)
            self.assertEqual(True, suc)

    def test_Setting_setHorizonLimitLow_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitLow(0)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitLow_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setHorizonLimitLow(0)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitLow_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitLow(-30)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitLow_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitLow(50)
            self.assertEqual(False, suc)

    #
    #
    # testing setHorizonLimitLow
    #
    #

    def test_Setting_setHorizonLimitHigh_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitHigh(80)
            self.assertEqual(True, suc)

    def test_Setting_setHorizonLimitHigh_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitHigh(80)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitHigh_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setHorizonLimitHigh(80)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitHigh_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitHigh(-1)
            self.assertEqual(False, suc)

    def test_Setting_setHorizonLimitHigh_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setHorizonLimitHigh(100)
            self.assertEqual(False, suc)

    #
    #
    # testing setRefractionTemp
    #
    #

    def test_Setting_setRefractionTemp_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionTemp(5)
            self.assertEqual(True, suc)

    def test_Setting_setRefractionTemp_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionTemp(5)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionTemp_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setRefractionTemp(5)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionTemp_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionTemp(-45)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionTemp_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionTemp(85)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionTemp_not_ok5(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionTemp(-0)
            self.assertEqual(True, suc)

    #
    #
    # testing setRefractionPress
    #
    #

    def test_Setting_setRefractionPress_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionPress(1000)
            self.assertEqual(True, suc)

    def test_Setting_setRefractionPress_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionPress(1000)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionPress_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setRefractionPress(1000)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionPress_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionPress(450)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionPress_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefractionPress(1400)
            self.assertEqual(False, suc)

    #
    #
    # testing setRefraction
    #
    #

    def test_Setting_setRefraction_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefraction(1)
            self.assertEqual(True, suc)

    def test_Setting_setRefraction_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setRefraction(1)
            self.assertEqual(False, suc)

    def test_Setting_setRefraction_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setRefraction(1)
            self.assertEqual(False, suc)

    #
    #
    # testing setRefractionParam
    #
    #

    def test_Setting_setRefractionParam_ok(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=800)
            self.assertEqual(True, suc)

    def test_Setting_setRefractionParam_not_ok1(self):
        setting = Setting()

        response = ['01']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=800)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok2(self):
        setting = Setting()

        response = ['10']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=800)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok3(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=800)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok4(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=-45,
                                             pressure=800)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok5(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=85,
                                             pressure=800)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok6(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=300)
            self.assertEqual(False, suc)

    def test_Setting_setRefractionParam_not_ok7(self):
        setting = Setting()

        response = ['11']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 2
            suc = setting.setRefractionParam(temperature=5,
                                             pressure=1500)
            self.assertEqual(False, suc)

    #
    #
    # testing setSlewRate
    #
    #

    def test_Setting_setSlewRate_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewRate(5)
            self.assertEqual(True, suc)

    def test_Setting_setSlewRate_not_ok1(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewRate(5)
            self.assertEqual(False, suc)

    def test_Setting_setSlewRate_not_ok2(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setSlewRate(5)
            self.assertEqual(False, suc)

    def test_Setting_setSlewRate_not_ok3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewRate(0)
            self.assertEqual(False, suc)

    def test_Setting_setSlewRate_not_ok4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewRate(25)
            self.assertEqual(False, suc)

    def test_setSlewSpeedMax(self):
        setting = Setting()
        response = []
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewSpeedMax()
            self.assertEqual(suc, True)

    def test_setSlewSpeedHigh(self):
        setting = Setting()
        response = []
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewSpeedHigh()
            self.assertEqual(suc, True)

    def test_setSlewSpeedMed(self):
        setting = Setting()
        response = []
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewSpeedMed()
            self.assertEqual(suc, True)

    def test_setSlewSpeedLow(self):
        setting = Setting()
        response = []
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setSlewSpeedLow()
            self.assertEqual(suc, True)

    #
    #
    # testing setUnattendedFlip
    #
    #

    def test_ObsSite_setUnattendedFlip_ok(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setUnattendedFlip(1)
            self.assertEqual(True, suc)

    def test_ObsSite_setUnattendedFlip_not_ok1(self):
        setting = Setting()

        response = []
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 0
            suc = setting.setUnattendedFlip(1)
            self.assertEqual(False, suc)

    #
    #
    # testing setUnattendedFlip
    #
    #

    def test_setDirectWeatherUpdateType_1(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = False, response, 1
            suc = setting.setDirectWeatherUpdateType(0)
            self.assertEqual(suc, False)

    def test_setDirectWeatherUpdateType_2(self):
        setting = Setting()

        response = ['0']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDirectWeatherUpdateType(0)
            self.assertEqual(suc, False)

    def test_setDirectWeatherUpdateType_3(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDirectWeatherUpdateType(0)
            self.assertEqual(suc, True)

    def test_setDirectWeatherUpdateType_4(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDirectWeatherUpdateType(-1)
            self.assertEqual(suc, False)

    def test_setDirectWeatherUpdateType_5(self):
        setting = Setting()

        response = ['1']
        with mock.patch('mountcontrol.setting.Connection') as mConn:
            mConn.return_value.communicate.return_value = True, response, 1
            suc = setting.setDirectWeatherUpdateType(5)
            self.assertEqual(suc, False)
