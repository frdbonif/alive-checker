# test-http v0.0.1
# This module is part of 'alive-checker'
# (C) 2021 Fred Boniface, distributed under the GPLv3 License, a copy of which
# is included with this software.

# Provides functions to test HTTP(S) endpoints.
# This module - test-http - consists of a single function that accepts two
# inputs and returns a tuple.

# Inputs: `url`, `requirement`.
# `url` is a string containing the full url and protocol to be tested, eg:
# "https://example.com"
# `requirement` is a string containing text that the response will be tested for eg:
# "<title>Example</title>".  The requirement will be searched for within the text
# response ignoring any whitespace, that means the above example will match:
# <title> Example </title> aswell as an exact match.

# Outputs: output.
# The out put is a tuple containing: HTTP Status Code, Boolean (reachable or not),
# Boolean (requirement matched or not.) eg. (200,True,True).

import requests

from settings import Parse

def get(url, requirement):

    try:

        # Obtain 'http' settings from `Parse` in `settings.py`.  Then extract
        # `custom-headers` from `http`.
        conf = Parse.parseConf('http')
        headers = conf.get('custom-headers')

        # Submit get request passing `url` from inputs, and the `headers` dict.
        response = requests.get(url, headers)

        # This is the three digit status code which will later be returned to caller
        print(response.status_code)

        # Search for `requirement` in the response, then evaluate the result, -1
        # means not found, else the character position is returned.
        requirementFind = response.text.find(requirement)

        if requirementFind != -1:
            requirementMet = True
        else:
            requirementMet = False

            # This is the result of the `requirement` test.
            print(requirementMet)

            # return the testing results.  Maybe change the order?  Reachable,Status-Code,RequirementTest may be better.
            return response.status_code, True, requirementMet

    # If the codeblock fails, then return "unknown" statuses and FALSE
    # connection test.
    except:
        return "unknown", False, "unknown"


    # NEXT STEPS:
    # - DONE...Parse HTTP Status code from `response`.
    # - DONE...Search `response.text` for `requirement`.
    # - Wrap the main contents into a try except block which will be able to return a FALSE if URL is not reachable.
    # - Return `result` as tuple containing `status`, `boolean - reachable`,
    #   `boolean - requirement test passed`
