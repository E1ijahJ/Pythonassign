import numpy as np
import subprocess
import time
"""
    Splits a 3D NumPy array into 8 equally sized chunks and returns the average of each chunk.

    Parameters:
    ----------
    arr : np.ndarray
        A 3D NumPy array where each dimension is divisible by 2.

    Returns:
    -------
    list of float
        A list containing the average of each of the 8 chunks.

    Raises:
    ------
    AssertionError
        If the input array does not have 3 dimensions or if any dimension is not divisible by 2.
    """
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
"""
    Calls the system's 'echo' command on each string in the input list.

    Parameters:
    strings : list of str
        A list of strings to be echoed to the console.
    Returns:
    None
    """
def echo_string(string):
    for s in string:
        subprocess.run(['echo'],s)

"""
    Sequentially prints each element  with a 1-second delay.

    Parameters:
        items (list): The list of items.
    """
def seq_print(items):
    for item in items:
        print(item)
        time.sleep(1)

