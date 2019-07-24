import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_teleport_installation(host):
    teleport_run = host.run("teleport version")
    tctl_run = host.run("tctl version")
    teleport_download = host.file("/tmp/teleport")

    assert 'Teleport v3.1.6' in teleport_run.stdout
    assert 'Teleport v3.1.6' in tctl_run.stdout
    assert not teleport_download.exists


@pytest.mark.parametrize('path', [
    '/var/lib/teleport',
    '/etc/teleport/',
    '/etc/teleport/ssl'
])
def test_teleport_directory(host, path):
    dir = host.file(path)

    assert dir.is_directory
    assert dir.user == 'ubuntu'
    assert dir.group == 'ubuntu'


def test_teleport_running(host):
    service = host.service('teleport')

    assert service.is_running
    assert service.is_enabled
