import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_teleport_license_file(host):
    license_file = host.file("/var/lib/teleport/license.pem")

    assert license_file.exists
    assert license_file.is_file
    assert licese_file.mode == '0400'
