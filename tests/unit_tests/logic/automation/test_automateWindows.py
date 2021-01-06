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
import os
import platform
from unittest import mock

# external packages
from PyQt5.QtCore import QThreadPool, QObject
from skyfield.api import load

# local import
if not platform.system() == 'Windows':
    pytest.skip("skipping windows-only tests", allow_module_level=True)

from logic.automation.automateWindows import AutomateWindows
import winreg
import pywinauto
from pywinauto import timings
import pywinauto.controls.win32_controls as controls
# todo: https://github.com/pywinauto/pywinauto/issues/858


@pytest.fixture(autouse=True, scope='module')
def module(qapp):
    yield


@pytest.fixture(autouse=True, scope='function')
def function(module):

    class MountObsSite:
        ts = load.timescale(builtin=True)

    class Mount:
        obsSite = MountObsSite()

    class Test(QObject):
        threadPool = QThreadPool()
        mount = Mount()
        mwGlob = {'tempDir': 'tests/temp',
                  'dataDir': 'tests/data',
                  }

    for file in ['tai-utc.dat', 'finals2000A.all']:
        path = 'tests/data/' + file
        if os.path.isfile(path):
            os.remove(path)

    window = AutomateWindows(app=Test())
    yield window


def test_getRegistrationKeyPath_1(function):
    with mock.patch.object(platform,
                           'machine',
                           return_value='64'):
        val = function.getRegistryPath()
        assert val == 'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall'


def test_getRegistrationKeyPath_2(function):
    with mock.patch.object(platform,
                           'machine',
                           return_value='32'):
        val = function.getRegistryPath()
        assert val == 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'


def test_convertRegistryEntryToDict(function):
    with mock.patch.object(winreg,
                           'QueryInfoKey',
                           return_value=[0, 1]):
        with mock.patch.object(winreg,
                               'EnumValue',
                               return_value=['test', 'test']):
            val = function.convertRegistryEntryToDict('test')
            assert val


def test_searchNameInRegistry_1(function):
    with mock.patch.object(winreg,
                           'QueryInfoKey',
                           return_value=[1]):
        with mock.patch.object(winreg,
                               'EnumKey',
                               return_value=['test']):
            val = function.searchNameInRegistry('test', 'test')
            assert val


def test_searchNameInRegistry_2(function):
    with mock.patch.object(winreg,
                           'QueryInfoKey',
                           return_value=[1]):
        with mock.patch.object(winreg,
                               'EnumKey',
                               return_value=['test']):
            val = function.searchNameInRegistry('none', 'none')
            assert not val


def test_getNameKeyFromRegistry_1(function):
    with mock.patch.object(function,
                           'getRegistryPath',
                           return_value='test'):
        with mock.patch.object(winreg,
                               'OpenKey',
                               return_value='test'):
            with mock.patch.object(function,
                                   'searchNameInRegistry',
                                   return_value='test'):
                with mock.patch.object(winreg,
                                       'CloseKey',
                                       return_value='test'):
                    val = function.getNameKeyFromRegistry('test')
                    assert val == 'test'


def test_extractPropertiesFromRegistry_1(function):
    with mock.patch.object(function,
                           'getNameKeyFromRegistry',
                           return_value=''):
        avail, path, name = function.extractPropertiesFromRegistry('')
        assert not avail
        assert path == ''
        assert name == ''


def test_extractPropertiesFromRegistry_2(function):
    with mock.patch.object(function,
                           'getNameKeyFromRegistry',
                           return_value='test'):
        with mock.patch.object(function,
                               'getValuesForNameKeyFromRegistry',
                               return_value={}):
            avail, path, name = function.extractPropertiesFromRegistry('test')
            assert not avail
            assert path == ''
            assert name == ''


def test_extractPropertiesFromRegistry_3(function):
    with mock.patch.object(function,
                           'getNameKeyFromRegistry',
                           return_value='test'):
        with mock.patch.object(function,
                               'getValuesForNameKeyFromRegistry',
                               return_value={'DisplayName': 'test',
                                             'InstallLocation': 'test'}):
            avail, path, name = function.extractPropertiesFromRegistry('test')
            assert avail
            assert path == 'test'
            assert name == 'test'


