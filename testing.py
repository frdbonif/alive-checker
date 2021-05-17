#! /bin/python3.8

# (C) 2021 Fred Boniface, distributed under the GPLv3 License, a copy of which
# is included with this software.

import json
import yaml

from settings import Parse
import testHttp

testfor = '<link rel="stylesheet" href="/index.php/apps/theming'
t = testHttp.get("https://nc.fjla.uk", testfor)
print("\n")
print(t)
