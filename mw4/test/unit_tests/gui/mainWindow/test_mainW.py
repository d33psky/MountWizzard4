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
# written in python 3, (c) 2019, 2020 by mworion
#
# Licence APL2.0
#
###########################################################
import mw4.base.packageConfig as Config
# standard libraries
import unittest.mock as mock
import pytest
import glob
import os
import gc
import shutil
import faulthandler
faulthandler.enable()

# external packages
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QTimer
from mountcontrol.qtmount import Mount
from skyfield.api import Topos
from skyfield.api import load

# local import
from mw4.gui.mainW import MainWindow
from mw4.gui.imageW import ImageWindow
from mw4.environment.sensorWeather import SensorWeather
from mw4.environment.directWeather import DirectWeather
from mw4.environment.onlineWeather import OnlineWeather
from mw4.environment.skymeter import Skymeter
from mw4.powerswitch.kmRelay import KMRelay
from mw4.powerswitch.pegasusUPB import PegasusUPB
from mw4.dome.dome import Dome
from mw4.imaging.camera import Camera
from mw4.imaging.filter import Filter
from mw4.imaging.focuser import Focuser
from mw4.cover.flipflat import FlipFlat
from mw4.modeldata.buildpoints import DataPoint
from mw4.remote.remote import Remote
from mw4.measure.measure import MeasureData
from mw4.telescope.telescope import Telescope
from mw4.astrometry.astrometry import Astrometry


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global eph
    eph = load('mw4/test/testData/de421_23.bsp')


@pytest.fixture(autouse=True, scope='function')
def function_setup_teardown(qtbot):
    global app

    class Test1(QObject):
        threadPool = QThreadPool()
        mount = Mount(host='localhost', MAC='00:00:00:00:00:00', expire=False, verbose=False,
                      pathToData='mw4/test/data')
        update10s = pyqtSignal()
        update1s = pyqtSignal()

    @staticmethod
    def testShowWindows():
        return

    @staticmethod
    def testSave(name=None):
        return

    @staticmethod
    def testStore():
        return

    @staticmethod
    def testQuit():
        return

    @staticmethod
    def testInitConfig():
        return

    class Test(QObject):
        __version__ = 'test'
        config = {'mainW': {},
                  'showImageW': True}
        update1s = pyqtSignal()
        redrawSimulator = pyqtSignal()
        showImage = pyqtSignal(str)
        update3s = pyqtSignal()
        update30m = pyqtSignal()
        remoteCommand = pyqtSignal(str)
        threadPool = QThreadPool()
        message = pyqtSignal(str, int)
        mount = Mount(host='localhost', MAC='00:00:00:00:00:00', expire=False, verbose=False,
                      pathToData='mw4/test/data')
        mount.obsSite.location = Topos(latitude_degrees=20,
                                       longitude_degrees=10,
                                       elevation_m=500)
        camera = Camera(app=Test1())
        filter = Filter(app=Test1())
        focuser = Focuser(app=Test1())
        sensorWeather = SensorWeather(app=Test1())
        onlineWeather = OnlineWeather(app=Test1())
        directWeather = DirectWeather(app=Test1())
        skymeter = Skymeter(app=Test1())
        dome = Dome(app=Test1())
        cover = FlipFlat(app=Test1())
        telescope = Telescope(app=Test1())
        relay = KMRelay()
        remote = Remote()
        data = DataPoint()
        ephemeris = eph
        measure = MeasureData(app=Test1())
        power = PegasusUPB(app=Test1())
        astrometry = Astrometry(app=Test1())
        timer0_1s = QTimer()

        uiWindows = {'showImageW': {'classObj': None}}
        mwGlob = {'imageDir': 'mw4/test/image',
                  'dataDir': 'mw4/test/data',
                  'modelDir': 'mw4/test/model',
                  'configDir': 'mw4/test/config'}
        deviceStat = {'camera': True,
                      'astrometry': True,
                      'mount': True}
        quit = testQuit
        quitSave = testQuit
        loadConfig = testQuit
        saveConfig = testSave
        storeConfig = testStore
        showWindows = testShowWindows
        initConfig = testInitConfig

    shutil.copy2('mw4/test/testData/active.txt', 'mw4/test/data/active.txt')

    with mock.patch.object(MainWindow,
                           'show'):
        with mock.patch.object(ImageWindow,
                               'show'):
            app = MainWindow(app=Test())
            yield

    files = glob.glob('mw4/test/config/*.cfg')
    for f in files:
        os.remove(f)