def test_extractPropertiesFromRegistry_4(function):
    with mock.patch.object(function,
                           'getNameKeyFromRegistry',
                           return_value='test'):
        with mock.patch.object(function,
                               'getValuesForNameKeyFromRegistry',
                               return_value={'DisplayName': 'none',
                                             'InstallLocation': 'test'}):
            avail, path, name = function.extractPropertiesFromRegistry('test')
            assert not avail
            assert path == ''
            assert name == ''


def test_cycleThroughAppNames_1(function):
    with mock.patch.object(function,
                           'extractPropertiesFromRegistry',
                           return_value=(False, 'test', 'test')):
        avail, path, name = function.getAppSettings('test')
        assert not avail
        assert path == ''
        assert name == ''


def test_cycleThroughAppNames_2(function):
    with mock.patch.object(function,
                           'extractPropertiesFromRegistry',
                           return_value=(True, 'test', 'test')):
        avail, path, name = function.getAppSettings('test')
        assert avail
        assert path == 'test'
        assert name == 'test'


def test_getAppSettings_1(function):
    with mock.patch.object(function,
                           'cycleThroughAppNames',
                           return_value=(False, 'test', 'test')):
        avail, path, name = function.getAppSettings(['test'])
        assert not avail
        assert path == 'test'
        assert name == 'test'


def test_getAppSettings_2(function):
    with mock.patch.object(function,
                           'cycleThroughAppNames',
                           return_value=(False, 'test', 'test'),
                           side_effect=Exception()):
        avail, path, name = function.getAppSettings(['test'])
        assert not avail
        assert path == ''
        assert name == ''


def test_checkFloatingPointErrorWindow_1(function):
    class Test1:
        @staticmethod
        def click():
            pass

    class Test:
        @staticmethod
        def window(handle=None):
            return {'OK': Test1()}

    function.updater = Test()
    with mock.patch.object(timings,
                           'wait_until_passes'):
        suc = function.checkFloatingPointErrorWindow()
        assert suc


def test_checkFloatingPointErrorWindow_2(function):
    class Test1:
        @staticmethod
        def click():
            pass

    class Test:
        @staticmethod
        def window(handle=None):
            return {'OK': Test1()}

    function.updater = Test()
    with mock.patch.object(timings,
                           'wait_until_passes',
                           side_effect=Exception()):
        suc = function.checkFloatingPointErrorWindow()
        assert not suc


def test_checkFloatingPointErrorWindow_3(function):
    class Test1:
        @staticmethod
        def click():
            pass

    class Test:
        @staticmethod
        def window(handle=None):
            return {'OK': Test1()}

    function.updater = Test()
    with mock.patch.object(timings,
                           'wait_until_passes',
                           side_effect=timings.TimeoutError):
        suc = function.checkFloatingPointErrorWindow()
        assert suc


def test_startUpdater_1(function):
    class Test:
        @staticmethod
        def start(a):
            pass

    with mock.patch.object(platform,
                           'architecture',
                           return_value=['32bit']):
        with mock.patch.object(pywinauto,
                               'Application',
                               return_value=Test()):
            with mock.patch.object(Test,
                                   'start',
                                   side_effect=pywinauto.application.AppStartError()):
                suc = function.startUpdater()
                assert not suc


def test_startUpdater_2(function):
    class Test:
        @staticmethod
        def start(a):
            pass

    with mock.patch.object(platform,
                           'architecture',
                           return_value=['64bit']):
        with mock.patch.object(pywinauto,
                               'Application',
                               return_value=Test()):
            with mock.patch.object(Test,
                                   'start',
                                   side_effect=Exception()):
                suc = function.startUpdater()
                assert not suc


def test_startUpdater_3(function):
    class Test:
        @staticmethod
        def start(a):
            pass

    with mock.patch.object(pywinauto,
                           'Application',
                           return_value=Test()):
        with mock.patch.object(function,
                               'checkFloatingPointErrorWindow'):
            suc = function.startUpdater()
            assert suc


def test_clearUploadMenuCommands(function):
    class Test:
        @staticmethod
        def click():
            pass

        @staticmethod
        def uncheck_by_click():
            pass

    win = {'next': Test(),
           'Control box firmware': Test(),
           'Orbital parameters of comets': Test(),
           'Orbital parameters of asteroids': Test(),
           'Orbital parameters of satellites': Test(),
           'UTC / Earth rotation data': Test()
           }
    function.updater = {'10 micron control box update': win}
    with mock.patch.object(controls,
                           'ButtonWrapper'):
        suc = function.clearUploadMenuCommands()
        assert suc


