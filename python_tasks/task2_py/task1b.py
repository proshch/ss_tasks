"""This module is for create generator"""


def chunk(start, end, step):
    """Create generator
    
    Positional arguments:
    start - first number in list
    end - last number in list
    step - size of chunk
    """
    while start < end:
        new_end = start+step
        if new_end > end:
            new_end = end
        yield [i for i in range(start, new_end)]
        start += step 

chunk_gen = chunk(7, 25, 7)
for i in chunk_gen:
    print(i)

