TrueCallerApp
===========================

Provides api to search number details from TrueCaller Website


Installation
---

	# install pip:
	$ sudo easy_install pip

	# install virtualenv:
	$ sudo easy_install virtualenv

	# inside your repo, create env and activate it:
	$ virtualenv env/ && . env/bin/activate

	# install required packages
	$ pip install -e .


Documentation
---
	# generate new static doc
	$ make doc


Environment Variable
---
    export TCAPP_SETTINGS=tcapi.TrueCallerApp.settings.DevConfig
    or
    export TCAPP_SETTINGS=tcapi.TrueCallerApp.settings.ProdConfig
    export YAHOO_USERNAME=<yahoo_username>
    export YAHOO_PASSWORD=<yahoo_password>
    export TCAPP_PORT=<port_number>

	# it will start on http://localhost:<port_number>
	$ python app.py

Example Usage
---

	$ curl 'localhost:<port_number>/v1/location/<string:location>/number/<string:number>'


