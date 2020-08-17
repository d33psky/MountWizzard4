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
#
# Licence APL2.0
#
###########################################################
# standard libraries
from unittest import mock
import pytest
import os
import glob
import platform
import shutil
import subprocess

# external packages
from PyQt5.QtCore import QThreadPool
from astropy.io import fits

# local import
from logic.astrometry.astrometry import Astrometry
from logic.astrometry.astrometryNET import AstrometryNET


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():

    yield

    files = glob.glob('tests/image/*.fit*')
    for f in files:
        os.remove(f)


@pytest.fixture(autouse=True, scope='function')
def app():
    class Test:
        threadPool = QThreadPool()
        mwGlob = {'tempDir': 'tests/temp'}

    parent = Astrometry(app=Test())
    app = AstrometryNET(parent=parent)

    for file in os.listdir('tests/temp'):
        fileP = os.path.join('tests/temp', file)
        if 'temp' not in file:
            continue
        os.remove(fileP)

    yield app


def test_setDefaultPath_1(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Darwin'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == '/Applications/KStars.app/Contents/MacOS/astrometry/bin'


def test_setDefaultPath_2(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Linux'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == '/usr/bin'


def test_setDefaultPath_3(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Windows'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == ''


def test_runImage2xy_1(app):
    suc = app.runImage2xy()
    assert not suc


def test_runImage2xy_2(app):
    class Test1:
        @staticmethod
        def decode():
            return 'decode'

    class Test:
        returncode = '1'
        stderr = Test1()
        stdout = Test1()

        @staticmethod
        def communicate(timeout=0):
            return Test1(), Test1()

    with mock.patch.object(subprocess,
                           'Popen',
                           return_value=Test()):
        suc = app.runImage2xy()
    assert not suc


def test_runSolveField_1(app):
    suc = app.runSolveField()
    assert not suc


def test_runSolveField_2(app):
    class Test1:
        @staticmethod
        def decode():
            return 'decode'

    class Test:
        returncode = '1'
        stderr = Test1()
        stdout = Test1()

        @staticmethod
        def communicate(timeout=0):
            return Test1(), Test1()

    with mock.patch.object(subprocess,
                           'Popen',
                           return_value=Test()):
        suc = app.runSolveField()
    assert not suc


def test_getWCSHeader_1(app):
    val = app.getWCSHeader()
    assert val is None


def test_getWCSHeader_2(app):
    hdu = fits.HDUList()
    hdu.append(fits.PrimaryHDU())
    val = app.getWCSHeader(wcsHDU=hdu)
    assert val


def test_solveNet_1(app):
    suc = app.solve()
    assert not suc


def test_solveNet_2(app):
    app.deviceName = 'KStars'
    app.environment = {
        'KStars': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=False):
        shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
        suc = app.solve(fitsPath='tests/image/m51.fit')
        assert not suc


def test_solveNet_3(app):
    app.deviceName = 'KStars'
    app.environment = {
        'KStars': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=True):
        with mock.patch.object(app,
                               'runSolveField',
                               return_value=False):
            shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
            suc = app.solve(fitsPath='tests/image/m51.fit')
            assert not suc


def test_solveNet_4(app):
    app.deviceName = 'KStars'
    app.environment = {
        'KStars': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=True):
        with mock.patch.object(app,
                               'runSolveField',
                               return_value=True):
            shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
            suc = app.solve(fitsPath='tests/image/m51.fit')
            assert not suc


def test_solveNet_5(app):
    app.deviceName = 'CloudMakers'
    app.environment = {
        'CloudMakers': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=True):
        with mock.patch.object(app,
                               'runSolveField',
                               return_value=True):
            with mock.patch.object(os,
                                   'remove',
                                   return_value=True):
                shutil.copy('tests/testData/tempNET.wcs', 'tests/temp/temp.wcs')
                shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
                suc = app.solve(fitsPath='tests/image/m51.fit')
                assert not suc


def test_solveNet_6(app):
    app.deviceName = 'KStars'
    app.environment = {
        'KStars': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=True):
        with mock.patch.object(app,
                               'runSolveField',
                               return_value=True):
            with mock.patch.object(os,
                                   'remove',
                                   return_value=True):
                shutil.copy('tests/testData/tempNET.solved', 'tests/temp/temp.solved')
                shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
                suc = app.solve(fitsPath='tests/image/m51.fit')
                assert not suc


def test_solveNet_7(app):
    app.deviceName = 'KStars'
    app.environment = {
        'KStars': {
            'programPath': '',
            'indexPath': '',
        }
    }
    app.indexPath = 'tests/temp'
    with mock.patch.object(app,
                           'runImage2xy',
                           return_value=True):
        with mock.patch.object(app,
                               'runSolveField',
                               return_value=True):
            with mock.patch.object(os,
                                   'remove',
                                   return_value=True):
                shutil.copy('tests/testData/tempNET.wcs', 'tests/temp/temp.wcs')
                shutil.copy('tests/testData/tempNET.solved', 'tests/temp/temp.solved')
                shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')
                suc = app.solve(fitsPath='tests/image/m51.fit')
                assert suc


def test_abort_1(app):
    app.process = None
    suc = app.abort()
    assert not suc


def test_abort_2(app):
    class Test:
        @staticmethod
        def kill():
            return True
    app.framework = 'KStars'
    app.process = Test()
    suc = app.abort()
    assert suc


def test_checkAvailability_1(app):
    with mock.patch.object(os.path,
                           'isfile',
                           return_value=True):
        with mock.patch.object(glob,
                               'glob',
                               return_value=True):
            with mock.patch.object(platform,
                                   'system',
                                   return_value='Darwin'):
                suc = app.checkAvailability()
                assert suc == (True, True)


def test_checkAvailability_2(app):
    with mock.patch.object(os.path,
                           'isfile',
                           return_value=True):
        with mock.patch.object(glob,
                               'glob',
                               return_value=True):
            with mock.patch.object(platform,
                                   'system',
                                   return_value='Linux'):
                suc = app.checkAvailability()
                assert suc == (True, True)


def test_checkAvailability_3(app):
    with mock.patch.object(os.path,
                           'isfile',
                           return_value=True):
        with mock.patch.object(glob,
                               'glob',
                               return_value=True):
            with mock.patch.object(platform,
                                   'system',
                                   return_value='Windows'):
                suc = app.checkAvailability()
                assert suc == (True, True)
