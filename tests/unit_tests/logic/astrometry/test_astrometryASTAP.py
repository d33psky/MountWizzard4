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
# standard libraries
from unittest import mock
import pytest
import shutil
import subprocess
import os
import glob
import platform

# external packages
from PyQt5.QtCore import QThreadPool

# local import
from logic.astrometry.astrometry import Astrometry
from logic.astrometry.astrometryASTAP import AstrometryASTAP


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
    app = AstrometryASTAP(parent=parent)

    for file in os.listdir('tests/temp'):
        fileP = os.path.join('tests/temp', file)
        if 'temp' not in file:
            continue
        os.remove(fileP)
    shutil.copy('tests/testData/m51.fit', 'tests/image/m51.fit')

    yield app


def test_setDefaultPath_1(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Darwin'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == '/Applications/ASTAP.app/Contents/MacOS'


def test_setDefaultPath_2(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Linux'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == '/opt/astap'


def test_setDefaultPath_3(app):
    with mock.patch.object(platform,
                           'system',
                           return_value='Windows'):
        suc = app.setDefaultPath()
        assert suc
        assert app.appPath == 'C:\\Program Files\\astap'


def test_runASTAP_1(app):
    suc = app.runASTAP()
    assert not suc


def test_runASTAP_2(app):
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
        val = app.runASTAP()
        assert val == 1


def test_runASTAP_3(app):
    with mock.patch.object(subprocess,
                           'Popen',
                           side_effect=Exception()):
        suc = app.runASTAP()
        assert not suc


def test_runASTAP_4(app):
    with mock.patch.object(subprocess,
                           'Popen',
                           side_effect=subprocess.TimeoutExpired):
        suc = app.runASTAP(binPath='clear')
        assert not suc


def test_getWCSHeader_1(app):
    val = app.getWCSHeader()
    assert val is None


def test_getWCSHeader_2(app):
    shutil.copy('tests/testData/tempASTAP.wcs', 'tests/temp/temp.wcs')
    val = app.getWCSHeader(wcsTextFile='tests/temp/temp.wcs')
    assert val


def test_solveASTAP_1(app):
    suc = app.solve()
    assert not suc


def test_solveASTAP_2(app):
    suc = app.solve()
    assert not suc


def test_solveASTAP_3(app):
    app.deviceName = 'ASTAP-Mac'
    app.environment = {
        'ASTAP-Mac': {
            'programPath': '',
            'indexPath': '',
        }
    }
    with mock.patch.object(app,
                           'runASTAP',
                           return_value=1):
        suc = app.solve(fitsPath='tests/image/m51.fit')
        assert not suc


def test_solveASTAP_4(app):
    app.deviceName = 'ASTAP-Mac'
    app.environment = {
        'ASTAP-Mac': {
            'programPath': '',
            'indexPath': '',
        }
    }
    with mock.patch.object(app,
                           'runASTAP',
                           return_value=0):
        suc = app.solve(fitsPath='tests/image/m51.fit')
        assert not suc


def test_solveASTAP_5(app):
    app.deviceName = 'ASTAP-Mac'
    app.environment = {
        'ASTAP-Mac': {
            'programPath': '',
            'indexPath': '',
        }
    }
    with mock.patch.object(app,
                           'runASTAP',
                           return_value=0):
        with mock.patch.object(os,
                               'remove',
                               return_value=True):
            shutil.copy('tests/testData/tempASTAP.wcs', 'tests/temp/temp.wcs')
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
    app.framework = 'ASTAP'
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
