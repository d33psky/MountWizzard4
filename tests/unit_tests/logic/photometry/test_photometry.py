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
# written in python3, (c) 2019-2022 by mworion
#
# Licence APL2.0
#
###########################################################
# standard libraries
import unittest.mock as mock
import pytest
import shutil

# external packages
from astropy.io import fits
import numpy as np
import sep

# local import
import logic.photometry.photometry
from logic.photometry.photometry import PhotometrySignals
from logic.photometry.photometry import Photometry
from tests.unit_tests.unitTestAddOns.baseTestApp import App


@pytest.fixture(autouse=True, scope='function')
def function(qapp):

    func = Photometry(App())
    yield func


def test_signals(function):
    sig = PhotometrySignals()


def test_workerGetHFR(function):
    function.filterConst = 5
    function.xm = np.linspace(0, 100, 100)
    function.ym = np.linspace(0, 100, 100)
    function.objs = {'x': np.linspace(0, 100, 20),
                     'y': np.linspace(0, 100, 20)}
    function.HFR = np.linspace(20, 30, 20)
    suc = function.workerGetHFR()
    assert suc
    assert function.hfrGrid.shape[0] == 100


def test_workerGetRoundness(function):
    function.filterConst = 5
    function.xm = np.linspace(0, 100, 100)
    function.ym = np.linspace(0, 100, 100)
    function.objs = {'x': np.linspace(0, 100, 20),
                     'y': np.linspace(0, 100, 20),
                     'a': np.random.rand(20, 1) + 1,
                     'b': np.random.rand(20, 1) + 1}
    with mock.patch.object(logic.photometry.photometry,
                           'griddata',
                           return_value=np.linspace(0, 100, 20)):
        suc = function.workerGetRoundness()
        assert suc
        assert len(function.roundnessGrid) == 20


def test_workerCalcTiltValuesSquare(function):
    function.w = 10
    function.h = 10
    function.objs = {'x': np.linspace(0, 50, 20),
                     'y': np.linspace(50, 100, 20)}
    function.image = np.random.rand(100, 100) + 1
    function.HFR = np.linspace(20, 30, 20)
    suc = function.workerCalcTiltValuesSquare()
    assert suc


def test_workerCalcTiltValuesTriangle(function):
    function.w = 10
    function.h = 10
    function.objs = {'x': np.linspace(0, 50, 20),
                     'y': np.linspace(50, 100, 20)}
    function.image = np.random.rand(100, 100) + 1
    function.HFR = np.linspace(20, 30, 20)
    suc = function.workerCalcTiltValuesTriangle()
    assert suc


def test_calcAberrationInspectView_1(function):
    function.w = 1000
    function.h = 1000
    function.image = np.random.rand(1000, 1000) + 1
    suc = function.calcAberrationInspectView()
    assert suc
    h, w = function.aberrationImage.shape
    assert w == function.ABERRATION_SIZE * 3
    assert h == function.ABERRATION_SIZE * 3


def test_calcAberrationInspectView_2(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100) + 1
    suc = function.calcAberrationInspectView()
    assert not suc
    h, w = function.aberrationImage.shape
    assert w == function.image.shape[0]
    assert h == function.image.shape[1]


def test_showTabBackground(function):
    img = np.random.rand(100, 100) + 1
    function.filterConst = 5
    function.bkg = sep.Background(img)
    suc = function.calcBackground()
    assert suc


def test_showTabBackgroundRMS(function):
    img = np.random.rand(100, 100) + 1
    function.filterConst = 5
    function.bkg = sep.Background(img)
    suc = function.calcBackgroundRMS()
    assert suc


def test_baseCalcs(function):
    function.w = 100
    function.h = 100
    function.objs = {'x': np.linspace(0, 50, 20),
                     'y': np.linspace(50, 100, 20)}
    function.HFR = np.linspace(20, 30, 20)
    function.image = np.random.rand(100, 100) + 1
    suc = function.baseCalcs()
    assert suc


