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
# written in python3, (c) 2019-2023 by mworion
# Licence APL2.0
#
###########################################################
# standard libraries
import pytest
import unittest.mock as mock

# external packages
from astropy.io import fits
from skyfield.api import Angle
import numpy as np

# local import
from logic.camera.cameraSupport import CameraSupport
import logic.camera.cameraSupport
from base.driverDataClass import Signals
from tests.unit_tests.unitTestAddOns.baseTestApp import App


@pytest.fixture(autouse=True, scope='function')
def function():
    func = CameraSupport()
    func.data = {'CCD_INFO.CCD_PIXEL_SIZE_X': 1,
                 'CCD_INFO.CCD_PIXEL_SIZE_Y': 1,
                 'CCD_TEMPERATURE.CCD_TEMPERATURE_VALUE': 0}
    func.abortExpose = False
    func.app = App()
    func.signals = Signals()
    yield func


def test_writeHeaderBasic_1(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    suc = function.writeHeaderBasic(header)
    assert suc
    assert header['OBJECT'] == 'SKY_OBJECT'


def test_writeHeaderCamera_1(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    suc = function.writeHeaderCamera(header, 1, 1)
    assert suc
    assert header['EXPTIME'] == 1


def test_writeHeaderTime_1(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    obs = function.app.mount.obsSite
    ts = obs.ts
    obs.timeJD = ts.tt_jd(1000 + 2400000.5)
    suc = function.writeHeaderTime(header, obs)
    assert suc
    assert header['DATE-OBS'] == '1861-08-13T00:00:00'
    assert header['MJD-OBS'] == 1000


def test_writeHeaderOptical_1(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    suc = function.writeHeaderOptical(header, 1, 100)
    assert suc
    assert header['FOCALLEN'] == 100


def test_writeHeaderOptical_2(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    suc = function.writeHeaderOptical(header, 1, None)
    assert not suc


def test_writeHeaderSite_1(function):
    header = fits.PrimaryHDU(data=np.array([])).header
    obs = function.app.mount.obsSite
    obs.raJNow = Angle(hours=0)
    obs.decJNow = Angle(degrees=0)
    function.raJ2000 = Angle(hours=0)
    function.decJ2000 = Angle(degrees=0)
    suc = function.writeHeaderSite(header, obs)
    assert suc
    assert header['SITELAT'] == '+20:00:00'


def test_writeHeaderFocus(function):
    header = fits.PrimaryHDU().header
    focuser = function.app.focuser
    suc = function.writeHeaderFocus(header, focuser)
    assert suc


def test_saveFits_1(function):
    data = np.array([])
    function.abortExpose = True
    val = function.saveFits('', data, 1, 1, 1)
    assert val == ''


def test_saveFits_2(function):
    data = np.array([])
    hdu = fits.PrimaryHDU(data=np.array([]))
    function.abortExpose = False
    with mock.patch.object(function,
                           'writeHeaderBasic'):
        with mock.patch.object(function,
                               'writeHeaderCamera'):
            with mock.patch.object(function,
                                   'writeHeaderTime'):
                with mock.patch.object(function,
                                       'writeHeaderOptical'):
                    with mock.patch.object(function,
                                           'writeHeaderSite'):
                        with mock.patch.object(function,
                                               'writeHeaderFocus'):
                            with mock.patch.object(fits.PrimaryHDU,
                                               'writeto'):
                                val = function.saveFits('', data, 1, 1, 1)
                                assert val == ''


def test_retrieveFits_1(function):
    function.abortExpose = True
    val = function.retrieveFits(None, None)
    assert len(val) == 0


def test_retrieveFits_2(function):
    def func(p):
        return None

    function.abortExpose = False
    val = function.retrieveFits(func, 'test')
    assert len(val) == 0


def test_retrieveFits_3(function):
    def func(p):
        return np.array([1, 2, 3])

    function.abortExpose = False
    val = function.retrieveFits(func, 'test')
    assert len(val) == 3


def test_waitExposed_1(function):
    def func(p):
        return False

    function.abortExpose = True
    suc = function.waitExposed(func, 'test', 1)
    assert suc


def test_waitExposed_2(function):
    function.start = True

    def func(p):
        function.start = not function.start
        return function.start

    function.abortExpose = False
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitExposed(func, 'test', 0)
        assert suc


def test_waitExposed_3(function):
    function.start = True

    def func(p):
        function.start = not function.start
        return function.start

    function.abortExpose = False
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitExposed(func, 'test', 1)
        assert suc


def test_waitStart_1(function):
    function.data = {'Device.Message': 'test'}
    function.abortExpose = True
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitStart()
        assert suc


def test_waitStart_2(function):
    function.data = {'Device.Message': 'test'}

    def func(p):
        function.data = {'Device.Message': 'integrating'}

    function.abortExpose = False
    logic.camera.cameraSupport.sleepAndEvents = func
    suc = function.waitStart()
    assert suc


def test_waitIntegrate_1(function):
    function.data = {'Device.Message': 'integrating'}
    function.abortExpose = True
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitExposedApp(1)
        assert suc


def test_waitIntegrate_2(function):
    function.data = {'Device.Message': 'integrating'}

    def func(p):
        function.data = {'Device.Message': 'test'}

    function.abortExpose = False
    logic.camera.cameraSupport.sleepAndEvents = func
    suc = function.waitExposedApp(1)
    assert suc


def test_waitIntegrate_3(function):
    function.data = {'Device.Message': 'integrating'}

    def func(p):
        function.data = {'Device.Message': 'test'}

    function.abortExpose = False
    logic.camera.cameraSupport.sleepAndEvents = func
    suc = function.waitExposedApp(0)
    assert suc


def test_waitDownload_1(function):
    function.data = {'Device.Message': 'downloading'}
    function.abortExpose = True
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitDownload()
        assert suc


def test_waitDownload_2(function):
    function.data = {'Device.Message': 'downloading'}

    def func(p):
        function.data = {'Device.Message': 'test'}

    function.abortExpose = False
    logic.camera.cameraSupport.sleepAndEvents = func
    suc = function.waitDownload()
    assert suc


def test_waitSave_1(function):
    function.data = {'Device.Message': 'image is ready'}
    function.abortExpose = True
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitSave()
        assert suc


def test_waitSave_2(function):
    function.data = {'Device.Message': 'image is ready'}

    def func(p):
        function.data = {'Device.Message': 'test'}

    function.abortExpose = False
    logic.camera.cameraSupport.sleepAndEvents = func
    suc = function.waitSave()
    assert suc


def test_waitFinish_1(function):
    function.start = True

    def func(p):
        function.start = not function.start
        return function.start

    function.abortExpose = True
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitFinish(func, 0)
        assert suc


def test_waitFinish_2(function):
    function.start = True

    def func(p):
        function.start = not function.start
        return function.start

    function.abortExpose = False
    with mock.patch.object(logic.camera.cameraSupport,
                           'sleepAndEvents'):
        suc = function.waitFinish(func, 0)
        assert suc
