#!/usr/bin/env sh
set -x

apt-get -y update && apt-get install sshpass

sshpass -p '$USERPASS' ssh $REMOTE_USER@$REMOTE_HOST 'bash -s' < ./runserver.sh