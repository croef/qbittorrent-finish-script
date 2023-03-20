#!/bin/bash

TORRENT_NAME=$1
CONTENT_PATH=$2
ROOT_PATH=$3
SAVE_PATH=$4

DOWN_PATH='/script/down.txt'

date >> $DOWN_PATH
echo 'TORRENT_NAME: '$TORRENT_NAME >> $DOWN_PATH
echo 'CONTENT_PATH: '$CONTENT_PATH >> $DOWN_PATH
echo 'ROOT_PATH: '$ROOT_PATH >> $DOWN_PATH
echo 'SAVE_PATH: '$SAVE_PATH >> $DOWN_PATH
echo '----------------------' >> $DOWN_PATH

python /script/complete.py "$CONTENT_PATH" "$ROOT_PATH"
