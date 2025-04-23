import numpy as np
from array_util import average_3d_chunks

def test_average_3d_chunks_basic():
    array = np.arange(64).reshape((4, 4, 4))  # 4x4x4 cube
    results = average_3d_chunks(array)
    
    assert len(results) == 8
    assert all(isinstance(val, float) for val in results)