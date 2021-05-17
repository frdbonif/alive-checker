# alive-checker
alive-checker is a small, modular Python program that can be used to monitor, log and alert to failed HTTP, LDAPS and SMTP servers.

Development began on 15/05/2021.

## Licensing
alive-checker (C) Fred Boniface 2021-

alive-checker is distributed under the GPLv3 license and is subject to all of it's terms, a copy of the license is available in this repository.

## About
I will begin by giving a general overview of the software, then an overview of the settings available before delving into the modules and what they do.

### What does it do?
alive-checker can monitor HTTP(S), LDAPS and (in the future) SMTP services.  It can run checks against these services and then output this data to it's output modules - currently the aim is to be able to send email and telegram alerts as well as outputting the test results to JSON files to be served by a webserver enabling live status pages.

### What modules does it include?
alive-checker contains the following modules.  All of which are currently under construction and are not yet ready for use.

 - `settings.py` - this module loads and parses the `settings.yaml` file.
 - `testHttp.py` - this module runs tests against HTTP/S services.
 - `testLdaps.py` - this module runs tests against LDAPS services.
 - `outputs.py` - this module parses all of the collected data and directs it to enabled output modules.
 - `outMail.py` - this module sends notifications via email.
 - `outTelegram.py` - this module sends notifications via telegram.
 - `outJson.py` - this module outputs data to a static JSON file.

All of these modules are managed by `main.py`.

### What tests are run?
alive-checker can currently run various tests which, obviously, differ per service.

#### HTTP
 - Connection test
 - Find defined string in HTTP response

#### LDAPS
 - bind to the server

#### SMTP
 - Connect to SMTP server.

## More help will be added as the project progresses.
