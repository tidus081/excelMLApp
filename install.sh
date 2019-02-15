#!/bin/bash

# Statics
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  sudo apt update
  sudo apt-get install python3-pip python3-dev
fi

pip3 install virtualenv
virtualenv venv 
source venv/bin/activate

# Install requirement python libraries for service_base
pip3 install -r requirements.txt
cp utils/ flask_server/
cp utils/ model_server/
cp utils/ store_server/
cp utils/ vec_server/