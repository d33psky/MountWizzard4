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
import pytest
import unittest.mock as mock

# external packages
from PyQt5.QtWidgets import QWidget
import numpy as np

# local import
from gui.utilities.tools4pyqtgraph import Plot
from gui.utilities.tools4pyqtgraph import PolarScatter
from gui.utilities.tools4pyqtgraph import NormalScatter
from gui.utilities.tools4pyqtgraph import PlotImageBar


@pytest.fixture(autouse=True, scope='module')
def module(qapp):
    yield


def test_Plot():
    Plot()


def test_Plot_mouseDoubleClickEvent():
    p = Plot()
    p.defRange = {'xMin': 0, 'xMax': 1, 'yMin': 0, 'yMax': 1}
    with mock.patch.object(p.plotItem,
                           'setRange'):
        p.mouseDoubleClickEvent(None)


def test_PolarScatter():
    p = PolarScatter()


def test_PolarScatter_setGrid_1():
    p = PolarScatter()
    suc = p.setGrid(np.array([0, 1, 2]), np.array([2, 3, 4]))
    assert suc


def test_PolarScatter_setGrid_2():
    p = PolarScatter()
    suc = p.setGrid(np.array([0, 1, 2]), np.array([2, 3, 4]), reverse=True)
    assert suc


def test_PolarScatter_plot1():
    p = PolarScatter()
    with mock.patch.object(p,
                           'setGrid'):
        suc = p.plot(np.array([0, 1, 2]), np.array([2, 3, 4]),
                     color='#000000', z=np.array([2, 3, 4]))
        assert not suc


def test_PolarScatter_plot2():
    p = PolarScatter()
    with mock.patch.object(p,
                           'setGrid'):
        suc = p.plot(np.array([0, 1, 2]), np.array([2, 3, 4]),
                     color=['#000000', '#000000', '#000000'],
                     ang=np.array([2, 3, 4]))
        assert suc


def test_PolarScatter_plotLoc():
    p = PolarScatter()
    suc = p.plotLoc(47)
    assert suc


def test_NormalScatter():
    function = NormalScatter()


def test_NormalScatter_plot1():
    p = NormalScatter()
    with mock.patch.object(p,
                           'mouseDoubleClickEvent'):
        suc = p.plot(np.array([0, 1, 2]), np.array([2, 3, 4]),
                     color='#000000', z=np.array([2, 3, 4]), bar=True)
        assert suc


def test_NormalScatter_plot2():
    p = NormalScatter()
    with mock.patch.object(p,
                           'mouseDoubleClickEvent'):
        suc = p.plot(np.array([0, 1, 2]), np.array([2, 3, 4]),
                     color=['#000000', '#000000', '#000000'],
                     ang=np.array([2, 3, 4]))
        assert suc


def test_NormalScatter_plot3():
    p = PolarScatter()
    with mock.patch.object(p,
                           'mouseDoubleClickEvent'):
        suc = p.plot(np.array([0, 1, 2]), np.array([2, 3, 4]),
                     z=np.array([2, 3, 4]),
                     ang=np.array([2, 3, 4]))
        assert suc


def test_PlotImageBar_constructPlot():
    function = PlotImageBar()
    function.constructPlot()


def test_PlotImageBar_setColorMap():
    function = PlotImageBar()
    suc = function.setColorMap('plasma')
    assert suc


def test_PlotImageBar_setImage():
    function = PlotImageBar()
    img = np.random.rand(100, 100)
    suc = function.setImage(img)
    assert suc


def test_PlotImageBar_showCrosshair():
    function = PlotImageBar()
    function.lx = QWidget()
    function.ly = QWidget()
    suc = function.showCrosshair(True)
    assert suc


def test_PlotImageBar_addEllipse():
    function = PlotImageBar()
    with mock.patch.object(function.plotItem,
                           'addItem'):
        suc = function.addEllipse(0, 0, 1, 1, 0)
        assert suc


def test_PlotImageBar_addValueAnnotation():
    function = PlotImageBar()
    with mock.patch.object(function.plotItem,
                           'addItem'):
        suc = function.addValueAnnotation(0, 0, 10)
        assert suc