# main module for a test python script in a zip file.

# standard modules
import argparse
import sys

# local modules 
import locpkg 
import locpkg.locmod 

# - - - 

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args(argv[1:])
    print('in main: args:', args)
    print('locpkg.BLUE_MARS:', locpkg.BLUE_MARS)
    locpkg.locmod.foo_func(args)

# - - - 

if __name__ == '__main__':
    main(sys.argv)

# end of file
