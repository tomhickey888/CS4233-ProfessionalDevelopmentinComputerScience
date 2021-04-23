import hashlib

#Returns a list of hash digests from a given range of (min) to (max) to its parent process using a pipe (writer)
def pipes(min, max, writer):
    hashvalues = []
    for x in range(min, max):
        hashvalues.append(hashlib.sha512(str(x).encode()).hexdigest())
    writer.send(hashvalues)
    writer.close()

#Returns a list of hash digests from a given range of (min) to (max) to its parent process directly for multiprocessing with a pool
def multi(min,max):
    hashvalues = []
    for x in range(min, max):
        hashvalues.append(hashlib.sha512(str(x).encode()).hexdigest())
    return(hashvalues)