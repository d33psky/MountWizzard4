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
from invoke import task
from PIL import Image
import glob
import time

#
# defining all necessary virtual client login for building over all platforms
#

# defining environment for ubuntu
clientUbuntu = 'astro-ubuntu.fritz.box'
userUbuntu = 'mw@' + clientUbuntu
workUbuntu = '/home/mw/test'
workUbuntuSCP = userUbuntu + ':/home/mw/test'

# same for windows10 with cmd.exe as shell
clientWindows = 'astro-windows.fritz.box'
userWindows = 'mw@' + clientWindows
workWindows = 'test'
workWindowsSCP = userWindows + ':/Users/mw/test'

# same for windows10 with cmd.exe as shell
clientMac = 'astro-mac-catalina.fritz.box'
userMac = 'mw@' + clientMac
workMac = 'test'
workMacSCP = userMac + ':/Users/mw/test'


def runMWd(c, param):
    c.run(param)


def runMW(c, param):
    # c.run(param, echo=False, hide='out')
    c.run(param)


def printMW(param):
    print('\n\033[95m\033[1m' + param + '\033[0m')


def printMWp(param):
    print('\033[95m\033[1m' + param + '\033[0m')


@task
def clean_mw(c):
    printMW('clean mountwizzard')
    runMW(c, 'rm -rf .pytest_cache')
    runMW(c, 'rm -rf mw4.egg-info')
    runMW(c, 'find ./mw4 | grep -E "(__pycache__)" | xargs rm -rf')


@task
def image_res(c):
    printMW('changing image resolution for docs to 150 dpi')
    files = glob.glob('./docs/**/*.png', recursive=True)
    for file in files:
        print(file)
        im = Image.open(file)
        im.save(file, dpi=(150, 150))


@task
def version_doc(c):
    printMW('changing the version number to setup.py')

    # getting version of desired package
    with open('setup.py', 'r') as setup:
        text = setup.readlines()

    for line in text:
        if line.strip().startswith('version'):
            _, number, _ = line.split("'")

    # reading configuration file
    with open('./docs/source/conf.py', 'r') as conf:
        text = conf.readlines()
    textNew = list()

    print(f'>{number}<')

    # replacing the version number
    for line in text:
        if line.startswith('version'):
            line = f"version = '{number}'\n"
        if line.startswith('release'):
            line = f"release = '{number}'\n"
        textNew.append(line)

    # writing configuration file
    with open('./docs/source/conf.py', 'w+') as conf:
        conf.writelines(textNew)


@task
def update_resource(c):
    printMW('building resources')
    runMW(c, 'cp ./data/de421_23.bsp ./mw4/resource/data/de421_23.bsp')
    runMW(c, 'cp ./data/active.txt ./mw4/resource/data/active.txt')
    runMW(c, 'cp ./data/deltat.data ./mw4/resource/data/deltat.data')
    runMW(c, 'cp ./data/deltat.preds ./mw4/resource/data/deltat.preds')
    runMW(c, 'cp ./data/Leap_Second.dat ./mw4/resource/data/Leap_Second.dat')


@task
def build_resource(c):
    printMW('building resources')
    resourceDir = './mw4/resource/'
    runMW(c, f'pyrcc5 -o {resourceDir}resources.py {resourceDir}resources.qrc')


@task
def build_widgets(c):
    printMW('building widgets')
    widgetDir = './mw4/gui/widgets/'
    widgets = ['hemisphere', 'image', 'main', 'measure', 'message',
               'satellite', 'keypad', 'devicePopup', 'analyse',
               'simulator', 'mount3D']
    for widget in widgets:
        name = widgetDir + widget
        runMW(c, f'python -m PyQt5.uic.pyuic -x {name}.ui -o {name}_ui.py')


@task()
def test_mc(c):
    printMW('testing mountcontrol')
    with c.cd('../mountcontrol'):
        runMW(c, 'flake8')
        runMW(c, 'pytest mountcontrol/test/* --cov-config tox.ini --cov mountcontrol/')


@task()
def test_ib(c):
    printMW('testing indibase')
    with c.cd('../indibase'):
        runMW(c, 'flake8')
        runMW(c, 'pytest indibase/test/test_units --cov-config .coveragerc --cov mw4/')


