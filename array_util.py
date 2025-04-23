import numpy as np
import subprocess

def average_3d_chunks(arr):
    x, y, z = arr.shape
    assert x % 2 == 0 and y % 2 == 0 and z % 2 == 0, "Each dimension must be divisible by 2"
    
    chunks = []
    for i in range(0, x, x // 2):
        for j in range(0, y, y // 2):
            for k in range(0, z, z // 2):
                chunk = arr[i:i + x // 2, j:j + y // 2, k:k + z // 2]
                chunks.append(np.mean(chunk))
    return chunks

def echo_string(string):
    for s in string:
        subprocess.run(['echo'],s)


