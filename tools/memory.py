'''
This code was stolen (and slightly adapted) from https://stackoverflow.com/questions/24455615/python-how-to-display-size-of-all-variables
'''

import sys

def sizeof_fmt(num, suffix='B'):
    ''' by Fred Cirera,  https://stackoverflow.com/a/1094933/1870254, modified'''
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

def ram_usage(max_vars=None):
    '''
    Prints a list of variables and the space each one takes in memory (RAM).
    
    max_vars: int, maximum number of variables to display (default: None)
    '''
    for name, size in sorted(((name, sys.getsizeof(value)) for name, value in list(
                              globals().items())), key= lambda x: -x[1])[:max_vars]:
        print("{:>30}: {:>8}".format(name, sizeof_fmt(size)))
