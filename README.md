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

| Teleport Config | Var Name | Default Value | Description |
|---------------- | -------- | ------------- | ----------- |
| teleport.nodename | `teleport_nodename` | `ansible_hostname` | |
| teleport.data_dir | `teleport_data_dir` | `"/var/lib/teleport"`| |
| teleport.auth_token | `teleport_auth_token` | `hostvars[groups['teleport_auth'][0]]['join_token']` | A random token will be generated on the root auth server |
| teleport.ca_pin | nil | `hostvars[groups['teleport_auth'][0]]['ca_pin']`| Value from root auth server will be obtained and set |
| teleport.advertise_ip | teleport default | teleport default | node public IP address |
| teleport.auth_servers | teleport default | `<public_ip>:3025` | Public IP address of all servers part of the
`teleport_auth` group, port 3025 |
| teleport.connection_limits.max_connections | teleport_connection_limits_max_connections | `1000` | |
| teleport.connection_limits.max_users | teleport_connection_limits_max_users | `250` | |
| teleport.log.output | teleport_log_output | `stderr` | |
| teleport.log.severity | teleport_log_severity | `ERROR` | |
| teleport.storage.type | teleport_storage_type | `"dir"` | |
| teleport.storage.region | teleport_storage_region | teleport default | |
| teleport.storage.table_name | teleport_storage_table_name | teleport default | |
| teleport.storage.audit_events_uri | teleport_storage_audit_events_uri | teleport default | |
| teleport.storage.audit_sessions_uri | teleport_storage_audit_sessions_uri | teleport default | |
| teleport.ciphers | teleport_ciphers | teleport default | |
| teleport.kex_algos | teleport_kex_algos | teleport default | |
| teleport.mac_algos | teleport_mac_algos | teleport default | |
| teleport.ciphersuites | teleport_ciphersuites | teleport default | |

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

