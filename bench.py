# bench myRandom(), show ns/iter

import timeit
import ctypes
import os
import platform

def main():
    if platform.system() == 'Windows':
        mylib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'libmyRandom.dll'))
    elif platform.system() == 'Linux':
        mylib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'libmyRandom.so'))
    elif platform.system() == 'Darwin':
        mylib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'libmyRandom.dylib'))
    else:
        print("Unsupported OS")
        return

    print("myRandom() =", mylib.myRandom())

    n = 1000000
    t = timeit.timeit(lambda: mylib.myRandom(), number=n)
    print(f"Total time: {t:.6f} s ({n} iter)")
    print(f"{t/n * 1e9:.6f} ns/iter")


if __name__ == "__main__":
    main()