#!/bin/bash
cd $(dirname "$0")

#
# Installer for Ubuntu
# (c) 2020 mworion
#

echo
echo --------------------------------------------------------
echo
echo "         ███╗   ███╗██╗    ██╗██╗  ██╗"
echo "         ████╗ ████║██║    ██║██║  ██║"
echo "         ██╔████╔██║██║ █╗ ██║███████║"
echo "         ██║╚██╔╝██║██║███╗██║╚════██║"
echo "         ██║ ╚═╝ ██║╚███╔███╔╝     ██║"
echo "         ╚═╝     ╚═╝ ╚══╝╚══╝      ╚═╝"
echo
echo --------------------------------------------------------
echo install script version 1.1
echo --------------------------------------------------------

echo install script version 1.1 > install.log 2>&1

echo
echo --------------------------------------------------------
echo checking installed python version
echo --------------------------------------------------------

echo checking environment and start script >> install.log 2>&1

T=`python3 --version`
P_VER=""

if [ "${T:0:10}" == "Python 3.9" ]; then
  P_VER="python3.9"
elif [ "${T:0:10}" == "Python 3.8" ]; then
  P_VER="python3.8"
elif [ "${T:0:10}" == "Python 3.7" ]; then
  P_VER="python3.7"
fi

echo variable P_VER has value of $P_VER >> install.log 2>&1

if [ "${P_VER:0:6}" == "python" ]; then
  echo
  echo --------------------------------------------------------
  echo python version ok
  echo --------------------------------------------------------
else
  echo
  echo --------------------------------------------------------
  echo No valid python version installed
  echo --------------------------------------------------------
  exit
fi

echo installing wheel >> install.log 2>&1
python3 -m pip install pip --upgrade >> install.log 2>&1

echo
echo --------------------------------------------------------
echo installing $P_VER in virtual environ
echo --------------------------------------------------------

echo Installing $P_VER in virtual environ >> install.log 2>&1

{
virtualenv venv >> install.log 2>&1
} || {
  echo
  echo --------------------------------------------------------
  echo no valid virtual environment installed
  echo please check the install.log for errors
  echo install virtualenv with
  echo sudo apt-get install python3-virtualenv
  echo --------------------------------------------------------

  echo no valid virtual environment installed >> install.log 2>&1
  exit
}

echo
echo --------------------------------------------------------
echo installing mountwizzard4 - takes some time
echo --------------------------------------------------------

source ./venv/bin/activate venv >> install.log  2>&1
python -m pip install pip --upgrade >> install.log 2>&1
python -m pip install setuptools --upgrade >> install.log 2>&1
python -m pip install wheel --upgrade >> install.log 2>&1
python -m pip install mountwizzard4.tar.gz >> install.log 2>&1

echo
echo --------------------------------------------------------
echo installed mountwizzard4 successfully
echo for details see install.log
echo --------------------------------------------------------

echo MountWizzard4 successfully installed >> install.log 2>&1