@task()
def test_mw_cov(c):
    printMW('testing mountwizzard')
    runMW(c, 'flake8')
    runMW(c, 'pytest tests/unit_tests/zStartup --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/base --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/astrometry --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/cover --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/dome --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/environment --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/imaging --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/measure --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/modeldata --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/powerswitch --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/remote --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/logic/telescope --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/gui/extWindows --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/gui/mainWindow --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/gui/mainWmixin --cov-append --cov=mw4/')
    runMW(c, 'pytest tests/unit_tests/gui/utilities --cov-append --cov=mw4/')
    runMW(c, 'bash <(curl -s https://codecov.io/bash) -t e1965db7-af35-4a93-9f3d-ed12a528607b')


@task()
def upload_cov(c):
    printMW('upload coverage')
    runMW(c, 'bash <(curl -s https://codecov.io/bash) -t e1965db7-af35-4a93-9f3d-ed12a528607b')


@task()
def test_mw(c):
    printMW('testing mountwizzard')
    runMW(c, 'flake8')
    runMW(c, 'pytest tests/unit_tests/zStartup')
    runMW(c, 'pytest tests/unit_tests/base')
    runMW(c, 'pytest tests/unit_tests/logic/astrometry')
    runMW(c, 'pytest tests/unit_tests/logic/cover')
    runMW(c, 'pytest tests/unit_tests/logic/dome')
    runMW(c, 'pytest tests/unit_tests/logic/environment')
    runMW(c, 'pytest tests/unit_tests/logic/imaging')
    runMW(c, 'pytest tests/unit_tests/logic/measure')
    runMW(c, 'pytest tests/unit_tests/logic/modeldata')
    runMW(c, 'pytest tests/unit_tests/logic/powerswitch')
    runMW(c, 'pytest tests/unit_tests/logic/remote')
    runMW(c, 'pytest tests/unit_tests/logic/telescope')
    runMW(c, 'pytest tests/unit_tests/gui/extWindows')
    runMW(c, 'pytest tests/unit_tests/gui/mainWindow')
    runMW(c, 'pytest tests/unit_tests/gui/mainWmixin')
    runMW(c, 'pytest tests/unit_tests/gui/utilities')


@task(pre=[])
def build_mc(c):
    printMW('building dist mountcontrol')
    with c.cd('../mountcontrol'):
        runMW(c, 'rm -f dist/*.tar.gz')
        runMW(c, 'python setup.py sdist')
        runMW(c, 'cp dist/mountcontrol*.tar.gz ../MountWizzard4/dist/mountcontrol.tar.gz')


@task(pre=[])
def build_ib(c):
    printMW('building dist indibase')
    with c.cd('../indibase'):
        runMW(c, 'rm -f dist/*.tar.gz')
        runMW(c, 'python setup.py sdist')
        runMW(c, 'cp dist/indibase*.tar.gz ../MountWizzard4/dist/indibase.tar.gz')


@task(pre=[build_resource, build_widgets, build_mc, build_ib, version_doc])
def build_mw(c):
    printMW('building dist mountwizzard4')
    with c.cd('.'):
        runMW(c, 'rm -f dist/mountwizzard4*.tar.gz')
        runMW(c, 'python setup.py sdist')
        runMW(c, 'cp dist/mountwizzard4*.tar.gz ../MountWizzard4/dist/mountwizzard4.tar.gz')


@task(pre=[])
def upload_mc(c):
    printMW('uploading dist mountcontrol')
    with c.cd('../mountcontrol/dist'):
        runMW(c, 'twine upload mountcontrol-*.tar.gz -r pypi')


@task(pre=[])
def upload_ib(c):
    printMW('uploading dist indibase')
    with c.cd('../indibase/dist'):
        runMW(c, 'twine upload indibase-*.tar.gz -r pypi')


@task(pre=[])
def upload_mw(c):
    printMW('uploading dist mountwizzard4')
    with c.cd('./dist'):
        runMW(c, 'twine upload mountwizzard4-*.tar.gz -r pypi')


@task(pre=[upload_mc, upload_ib, upload_mw])
def upload_all(c):
    printMW('uploading dist complete')


@task(pre=[build_resource, build_widgets, build_mc, build_ib])
def install_all(c):
    printMW('installing in work dir')
    with c.cd('./dist'):
        runMW(c, 'pip install indibase.tar.gz')
        runMW(c, 'pip install mountcontrol.tar.gz')