def test_mwSuper():
    suc = app.mwSuper('')
    assert suc


def test_initConfig_1():
    app.app.config['mainW'] = {}
    with mock.patch.object(app,
                           'mwSuper'):
        suc = app.initConfig()
        assert suc


def test_initConfig_2():
    del app.app.config['mainW']
    with mock.patch.object(app,
                           'mwSuper'):
        suc = app.initConfig()
        assert suc


def test_initConfig_3():
    app.app.config['mainW'] = {}
    app.app.config['mainW']['winPosX'] = 10000
    app.app.config['mainW']['winPosY'] = 10000
    with mock.patch.object(app,
                           'mwSuper'):
        suc = app.initConfig()
        assert suc


def test_storeConfigExtendedWindows_1():
    suc = app.storeConfigExtendedWindows()
    assert suc


def test_storeConfig_1():
    with mock.patch.object(app,
                           'mwSuper'):
        suc = app.storeConfig()
        assert suc


def test_storeConfig_2():
    del app.app.config['mainW']
    with mock.patch.object(app,
                           'mwSuper'):
        suc = app.storeConfig()
        assert suc


def test_closeEvent_1(qtbot):
    app.closeEvent(QCloseEvent())


def test_quitSave_1(qtbot):
    app.ui.profile.setText('test')
    suc = app.quitSave()
    assert suc


def test_setupIcons():
    suc = app.setupIcons()
    assert suc


def test_updateMountConnStat_1():
    suc = app.updateMountConnStat(True)
    assert suc
    assert app.deviceStat['mount']


def test_updateMountConnStat_2():
    suc = app.updateMountConnStat(False)
    assert suc
    assert not app.deviceStat['mount']


def test_updateMountWeatherStat_1():
    class S:
        weatherPressure = None
        weatherTemperature = None
        weatherStatus = None

    suc = app.updateMountWeatherStat(S())
    assert suc
    assert app.deviceStat['directWeather'] is None


def test_updateMountWeatherStat_2():
    class S:
        weatherPressure = 1000
        weatherTemperature = 10
        weatherStatus = None

    suc = app.updateMountWeatherStat(S())
    assert suc
    assert not app.deviceStat['directWeather']


def test_updateMountWeatherStat_3():
    class S:
        weatherPressure = 1000
        weatherTemperature = 10
        weatherStatus = True

    suc = app.updateMountWeatherStat(S())
    assert suc
    assert app.deviceStat['directWeather']


def test_smartFunctionGui_1():
    app.deviceStat['mount'] = True
    app.deviceStat['camera'] = True
    app.deviceStat['astrometry'] = True
    app.app.data.buildP = [(0, 0)]
    suc = app.smartFunctionGui()
    assert suc
    assert app.ui.runModel.isEnabled()
    assert app.ui.plateSolveSync.isEnabled()


def test_smartFunctionGui_2():
    app.deviceStat['mount'] = True
    app.deviceStat['camera'] = False
    app.deviceStat['astrometry'] = True
    app.app.data.buildP = [(0, 0)]
    suc = app.smartFunctionGui()
    assert suc
    assert not app.ui.runModel.isEnabled()
    assert not app.ui.plateSolveSync.isEnabled()


def test_smartFunctionGui_3():
    app.deviceStat['mount'] = True
    suc = app.smartFunctionGui()
    assert suc
    assert app.ui.batchModel.isEnabled()


def test_smartFunctionGui_4():
    app.deviceStat['mount'] = False
    suc = app.smartFunctionGui()
    assert suc
    assert not app.ui.batchModel.isEnabled()


def test_smartFunctionGui_5():
    app.deviceStat['environOverall'] = None
    suc = app.smartFunctionGui()
    assert suc
    assert not app.ui.refractionGroup.isEnabled()
    assert not app.ui.setRefractionManual.isEnabled()


