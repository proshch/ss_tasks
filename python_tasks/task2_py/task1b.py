"""This module is for create generator"""


def chunk(start, end, step):
    """Create generator
    
    Positional arguments:
    start - first number in list
    end - last number in list
    step - size of chunk
    """
    step = round(step)
    for i in range(start, end, step):
        my_list = [n for n in range(start, start+step) if n < end]
        yield my_list
        start+=step
 

chunk_gen = chunk(5, 27, 6.4)
for i in chunk_gen:
    print(i)



