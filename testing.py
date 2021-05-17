#! /bin/python3.8

import json
import yaml

from settings import Parse
import testHttp

testfor = '<link rel="stylesheet" href="/index.php/apps/theming'
t = testHttp.get("https://nc.fjla.uk", testfor)
print("\n")
print(t)
