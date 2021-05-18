# Provides functions to test LDAPS endpoints.

# Module Version 0.1.0

# (C) 2021 Fred Boniface, distributed under the GPLv3 License, a copy of which
# is included with this software.

import ldap

from settings import Parse


def tryLdap(url):

#    try:

        # Get LDAP settings from settings.Parse and separate User & Pass
        conf = Parse.parseConf('ldaps')
        ldapUser = conf.get('bindUser')
        ldapPass = conf.get('bindPass')
        ldapBase = conf.get('userPath')
        ldapLogin = ldapUser + ", " + ldapBase
        print(ldapBase)
        print(ldapLogin)

        # Connect and bind to LDAPS
#        connect = ldap.initialize(url)
#        connect.set_option(ldap.OPT_REFERRALS, 0)
#        connect.simple_bind_s(ldapUser, ldapPass)

        print(conf)
        print("\n")
        print(ldapUser)
        print(ldapPass)

        return "Done"

#    except:
#        return "Fail"
