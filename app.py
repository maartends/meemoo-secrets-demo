#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#  
#  Copyleft 2020 meemoo
#  
#  @author: Maarten De Schrijver
#  

# System imports

# Third-party imports

# Local imports
from meemoo.secrets import secrets

LDAP_PASSWD = secrets.get('LDAP_PASSWD')

def main(args):
    print(f'The LDAP password is: {LDAP_PASSWD}')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
