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
import pytest
# external packages
# local import
from mw4.test.test_old.setupQt import setupQt
from mw4.gui.satelliteW import SatelliteWindowSignals


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test
    app, spy, mwGlob, test = setupQt()
    app.config['showSatelliteWindow'] = True
    app.toggleWindow(windowTag='showSatelliteW')
    yield


def testSignals():
    a = SatelliteWindowSignals()
    assert a.show
    assert a.update


def test_initConfig_1():
    app.config['satelliteW'] = {}
    suc = app.uiWindows['showSatelliteW']['classObj'].initConfig()
    assert suc


def test_initConfig_2():
    del app.config['satelliteW']
    suc = app.uiWindows['showSatelliteW']['classObj'].initConfig()
    assert suc


def test_initConfig_3():
    app.config['satelliteW'] = {}
    app.config['satelliteW']['winPosX'] = 10000
    app.config['satelliteW']['winPosY'] = 10000
    suc = app.uiWindows['showSatelliteW']['classObj'].initConfig()
    assert suc


def test_storeConfig():
    app.uiWindows['showSatelliteW']['classObj'].storeConfig()


def test_resizeEvent(qtbot):
    app.uiWindows['showSatelliteW']['classObj'].resizeEvent(None)


def test_receiveSatelliteAndShow_1():
    suc = app.uiWindows['showSatelliteW']['classObj'].receiveSatelliteAndShow()
    assert not suc


def test_receiveSatelliteAndShow_2():
    suc = app.uiWindows['showSatelliteW']['classObj'].receiveSatelliteAndShow(satellite=app.mainW.satellites['ZARYA'])
    assert suc


def test_updatePositions_1():
    suc = app.uiWindows['showSatelliteW']['classObj'].updatePositions()
    assert not suc


def test_updatePositions_2():
    suc = app.uiWindows['showSatelliteW']['classObj'].updatePositions(observe='t')
    assert not suc


def test_updatePositions_3():
    suc = app.uiWindows['showSatelliteW']['classObj'].updatePositions(observe='t', subpoint='t')
    assert not suc


def test_updatePositions_4():
    app.mainW.satellite = app.mainW.satellites['ZARYA']
    now = app.mount.obsSite.ts.now()
    observe = app.mainW.satellite.at(now)
    subpoint = observe.subpoint()
    difference = app.mainW.satellite - app.mount.obsSite.location
    altaz = difference.at(now).altaz()

    suc = app.uiWindows['showSatelliteW']['classObj'].updatePositions(observe=observe,
                                         subpoint=subpoint,
                                         altaz=altaz)
    assert suc

