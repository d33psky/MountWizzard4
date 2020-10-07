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
# GUI with PyQT5 for python !

#
# written in python3 , (c) 2019, 2020 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries
import unittest.mock as mock
import pytest
import time
import os
import shutil
import glob

# external packages
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox
from mountcontrol.qtmount import Mount
import skyfield.api
from skyfield.api import Angle
from skyfield.api import Topos
from mountcontrol.modelStar import ModelStar

# local import
from gui.mainWmixin.tabModel import Model
from gui.widgets.main_ui import Ui_MainWindow
from gui.utilities.widget import MWidget
from logic.imaging.camera import Camera
from logic.dome.dome import Dome
from logic.astrometry.astrometry import Astrometry
from logic.modeldata.buildpoints import DataPoint


@pytest.fixture(autouse=True, scope='module')
def module(qapp):
    yield


@pytest.fixture(autouse=True, scope='function')
def function(module):
    class Test3:
        checkAutoSolve = QCheckBox()
        checkStackImages = QCheckBox()

    class Test2:
        deviceStat = {}
        ui = Test3()

        @staticmethod
        def abortImage():
            pass

    class Test1(QObject):
        mount = Mount(host='localhost', MAC='00:00:00:00:00:00', verbose=False,
                      pathToData='tests/data')
        update1s = pyqtSignal()
        update10s = pyqtSignal()
        threadPool = QThreadPool()
        mwGlob = {'modelDir': 'tests/model',
                  'imageDir': 'tests/image',
                  'configDir': 'tests/config',
                  'tempDir': 'tests/temp'}

    class Test(QObject):
        config = {'mainW': {}}
        threadPool = QThreadPool()
        update1s = pyqtSignal()
        showImage = pyqtSignal(str)
        updatePointMarker = pyqtSignal()
        __version__ = 'test'
        message = pyqtSignal(str, int)
        mount = Mount(host='localhost', MAC='00:00:00:00:00:00', verbose=False,
                      pathToData='tests/data')
        mount.obsSite.location = Topos(latitude_degrees=20,
                                       longitude_degrees=10,
                                       elevation_m=500)
        data = DataPoint(app=Test1())
        camera = Camera(app=Test1())
        astrometry = Astrometry(app=Test1())
        dome = Dome(app=Test1())
        mwGlob = {'modelDir': 'tests/model',
                  'configDir': 'tests/config',
                  'imageDir': 'tests/image'}
        uiWindows = {'showImageW': {'classObj': Test2()}}

    class Mixin(MWidget, Model):
        def __init__(self):
            super().__init__()
            self.app = Test()
            self.deviceStat = {}
            self.refreshName = None
            self.refreshModel = None
            self.playSound = None
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            Model.__init__(self)

    window = Mixin()
    yield window

    files = glob.glob('tests/model/m-*.model')
    for f in files:
        os.remove(f)
    for path in glob.glob('tests/image/m-*'):
        shutil.rmtree(path)


def test_initConfig_1(function):
    function.app.config['mainW'] = {}
    suc = function.initConfig()
    assert suc


def test_storeConfig_1(function):
    suc = function.storeConfig()
    assert suc


def test_updateAlignGui_numberStars(function):
    value = '50'
    function.app.mount.model.numberStars = value
    function.updateAlignGUI(function.app.mount.model)
    assert ' 50' == function.ui.numberStars.text()
    assert ' 50' == function.ui.numberStars1.text()
    value = None
    function.app.mount.model.numberStars = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.numberStars.text()
    assert '-' == function.ui.numberStars1.text()


def test_updateAlignGui_altitudeError(function):
    value = '50'
    function.app.mount.model.altitudeError = value
    function.updateAlignGUI(function.app.mount.model)
    assert ' 50.0' == function.ui.altitudeError.text()
    value = None
    function.app.mount.model.altitudeError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.altitudeError.text()


def test_updateAlignGui_errorRMS(function):
    value = '50'
    function.app.mount.model.errorRMS = value
    function.updateAlignGUI(function.app.mount.model)
    assert '50.0' == function.ui.errorRMS.text()
    assert '50.0' == function.ui.errorRMS1.text()
    value = None
    function.app.mount.model.errorRMS = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.errorRMS.text()
    assert '-' == function.ui.errorRMS1.text()


def test_updateAlignGui_azimuthError(function):
    value = '50'
    function.app.mount.model.azimuthError = value
    function.updateAlignGUI(function.app.mount.model)
    assert ' 50.0' == function.ui.azimuthError.text()
    value = None
    function.app.mount.model.azimuthError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.azimuthError.text()


def test_updateAlignGui_terms(function):
    value = '50'
    function.app.mount.model.terms = value
    function.updateAlignGUI(function.app.mount.model)
    assert '50' == function.ui.terms.text()
    value = None
    function.app.mount.model.terms = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.terms.text()


