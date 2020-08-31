*****
Thank you for choosing Aardvark!
*****

Getting Started:
########
To get started with your first output do: ``output('hello world!\n')``. There you go, you've officially ran your first program! Take note of the ``\n``. If you (like me) get tired quickly of writing ``\n`` you can go ahead and use ``#include anr`` press enter, and then run ``output('hello world!')``. See! works without the ``\n``. We'll talk more about ``#include`` later, but for now thats all you need to know. Comments start with ``/`` and end with ``\``.

Running Files:
########
To run files all you need to do is run ``#include file-to-run`` this imports all aspects of a file and runs them directly to the terminal.

Math And String Concantonations:
########
Math works as usual (Multiplication: *, Division: /, Addition: +, Subtraction: -), and ``ints()`` are defined as ``number(perameter)``. String concantonations is done by simply putting an addition sign between strings: ``'string '+'concantonation!'``, ``'string ' + 'concantonation!'`` is also valid.

Booleans
########
Booleans in Aardvark are ``True`` and ``False``, they can both be assigned to a variable.
::
    myBoolean = True
    if myBoolean == True {
      output('Nice!')
    }
    if myBoolean == False {
      output('Sad...')
    }

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
    myVar = input('How are you? ')
    if myVar == 'good' {
        output('Nice!')
    }

While Loops:
########
While statements are so useful in all the languages, and also in Aardvark! While is used to check if something is true, and if it is true it will continue to execute the code within the while block until it is false (this can also work if something is always true).

::

    n = 0
    while n < 10 {
      output(n)
      n += 1
    }

Functions:
########
Functions are defined by the ``funct`` keyword. Syntax:
::
    funct myFunction(args) {
        do something
    }
Function can be called by typing the function's name with parenthese at the end (if the function has parameters include the parameter values too!) like so: ``myFunction()``, or ``myFunction(args)`` if the function was defined with arguments. Function arguments are seperated by commas (``,``). Functions defined by the user run like any other function.

'Statements':
#########
All statments start with ``#``, there are currently 2 statments, ``#include`` and ``#max-memory``.
``#include`` includes the specified module. Syntax:
::
    #include file

``#max-memory`` sets the program's maximum allowed memory. Syntax:
::
    #max-memory number / For instance Sets the maximum memory to 50mb \

File Handling:
#########
