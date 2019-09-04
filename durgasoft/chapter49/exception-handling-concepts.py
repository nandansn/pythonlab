'''
2 types of errors,
1. syntax errors
2. runtime errors

execption handling talks about runtime errors only,

an unexpected event happens, that disturbs the normal flow of the program.

highly recommended to handle the exceptions,
graceful termination of the program.

Error is an object in python.
Every exception is child class of BaseException
BaseException
    - Exception
        - AttributeError
            - ZeroDivisionError
            - OverflowError
            - FloatingPointError
        - ArithmeticError
        - EOFError
        - NameError
        - OSError
            - FilenotFoundError
            - TimeoutError
            - PermissionError
            - InterruptedError
        - LookUpError
            - IndexError
            - KeyError
        - TypeError
        - ValueError
    - SystemExit
    - GeneratorExit
    - KeyBoardInterrupt


try:
    Risky code
except:
    Error/Exception handling code.


multiple exception handling:
---------------------------

try:
    risky code
except ZeroDivisionError:
    handle error
except FileNotFoundError:
    handle error


Single Exception Block can handle multiple exceptions:
-----------------------------------------------------

try:
    risky code
except (ZeroDivisionError,ValueError) as msg:
    handling code

finally block
------------

try:
    risky code
except expression as identifier:
    handling code
finally:
    cleanup/reset code

Finally executed in the following cases:

    if no exception
    if exception handled exception
    if excpetion not handled
    when you use os._exit(0), in this finally block will not be executed.
'''