def test_updateAlignGui_orthoError(function):
    value = '50'
    function.app.mount.model.orthoError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '180000' == function.ui.orthoError.text()
    value = None
    function.app.mount.model.orthoError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.orthoError.text()


def test_updateAlignGui_positionAngle(function):
    value = '50'
    function.app.mount.model.positionAngle = value
    function.updateAlignGUI(function.app.mount.model)
    assert ' 50.0' == function.ui.positionAngle.text()
    value = None
    function.app.mount.model.positionAngle = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.positionAngle.text()


def test_updateAlignGui_polarError(function):
    value = '50'
    function.app.mount.model.polarError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '180000' == function.ui.polarError.text()
    value = None
    function.app.mount.model.polarError = value
    function.updateAlignGUI(function.app.mount.model)
    assert '-' == function.ui.polarError.text()


def test_updateTurnKnobsGUI_altitudeTurns_1(function):
    value = 1.5
    function.app.mount.model.altitudeTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '1.50 revs down' == function.ui.altitudeTurns.text()
    value = None
    function.app.mount.model.altitudeTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '-' == function.ui.altitudeTurns.text()


def test_updateTurnKnobsGUI_altitudeTurns_2(function):
    value = -1.5
    function.app.mount.model.altitudeTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '1.50 revs up' == function.ui.altitudeTurns.text()
    value = None
    function.app.mount.model.altitudeTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '-' == function.ui.altitudeTurns.text()


def test_updateTurnKnobsGUI_azimuthTurns_1(function):
    value = 1.5
    function.app.mount.model.azimuthTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '1.50 revs left' == function.ui.azimuthTurns.text()
    value = None
    function.app.mount.model.azimuthTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '-' == function.ui.azimuthTurns.text()


def test_updateTurnKnobsGUI_azimuthTurns_2(function):
    value = -1.5
    function.app.mount.model.azimuthTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '1.50 revs right' == function.ui.azimuthTurns.text()
    value = None
    function.app.mount.model.azimuthTurns = value
    function.updateTurnKnobsGUI(function.app.mount.model)
    assert '-' == function.ui.azimuthTurns.text()


def test_updateProgress_1(function):
    function.startModeling = time.time()
    suc = function.updateProgress()
    assert not suc


def test_updateProgress_2(function):
    function.startModeling = time.time()
    suc = function.updateProgress(number=3, count=2)
    assert suc


def test_updateProgress_3(function):
    function.startModeling = time.time()
    suc = function.updateProgress(number=2, count=3)
    assert not suc


def test_updateProgress_4(function):
    suc = function.updateProgress(number=0, count=2)
    function.startModeling = time.time()
    assert not suc


def test_updateProgress_5(function):
    function.startModeling = time.time()
    suc = function.updateProgress(number=3, count=1)
    assert suc


def test_updateProgress_6(function):
    function.startModeling = time.time()
    suc = function.updateProgress(number=3, count=-1)
    assert not suc


def test_updateProgress_7(function):
    function.startModeling = time.time()
    suc = function.updateProgress(number=3, count=2)
    assert suc


def test_updateProgress_8(function):
    function.startModeling = time.time()
    suc = function.updateProgress(count=-1)
    assert not suc


def test_modelSolveDone_0(function, qtbot):
    result = {'raJ2000S': 0,
              'decJ2000S': 0,
              'angleS': 0,
              'scaleS': 1,
              'errorRMS_S': 1,
              'flippedS': False,
              'success': False,
              'message': 'test',
              }

    suc = function.modelSolveDone(result)
    assert not suc


def test_modelSolveDone_1(function, qtbot):
    mPoint = {'lenSequence': 3,
              'countSequence': 3}

    function.resultQueue.put(mPoint)

    result = {'raJ2000S': 0,
              'decJ2000S': 0,
              'angleS': 0,
              'scaleS': 1,
              'errorRMS_S': 1,
              'flippedS': False,
              'success': False,
              'message': 'test',
              }

    with qtbot.waitSignal(function.app.message) as blocker:
        with mock.patch.object(function,
                               'updateProgress'):
            with mock.patch.object(function,
                                   'modelCycleThroughBuildPointsFinished'):
                suc = function.modelSolveDone(result)
                assert suc
    assert ['Solving  image-003:  test', 2] == blocker.args


def test_modelSolveDone_2(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3}

    function.resultQueue.put(mPoint)

    suc = function.modelSolveDone({})
    assert not suc


