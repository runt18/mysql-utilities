#!/usr/bin/python
#
# Copyright (c) 2010, 2013, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
"""Helper Module used on build, generates excutable version of scripts"""

import sys

from info import META_INFO, INSTALL
import cx_Freeze
from cx_Freeze import setup     # Setup function to use

if sys.platform.startswith("win32"):
    META_INFO['name'] = 'MySQL Utilities'

ARGS = {
    'executable': [
        cx_Freeze.Executable(exe, base="Console") for exe in INSTALL['scripts']
    ],
    'options': {
        'bdist_msi': {'add_to_path': True, },
    }
}

ARGS.update(META_INFO)
ARGS.update(INSTALL)
setup(**ARGS)
