import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_teleport_installation(host):
    teleport_run = host.run("teleport version")
    tctl_run = host.run("tctl version")
    package = host.file("/tmp/teleport-ent-v3.1.6-linux-amd64/")

    assert 'v3.1.6' in teleport_run.stdout
    assert 'v3.1.6' in tctl_run.stdout
    assert 'Enterprise' in teleport_run.stdout
    assert not package.exists


def test_teleport_license_file(host):
    license_file = host.file("/var/lib/teleport/license.pem")

    assert license_file.exists
    assert license_file.is_file
    assert licese_file.mode == '0400'