def test_modelSolveDone_3(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3}

    function.resultQueue.put(mPoint)
    function.app.data.buildP = [(0, 0, True), (1, 1, True), (2, 2, True)]

    class Julian:
        ut1 = 2458635.168

    result = {'raJ2000S': skyfield.api.Angle(hours=0),
              'decJ2000S': skyfield.api.Angle(degrees=0),
              'angleS': 0,
              'scaleS': 1,
              'errorRMS_S': 1,
              'flippedS': False,
              'success': True,
              'message': 'test',
              'raJNowM': skyfield.api.Angle(hours=0),
              'decJNowM': skyfield.api.Angle(degrees=0),
              'raJNowS': skyfield.api.Angle(hours=0),
              'decJNowS': skyfield.api.Angle(degrees=0),
              'siderealTime': 0,
              'julianDate': Julian(),
              'pierside': 'E',
              'errorRA': 1,
              'errorDEC': 2,
              'errorRMS': 3,
              }

    function.resultQueue.put(mPoint)
    with mock.patch.object(function,
                           'updateProgress'):
        with mock.patch.object(function,
                               'modelCycleThroughBuildPointsFinished'):
            suc = function.modelSolveDone(result)
            assert suc


def test_modelSolveDone_4(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3}

    result = {'raJ2000S': skyfield.api.Angle(hours=0),
              'decJ2000S': skyfield.api.Angle(degrees=0),
              'angleS': 0,
              'scaleS': 1,
              'errorRMS_S': 1,
              'flippedS': False,
              'success': True,
              'message': 'test',
              'julianDate': function.app.mount.obsSite.timeJD,
              }

    function.resultQueue.put(mPoint)
    function.app.data.buildP = [(0, 0, True), (1, 1, True), (2, 2, True)]

    with mock.patch.object(function,
                           'updateProgress'):
        with mock.patch.object(function,
                               'modelCycleThroughBuildPointsFinished'):
            suc = function.modelSolveDone(result)
            assert suc


def test_modelSolveDone_5(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 2}

    result = {'raJ2000S': skyfield.api.Angle(hours=0),
              'decJ2000S': skyfield.api.Angle(degrees=0),
              'angleS': 0,
              'scaleS': 1,
              'errorRMS_S': 999999999,
              'flippedS': False,
              'success': True,
              'message': 'test',
              'julianDate': function.app.mount.obsSite.timeJD,
              }

    function.startModeling = 0
    function.resultQueue.put(mPoint)

    with mock.patch.object(function,
                           'modelCycleThroughBuildPointsFinished'):
        suc = function.modelSolveDone(result)
        assert suc


def test_modelSolve_1(function):
    suc = function.modelSolve()
    assert not suc


def test_modelSolve_2(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': '',
              'searchRadius': 1,
              'solveTimeout': 10,

              }

    function.solveQueue.put(mPoint)
    with mock.patch.object(function.app.astrometry,
                           'solveThreading'):
        suc = function.modelSolve()
        assert suc


def test_modelImage_1(function):
    suc = function.modelImage()
    assert not suc


def test_modelImage_2(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': '',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'focalLength': 1,
              }

    function.imageQueue.put(mPoint)
    with mock.patch.object(function.app.camera,
                           'expose'):
        suc = function.modelImage()
        assert suc


def test_modelSlew_1(function):
    suc = function.modelSlew()
    assert not suc


def test_modelSlew_2(function):
    function.deviceStat['dome'] = False
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': '',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              }

    function.slewQueue.put(mPoint)
    with mock.patch.object(function.app.camera,
                           'expose'):
        suc = function.modelSlew()
        assert not suc


def test_modelSlew_3(function):
    function.deviceStat['dome'] = True
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': '',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              }
    function.slewQueue.put(mPoint)
    with mock.patch.object(function.app.camera,
                           'expose'):
        with mock.patch.object(function.app.dome,
                               'slewDome',
                               return_value=0):
            with mock.patch.object(function.app.mount.obsSite,
                                   'setTargetAltAz',
                                   return_value=True):
                suc = function.modelSlew()
                assert suc


def test_modelSlew_4(function):
    function.deviceStat['dome'] = True
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': '',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              }
    function.slewQueue.put(mPoint)
    function.ui.checkDomeGeometry.setChecked(True)
    with mock.patch.object(function.app.camera,
                           'expose'):
        with mock.patch.object(function.app.dome,
                               'slewDome',
                               return_value=0):
            with mock.patch.object(function.app.mount.obsSite,
                                   'setTargetAltAz',
                                   return_value=True):
                suc = function.modelSlew()
                assert suc


def test_changeStatusDAT_1(function):
    function.ui.checkDisableDAT.setChecked(True)
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(function.app.mount.setting,
                           'setDualAxisTracking'):
        suc = function.disableDAT()
        assert suc
        assert function.statusDAT


