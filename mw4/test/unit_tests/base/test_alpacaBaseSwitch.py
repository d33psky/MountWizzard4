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

# external packages
import pytest

# local import
from mw4.base.alpacaBase import Switch


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    global app
    app = Switch()

    yield


def test_maxswitch():
    app.maxswitch()


def test_canwrite():
    val = app.canwrite(Id=0)
    assert val is None


def test_getswitch():
    val = app.getswitch(Id=0)
    assert val is None


def test_getswitchdescription():
    val = app.getswitchdescription()
    assert val is None


def test_getswitchname():
    val = app.getswitchname()
    assert val is None


def test_getswitchvalue():
    val = app.getswitchvalue()
    assert val is None


def test_minswitchvalue():
    val = app.minswitchvalue()
    assert val is None


def test_setswitch():
    val = app.setswitch(Id=0, State=True)
    assert val is None


def test_setswitchname():
    val = app.setswitchname(Id=0, Name='test')
    assert val is None


def test_setswitchvalue():
    val = app.setswitchvalue(Id=0, Value='test')
    assert val is None
