# SIDIK JARI ![Django Heroku CI](https://github.com/hendrapaiton/sidik/workflows/Django%20Heroku%20CI/badge.svg?branch=master)
> Finger Apps with FlexCodeSDK

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This project was mirror from [flexcodesdk](http://fingerspot.org/demo_flexcodesdk/) and convert to django program for prototypes.
Using flexcodesdk, we can capture finger from usb fingerprint digital persona 4500 to our web application. And data captured can
used to be indentification or authentication.

## Technologies
* Python
* Django
* FlexCodeSDK

## Setup
First, clone or fork this repository and edit with your needs.
```
$ git clone https://github.com/hendrapaiton/sidik.git
```

Second, create and test the github action workflow and customize with your repo.

Third, register to heroku and create api key for your apps. Edit in your workflow github actions.
```
heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
heroku_app_name: "<your appname>"
heroku_email: "<your email>"
```

## Features
- [x] CI/CD with Github Actions
- [x] Deploy to Heroku
- [ ] Web interface using bootstrap & jquery
- [ ] Function parameter & query http
- [ ] Model and Views in Django
- [ ] Register Device for Digital Persona 4500
- [ ] Create user and register finger from devices
- [ ] Login using devices with user fingerprint

## Contact
Created by [@hendrapaiton](https://github.com/hendrapaiton)
