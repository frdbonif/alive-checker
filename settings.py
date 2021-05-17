# `settings.py` v2.1.0 - The major version of this file must match the major
# version of `setings.yaml`.

import yaml
import logging

class Load:

    # Open 'settings.yaml' and output to dictonary 'config' and return that dict.
    def loadConfSafe():
        with open("settings_new.yaml", 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                return config
            except yaml.YAMLError as exc:
                print("Error reading 'settings.yaml', loading default configuration")
                config = ''

    # Currently does nothing.  Aim is that this function tests the config dict,
    # and replaces missing values with default values whic are defined in this
    # class.
    def checkConf():
        conf = Load.loadConfSafe()
        return conf

    # Default settings which will be loaded if 'settings.yaml' is missing a parameter.
    defaultchecks = {'secondsinterval': 120, 'reportHttpStatus': True}

class Parse:

    # Simply calls the Load.checkConf() function to retreive a given subset of
    # data from the parsed YAML file, and adds it to a 'confCheck' dict which
    # is returned to the calling code.
    def parseConf(dict):
        config = Load.checkConf()
        confCheck = config.get(dict)
        return confCheck
