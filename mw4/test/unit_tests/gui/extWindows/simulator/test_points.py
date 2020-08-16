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
import pytest
from unittest import mock
import faulthandler
faulthandler.enable()

# external packages
from PyQt5.Qt3DCore import QEntity
from PyQt5.Qt3DExtras import QExtrudedTextMesh
from PyQt5.QtCore import QObject
from mountcontrol.mount import Mount
from skyfield.api import Topos

# local import
from gui.extWindows.simulator import SimulatorBuildPoints


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    global app

    class Test1:
        buildP = [(45, 45), (50, 50)]

    class Test(QObject):
        data = Test1()
        mount = Mount(host='localhost', MAC='00:00:00:00:00:00', verbose=False,
                      pathToData='mw4/test/data')
        mount.obsSite.location = Topos(latitude_degrees=20,
                                       longitude_degrees=10,
                                       elevation_m=500)
        mwGlob = {'modelDir': 'mw4/test/model',
                  'imageDir': 'mw4/test/image'}
        uiWindows = {'showImageW': {'classObj': None}}

    app = SimulatorBuildPoints(app=Test())
    yield


def test_createAnnotation_1(qtbot):
    e = QEntity()
    with mock.patch.object(QExtrudedTextMesh,
                           'setText'):
        val = app.createAnnotation(e, 45, 45, 'test')
        assert isinstance(val, QEntity)


def test_createAnnotation_2(qtbot):
    e = QEntity()
    with mock.patch.object(QExtrudedTextMesh,
                           'setText'):
        val = app.createAnnotation(e, 45, 45, 'test', faceIn=True)
        assert isinstance(val, QEntity)


def test_create_1(qtbot):
    e = QEntity()
    suc = app.create(e, False)
    assert not suc


def test_create_2(qtbot):
    e = QEntity()
    app.pointRoot = e
    app.points = [{'e': e}]
    suc = app.create(e, False)
    assert not suc


def test_create_3(qtbot):
    e = QEntity()
    app.pointRoot = e
    app.points = [{'e': e}]
    suc = app.create(e, True)
    assert suc


def test_create_4():
    e = QEntity()
    app.pointRoot = e
    app.app.data.buildP = None
    app.points = [{'e': e}]
    suc = app.create(e, True)


def test_create_5():
    e = QEntity()
    app.pointRoot = e
    app.points = [{'e': e}]

    with mock.patch.object(app,
                           'createAnnotation',
                           return_value=(QEntity(), 1, 1, 1)):
        suc = app.create(e, True, numbers=True, path=True)
        assert suc
