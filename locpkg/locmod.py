# this is the locmod module 

import os
import os.path

def foo_func(args):
    sz = os.path.getsize(args.input_file)
    print('locpkg.locmod.foo_func: sz=', sz)    

# end of locmod module
