"""This module is for creating parser for Command Line Interface."""
import argparse
import sys


tables = ['students', 'teachers']
table_fields = {'students': {'student_id': [1, 2], 
                            'first_name': ['Oleh', 'Makar'], 
                            'last_name': ['Bartosh', 'Lopez']}, 
                'teachers': {'teacher_id': [1, 2], 
                            'last_name': ['Kropyvnytska', 'Lebid']
                            }
                }

parser = argparse.ArgumentParser()

parser.add_argument('table_name', action='store', 
                    help=f'Use one of tables: {tables}')
table = sys.argv[1]

if table in tables:
    table = table_fields[sys.argv[1]]
 
    subparsers = parser.add_subparsers(help='Choose command')
    select = subparsers.add_parser('SELECT', help=f'Available fields to SELECT \
                                    are {table.keys()}')
    select.add_argument('-all', action='store_true', help='Command to select \
                        cords from table')
    select.add_argument('-sf', action='store', nargs=2, help='Command to select \
                        records with specified field(column value)')
     
    insert = subparsers.add_parser('INSERT', help=f'Available fields to INSERT \
                                    are {table.keys()}')
    insert.add_argument('-field', action='store', nargs=2, help='Command to \
                        insert value into column(column value)')
    
    update = subparsers.add_parser('UPDATE', help=f'Available fields to UPDATE \
                                    are {table.keys()}')
    update.add_argument('-u', action='store', nargs=4, 
                        help='Command to update value into field with condition \
                        (column condition_value column_to_set new_value)')
   
    delete = subparsers.add_parser('DELETE', help=f'Available fields to DELETE \
                                    are {table.keys()}')
    delete.add_argument('-df', action='store', help='Command to delete column')
    delete.add_argument('-dr', action='store', nargs=2, help='Command to delete \
                        all records where (column value)')
     
args=parser.parse_args()

if 'all' in args and args.all != False:
    print(f'SELECT * FROM {sys.argv[1]};\n')
    for k, v in table.items():
        print(k, v)

if 'sf' in args and args.sf != None:
    print('SELECT * FROM {} WHERE {}={};'.format(sys.argv[1], args.sf[0], args.sf[1]))
    i = table[args.sf[0]].index(args.sf[1])
    for k, v in table.items():
        print(k, v[i])

if 'field' in args:
    if args.field[0] in table.keys():
        print('INSERT INTO {} ({})\nVALUES({});\n'.format(sys.argv[1], args.field[0], args.field[1]))
        table[args.field[0]].append(args.field[1])
        for k, v in table.items():
            print(k, v)    

if 'u' in args:
    if args.u[0] in table.keys():
        i = table[args.u[0]].index(args.u[1])
        table[args.u[2]][i] = args.u[3]
        print('UPDATE {}\nSET {}={}\nWHERE {}={};\n'.format(sys.argv[1], args.u[2], args.u[3], args.u[0], args.u[1]))
        for k, v in table.items():
            print(k, v[i]) 

if 'df' in args:
    if args.df in table.keys():
        print('ALTER TABLE {}\nDROP COLUMN {};\n'.format(sys.argv[1], args.df))
        table.pop(args.df, None)
        for k, v in table.items():
            print(k, v)

if 'dr' in args:
    if args.dr[0] in table.keys():
        print('DELETE FROM {}\nWHERE {}={};\n'.format(sys.argv[1], args.dr[0], args.dr[1]))
        i = table[args.dr[0]].index(args.dr[1])       
        for k, v in table.items():
            del v[i]
            print(k, v)