def test_clearUploadMenu_1(function):
    with mock.patch.object(function,
                           'clearUploadMenuCommands'):
        suc = function.clearUploadMenu()
        assert suc


def test_clearUploadMenu_2(function):
    with mock.patch.object(function,
                           'clearUploadMenuCommands',
                           side_effect=Exception()):
        suc = function.clearUploadMenu()
        assert not suc


def test_prepareUpdater_0(function):
    function.installPath = ''
    with mock.patch.object(os,
                           'chdir'):
        with mock.patch.object(function,
                               'startUpdater',
                               return_value=False):
            suc = function.prepareUpdater()
            assert not suc


def test_prepareUpdater_1(function):
    with mock.patch.object(os,
                           'chdir'):
        with mock.patch.object(function,
                               'startUpdater',
                               return_value=False):
            suc = function.prepareUpdater()
            assert not suc


def test_prepareUpdater_2(function):
    with mock.patch.object(os,
                           'chdir'):
        with mock.patch.object(function,
                               'startUpdater',
                               return_value=True):
            with mock.patch.object(function,
                                   'clearUploadMenu',
                                   return_value=False):
                suc = function.prepareUpdater()
                assert not suc


def test_prepareUpdater_3(function):
    with mock.patch.object(os,
                           'chdir'):
        with mock.patch.object(function,
                               'startUpdater',
                               return_value=True):
            with mock.patch.object(function,
                                   'clearUploadMenu',
                                   return_value=True):
                suc = function.prepareUpdater()
                assert suc


def test_doUploadAndCloseInstallerCommands(function):
    class Test:
        @staticmethod
        def click():
            pass

    win = {'next': Test(),
           'Update Now': Test(),
           'OK': Test()
           }
    function.updater = {'10 micron control box update': win}
    with mock.patch.object(timings,
                           'wait_until_passes'):
        suc = function.doUploadAndCloseInstallerCommands()
        assert suc


def test_pressOK(function):
    class Test1:
        @staticmethod
        def click():
            pass

    class Test:
        @staticmethod
        def window(handle=None):
            return {'OK': Test1()}

    function.updater = Test()
    with mock.patch.object(timings,
                           'wait_until_passes'):
        suc = function.pressOK()
        assert suc


def test_doUploadAndCloseInstaller_1(function):
    with mock.patch.object(function,
                           'doUploadAndCloseInstallerCommands'):
        with mock.patch.object(function,
                               'pressOK'):
            suc = function.doUploadAndCloseInstaller()
            assert suc


def test_doUploadAndCloseInstaller_2(function):
    with mock.patch.object(function,
                           'doUploadAndCloseInstallerCommands'):
        with mock.patch.object(function,
                               'pressOK',
                               side_effect=Exception()):
            suc = function.doUploadAndCloseInstaller()
            assert not suc


def test_uploadMPCDataCommands_1(function):
    class Test:
        @staticmethod
        def click():
            pass

        @staticmethod
        def check_by_click():
            pass

        @staticmethod
        def set_text(a):
            pass

    win = {'Orbital parameters of comets': Test(),
           'Orbital parameters of asteroids': Test(),
           'Edit...4': Test(),
           'Edit...3': Test(),
           }
    popup = {'MPC file': Test(),
             'Close': Test(),
             }
    dialog = {'OpenButton4': Test(),
              'Button16': Test(),
              'File &name:Edit': Test(),
              }
    function.updater = {'10 micron control box update': win,
                        'Asteroid orbits': popup,
                        'Comet orbits': popup,
                        'Dialog': dialog,
                        }
    with mock.patch.object(controls,
                           'ButtonWrapper'):
        with mock.patch.object(controls,
                               'EditWrapper'):
            suc = function.uploadMPCDataCommands()
            assert suc


