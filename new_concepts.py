'''
Python is an interpreted language. What does that mean?
Well, when you type in the high-level code, it will get translated into
bytecode which is later translated into an interpreter which compiles at run-time.
In the interpreter, it will check if the code has appropriate syntax and format only.
If appropriate syntax and format, it compiles in run-time, 
and each line is converted to machine code understood by the OS
and executed thus everything rendered in Python is live and everything is addressed as an
object with a memory address location.
'''

import inspect #inspect live objects
from queue import Queue

print(inspect.getsource(Queue))