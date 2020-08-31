*****
Thank you for choosing Aardvark!
*****

Getting Started:
########
To get started with your first output do: ``output('hello world!\n')``. There you go, you've officially ran your first program! Take note of the ``\n``. If you (like me) get tired quickly of writing ``\n`` you can go ahead and use ``#include anr`` press enter, and then run ``output('hello world!')``. See! works without the ``\n``. We'll talk more about ``#include`` later, but for now thats all you need to know. Comments start with ``/`` and end with ``\``. Clearing the terminal is done by using ``clear()``.

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
Function can be called by typing the function's name with parenthese at the end (if the function has parameters include the parameter values too!) like so: ``myFunction()``, or ``myFunction(args)`` if the function was defined with arguments. Function arguments are seperated by commas (``,``). Functions defined by the user run like any other function. To return from a function simply do ``return data``, ``data`` can be equal to anything, a string, a number, function, or a variable ect...

'Statements':
#########
All statments start with ``#``, there are currently 3 statments, ``#include``, ``#ape``, and ``#max-memory``.
``#include`` includes the specified module. Syntax:
::
    #include file

``#max-memory`` sets the program's maximum allowed memory. Syntax:
::
    #max-memory number / For instance Sets the maximum memory to 50mb \

File Handling:
#########
Aardvark's file handling is very similar to Python's, as it is very straight forward: ``open(file).read()`` will read a file, ``.write(data)`` will write something to a file, ``.append(data)`` will apend something to the end of a file. You can also open files into variable like so: ``a = open(file)``. You can get the ammount of space a file takes up in kilobytes by using ``file_size()``, Syntax: ``file_size(file)``.

APE:
########
APE is Aardvark's package manager, it stands for Aardvark Packager Extension. You can install .adk files from the website. Go ahead, and type ``#ape atest``, that will install atest.adk on to your computer. To run that file just ``#include atest`` (it has to be in the same directory as the file you are running it from or in your ``scripts`` folder). Extension/Packages can also be writen in python, these have to be in the same folder as ``main.py``. To do this you have to put ``#Aardvark.library`` at the beginning of the file, and don't forget to do ``from Aardvark import *`` this allows you to use Aardvark's function and type creators, amoung other things: ``Aardvark.function('function_name')``, ``Aardvark.type('name')``... To learn more about this look into ``main.py`` and your ``Language`` folder.

Visual Module:
########
To use the visual module first you have to include it (``#include visual``), after that you are good to go! The visual module allows you to display things to the screen in a sperate window, to first initiate the window you do: ``visual(title, geometry)``, the window geometry is formated as follows: ``NUMBERxNUMBER``. To make words apear to the screen use the label method: ``label(text, foreground, background, xcord, ycord)``, for the list of colors see Tkinter's list of colors. To recieve input use: ``entry(prompt, foreground, background, xplace, yplace)``. All of these methods can be assigned to a variable. Last off, to make the window visible use: ``show()``, make sure you do this, otherwise your window will be invisible. Example:
::
    #include visual
    visual('myWindow', '800x800')
    label('hello world!', 'black', 'white', 80, 150)
    entry('Entry! ', 'black', 'white', 100, 100)
    show()

Server Module
########
To start, lets include server using ``#include server``, when thats done, you can start making your first Aardvark web server. Aardvark we servers work similar to python's flask (If you know what that is). Lets start by making a basic website in just 3 lines of code.
::
    #include server
    render_string('Hello World!')
    run_server()

Run that and there you go, your first Aardvark web server. Now, lets learn something a little harder, rendering files. In ``render_string()`` you can add the second argument for the part of the site it will show up on. There is also ``render_file()`` which takes the same arguments as ``render_string``, except that the first argument is the name of the file to render. Make a file called index.html and put some html code in it. And try this code:
::
    #include server
    render_file('index.html')
    run_server()

Run the code and look at the output, your html file shows up in the browser. Now we will learn how to catch errors like 404. You can use ``errorhandler()`` to do that. ``errorhandler()`` takes to arguments, the error code, and the file to run if that error comes. Make a file called error.html and write an error message. Now run this code:
::
    #include server
    render_file('index.html')
    errorhandler(404, 'error.html')
    run_server

And try going to a page that does not exist like ``/abc.html`` for example, your error message should come up. 

Exec And Running Other Langs:
#######
In Aardvark you are able to run Python, and C++, this can be done by using the ``exec()`` function: ``exec('code', 'language')``. Keep in mind this is for code snippets, NOT FULL PROGRAMS. Example:
::
    exec('print("Hello world in python!")', 'py')

Current Memory:
#######
You can recieve the program's current memory usage by doing ``currentMemUsage()``. This takes no parameters.