def test_changeStatusDAT_2(function):
    function.ui.checkDisableDAT.setChecked(True)
    function.app.mount.setting.statusDualAxisTracking = False
    with mock.patch.object(function.app.mount.setting,
                           'setDualAxisTracking'):
        suc = function.disableDAT()
        assert suc
        assert not function.statusDAT


def test_changeStatusDAT_3(function):
    function.ui.checkDisableDAT.setChecked(True)
    function.statusDAT = True
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(function.app.mount.setting,
                           'setDualAxisTracking'):
        suc = function.disableDAT()
        assert suc
        assert function.statusDAT


def test_changeStatusDAT_4(function):
    function.ui.checkDisableDAT.setChecked(False)
    function.statusDAT = True
    function.app.mount.setting.statusDualAxisTracking = True
    with mock.patch.object(function.app.mount.setting,
                           'setDualAxisTracking'):
        suc = function.disableDAT()
        assert not suc
        assert function.statusDAT


def test_restoreStatusDAT_1(function):
    function.ui.checkDisableDAT.setChecked(True)
    function.statusDAT = None
    suc = function.restoreStatusDAT()
    assert not suc


def test_restoreStatusDAT_2(function):
    function.ui.checkDisableDAT.setChecked(True)
    function.statusDAT = True
    with mock.patch.object(function.app.mount.setting,
                           'setDualAxisTracking'):
        suc = function.restoreStatusDAT()
        assert suc


def test_restoreStatusDAT_3(function):
    function.ui.checkDisableDAT.setChecked(False)
    suc = function.restoreStatusDAT()
    assert not suc


def test_clearQueues(function):
    suc = function.clearQueues()
    assert suc


def test_setupModelRunContextAndGuiStatus_1(function):
    function.app.uiWindows['showImageW']['classObj']=None
    suc = function.setupModelRunContextAndGuiStatus()
    assert not suc


def test_setupModelRunContextAndGuiStatus_2(function):
    function.app.uiWindows['showImageW']['classObj'].deviceStat['expose'] = False
    function.app.uiWindows['showImageW']['classObj'].deviceStat['exposeN'] = False
    suc = function.setupModelRunContextAndGuiStatus()
    assert not suc


def test_setupModelRunContextAndGuiStatus_3(function):
    function.app.uiWindows['showImageW']['classObj'].deviceStat['expose'] = True
    function.app.uiWindows['showImageW']['classObj'].deviceStat['exposeN'] = False
    suc = function.setupModelRunContextAndGuiStatus()
    assert not suc


def test_setupModelRunContextAndGuiStatus_4(function):
    function.app.uiWindows['showImageW']['classObj'].deviceStat['expose'] = True
    function.app.uiWindows['showImageW']['classObj'].deviceStat['exposeN'] = True
    suc = function.setupModelRunContextAndGuiStatus()
    assert suc


def test_restoreModelDefaultContextAndGuiStatus(function):
    suc = function.restoreModelDefaultContextAndGuiStatus()
    assert suc


def test_setupSignalsForModelRun_1(function):
    suc = function.setupSignalsForModelRun()
    assert suc


def test_setupSignalsForModelRun_2(function):
    function.deviceStat['dome'] = True
    function.app.dome.data = {'ABS_DOME_POSITION.DOME_ABSOLUTE_POSITION': 1}

    suc = function.setupSignalsForModelRun()
    assert suc


def test_setupSignalsForModelRun_3(function):
    function.deviceStat['dome'] = True

    suc = function.setupSignalsForModelRun()
    assert suc


def test_restoreSignalsModelDefault(function):
    function.app.camera.signals.saved.connect(function.modelSolve)
    function.app.camera.signals.integrated.connect(function.modelSlew)
    function.app.astrometry.signals.done.connect(function.modelSolveDone)
    function.collector.ready.connect(function.modelImage)

    suc = function.restoreSignalsModelDefault()
    assert suc


def test_pauseBuild_1(function):
    function.ui.pauseModel.setProperty('pause', True)
    suc = function.pauseBuild()
    assert suc
    assert not function.ui.pauseModel.property('pause')


def test_pauseBuild_2(function):
    function.ui.pauseModel.setProperty('pause', False)
    suc = function.pauseBuild()
    assert suc
    assert function.ui.pauseModel.property('pause')


def test_cancelBuild(function, qtbot):
    suc = function.setupSignalsForModelRun()
    assert suc
    with mock.patch.object(function.app.camera,
                           'abort'):
        with mock.patch.object(function.app.astrometry,
                               'abort'):
            with qtbot.waitSignal(function.app.message) as blocker:
                suc = function.cancelBuild()
                assert suc
                assert blocker.args == ['Modeling cancelled', 2]


