"""This module is for creating decorator that 
filter and chage specified words"""


old_new = ['submarine', 'ball']
smth_to_delete = ['interrupt', 'else']

def change_text(old_new, smth_to_delete):
    """Decorator for change my text"""
    
    def wrapped(func):
        text = func()
        for w in smth_to_delete:
           text = text.replace(*old_new).replace(w, '\b')
        print(text)
        return func
    return wrapped

@change_text(old_new, smth_to_delete)
def my_text():
    """Method that return some text"""

    return "Yellow submarine, something else, yellow interrupt submarine"

my_text()