def test_uploadMPCDataCommands_2(function):
    class Test:
        @staticmethod
        def click():
            pass

        @staticmethod
        def check_by_click():
            pass

        @staticmethod
        def set_text(a):
            pass

    win = {'Orbital parameters of comets': Test(),
           'Orbital parameters of asteroids': Test(),
           'Edit...4': Test(),
           'Edit...3': Test(),
           }
    popup = {'MPC file': Test(),
             'Close': Test(),
             }
    dialog = {'OpenButton4': Test(),
              'Button16': Test(),
              'File &name:Edit': Test(),
              }
    function.updater = {'10 micron control box update': win,
                        'Asteroid orbits': popup,
                        'Comet orbits': popup,
                        'Dialog': dialog,
                        }
    with mock.patch.object(controls,
                           'ButtonWrapper'):
        with mock.patch.object(controls,
                               'EditWrapper'):
            suc = function.uploadMPCDataCommands(comets=True)
            assert suc


def test_uploadMPCData_1(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadMPCDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=False):
                suc = function.uploadMPCData()
                assert not suc


def test_uploadMPCData_2(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadMPCDataCommands',
                               side_effect=Exception()):
            suc = function.uploadMPCData()
            assert not suc


def test_uploadMPCData_3(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadMPCDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                suc = function.uploadMPCData()
                assert suc


def test_uploadMPCData_4(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadMPCDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                with mock.patch.object(platform,
                                       'architecture',
                                       return_value=['64bit']):
                    suc = function.uploadMPCData()
                    assert suc


def test_uploadEarthRotationDataCommands(function):
    class Test:
        @staticmethod
        def click():
            pass

        @staticmethod
        def check_by_click():
            pass

        @staticmethod
        def set_text(a):
            pass

    win = {'UTC / Earth rotation data': Test(),
           'Edit...1': Test(),
           }
    popup = {'Import files...': Test()
             }
    dialog = {'OpenButton4': Test(),
              'Button16': Test(),
              'File &name:Edit': Test(),
              }
    ok = {'OK': Test()
          }
    function.updater = {'10 micron control box update': win,
                        'UTC / Earth rotation data': popup,
                        'Open finals data': dialog,
                        'Open tai-utc.dat': dialog,
                        'UTC data': ok
                        }
    with mock.patch.object(controls,
                           'ButtonWrapper'):
        with mock.patch.object(controls,
                               'EditWrapper'):
            suc = function.uploadEarthRotationDataCommands()
            assert suc


def test_uploadEarthRotationData_1(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadEarthRotationDataCommands',
                               side_effect=Exception()):
            suc = function.uploadEarthRotationData()
            assert not suc


def test_uploadEarthRotationData_2(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadEarthRotationDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=False):
                suc = function.uploadEarthRotationData()
                assert not suc


def test_uploadEarthRotationData_3(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadEarthRotationDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                suc = function.uploadEarthRotationData()
                assert suc


def test_uploadEarthRotationData_4(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadEarthRotationDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                with mock.patch.object(platform,
                                       'architecture',
                                       return_value=['64bit']):
                    suc = function.uploadEarthRotationData()
                    assert suc


def test_uploadTLEDataCommands(function):
    class Test:
        @staticmethod
        def click():
            pass

        @staticmethod
        def check_by_click():
            pass

        @staticmethod
        def set_text(a):
            pass

    win = {'Orbital parameters of satellites': Test(),
           'Edit...2': Test(),
           }
    popup = {'Load from file': Test(),
             'Close': Test(),
             }
    dialog = {'OpenButton4': Test(),
              'Button16': Test(),
              'File &name:Edit': Test(),
              }
    function.updater = {'10 micron control box update': win,
                        'Satellites orbits': popup,
                        'Dialog': dialog,
                        }

    with mock.patch.object(controls,
                           'ButtonWrapper'):
        with mock.patch.object(controls,
                               'EditWrapper'):
            suc = function.uploadTLEDataCommands()
            assert suc


def test_uploadTLEData_1(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadTLEDataCommands',
                               side_effect=Exception()):
            suc = function.uploadTLEData()
            assert not suc


def test_uploadTLEData_2(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadTLEDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=False):
                suc = function.uploadTLEData()
                assert not suc


def test_uploadTLEData_3(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadTLEDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                suc = function.uploadTLEData()
                assert suc


def test_uploadTLEData_4(function):
    function.actualWorkDir = os.getcwd()
    with mock.patch.object(function,
                           'prepareUpdater'):
        with mock.patch.object(function,
                               'uploadTLEDataCommands'):
            with mock.patch.object(function,
                                   'doUploadAndCloseInstaller',
                                   return_value=True):
                with mock.patch.object(platform,
                                       'architecture',
                                       return_value=['64bit']):
                    suc = function.uploadTLEData()
                    assert suc
