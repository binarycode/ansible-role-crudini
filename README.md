Ansible Role: Crudini
=========

[Crudini](https://github.com/pixelb/crudini) is a utility for manipulating ini files. This role installs crudini on RHEL/Debian-based systems and provides a module to manage it.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - binarycode.crudini
    - hosts: servers
      tasks:
        - name: Configure RabbitMQ access.
          crudini:
            path: /etc/cinder/cinder.conf
            config:
              DEFAULT:
                rpc_backend: rabbit
              oslo_messaging_rabbit:
                rabbit_host: controller
                rabbit_userid: openstack
                rabbit_password: password

This is going to configure `/etc/cinder/cinder.conf` (assuming it already exists) in a following way:

    [DEFAULT]
    rpc_backend = rabbit
    [oslo_messaging_rabbit]
    rabbit_host = controller
    rabbit_userid = openstack
    rabbit_password = password

License
-------

BSD

Author Information
------------------

[Igor Sidorov](https://github.com/binarycode)