def test_smartFunctionGui_6():
    app.deviceStat['environOverall'] = True
    app.deviceStat['mount'] = True
    suc = app.smartFunctionGui()
    assert suc
    assert app.ui.refractionGroup.isEnabled()
    assert app.ui.setRefractionManual.isEnabled()


def test_smartFunctionGui_7():
    app.deviceStat['environOverall'] = True
    app.deviceStat['mount'] = False
    suc = app.smartFunctionGui()
    assert suc
    assert not app.ui.refractionGroup.isEnabled()
    assert not app.ui.setRefractionManual.isEnabled()


def test_smartTabGui_1():
    suc = app.smartTabGui()
    assert suc


def test_mountBoot1(qtbot):
    with mock.patch.object(app.app.mount,
                           'bootMount',
                           return_value=True):
        with qtbot.waitSignal(app.app.message) as blocker:
            suc = app.mountBoot()
            assert suc
        assert ['Sent boot command to mount', 0] == blocker.args


def test_smartEnvironGui_1():
    app.deviceStat['directWeather'] = False
    app.deviceStat['sensorWeather'] = False
    app.deviceStat['onlineWeather'] = False
    app.deviceStat['skymeter'] = False
    app.deviceStat['power'] = False
    suc = app.smartEnvironGui()
    assert suc
    assert not app.ui.directWeatherGroup.isEnabled()
    assert not app.ui.sensorWeatherGroup.isEnabled()
    assert not app.ui.onlineWeatherGroup.isEnabled()
    assert not app.ui.skymeterGroup.isEnabled()
    assert not app.ui.powerGroup.isEnabled()


def test_smartEnvironGui_2():
    app.deviceStat['directWeather'] = True
    app.deviceStat['sensorWeather'] = True
    app.deviceStat['onlineWeather'] = True
    app.deviceStat['skymeter'] = True
    app.deviceStat['power'] = True
    suc = app.smartEnvironGui()
    assert suc
    assert app.ui.directWeatherGroup.isEnabled()
    assert app.ui.sensorWeatherGroup.isEnabled()
    assert app.ui.onlineWeatherGroup.isEnabled()
    assert app.ui.skymeterGroup.isEnabled()
    assert app.ui.powerGroup.isEnabled()


def test_smartEnvironGui_3():
    app.deviceStat['directWeather'] = None
    app.deviceStat['sensorWeather'] = None
    app.deviceStat['onlineWeather'] = None
    app.deviceStat['skymeter'] = None
    app.deviceStat['power'] = None
    suc = app.smartEnvironGui()
    assert suc
    assert not app.ui.directWeatherGroup.isEnabled()
    assert not app.ui.sensorWeatherGroup.isEnabled()
    assert not app.ui.onlineWeatherGroup.isEnabled()
    assert not app.ui.skymeterGroup.isEnabled()
    assert not app.ui.powerGroup.isEnabled()


def test_updateWindowsStats_1():
    app.app.uiWindows = {'showMessageW': {'classObj': 1,
                                          'button': QPushButton()}}
    suc = app.updateWindowsStats()
    assert suc


def test_updateDeviceStats_1():
    app.deviceStat = {'online': True}
    app.refractionSource = 'online'
    suc = app.updateDeviceStats()
    assert suc
    assert app.deviceStat['environOverall']


def test_updateDeviceStats_2():
    app.deviceStat = {'test': True}
    app.refractionSource = 'online'
    suc = app.updateDeviceStats()
    assert suc
    assert app.deviceStat['environOverall'] is None


def test_updateDeviceStats_3():
    app.deviceStat = {'online': True}
    app.refractionSource = 'online'
    suc = app.updateDeviceStats()
    assert suc


def test_updateDeviceStats_4():
    app.deviceStat = {}
    app.refractionSource = 'online'
    suc = app.updateDeviceStats()
    assert suc


def test_updateOnlineWeatherStat_1():
    suc = app.updateOnlineWeatherStat(True)
    assert suc
    assert app.deviceStat['onlineWeather']


def test_updateOnlineWeatherStat_2():
    suc = app.updateOnlineWeatherStat(False)
    assert suc
    assert not app.deviceStat['onlineWeather']