def test_runCalcs(function):
    with mock.patch.object(function,
                           'baseCalcs'):
        with mock.patch.object(function,
                               'workerGetHFR'):
            with mock.patch.object(function,
                                   'workerCalcTiltValuesSquare'):
                with mock.patch.object(function,
                                       'workerCalcTiltValuesTriangle'):
                    with mock.patch.object(function,
                                           'workerGetRoundness'):
                        with mock.patch.object(function,
                                               'calcAberrationInspectView'):
                            with mock.patch.object(function,
                                                   'calcBackground'):
                                with mock.patch.object(function,
                                                       'calcBackgroundRMS'):
                                    suc = function.runCalcs()
                                    assert suc


def test_workerCalcPhotometry_1(function):
    function.image = np.random.rand(100, 100) + 1
    function.image[50][50] = 100
    function.image[51][50] = 50
    function.image[50][51] = 50
    function.image[50][49] = 50
    function.image[49][50] = 50
    with mock.patch.object(function,
                           'runCalcs'):
        suc = function.workerCalcPhotometry()
        assert suc
        assert function.bkg is not None
        assert function.HFR is not None
        assert function.objs is not None


def test_processPhotometry(function):
    with mock.patch.object(function.threadPool,
                           'start'):
        suc = function.processPhotometry()
        assert suc


def test_debayerImage_1(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100)
    suc = function.debayerImage('GBRG')
    assert suc
    assert function.image.shape == (100, 100)


def test_debayerImage_2(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100)
    suc = function.debayerImage('RGGB')
    assert suc
    assert function.image.shape == (100, 100)


def test_debayerImage_3(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100)
    suc = function.debayerImage('GRBG')
    assert suc
    assert function.image.shape == (100, 100)


def test_debayerImage_4(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100)
    suc = function.debayerImage('BGGR')
    assert suc
    assert function.image.shape == (100, 100)


def test_debayerImage_5(function):
    function.w = 100
    function.h = 100
    function.image = np.random.rand(100, 100)
    suc = function.debayerImage('test')
    assert not suc
    assert function.image.shape == (100, 100)


def test_cleanImageFormat(function):
    function.image = np.random.rand(100, 100) + 1
    suc = function.cleanImageFormat()
    assert suc
    assert function.image.dtype == np.dtype('float32')


def test_workerLoadImage_1(function):
    class Data:
        data = np.random.rand(100, 100)
        header = None

    class FitsHandle:
        @staticmethod
        def __enter__():
            return [Data(), Data()]

        @staticmethod
        def __exit__(a, b, c):
            return

    imageFileName = 'tests/workDir/image/m51.fit'
    shutil.copy('tests/testData/m51.fit', 'tests/workDir/image/m51.fit')
    with mock.patch.object(fits,
                           'open',
                           return_value=FitsHandle()):
        suc = function.workerLoadImage(imageFileName)
        assert not suc


def test_workerLoadImage_2(function):
    class Data:
        data = None
        header = 2

    class FitsHandle:
        @staticmethod
        def __enter__():
            return [Data(), Data()]

        @staticmethod
        def __exit__(a, b, c):
            return

    imageFileName = 'tests/workDir/image/m51.fit'
    shutil.copy('tests/testData/m51.fit', 'tests/workDir/image/m51.fit')
    with mock.patch.object(fits,
                           'open',
                           return_value=FitsHandle()):
        suc = function.workerLoadImage(imageFileName)
        assert not suc


def test_workerLoadImage_3(function):
    class Data:
        data = np.random.rand(100, 100)
        header = {'BAYERPAT': 1,
                  'CTYPE1': 'DEF',
                  'CTYPE2': 'DEF',
                  }

    class FitsHandle:
        @staticmethod
        def __enter__():
            return [Data(), Data()]

        @staticmethod
        def __exit__(a, b, c):
            return

    imageFileName = 'tests/workDir/image/m51.fit'
    shutil.copy('tests/testData/m51.fit', 'tests/workDir/image/m51.fit')
    with mock.patch.object(fits,
                           'open',
                           return_value=FitsHandle()):
        suc = function.workerLoadImage(imageFileName)
        assert suc


def test_processImage_1(function):
    with mock.patch.object(function.threadPool,
                           'start'):
        suc = function.processImage()
        assert not suc


def test_processImage_2(function):
    imageFileName = 'tests/workDir/image/m51.fit'
    shutil.copy('tests/testData/m51.fit', 'tests/workDir/image/m51.fit')
    with mock.patch.object(function.threadPool,
                           'start'):
        suc = function.processImage(imageFileName)
        assert suc