"""This module is for create generator"""


data=[1,2,3,4,5,6,7,8,9,10]

def chunk(data, chunk_size):
    """Create generator
    
    Positional arguments:
    data - list of elements
    chunk_size - size of chunk 
    """
    end = chunk_size
    for i in range(0,len(data), end):
        yield data[i:chunk_size]
        chunk_size+=end

chunk_gen = chunk(data, 3)

for i in chunk_gen:
    print(i)