def test_updateTime_1():
    app.ui.isOnline.setChecked(True)
    suc = app.updateTime()
    assert suc


def test_updateTime_2():
    app.ui.isOnline.setChecked(False)
    suc = app.updateTime()
    assert suc


def test_updateAstrometryStatus():
    suc = app.updateAstrometryStatus('test')
    assert suc
    assert app.ui.astrometryText.text() == 'test'


def test_updateDomeStatus():
    suc = app.updateDomeStatus('test')
    assert suc
    assert app.ui.domeText.text() == 'test'


def test_updateCameraStatus():
    suc = app.updateCameraStatus('test')
    assert suc
    assert app.ui.cameraText.text() == 'test'


def test_updateStatusGUI_1():
    class OB:
        @staticmethod
        def statusText():
            return None

    app.app.mount.obsSite.status = 0
    suc = app.updateStatusGUI(OB)
    assert suc


def test_updateStatusGUI_2():
    class OB:
        @staticmethod
        def statusText():
            return 'test'

    app.app.mount.obsSite.status = 0
    suc = app.updateStatusGUI(OB)
    assert suc
    assert app.ui.statusText.text() == 'test'


def test_updateStatusGUI_3():
    class OB:
        @staticmethod
        def statusText():
            return None

    app.app.mount.obsSite.status = 5
    suc = app.updateStatusGUI(OB)
    assert suc


def test_updateStatusGUI_4():
    class OB:
        @staticmethod
        def statusText():
            return None

    app.app.mount.obsSite.status = 1
    suc = app.updateStatusGUI(OB)
    assert suc


def test_deleteWindowResource_1():
    suc = app.deleteWindowResource()
    assert not suc


def test_deleteWindowResource_2():
    suc = app.deleteWindowResource(widget=app.ui.openImageW)
    assert suc


def test_deleteWindowResource_3():
    class Test:
        @staticmethod
        def objectName():
            return 'ImageDialog'

    with mock.patch.object(gc,
                           'collect'):
        suc = app.deleteWindowResource(widget=Test())
        assert suc


def test_buildWindow_1():
    class Test(QObject):
        destroyed = pyqtSignal()

    app.uiWindows['showImageW']['classObj'] = Test()

    suc = app.buildWindow('showImageW')
    assert suc


def test_toggleWindow_1():
    suc = app.toggleWindow()
    assert suc


def test_toggleWindow_2():
    def Sender():
        return app.ui.openImageW

    app.sender = Sender
    app.uiWindows['showImageW']['classObj'] = None

    with mock.patch.object(app,
                           'buildWindow'):
        suc = app.toggleWindow()
        assert suc


def test_toggleWindow_3():
    def Sender():
        return app.ui.openImageW

    app.sender = Sender
    app.uiWindows['showImageW']['classObj'] = 1

    suc = app.toggleWindow()
    assert suc


def test_showExtendedWindows_1():
    with mock.patch.object(app,
                           'buildWindow'):
        suc = app.showExtendedWindows()
        assert suc


def test_closeExtendedWindows_1():
    suc = app.closeExtendedWindows()
    assert suc


def test_checkExtension_1():
    val = app.checkExtension('mw4/test/image/test.fit', 'fit')
    assert val == 'mw4/test/image/test.fit'


def test_checkExtension_2():
    val = app.checkExtension('mw4/test/image/test', '.fit')
    assert val == 'mw4/test/image/test.fit'


def test_mountBoot2(qtbot):
    with mock.patch.object(app.app.mount,
                           'bootMount',
                           return_value=False):
        with qtbot.waitSignal(app.app.message) as blocker:
            suc = app.mountBoot()
            assert not suc
        assert ['Mount cannot be booted', 2] == blocker.args


def test_mountShutdown1(qtbot):
    with mock.patch.object(app.app.mount.obsSite,
                           'shutdown',
                           return_value=True):
        with qtbot.waitSignal(app.app.message) as blocker:
            suc = app.mountShutdown()
            assert suc
        assert ['Shutting mount down', 0] == blocker.args


def test_mountShutdown2(qtbot):
    with mock.patch.object(app.app.mount.obsSite,
                           'shutdown',
                           return_value=False):
        with qtbot.waitSignal(app.app.message) as blocker:
            suc = app.mountShutdown()
            assert not suc
        assert ['Mount cannot be shutdown', 2] == blocker.args