def test_retrofitModel_1(function):
    function.app.mount.model.starList = list()

    point = ModelStar(coord=skyfield.api.Star(ra_hours=0, dec_degrees=0),
                      number=1,
                      errorRMS=10,
                      errorAngle=skyfield.api.Angle(degrees=0))
    stars = list()
    stars.append(point)
    mPoint = {}
    function.model = list()
    function.model.append(mPoint)
    with mock.patch.object(function,
                           'writeRetrofitData',
                           return_value={}):
        suc = function.retrofitModel()
        assert suc
        assert function.model == {}


def test_generateSaveModel_1(function):
    mPoint = {'raJNowM': Angle(hours=0),
              'decJNowM': Angle(degrees=0),
              'raJNowS': Angle(hours=0),
              'decJNowS': Angle(degrees=0),
              'angularPosRA': Angle(degrees=0),
              'angularPosDEC': Angle(degrees=0),
              'raJ2000S': Angle(hours=0),
              'decJ2000S': Angle(degrees=0),
              'siderealTime': Angle(hours=0),
              'julianDate': function.app.mount.obsSite.timeJD,
              }
    function.model = list()
    function.model.append(mPoint)
    function.model.append(mPoint)
    function.model.append(mPoint)

    val = function.generateSaveModel()
    assert len(val) == 3
    assert 'profile' in val[0]
    assert 'firmware' in val[0]
    assert 'latitude' in val[0]
    assert 'version' in val[0]


def test_saveModelFinish_1(function):
    function.modelName = 'test'
    function.app.mount.signals.alignDone.connect(function.saveModelFinish)
    suc = function.saveModelFinish()
    assert suc


def test_saveModelPrepare_1(function):
    suc = function.saveModelPrepare()
    assert not suc


def test_saveModelPrepare_2(function):
    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': 'testPath',
              'name': 'test',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              }

    function.model = list()
    function.model.append(mPoint)
    function.model.append(mPoint)

    suc = function.saveModelPrepare()
    assert not suc


def test_saveModelPrepare_3(function):
    class Julian:
        ut1 = 2458635.168

    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': 'testPath',
              'name': 'test',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              'raJNowM': skyfield.api.Angle(hours=0),
              'decJNowM': skyfield.api.Angle(degrees=0),
              'raJNowS': skyfield.api.Angle(hours=0),
              'decJNowS': skyfield.api.Angle(degrees=0),
              'siderealTime': 0,
              'julianDate': Julian(),
              'pierside': 'E',
              'errorRA': 1,
              'errorDEC': 2,
              'errorRMS': 3,
              }

    function.model = list()
    function.modelName = 'test'
    function.model.append(mPoint)
    function.model.append(mPoint)
    function.model.append(mPoint)

    suc = function.saveModelPrepare()
    assert suc


def test_saveModel_4(function):
    class Julian:
        @staticmethod
        def utc_iso():
            return 2458635.168

    mPoint = {'lenSequence': 3,
              'countSequence': 3,
              'imagePath': 'testPath',
              'name': 'test',
              'exposureTime': 1,
              'binning': 1,
              'subFrame': 100,
              'fastReadout': False,
              'azimuth': 0,
              'altitude': 0,
              'raJ2000S': skyfield.api.Angle(hours=0),
              'decJ2000S': skyfield.api.Angle(degrees=0),
              'raJNowM': skyfield.api.Angle(hours=0),
              'decJNowM': skyfield.api.Angle(degrees=0),
              'raJNowS': skyfield.api.Angle(hours=0),
              'decJNowS': skyfield.api.Angle(degrees=0),
              'siderealTime': skyfield.api.Angle(hours=0),
              'julianDate': Julian(),
              'pierside': 'E',
              'errorRA': 1,
              'errorDEC': 2,
              'errorRMS': 3,
              }
    function.model = list()
    function.model.append(mPoint)
    function.model.append(mPoint)
    function.model.append(mPoint)

    suc = function.saveModelPrepare()
    assert suc


def test_generateBuildData_1(function):
    build = function.generateBuildData()
    assert build == []


def test_generateBuildData_2(function):
    inputData = [
        {
            "altitude": 44.556745182012854,
            "azimuth": 37.194805194805184,
            "binning": 1.0,
            "countSequence": 0,
            "decJNowS": 64.3246,
            "decJNowM": 64.32841185357267,
            "errorDEC": -229.0210134131381,
            "errorRMS": 237.1,
            "errorRA": -61.36599559380768,
            "exposureTime": 3.0,
            "fastReadout": True,
            "julianDate": "2019-06-08T08:57:57Z",
            "name": "m-file-2019-06-08-08-57-44",
            "lenSequence": 3,
            "imagePath": "/Users/mw/PycharmProjects/MountWizzard4/image/m-file-2019-06-08-08"
                         "-57-44/image-000.fits",
            "pierside": "W",
            "raJNowS": 8.42882,
            "raJNowM": 8.427692953132278,
            "siderealTime": skyfield.api.Angle(hours=12.5),
            "subFrame": 100.0
        },
    ]

    build = function.generateBuildData(inputData)
    assert build[0].sCoord.dec.degrees == 64.3246


