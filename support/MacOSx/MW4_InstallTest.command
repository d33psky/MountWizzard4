#!/bin/bash
cd $(dirname "$0")

#
# Installer for osx
# (c) 2020 mworion
#

echo
echo ---------------------------------------------
echo
echo " ███╗   ███╗ ██╗    ██╗ ██╗  ██╗"
echo " ████╗ ████║ ██║    ██║ ██║  ██║"
echo " ██╔████╔██║ ██║ █╗ ██║ ███████║"
echo " ██║╚██╔╝██║ ██║███╗██║ ╚════██║"
echo " ██║ ╚═╝ ██║ ╚███╔███╔╝      ██║"
echo " ╚═╝     ╚═╝  ╚══╝╚══╝       ╚═╝"
echo
echo ---------------------------------------------
echo install script version 0.2
echo ---------------------------------------------
echo

echo
echo ---------------------------------------------
echo checking installed python version
echo ---------------------------------------------
echo

# starting a new install log
python3 --version > install.log 2>&1

# changing to the actual directory as working directory

# get version of python3 installation
T=$(python3 --version)

# check which valid version is installed
if [[ $T == *"3.8"* ]]; then
  P_VER="python3.8"

elif [[ $T == *"3.7"* ]]; then
  P_VER="python3.7"

elif [[ $T == *"3.6"* ]]; then
  P_VER="python3.6"
fi

if [ "${P_VER:0:6}" == "python" ]; then
  echo
  echo ---------------------------------------------
  echo python version ok
  echo ---------------------------------------------
  echo
else
  echo
  echo ---------------------------------------------
  echo no valid python version installed
  echo ---------------------------------------------
  echo
  echo no valid python version installed >> install.log 2>&1
  exit
fi

echo
echo ---------------------------------------------
echo updating pip installer
echo ---------------------------------------------
echo

python3 -m pip install --upgrade pip --user >> install.log 2>&1

echo
echo ---------------------------------------------
echo installing $P_VER in virtual environ
echo ---------------------------------------------
echo

python3 -m venv venv >> install.log 2>&1

# check if virtualenv is available
if [ ! -f ./venv/bin/activate ]; then
  echo
  echo ---------------------------------------------
  echo no valid virtual environment installed
  echo please check the install.log for errors
  echo ---------------------------------------------
  echo
  echo no valid virtual environment installed >> install.log 2>&1
  exit
fi

echo
echo ---------------------------------------------
echo installing mountwizzard4 - takes some time
echo ---------------------------------------------
echo

source ./venv/bin/activate venv >> install.log 2>&1
python -m pip install pip --upgrade >> install.log 2>&1
python -m pip install setuptools --upgrade >> install.log 2>&1
python -m pip install wheel --upgrade >> install.log 2>&1
pip install mountwizzard4.tar.gz >> install.log 2>&1
deactivate >> install.log 2>&1

echo
echo ---------------------------------------------
echo installed mountwizzard4 successfully
echo for details see install.log
echo ---------------------------------------------
echo

echo MountWizzard4 successfully installed >> install.log 2>&1