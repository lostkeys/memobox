#!/bin/bash

source /backupbox/system/config/dirs.cfg

cd $ROOT_DIR
git fetch --all
git reset --hard origin/prototype
/etc/init.d/uwsgi restart
cd $BIN_DIR