def test_collectingModelRunOutput_1(function):
    with mock.patch.object(function,
                           'restoreSignalsModelDefault'):
        with mock.patch.object(function,
                               'restoreModelDefaultContextAndGuiStatus'):
            with mock.patch.object(function,
                                   'restoreStatusDAT'):
                suc = function.collectingModelRunOutput()
                assert not suc


def test_collectingModelRunOutput_2(function):
    class Julian:
        ut1 = 2458635.168

    inputData = {
        'raJ2000S': skyfield.api.Angle(hours=0),
        'decJ2000S': skyfield.api.Angle(degrees=0),
        'angleS': 0,
        'scaleS': 1,
        'errorRMS_S': 1,
        'flippedS': False,
        'success': True,
        'message': 'test',
        'raJNowM': skyfield.api.Angle(hours=0),
        'decJNowM': skyfield.api.Angle(degrees=0),
        'raJNowS': skyfield.api.Angle(hours=0),
        'decJNowS': skyfield.api.Angle(degrees=0),
        'siderealTime': skyfield.api.Angle(hours=0),
        'julianDate': Julian(),
        'pierside': 'E',
        'errorRA': 1,
        'errorDEC': 2,
        'errorRMS': 3,
    }

    function.modelQueue.put(inputData)
    function.modelQueue.put(inputData)
    function.modelQueue.put(inputData)

    with mock.patch.object(function,
                           'restoreSignalsModelDefault'):
        with mock.patch.object(function,
                               'restoreModelDefaultContextAndGuiStatus'):
            with mock.patch.object(function,
                                   'restoreStatusDAT'):
                suc = function.collectingModelRunOutput()
                assert suc


def test_programModelToMount_1(function):
    with mock.patch.object(function,
                           'generateBuildData',
                           return_value=None):
        with mock.patch.object(function.app.mount.model,
                               'programAlign',
                               return_value=False):
            suc = function.programModelToMount(function.model)
            assert not suc


def test_programModelToMount_2(function):
    with mock.patch.object(function,
                           'generateBuildData',
                           return_value=None):
        with mock.patch.object(function.app.mount.model,
                               'programAlign',
                               return_value=True):
            with mock.patch.object(function,
                                   'saveModelPrepare'):
                with mock.patch.object(function,
                                       'refreshName'):
                    with mock.patch.object(function,
                                           'refreshModel'):
                        with mock.patch.object(function.app.mount.model,
                                               'storeName'):
                            suc = function.programModelToMount(function.model)
                            assert suc


def test_renewHemisphereView_1(function):
    function.app.data.buildP = [(0, 0, True), (1, 1, True), (2, 2, True)]

    with mock.patch.object(function.app.data,
                           'setStatusBuildP'):
        suc = function.renewHemisphereView()
        assert suc


def test_processModelData_1(function):
    with mock.patch.object(function,
                           'collectingModelRunOutput',
                           return_value=False):
        suc = function.processModelData()
        assert not suc


def test_processModelData_2(function):
    def playSound(a):
        return

    function.playSound = playSound
    with mock.patch.object(function,
                           'collectingModelRunOutput',
                           return_value=True):
        with mock.patch.object(function,
                               'programModelToMount',
                               return_value=False):
            with mock.patch.object(function,
                                   'renewHemisphereView'):
                with mock.patch.object(function.app.mount.obsSite,
                                       'park',
                                       return_value=False):
                    suc = function.processModelData()
                    assert suc


def test_processModelData_3(function):
    def playSound(a):
        return

    function.playSound = playSound
    function.ui.parkMountAfterModel.setChecked(True)
    with mock.patch.object(function,
                           'collectingModelRunOutput',
                           return_value=True):
        with mock.patch.object(function,
                               'programModelToMount',
                               return_value=True):
            with mock.patch.object(function,
                                   'renewHemisphereView'):
                with mock.patch.object(function.app.mount.obsSite,
                                       'park',
                                       return_value=False):
                    suc = function.processModelData()
                    assert suc


def test_processModelData_4(function):
    def playSound(a):
        return

    function.playSound = playSound
    function.ui.parkMountAfterModel.setChecked(True)
    with mock.patch.object(function,
                           'collectingModelRunOutput',
                           return_value=True):
        with mock.patch.object(function,
                               'programModelToMount',
                               return_value=True):
            with mock.patch.object(function,
                                   'renewHemisphereView'):
                with mock.patch.object(function.app.mount.obsSite,
                                       'park',
                                       return_value=True):
                    suc = function.processModelData()
                    assert suc


