# twitter-bot-selenium

First create a virtual environment

    python3 -m venv venv

activate the virtual evironment

    source ./venv/bin/activate

install requirements

    pip3 install -r requirements.txt

You will need a web driver installed for FireFox/Google

# Procedure for installing a webdriver for FireFox

Download the latest version of geckodriver for linux via https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

on terminal, write the following

    tar -xvzf geckodriver*
    
    
    chmod +x geckodriver
    
    
    sudo cp geckodriver /usr/local/bin/


# Procedure for installing a webdriver for Google Chrome

Download the latest version of chrome web driver for linux via https://chromedriver.chromium.org/

In the directory you downloaded the chrome web driver, write the following on terminal

    unzip chromedriver_linux64.zip
    sudo mv chromedriver /usr/bin/chromedriver
    sudo chown root:root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver


