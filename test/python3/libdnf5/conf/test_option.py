# Copyright Contributors to the libdnf project.
#
# This file is part of libdnf: https://github.com/rpm-software-management/libdnf/
#
# Libdnf is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Libdnf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with libdnf.  If not, see <https://www.gnu.org/licenses/>.

import libdnf5

import base_test_case


class TestConfigurationOptions(base_test_case.BaseTestCase):
    def test_set_with_runtime_priority(self):
        proxy = self.base.get_config().proxy()
        self.assertEqual(proxy.get_priority(), libdnf5.conf.Option.Priority_DEFAULT)
        
        proxy.set('abcd')
        self.assertEqual(proxy.get_value(), 'abcd')
        self.assertEqual(proxy.get_priority(), libdnf5.conf.Option.Priority_RUNTIME)

    def test_container_add_item(self):
        auths_config = self.base.get_config().proxy_auth_method()
        auths_config.set(('basic', 'ntlm'))
        auths_config.add_item('digest')
        self.assertEqual(auths_config.get_value(), ('basic', 'digest', 'ntlm'))

    def test_container_add(self):
        types_config = self.base.get_config().optional_metadata_types()
        types_config.set((libdnf5.conf.METADATA_TYPE_FILELISTS,))
        types_config.add((libdnf5.conf.METADATA_TYPE_COMPS, libdnf5.conf.METADATA_TYPE_UPDATEINFO))
        self.assertEqual(types_config.get_value(), (libdnf5.conf.METADATA_TYPE_COMPS, libdnf5.conf.METADATA_TYPE_FILELISTS, libdnf5.conf.METADATA_TYPE_UPDATEINFO))