def test_modelCycleThroughBuildPointsFinished_1(function):
    inputData = {
         'lenSequence': 0,
         'countSequence': 1,
         }

    function.modelQueue.put(inputData)

    with mock.patch.object(function,
                           'processModelData'):
        suc = function.modelCycleThroughBuildPointsFinished()
        assert suc


def test_modelCycleThroughBuildPointsFinished_2(function):
    inputData = {
        'lenSequence': 0,
        'countSequence': 1,
    }

    function.retryQueue.put(inputData)

    with mock.patch.object(function,
                           'processModelData'):
        with mock.patch.object(function,
                               'modelSlew'):
            suc = function.modelCycleThroughBuildPointsFinished()
            assert suc


def test_modelCycleThroughBuildPointsFinished_3(function, qtbot):
    inputData = {
        'lenSequence': 0,
        'countSequence': 1,
    }

    function.retryQueue.put(inputData)
    function.modelBuildRetryCounter = 1

    with mock.patch.object(function,
                           'processModelData'):
        with mock.patch.object(function,
                               'modelSlew'):
            suc = function.modelCycleThroughBuildPointsFinished()
            assert suc


def test_checkModelRunConditions_1(function):
    suc = function.checkModelRunConditions()
    assert not suc


def test_checkModelRunConditions_2(function):
    function.app.data.buildP = [(0, 0, True)] * 100
    suc = function.checkModelRunConditions()
    assert not suc


def test_checkModelRunConditions_3(function):
    function.app.data.buildP = [(0, 0, True)] * 2
    function.ui.excludeDonePoints.setChecked(True)
    suc = function.checkModelRunConditions()
    assert not suc


def test_checkModelRunConditions_4(function):
    function.app.data.buildP = [(0, 0, True)] * 5
    with mock.patch.object(function.ui.astrometryDevice,
                           'currentText',
                           return_value='No device'):
        suc = function.checkModelRunConditions()
        assert not suc


def test_checkModelRunConditions_5(function):
    function.app.data.buildP = [(0, 0, True)] * 5
    with mock.patch.object(function.app.astrometry,
                           'checkAvailability',
                           return_value=(False, False)):
        suc = function.checkModelRunConditions()
        assert not suc


def test_checkModelRunConditions_6(function):
    function.app.data.buildP = [(0, 0, True)] * 5
    with mock.patch.object(function.app.astrometry,
                           'checkAvailability',
                           return_value=(True, True)):
        suc = function.checkModelRunConditions()
        assert suc


def test_clearAlignAndBackup_1(function):
    with mock.patch.object(function.app.mount.model,
                           'clearAlign',
                           return_value=False):
        suc = function.clearAlignAndBackup()
        assert not suc


def test_clearAlignAndBackup_2(function):
    with mock.patch.object(function.app.mount.model,
                           'clearAlign',
                           return_value=True):
        with mock.patch.object(function.app.mount.model,
                               'deleteName',
                               return_value=False):
            with mock.patch.object(function,
                                   'refreshModel'):
                suc = function.clearAlignAndBackup()
                assert not suc


def test_clearAlignAndBackup_3(function):
    with mock.patch.object(function.app.mount.model,
                           'clearAlign',
                           return_value=True):
        with mock.patch.object(function.app.mount.model,
                               'deleteName',
                               return_value=True):
            with mock.patch.object(function,
                                   'refreshModel'):
                with mock.patch.object(function.app.mount.model,
                                       'storeName',
                                       return_value=False):
                    suc = function.clearAlignAndBackup()
                    assert not suc


def test_clearAlignAndBackup_4(function):
    with mock.patch.object(function.app.mount.model,
                           'clearAlign',
                           return_value=True):
        with mock.patch.object(function.app.mount.model,
                               'deleteName',
                               return_value=True):
            with mock.patch.object(function.app.mount.model,
                                   'storeName',
                                   return_value=True):
                with mock.patch.object(function,
                                       'refreshModel'):
                    suc = function.clearAlignAndBackup()
                    assert suc


def test_setupModelPointsAndContextData_1(function):
    val = function.setupModelPointsAndContextData()
    assert val == []


def test_setupModelPointsAndContextData_2(function):
    function.app.data.buildP = [(0, 0, True), (10, 10, True), (20, 20, True)]
    val = function.setupModelPointsAndContextData()
    assert len(val) == 3
    assert val[0]['lenSequence'] == 3
    assert val[0]['countSequence'] == 1
    assert val[1]['countSequence'] == 2
    assert val[1]['altitude'] == 10
    assert val[1]['azimuth'] == 10


