#!/bin/bash

# create rutes and move a base directory
CURRENT_FILE=$(readlink -f $0)
PATH_SETTING=$(dirname $CURRENT_FILE)
PATH_APP=$(dirname $PATH_SETTING)
PATH_BASE=$(dirname $PATH_APP)

cd $PATH_BASE

# add and init virtual enviroment
PYTHON_VERSION=$(python3 --version || 'false' )
if [ $PYTHON_VERSION != false ]
then
    python3 -m venv .env  
    source .env/bin/activate
    pip install -r requirements.txt
else
    clear
    echo "ERROR: Python is not installed or its veresion is lower python3"
    echo "Please install python3"
    break
fi

# run config flie
source $PATH_SETTING/config_flask_server.sh

# final message
echo "--------------------"
echo "Installing Completed"
echo "--------------------"
echo "Review the configuration file to modify the defaults in:\n $PATH_SETTING" 