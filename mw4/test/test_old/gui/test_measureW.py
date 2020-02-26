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
import unittest.mock as mock
import pytest
# external packages
import numpy as np
# local import
from mw4.test.test_old.setupQt import setupQt


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test
    app, spy, mwGlob, test = setupQt()

    value = np.datetime64('2014-12-12 20:20:20')
    app.measure.devices['sensorWeather'] = ''
    app.measure.devices['power'] = ''
    app.measure.devices['skymeter'] = ''
    app.measure.data = {
        'time': np.empty(shape=[0, 1], dtype='datetime64'),
        'sensorWeatherTemp': np.full([5, 1], 1.0),
        'sensorWeatherHum': np.full([5, 1], 1.0),
        'sensorWeatherPress': np.full([5, 1], 1.0),
        'sensorWeatherDew': np.full([5, 1], 1.0),
        'skySQR': np.full([5, 1], 1.0),
        'skyTemp': np.full([5, 1], 1.0),
        'raJNow': np.full([5, 1], 1.0),
        'decJNow': np.full([5, 1], 1.0),
        'status': np.full([5, 1], 1.0),
        'powCurr1': np.full([5, 1], 1.0),
        'powCurr2': np.full([5, 1], 1.0),
        'powCurr3': np.full([5, 1], 1.0),
        'powCurr4': np.full([5, 1], 1.0),
        'powVolt': np.full([5, 1], 1.0),
        'powCurr': np.full([5, 1], 1.0),
        'powHum': np.full([5, 1], 1.0),
        'powTemp': np.full([5, 1], 1.0),
        'powDew': np.full([5, 1], 1.0),
    }
    app.measure.data['time'] = np.append(app.measure.data['time'], value)
    app.measure.data['time'] = np.append(app.measure.data['time'], value)
    app.measure.data['time'] = np.append(app.measure.data['time'], value)
    app.measure.data['time'] = np.append(app.measure.data['time'], value)
    app.measure.data['time'] = np.append(app.measure.data['time'], value)

    app.config['showMeasureW'] = True
    app.toggleWindow(windowTag='showMeasureW')
    yield


def test_initConfig_1():
    with mock.patch.object(app.uiWindows['showMeasureW']['classObj'],
                           'setupButtons'):
        suc = app.uiWindows['showMeasureW']['classObj'].initConfig()
        assert suc


def test_initConfig_1a():
    with mock.patch.object(app.uiWindows['showMeasureW']['classObj'],
                           'setupButtons'):
        suc = app.uiWindows['showMeasureW']['classObj'].initConfig()
        assert suc


def test_initConfig_2():
    with mock.patch.object(app.uiWindows['showMeasureW']['classObj'],
                           'setupButtons'):
        suc = app.uiWindows['showMeasureW']['classObj'].initConfig()
        assert suc


def test_initConfig_3():
    app.config['measureW']['winPosX'] = 10000
    app.config['measureW']['winPosY'] = 10000
    with mock.patch.object(app.uiWindows['showMeasureW']['classObj'],
                           'setupButtons',
                           return_value=True):
        suc = app.uiWindows['showMeasureW']['classObj'].initConfig()
        assert suc


def test_storeConfig_1():
    app.uiWindows['showMeasureW']['classObj'].storeConfig()


def test_setupAxes_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=0)
    assert not suc


def test_setupAxes_2():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=4)
    assert not suc


def test_setupAxes_3():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = False
    # suc = app.uiWindows['showMeasureW']['classObj'].setupAxes()
    assert not suc


def test_setupAxes_4():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    assert suc
    assert len(app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes) == 1


def test_setupAxes_5():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=4)
    assert not suc


def test_setupAxes_6():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    suc = app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=2)
    assert suc
    assert len(app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes) == 2


def test_plotRa_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotRa(axe=axe,
                              title='test',
                              data=app.measure.data,
                              cycle=1,
                              )
    assert suc


def test_plotDec_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotDec(axe=axe,
                               title='test',
                               data=app.measure.data,
                               cycle=1,
                               )
    assert suc


def test_plotTemperature_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotTemperature(axe=axe,
                                       title='test',
                                       data=app.measure.data,
                                       cycle=1,
                                       )
    assert suc


def test_plotPressure_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotPressure(axe=axe,
                                    title='test',
                                    data=app.measure.data,
                                    cycle=1,
                                    )
    assert suc


def test_plotHumidity_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotHumidity(axe=axe,
                                    title='test',
                                    data=app.measure.data,
                                    cycle=1,
                                    )
    assert suc


def test_plotSQR_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotSQR(axe=axe,
                               title='test',
                               data=app.measure.data,
                               cycle=1,
                               )
    assert suc


def test_plotVoltage_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotVoltage(axe=axe,
                                   title='test',
                                   data=app.measure.data,
                                   cycle=1,
                                   )
    assert suc


def test_plotCurrent_1():
    fig = app.uiWindows['showMeasureW']['classObj'].measureMat.figure
    app.uiWindows['showMeasureW']['classObj'].setupAxes(figure=fig, numberPlots=1)
    axe = app.uiWindows['showMeasureW']['classObj'].measureMat.figure.axes[0]
    suc = app.uiWindows['showMeasureW']['classObj'].plotCurrent(axe=axe,
                                   title='test',
                                   data=app.measure.data,
                                   cycle=1,
                                   )
    assert suc


def test_drawMeasure_1():
    suc = app.uiWindows['showMeasureW']['classObj'].drawMeasure()
    assert not suc


def test_drawMeasure_2():
    app.uiWindows['showMeasureW']['classObj'].ui.measureSet1.setCurrentIndex(1)
    suc = app.uiWindows['showMeasureW']['classObj'].drawMeasure(1)
    assert suc