def test_saveProfile1(qtbot):
    with mock.patch.object(app.app,
                           'saveConfig',
                           return_value=True):
        with qtbot.waitSignal(app.app.message) as blocker:
            app.saveProfile()
        assert ['Actual profile saved', 0] == blocker.args


def test_loadProfile1(qtbot):
    with mock.patch.object(app,
                           'openFile',
                           return_value=('config', 'test', 'cfg')):
        with mock.patch.object(app.app,
                               'loadConfig',
                               return_value=True):
            with mock.patch.object(app,
                                   'closeExtendedWindows'):
                with mock.patch.object(app,
                                       'showExtendedWindows'):
                    with mock.patch.object(app,
                                           'initConfig'):
                        with qtbot.waitSignal(app.app.message) as blocker:
                            suc = app.loadProfile()
                            assert suc
                        assert ['Profile: [test] loaded', 0] == blocker.args


def test_loadProfile2(qtbot):
    with mock.patch.object(app,
                           'openFile',
                           return_value=('config', 'test', 'cfg')):
        with mock.patch.object(app.app,
                               'loadConfig',
                               return_value=False):
            with mock.patch.object(app,
                                   'closeExtendedWindows'):
                with mock.patch.object(app,
                                       'showExtendedWindows'):
                    with mock.patch.object(app,
                                           'initConfig'):
                        with qtbot.waitSignal(app.app.message) as blocker:
                            suc = app.loadProfile()
                            assert suc
                        assert ['Profile: [test] cannot no be loaded', 2] == blocker.args


def test_loadProfile3(qtbot):
    with mock.patch.object(app,
                           'openFile',
                           return_value=(None, None, 'cfg')):
        suc = app.loadProfile()
        assert not suc


def test_saveProfileAs1(qtbot):
    with mock.patch.object(app,
                           'saveFile',
                           return_value=('config', 'test', 'cfg')):
        with mock.patch.object(app.app,
                               'saveConfig',
                               return_value=True):
            with qtbot.waitSignal(app.app.message) as blocker:
                suc = app.saveProfileAs()
                assert suc
            assert ['Profile: [test] saved', 0] == blocker.args


def test_saveProfileAs2(qtbot):
    with mock.patch.object(app,
                           'saveFile',
                           return_value=('config', 'test', 'cfg')):
        with mock.patch.object(app.app,
                               'saveConfig',
                               return_value=False):
            with qtbot.waitSignal(app.app.message) as blocker:
                suc = app.saveProfileAs()
                assert suc
            assert ['Profile: [test] cannot no be saved', 2] == blocker.args


def test_saveProfileAs3(qtbot):
    with mock.patch.object(app,
                           'saveFile',
                           return_value=(None, None, 'cfg')):
        suc = app.saveProfileAs()
        assert not suc


def test_saveProfile2(qtbot):
    with mock.patch.object(app.app,
                           'saveConfig',
                           return_value=False):
        with qtbot.waitSignal(app.app.message) as blocker:
            app.saveProfile()
        assert ['Actual profile cannot not be saved', 2] == blocker.args


def test_remoteCommand_1():
    suc = app.remoteCommand('')
    assert suc


def test_remoteCommand_2(qtbot):
    with qtbot.waitSignal(app.app.message) as blocker:
        with mock.patch.object(app.app,
                               'quitSave'):
            suc = app.remoteCommand('shutdown')
            assert suc
            assert ['Actual profile cannot not be saved', 2] == blocker.args


def test_remoteCommand_3(qtbot):
    with qtbot.waitSignal(app.app.message) as blocker:
        with mock.patch.object(app,
                               'mountShutdown'):
            suc = app.remoteCommand('shutdown mount')
            assert suc
            assert ['Shutdown mount remotely', 2] == blocker.args


def test_remoteCommand_4(qtbot):
    with qtbot.waitSignal(app.app.message) as blocker:
        with mock.patch.object(app,
                               'mountBoot'):
            suc = app.remoteCommand('boot mount')
            assert suc
            assert ['Boot mount remotely', 2] == blocker.args
