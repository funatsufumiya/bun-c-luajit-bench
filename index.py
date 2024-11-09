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

if __name__ == "__main__":
    main()