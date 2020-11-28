#!/bin/bash
cd $(dirname "$0")

#
# run script for Ubuntu
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
echo run script version 0.3
echo ---------------------------------------------
echo run script version 0.3 > run.log 2>&1
echo

if [ ! -f ./venv/bin/activate ]; then
  echo
  echo ---------------------------------------------
  echo no valid virtual environment installed
  echo please run MW4_Install.command first
  echo ---------------------------------------------
  echo
  exit
fi

source ./venv/bin/activate venv >> run.log 2>&1

echo
echo ---------------------------------------------
echo checking installed python version
echo ---------------------------------------------
echo

echo Checking environment and start script >> run.log 2>&1

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

echo variable P_VER has value of $P_VER >> run.log 2>&1

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
  echo please run MW4_Install.command first
  echo ---------------------------------------------
  echo
  exit
fi

COMMAND="python ./venv/lib/$P_VER/site-packages/mw4/loader.py test >> run.log 2>&1"
eval ${COMMAND}
deactivate >> run.log  2>&1

echo
echo ---------------------------------------------
echo mountwizzard4 test run finished
echo ---------------------------------------------
echo