def test_setupModelPointsAndContextData_3(function):
    function.app.data.buildP = [(0, 0, True), (10, 10, False), (20, 20, True)]
    function.ui.excludeDonePoints.setChecked(True)
    val = function.setupModelPointsAndContextData()
    assert len(val) == 2
    assert val[0]['lenSequence'] == 3
    assert val[0]['countSequence'] == 1
    assert val[1]['countSequence'] == 3
    assert val[1]['altitude'] == 20
    assert val[1]['azimuth'] == 20


def test_modelCycleThroughBuildPoints_1(function):
    points = [1, 2]
    with mock.patch.object(function,
                           'setupSignalsForModelRun'):
        with mock.patch.object(function,
                               'modelSlew'):
            suc = function.modelCycleThroughBuildPoints(points)
            assert suc


def test_setupModelFilenamesAndDirectories_1(function):
    function.lastGenerator = 'test'
    with mock.patch.object(os.path,
                           'isdir',
                           return_value=False):
        with mock.patch.object(os,
                               'mkdir'):
            suc = function.setupModelFilenamesAndDirectories()
            assert suc


def test_modelBuild_1(function):
    with mock.patch.object(function,
                           'checkModelRunConditions',
                           return_value=False):
        suc = function.modelBuild()
        assert not suc


def test_modelBuild_2(function):
    with mock.patch.object(function,
                           'checkModelRunConditions',
                           return_value=True):
        with mock.patch.object(function,
                               'clearAlignAndBackup',
                               return_value=False):
            suc = function.modelBuild()
            assert not suc


def test_modelBuild_3(function):
    with mock.patch.object(function,
                           'checkModelRunConditions',
                           return_value=True):
        with mock.patch.object(function,
                               'clearAlignAndBackup',
                               return_value=True):
            with mock.patch.object(function,
                                   'setupModelFilenamesAndDirectories'):
                with mock.patch.object(function,
                                       'setupModelPointsAndContextData',
                                       return_value=[]):
                    suc = function.modelBuild()
                    assert not suc


def test_modelBuild_4(function):
    with mock.patch.object(function,
                           'checkModelRunConditions',
                           return_value=True):
        with mock.patch.object(function,
                               'clearAlignAndBackup',
                               return_value=True):
            with mock.patch.object(function,
                                   'setupModelFilenamesAndDirectories'):
                with mock.patch.object(function,
                                       'setupModelPointsAndContextData',
                                       return_value=[1, 2]):
                    with mock.patch.object(function,
                                           'setupModelRunContextAndGuiStatus'):
                        with mock.patch.object(function,
                                               'disableDAT'):
                            with mock.patch.object(function,
                                                   'modelCycleThroughBuildPoints'):
                                suc = function.modelBuild()
                                assert suc


def test_loadProgramModel_1(function):
    def openFile(a, b, c, d, multiple=False):
        return ([],
                [],
                [])
    function.openFile = openFile

    suc = function.loadProgramModel()
    assert not suc


def test_loadProgramModel_2(function):
    shutil.copy('tests/testData/test.model', 'tests/model/test.model')

    def openFile(a, b, c, d, multiple=False):
        return ('tests/model/test.model',
                'test',
                '.model')
    function.openFile = openFile

    with mock.patch.object(function,
                           'clearAlignAndBackup',
                           return_value=False):
        suc = function.loadProgramModel()
        assert not suc


def test_loadProgramModel_3(function):
    shutil.copy('tests/testData/test.model', 'tests/model/test.model')

    def openFile(a, b, c, d, multiple=False):
        return (['tests/model/test.model'],
                ['test'],
                ['.model'])
    function.openFile = openFile

    with mock.patch.object(function,
                           'clearAlignAndBackup',
                           return_value=True):
        with mock.patch.object(function,
                               'programModelToMount',
                               return_value=False):
            suc = function.loadProgramModel()
            assert not suc


def test_loadProgramModel_4(function):
    shutil.copy('tests/testData/test.model', 'tests/model/test.model')

    def openFile(a, b, c, d, multiple=False):
        return (['tests/model/test.model'],
                ['test'],
                ['.model'])
    function.openFile = openFile

    with mock.patch.object(function,
                           'clearAlignAndBackup',
                           return_value=True):
        with mock.patch.object(function,
                               'programModelToMount',
                               return_value=True):
            suc = function.loadProgramModel()
            assert suc


def test_loadProgramModel_5(function):
    shutil.copy('tests/testData/test.model', 'tests/model/test.model')
    shutil.copy('tests/testData/test1.model', 'tests/model/test1.model')

    def openFile(a, b, c, d, multiple=False):
        return (['tests/model/test.model',
                 'tests/model/test1.model'],
                ['test', 'test1'],
                ['.model', '.model'])
    function.openFile = openFile

    with mock.patch.object(function,
                           'clearAlignAndBackup',
                           return_value=True):

        suc = function.loadProgramModel()
        assert not suc
