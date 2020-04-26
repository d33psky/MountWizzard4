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
from mw4.base import tpool


@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    pass


def test_WorkerSignals():
    a = tpool.WorkerSignals()
    assert a.finished
    assert a.error
    assert a.result


def test_Worker_1():
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)
    assert a.signals


def test_Worker_2(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.finished):
        a.run()


def test_Worker_3(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.result):
        a.run()


def test_Worker_4(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.assertNotEmitted(a.signals.error):
        a.run()


def test_Worker_5(qtbot):
    def testFunc():
        raise Exception('Test')
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.error):
        a.run()
