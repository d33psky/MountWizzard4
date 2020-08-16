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

# external packages
import pytest
import requests

# local import
from mw4.base.alpacaBase import AlpacaBase


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    global app
    app = AlpacaBase()

    yield


def test_properties_1():
    app.host = ('localhost', 11111)
    app.deviceName = 'test'
    app.deviceName = 'test:2'
    app.apiVersion = 1
    app.protocol = 1


def test_properties_2():
    host = app.host
    assert host == ('localhost', 11111)
    assert app.deviceName == ''
    assert app.apiVersion == 1
    assert app.protocol == 'http'
    assert app.baseUrl == 'http://localhost:11111/api/v1//0'


def test_get_1():
    val = app.get('')
    assert val is None


def test_get_2():
    class Test:
        status_code = 400
        text = 'test'
    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'get',
                           side_effect=Exception(),
                           return_value=Test()):
        val = app.get('')
        assert val is None


def test_get_3():
    class Test:
        status_code = 400
        text = 'test'
    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'get',
                           return_value=Test()):
        val = app.get('')
        assert val is None


def test_get_4():
    class Test:
        status_code = 200
        text = 'test'

        @staticmethod
        def json():
            return {'ErrorNumber': 1,
                    'ErrorMessage': 'msg'}

    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'get',
                           return_value=Test()):
        val = app.get('')
        assert val is None


def test_get_5():
    class Test:
        status_code = 200
        text = 'test'

        @staticmethod
        def json():
            return {'ErrorNumber': 0,
                    'ErrorMessage': 'msg',
                    'Value': 'test'}

    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'get',
                           return_value=Test()):
        val = app.get('')
        assert val == 'test'


def test_put_1():
    val = app.put('')
    assert val is None


def test_put_2():
    class Test:
        status_code = 400
        text = 'test'
    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'put',
                           side_effect=Exception(),
                           return_value=Test()):
        val = app.put('')
        assert val is None


def test_put_3():
    class Test:
        status_code = 400
        text = 'test'
    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'put',
                           return_value=Test()):
        val = app.put('')
        assert val is None


def test_put_4():
    class Test:
        status_code = 200
        text = 'test'

        @staticmethod
        def json():
            return {'ErrorNumber': 1,
                    'ErrorMessage': 'msg'}

    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'put',
                           return_value=Test()):
        val = app.put('')
        assert val is None


def test_put_5():
    class Test:
        status_code = 200
        text = 'test'

        @staticmethod
        def json():
            return {'ErrorNumber': 0,
                    'ErrorMessage': 'msg',
                    'Value': 'test'}

    app.deviceName = 'test'

    with mock.patch.object(requests,
                           'put',
                           return_value=Test()):
        val = app.put('')
        assert val == {'ErrorMessage': 'msg', 'ErrorNumber': 0, 'Value': 'test'}


def test_action():
    app.action(Action='test')


def test_commandblind():
    app.commandblind(Command='test', Raw='test')


def test_commandbool():
    app.commandbool(Command='test', Raw='test')


def test_commandstring():
    app.commandstring(Command='test', Raw='test')


def test_connected_1():
    app.connected(Connected=True)


def test_connected_2():
    app.connected(Connected=False)


def test_connected_3():
    val = app.connected()
    assert val is None


def test_description():
    val = app.description()
    assert val is None


def test_driverVersion():
    val = app.driverVersion()
    assert val is None


def test_interfaceVersion():
    val = app.interfaceVersion()
    assert val is None


def test_nameDevice():
    val = app.nameDevice()
    assert val is None


def test_supportedActions():
    val = app.supportedActions()
    assert val is None
