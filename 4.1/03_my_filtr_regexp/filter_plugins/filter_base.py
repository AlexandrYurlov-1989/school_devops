#!/usr/bin/python

import re
from ansible.errors import (
    AnsibleFilterTypeError
)


def concat_strings(var_a):
    '''
        function doc
    '''
    pattern = re.compile('^[0-9A-Fa-f]+$')
    
    if isinstance(var_a, int):
        raise AnsibleFilterTypeError("the not string %s instead " % str(var_a))
    
    if pattern.match(var_a):
        if len(var_a) % 2 != 0:
            return "The string can't be split into an even number of groups of two"
    else:
        return "The string has an invalid character"

    


    # Split string using slicing in a loop with step of 2
    new_s = re.sub(r"(\d{2})(?=\d)", r"\1:", var_a)
    return new_s 



class FilterModule(object):
    def filters(self):
        return {
            'concat_strings': concat_strings
        }