@task(pre=[])
def test_win(c):
    printMW('test windows install')
    printMWp('...delete test dir')
    runMW(c, f'ssh {userWindows} "if exist {workWindows} rd /s /q {workWindows}"')
    time.sleep(1)
    printMWp('...make test dir')
    runMW(c, f'ssh {userWindows} "if not exist {workWindows} mkdir {workWindows}"')
    time.sleep(1)

    with c.cd('dist'):
        printMWp('...copy *.tar.gz to test dir')
        runMWd(c, f'scp -r mountwizzard4.tar.gz {workWindowsSCP}')

    with c.cd('support/Windows'):
        printMWp('...copy install script to test dir')
        runMWd(c, f'scp -r MW4_InstallTest.bat {workWindowsSCP}')
        runMWd(c, f'scp -r MW4_Install.bat {workWindowsSCP}')
        printMWp('...run install script in test dir')
        runMWd(c, f'ssh {userWindows} "cd {workWindows} && MW4_InstallTest.bat"')
        printMWp('...copy run script to test dir')
        runMWd(c, f'scp -r MW4_RunTest.bat {workWindowsSCP}')
        runMWd(c, f'scp -r MW4_Run.bat {workWindowsSCP}')
        printMWp('...run MountWizzard4 for 3 seconds')
        runMWd(c, f'ssh {userWindows} "cd {workWindows} && MW4_RunTest.bat"')


@task(pre=[])
def test_ubuntu(c):
    printMW('test ubuntu install')
    printMWp('...delete test dir')
    runMW(c, f'ssh {userUbuntu} "rm -rf {workUbuntu}"')
    time.sleep(1)
    printMWp('...make test dir')
    runMW(c, f'ssh {userUbuntu} "mkdir {workUbuntu}"')
    time.sleep(1)

    with c.cd('dist'):
        printMWp('...copy *.tar.gz to test dir')
        runMWd(c, f'scp -r mountwizzard4.tar.gz {workUbuntuSCP}')

    with c.cd('support/Ubuntu'):
        printMWp('...copy install script to test dir')
        runMWd(c, f'scp -r MW4_InstallTest.sh {workUbuntuSCP}')
        runMWd(c, f'scp -r MW4_Install.sh {workUbuntuSCP}')
        printMWp('...run install script in test dir')
        runMWd(c, f'ssh {userUbuntu} "cd {workUbuntu} && ./MW4_InstallTest.sh"')
        printMWp('...copy run script and environ to test dir')
        runMWd(c, f'scp -r MW4_RunTest.sh {workUbuntuSCP}')
        runMWd(c, f'scp -r MW4_Run.sh {workUbuntuSCP}')
        runMWd(c, f'scp -r MountWizzard4.desktop {workUbuntuSCP}')
        runMWd(c, f'scp -r mw4.png {workUbuntuSCP}')
        printMWp('...run MountWizzard4 for 3 seconds')
        runMWd(c, f'ssh {userUbuntu} "cd {workUbuntu} && xvfb-run ./MW4_RunTest.sh"')


@task(pre=[])
def test_mac(c):
    printMW('test catalina install')
    printMWp('...delete test dir')
    runMW(c, f'ssh {userMac} "rm -rf {workMac}"')
    time.sleep(1)
    printMWp('...make test dir')
    runMW(c, f'ssh {userMac} "mkdir {workMac}"')
    time.sleep(1)

    with c.cd('dist'):
        printMWp('...copy *.tar.gz to test dir')
        runMWd(c, f'scp -r mountwizzard4.tar.gz {workMacSCP}')

    with c.cd('support/MacOSx'):
        printMWp('...copy install script to test dir')
        runMWd(c, f'scp -r MW4_InstallTest.command {workMacSCP}')
        runMWd(c, f'scp -r MW4_Install.command {workMacSCP}')
        printMWp('...run install script in test dir')
        runMWd(c, f'ssh {userMac} "cd {workMac} && ./MW4_InstallTest.command"')
        printMWp('...copy run script and environ to test dir')
        runMWd(c, f'scp -r MW4_RunTest.command {workMacSCP}')
        runMWd(c, f'scp -r MW4_Run.command {workMacSCP}')
        printMWp('...run MountWizzard4 for 3 seconds')
        runMWd(c, f'ssh {userMac} "cd {workMac} && ./MW4_RunTest.command"')
