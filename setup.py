# Created on 2015.02.20
#
# @author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of sldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from json import load

version_dict = load(open('_version.json', 'r'))
version = str(version_dict['version'])
author = str(version_dict['author'])
email = str(version_dict['email'])
license = str(version_dict['license'])
url = str(version_dict['url'])
description = str(version_dict['description'])
package_name = str(version_dict['package_name'])
package_folder = str(version_dict['package_folder'])
status = str(version_dict['status'])

long_description = str(open('README.rst').read())

setup(name=package_name,
      version=version,
      packages=['sldap3',
                'sldap3.core',
                'sldap3.backend',
                'sldap3.backend.user',
                'sldap3.operation',
                'sldap3.protocol',
                'sldap3.utils',
                ],
      package_dir={'': package_folder},
      install_requires=['pyasn1 >= 0.1.7',
                        'ldap3 >= 0.9.8.2'],
      license=license,
      author=author,
      author_email=email,
      description=description,
      long_description=long_description,
      keywords='python3 python2 ldap server',
      url=url,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP']
      )
