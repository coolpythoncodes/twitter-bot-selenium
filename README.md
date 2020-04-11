# twitter-bot-selenium

First create a virtual environment

    python3 -m venv venv

activate the virtual evironment

    source ./venv/bin/activate

install requirements

    pip3 install -r requirements.txt

You will need a web driver installed for FireFox

# Procedure for installing a webdriver for FireFox

Download the latest version of geckodriver for linux via https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

on terminal, write the following

    tar -xvzf geckodriver*
    
    chmod +x geckodriver
    
    sudo cp geckodriver /usr/local/bin/
