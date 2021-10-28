from unittest import TestCase
from recursiveTiming.recursive_timing import RecursiveTimer


size = 30*1e6

RecursiveTimer()

def get_random_array(size=size):
    random_array = np.random.random((int(size)))
    return random_array

random_array = get_random_array()


output = np.zeros_like(random_array)

def __foo(i):
    output[i] = random_array[i] * 2
    return None

@timer('CPU', runs=3)
def foo():
    reference = [__foo(i) for i in range(len(random_array))]
    return reference



@timer('numpy_Vectorized', runs=3)
def numpy_Vectorized():
    reference = random_array * 2
    return reference


class TestEpiWeeks(TestCase):
        
    def test_RecursiveTimer(self):
        try:
            
            foo()

            numpy_Vectorized()
            
            print(timer.reference)
            
        except BaseException as err:
            print(err)
        