Role Name
=========

Install [Gravitational Teleport
Cluster](https://gravitational.com/teleport/docs/intro/)

Usage
-----
Currently role is not published onto ansible-galaxy, so we pull it from this
repository directly. Ensure you have the permissions to read the repository.
```
cat <EOF >> requirements.yml
- src: git@github.com:madsonic/ansible-teleport.git
  scm: git
  version: master
  name: teleport
EOF

ansible-galaxy install -r requirements.yml
```

Requirements
------------
- Ansible >= 2.8.2 (Earlier versions might work but they are not tested)

Role Variables
--------------
Most of the variables maps directly to those in [Teleport configuration
file](https://gravitational.com/teleport/docs/admin-guide/#configuration-file).
Otherwise, they maybe systemd service options, teleport configuration flags.
These values have an empty value in the Teleport Config column

| Teleport Config | Var Name | Default Value | Description |
|---------------- | -------- | ------------- | ----------- |
| Role specific | `teleport_version` | `"v3.1.6"`| Teleport version to install. [Changelog](https://github.com/gravitational/teleport/blob/master/CHANGELOG.md) |
| Role specific | `teleport_node_arch` | `"linux-amd64"`| [Teleport architecture to install](https://gravitational.com/teleport/download/) |
| Role specific | `teleport_bin_path` | `"/usr/local/bin/teleport"`| Install path |
| Role specific | `teleport_config_dir` | `"/etc/teleport"`| Config directory |
| Role specific | `teleport_config_path` | `"/etc/teleport/teleport.yml"`| Config file path |
| Role specific | `teleport_roles_dir` | `"/etc/teleport/roles"`| Role files directory. **FUTURE** |
| Role specific | `teleport_ssl_dir` | `"/etc/teleport/ssl"`| Directory for https files |
| Role specific | `teleport_service_path` | `"/etc/systemd/system/teleport.service"`| Systemd service file |
| Role specific | `teleport_pid_path` | `"/var/run/teleport.pid"`| PID file for systemd service |
| Role specific | `teleport_diag_enabled` | `true`| `--diag-addr` flag |
| Role specific | `teleport_diag_listen_addr` | `127.0.0.1:3000`| `--diag-addr` flag value |
| Role specific | `teleport_insecure` | `no`| `--insecure-no-tls` flag. Useful for testing role. Not recommended for production use |
| Role specific | `teleport_use_ca_pin` | `yes`| Leave `teleport.ca_pin` unset which generates a warning from Teleport. Usefule for testing role. Not recommended for production use |
| | `teleport_enterprise_mode` | `no`| Selects binary to download Selects binary to download. `no` uses OSS version |
| `teleport.nodename` | `teleport_nodename` | `ansible_hostname` | |
| `teleport.data_dir` | `teleport_data_dir` | `"/var/lib/teleport"`| |
| `teleport.auth_token` | `teleport_auth_token` | `hostvars[groups['teleport_auth'][0]]['join_token']` | A random token will be generated on the root auth server |
| `teleport.ca_pin` | nil | `hostvars[groups['teleport_auth'][0]]['ca_pin']`| Value from root auth server will be obtained and set |
| `teleport.advertise_ip` | nil | teleport default | node public IP address |
| `teleport.auth_servers` | nil | `<public_ip>:3025` | Public IP address of all servers part of the `teleport_auth` group, port 3025 |
| `teleport.connection_limits.max_connections` | `teleport_connection_limits_max_connections` | `1000` | |
| `teleport.connection_limits.max_users` | `teleport_connection_limits_max_users` | `250` | |
| `teleport.log.output` | `teleport_log_output` | `stderr` | |
| `teleport.log.severity` | `teleport_log_severity` | `ERROR` | |
| `teleport.storage.type` | `teleport_storage_type` | `"dir"` | |
| `teleport.storage.region` | `teleport_storage_region` | teleport default | |
| `teleport.storage.table_name` | `teleport_storage_table_name` | teleport default | |
| `teleport.storage.audit_events_uri` | `teleport_storage_audit_events_uri` | teleport default | |
| `teleport.storage.audit_sessions_uri` | `teleport_storage_audit_sessions_uri` | teleport default | |
| `teleport.ciphers` | `teleport_ciphers` | teleport default | |
| `teleport.kex_algos` | `teleport_kex_algos` | teleport default | |
| `teleport.mac_algos` | `teleport_mac_algos` | teleport default | |
| `teleport.ciphersuites` | `teleport_ciphersuites` | teleport default | |
| `auth_service.enabled` | `teleport_auth_service_enabled` | `no` | If set to no, all other `teleport_auth_service_*` values will be ignored |
| `auth_service.cluster_name` | `teleport_auth_service_cluster_name` | `"main"` | |
| `auth_service.authentication` | `teleport_auth_service_authentication.*` | | Same map structure as per Teleport config file |
| `auth_service.listen_addr` | `teleport_auth_service_listen_addr` | `0.0.0.0:3025` | |
| `auth_service.public_addr` | `teleport_auth_service_public_addr` | teleport default | |
| `auth_service.tokens` | `teleport_auth_service_tokens` | teleport default | |
| `auth_service.session_recording` | `teleport_auth_service_session_recording` | teleport default | |
| `auth_service.proxy_checks_host_keys` | `teleport_auth_service_proxy_checks_host_keys` | teleport default | |
| `auth_service.client_idle_timeout` | `teleport_auth_service_client_idle_timeout` | teleport default | |
| `auth_service.disconnect_expired_cert` | `teleport_auth_service_disconnect_expired_cert` | teleport default | |
| `auth_service.license_file` | `teleport_auth_service_license_file` | teleport default | Enterprise mode config |
| | `teleport_auth_service_license_src` | `"license.pem"` | Enterprise mode config |
| `proxy_service.enabled` | `teleport_proxy_service_enabled` | `no` | If set to no, all other `teleport_proxy_service_*` values will be ignored |
| `proxy_service.listen_addr` | `teleport_proxy_service_listen_addr` | `0.0.0.0:3023` | |
| `proxy_service.web_listen_addr` | `teleport_proxy_service_web_listen_addr` | `0.0.0.0:3080` | |
| `proxy_service.tunnel_listen_addr` | `teleport_proxy_service_tunnel_listen_addr` | teleport default | |
| `proxy_service.ssh_public_addr` | `teleport_proxy_service_ssh_public_addr` | teleport default | |
| `proxy_service.https_key_file` | `teleport_proxy_service_https_key_file` | teleport default | |
| `proxy_service.https_cert_file` | `teleport_proxy_service_https_cert_file` | teleport default | |
| `proxy_service.kubernetes` | `teleport_proxy_service_kubernetes.*` | teleport default | Same map structure as per Teleport config |
| `ssh_service.enabled` | `teleport_ssh_service_enabled` | `no` | If set to no, all other `teleport_ssh_service_*` values will be ignored |
| `ssh_service.listen_addr` | `teleport_ssh_service_listen_addr` | `0.0.0.0:3022` | |
| `ssh_service.public_addr` | `teleport_ssh_service_public_addr` | teleport default | |
| `ssh_service.labels` | `teleport_ssh_service_labels` | teleport default | Same structure as per Teleport config |
| `ssh_service.commands` | `teleport_ssh_service_commands` | teleport default | Same structure as per Teleport config |
| `ssh_service.permit_user_env` | `teleport_ssh_service_permit_user_env` | teleport default | |
| `ssh_service.pam` | `teleport_ssh_service_pam` | teleport default | Same structure as per Teleport config |

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: teleport, x: 42 }

License
-------

