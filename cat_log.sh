#!/bin/bash

LOG_DIR=`docker volume inspect --format '{{ .Mountpoint }}' log`
sudo cat $LOG_DIR/log.txt
