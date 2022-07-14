from functools import reduce
import multiprocessing as mp
import time


def time_function(f):
    def inner(*args, **kwargs):
        t0 = time.time()
        x = f(*args, *kwargs)
        print("Time taken:", time.time()-t0)
        return x
    return inner


def parse_value(value):
    if isinstance(value, str):
        if value.startswith('#'):
            return 0
        return int(value)
    return value

@time_function
def sum_of_squares(l,parallel=False):
    print("Processing", len(l), "values.")
    if parallel:
        with mp.Pool(8) as pool:
            parsed_l =[x**2 for x in pool.map(parse_value, l)]
    else:
        parsed_l = [parse_value(e)**2 for e in l]
    return reduce(lambda a,b: a+b, parsed_l)
    


if __name__ == '__main__':
    print(sum_of_squares([0]))
    print(sum_of_squares([1]))
    print(sum_of_squares([1, 2, 3]))
    print(sum_of_squares([1, 2, 3],parallel=True))
    print(sum_of_squares([-1]))
    print(sum_of_squares([-1, -2, -3]))
    print(sum_of_squares(['1', '2', '3']))
    print(sum_of_squares(['-1', '-2', '-3']))
    print(sum_of_squares(['1', '2', '#100', '3']))

