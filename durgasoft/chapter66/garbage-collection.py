'''
Python will provide assistance to destroy useless object callled, garbage collector.
    If the object does not contain any reference variable, then the object is eligible for garbage collection.

how to enable and disable gc in our program,
    using the module called gc.
        gc.isenabled() - by default garbage collection enabled.
        gc.disable() - enable gc
        gc.enable() - disable gc
        gc in python, asks for if any last wish, if so then fulfills and delete the object.
        __del__ method used for deletion.
'''