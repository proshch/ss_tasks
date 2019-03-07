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

subparsers = parser.add_subparsers(help='Available tables:', dest='table_name')
parser_students = subparsers.add_parser('students', help='Student table')
parser_teachers = subparsers.add_parser('teachers', help='Teacher table')
 
sub_subparsers = parser_students.add_subparsers(help='Commands', dest='command')
sub_subparsers_teacher = parser_teachers.add_subparsers(help='Commands', dest='command') 

#students
select = sub_subparsers.add_parser('SELECT', help=f'SELECT data from table')
select.add_argument('-all', action='store_true', help='Command to select \
                    cords from table')
select.add_argument('-sf', action='store', nargs=2, help='Command to select \
                    records with specified field(column value)')
 
insert = sub_subparsers.add_parser('INSERT', help=f'INSERT data into table')
insert.add_argument('-field', action='store', nargs=2, help='Command to \
                    insert value into column(column value)')

update = sub_subparsers.add_parser('UPDATE', help=f'UPDATE data into table')
update.add_argument('-u', action='store', nargs=4, 
                    help='Command to update value into field with condition \
                    (column condition_value column_to_set new_value)')

delete = sub_subparsers.add_parser('DELETE', help=f'DELETE data from table')
delete.add_argument('-df', action='store', help='Command to delete column')
delete.add_argument('-dr', action='store', nargs=2, help='Command to delete \
                    all records where (column value)')
#teacher
select = sub_subparsers_teacher.add_parser('SELECT', help=f'SELECT data from table')
select.add_argument('-all', action='store_true', help='Command to select \
                    cords from table')
select.add_argument('-sf', action='store', nargs=2, help='Command to select \
                    records with specified field(column value)')
 
insert = sub_subparsers_teacher.add_parser('INSERT', help=f'INSERT data into table')
insert.add_argument('-field', action='store', nargs=2, help='Command to \
                    insert value into column(column value)')

update = sub_subparsers_teacher.add_parser('UPDATE', help=f'UPDATE data into table')
update.add_argument('-u', action='store', nargs=4, 
                    help='Command to update value into field with condition \
                    (column condition_value column_to_set new_value)')

delete = sub_subparsers_teacher.add_parser('DELETE', help=f'DELETE data from table')
delete.add_argument('-df', action='store', help='Command to delete column')
delete.add_argument('-dr', action='store', nargs=2, help='Command to delete \
                    all records where (column value)')
     
args=parser.parse_args()
table = table_fields[args.table_name]

if 'all' in args and args.all != False:
    print(f'SELECT * FROM {sys.argv[1]};\n')
    for k, v in table.items():
        print(k, v)

if 'sf' in args and args.sf != None:
    print('SELECT * FROM {} WHERE {}={};'.format(args.table_name, args.sf[0], args.sf[1]))
    i = table[args.sf[0]].index(args.sf[1])
    for k, v in table.items():
        print(k, v[i])

if 'field' in args:
    if args.field[0] in table.keys():
        print('INSERT INTO {} ({})\nVALUES({});\n'.format(args.table_name, args.field[0], args.field[1]))
        table[args.field[0]].append(args.field[1])
        for k, v in table.items():
            print(k, v)    

if 'u' in args:
    if args.u[0] in table.keys():
        i = table[args.u[0]].index(args.u[1])
        table[args.u[2]][i] = args.u[3]
        print('UPDATE {}\nSET {}={}\nWHERE {}={};\n'.format(args.table_name, args.u[2], args.u[3], args.u[0], args.u[1]))
        for k, v in table.items():
            print(k, v[i]) 

if 'df' in args:
    if args.df in table.keys():
        print('ALTER TABLE {}\nDROP COLUMN {};\n'.format(args.table_name, args.df))
        table.pop(args.df, None)
        for k, v in table.items():
            print(k, v)

if 'dr' in args:
    if args.dr[0] in table.keys():
        print('DELETE FROM {}\nWHERE {}={};\n'.format(args.table_name, args.dr[0], args.dr[1]))
        i = table[args.dr[0]].index(args.dr[1])       
        for k, v in table.items():
            del v[i]
            print(k, v)

