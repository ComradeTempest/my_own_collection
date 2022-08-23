#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
test documentation
Basically it's a dummy module, comments cut, some code inserted.
'''

EXAMPLES = r'''

test info

'''

RETURN = r'''
'''

import os

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        file=dict(type='str', required=True),
        text=dict(type='str', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file_exists = os.path.exists(module.params['file'])
    file_content = ''

    if not file_exists:
        result['changed'] = True
    else:
        file = open(module.params['file'], mode='r')
        file_content = file.read()
        file.close()

        if file_content != module.params['text']:
            result['changed'] = True

    if module.check_mode:
        module.exit_json(**result)

    if result['changed'] == False:
        module.exit_json(**result)

    file = open(module.params['file'], mode='w')
    file.write(module.params['text'])
    file.close()

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main() 
