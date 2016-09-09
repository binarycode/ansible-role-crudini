#!/usr/bin/python

import os
import re

from ansible.module_utils.basic import *

def main():
    def flatten(d, parent_key=''):
        items = []
        for k, v in d.items():
            new_key = parent_key + ' ' + k if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)

    module = AnsibleModule(
        argument_spec = dict(
            path   = dict(required=True),
            config = dict(required=True, type='dict'),
        ),
    )

    crudini = module.get_bin_path('crudini')
    path    = os.path.expanduser(module.params['path'])
    config  = flatten(module.params['config'])
    changed = False

    for key, value in config.iteritems():
        cmd = ' '.join([crudini, '--verbose', '--set', path, key, value])

        (rc, stdout, stderr) = module.run_command(cmd, check_rc=True, use_unsafe_shell=True)

        if re.match('^changed', stderr):
            changed = True

    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
