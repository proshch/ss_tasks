"""This module is for creating script that printing dict content"""


simple_dict={'points': [(0, 0), (1, 2), (4, 2)],
             'string_key1': [{'key': 'info1', 'value': 100},
                             {'def': ['def_file_name1', 'def_file_name2'],
                              'key': '/path/to/...',
                              'value': ['file_name_1', 'file_name_2', 'file_name_3']},
                             {(1, 2, 3): (1, [1, 2, 3], {'key1': {'score': 12.39}, 'key2': 100})}],
              'string_key2': 'string_key2-value',
              ('test', 'data'): 123654789}

def parse_dict(val, c):
    """ This method is for mining dict content:
    key information (value, type)
    value information (value, type, subvalues, ...) 

    Positional arguments:
    val - value of key in initial dict
    """
    if isinstance(val, (list, tuple, set)):
        for elem in val:
            c += 1  
            print('--->'*c+'Subvalue {}'.format(elem))
            print('--->'*c+'Subvalue type - {} \n'.format(type(elem)))
            if isinstance(elem, (list, tuple, set, dict)):
               parse_dict(elem, c)
               c = 0
            else:
                c -= 1
    elif isinstance(val, dict):
        for subvalue in val.values():
            c += 1  
            print('--->'*c+'Subvalue {}'.format(subvalue))
            print('--->'*c+'Subvalue type - {} \n'.format(type(subvalue)))        
            if isinstance(subvalue, (list, tuple, set, dict)):
                parse_dict(subvalue, c)
                c = 0
            else:
                c -= 1

for val in simple_dict.values():
    c = 0 
    print('Value {}'.format(val))
    print('Value type - {} \n'.format(type(val)))    
    parse_dict(val, c)

