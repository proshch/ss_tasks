"""Module for Python File I/O"""

USER = 'oleksandr'
FILE_PATH = f'/home/{USER}/py_scripts/task_io/result.txt'

data = {'IPs': ('192.168.2.3', '6.6.6.6', '168.156.98.2'),
        'Phones': ('0986783422', '0634666982', '0500901212'),
        'URLs Domains': ('test.com', 'test1.com', 'test2.com')
        }

new_data = {'IPs': ('123.168.2.3', '6.6.6.6', '18.156.58.52'),
            'Phones': ('0656583422', '0934362912', '0501921312'),
            'URLs Domains': ('test.com', 'test3.com', 'test4.com')
            }

def recreate(data, file_path):
    """Each run recreate result file.

    Positional arguments:
    data (dict): data
    file_path (str): path to file
    """

    with open(file_path, 'w', encoding='utf-8') as result_file:
        for key, value in data.items():
            line = '{}: {}\n'.format(key, ' '.join(value))
            result_file.write(line)

def append_to_file(data, file_path):
    """Each run append data to existing file.

    Positional arguments:
    data (dict): data
    file_path (str): path to file
    """

    with open(file_path, 'a', encoding='utf-8') as result_file:
        result_file.write('\n')
        for key, value in data.items():
            line = '{}: {}\n'.format(key, ' '.join(value))
            result_file.write(line)

def combine_data(new_data, file_path):
    """Combine data from existing file and new info. Result file should
    be updated with combined unique data

    Positional arguments:
    new_data (dict): with new data
    file_path (str): path to file
    """

    with open(file_path, 'r+', encoding='utf-8') as txt_file:
        text = txt_file.read()
        txt_file.write('\nNew data: \n')
        for key, value in new_data.items():
            txt_file.write(key+': ')
            for item in value:
                if item in text:
                    words = text.split()
                    print('Count of '+item+' is: '+str(words.count(item)))
                else:
                    txt_file.write(item+' ')
            txt_file.write('\n')
