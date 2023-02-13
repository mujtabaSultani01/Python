# Standard exceptions are direct descendants of StandardError.
# Let's have a simple example:
try:
    raise MemoryError ("Memory Error")
except MemoryError as e:
    print(e)