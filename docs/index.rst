*****
Thank you for choosing Aardvark!
*****

Getting Started:
########
To get started with your first output do: ``output('hello world!\n')``. There you go, you've officially ran your first program! Take note of the ``\n``. If you (like me) get tired quickly of writing ``\n`` you can go ahead and use ``#include anr`` press enter, and then run ``output('hello world!')``. See! works without the ``\n``. We'll talk more about ``#include`` later, but for now thats all you need to know.

Running Files:
########
To run files all you need to do is run ``#include file-to-run`` this imports all aspects of a file and runs them directly to the terminal.

Math And String Concantonations:
########
Math works as usual (Multiplication: *, Division: /, Addition: +, Subtraction: -), and ``ints`` are defined as ``number()``. String concantonations is done by simply putting an addition sign between strings: ``'string '+'concantonation!'``, ``'string ' + 'concantonation!'`` is also valid.

If Statements:
########
If statments work like most other langages; it runs a check to see if the conditions described in the first line (the one with the initial ``if``) are met. If the conditions are true it will execute the given code inside the brackets. Syntax:
::
    if condition(s) {
        result
    }

Recieving User Input:
########
To get user input use the ``input()`` function. Syntax: ``input(prompt)``. This can be assigned to a variable like so: ``myVar = input(prompt)``, as it is assigned to a variable you can check if (in this case) ``myVar`` is equal to something code-block:
::

    if myVar == 'hello!' {
        do something
    }

Functions:
########
Functions are defined by the ``funct`` keyword. Syntax:
::
    funct myFunction(arg1, arg2) {
        do something
    }
Functions defined by the user run like any other function.

Statements
#########
All statments start with ``#``, there are currently 2 statments, ``#include`` and ``#max-memory``.
``#include`` includes the specified module. Syntax:
::
    #include server

``#max-memory`` sets the program's maximum allowed memory. Syntax:
::
    #max-memory 50 /Sets the maximum memory to 50mb\