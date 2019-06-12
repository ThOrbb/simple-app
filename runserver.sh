#!/usr/bin/env sh
set -x

apt-get -y update && apt-get install python3 python3-pip

git clone https://github.com/ThOrbb/simple-app.git
cd simple-app
pip3 install Flask

python3 app.py &
