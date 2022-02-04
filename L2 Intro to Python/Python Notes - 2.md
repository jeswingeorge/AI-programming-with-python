# Importing Time Module

Timing your program or a portion of your program's code allows one to compare the time costs associated with using different algorithms to solve a problem. Additionally, timing your code allows one to know the time costs associated with running a program using given computing resources.

To time your code In Python requires the import of the `time()` function from the python time module. To simulate our program running for a certain period of time, we are going to use the time module's `sleep()` function. It will pause the program execution for a set number of seconds.

Since we only need to use the `time()` and `sleep()` functions, we will only import these two functions and not the entire time module. Only importing the functions from the module that you need saves on memory (RAM) your program requires to execute.

Such an import would look like the following:

```
# Imports time() and sleep() functions from time module
from time import time, sleep
```

## Using Time and Sleep Functions
To time your code you will need to:

- First, create a variable that records the __start time__ (start_time), the point you want to start timing your code
- Next, create a variable that records the __stop time__ (end_time), the point you want to stop timing your code
- Finally, to calculate the __total runtime__ (tot_time) by subtracting the start_time from end_time
- Note: the following:
        - __tot_time__ will be the total time your code ran in seconds
        - `sleep()` is used in the code below to pause the program execution for 75 seconds. To time actual code, you'd replace sleep(75) with the code that you wanted to time.

The code below demonstrates the use of `time()` and `sleep()`.

```
# Sets start time
start_time = time()

# Replace sleep(75) below with code you want to time
sleep(75)

# Sets end time
end_time = time()

# Computes overall runtime in seconds
tot_time = end_time - start_time

# Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
```

## Formatting Time

Likely you will want to format your runtime into a nice format like _hh:mm:ss_ where:

- _hh_ is two digit hours indicator
- _mm_ is two digit minutes indicator
- _ss_ is two digit seconds indicator

Recall the following regarding formatting time in seconds within python:
- __3600__ seconds in an hour
- __60__ seconds in a minute
- __/ (division operator)__ with `int()` function will return only the whole number part of a division
- __% (modulo operator)__ returns the remainder of a division
- `str()` function converts numeric values into strings
- Lesson __Data Types and Operators__: Arithmetic Operators and Integers and Floats will help with formatting time in python.  

Using the information above provides the following format of total runtime, as tot_time:

- `hours = int( (tot_time / 3600) )`
- `minutes = int( ( (tot_time % 3600) / 60 ) )`
- `seconds = int( ( (tot_time % 3600) % 60 ) )`

Below you will find code that will print the runtime in the format hh:mm:ss:

```
# Prints overall runtime in format hh:mm:ss
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int(  ( (tot_time % 3600) % 60 ) ) ) ) 
```

### Note
Instead of rounding to the nearest second, our code using the int() function and will truncate the value of seconds. This means if your Total Runtime: 4.519087974567, then it would be formatted to Total Runtime: 0:0:4. If you instead want to round to the nearest second, you will want to replace the int() function with the round() function in calculating the number of seconds above.

# Command Line Arguments - ARGPARSE
Argparse makes it easy to write user-friendly command-line interfaces.

The purpose of command line arguments is to provide a way for your programs to be more flexible by allowing external inputs (command line arguments) to be input into a program. The key is that these external arguments can change as to allow more flexibility in the program.

For example, imagine you wrote a program that simply counts the number of lines in a file and prints out that number to the screen. To allow the user to enter any file without having to change the program, one would want to pass in the file location as a command line argument. In this way, the program could be used on any file since the value is passed as an external input at runtime.

We will be using the `argparse` module to input the following external inputs into our program `check_image.py`.
## Usage of Argparse:

We will be using the __argparse__ module to input the following external inputs into our program __check_image.py__. We recommend writing the __get_input_args__ function to get the command line arguments using __argparse__.

Below are the three external inputs your __check_image.py__ program will need to retrieve from the user along with the suggested _default_ values each should have.

- Folder that contains the pet images
    - _pet_images/_
- The CNN model architecture to use
    - _resnet, alexnet, or vgg_ (pick one as the default). You will find them in classifier.py.
- The file that contains the list of valid dognames
    - _dognames.txt_

The `get_input_args` function will need to create an argument parser object using __[argparse.ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)__ and then use the __[add_argument](https://docs.python.org/3/library/argparse.html#adding-arguments)__ method to allow the users to enter in these three external inputs from above.

Below is an example of creating an argument parser object and then using __add_argument__ to add an argument that's a path to a folder and a second argument that's an integer.

```
# Creates Argument Parser object named parser
parser = argparse.ArgumentParser()

# Argument 1: that's a path to a folder
parser.add_argument('--dir', type = str, default = 'pet_images/', 
                    help = 'path to the folder of pet images') 
```
Below you will find an explanation of the inputs into __add_argument__.

- Argument 1:
    - `--dir` = The variable name of the argument (here it's dir)
    - `type` = The type of the argument (here it's a string)
    - `default` = The default value (here it's 'pet_images/')
    - `help` = The text that will appear if the user types the program name and then -h or --help. This allows the user to understand what's expected an argument's value

## Accessing Argparse Arguments

To access the arguments passed into the program through your argparse object, you will need to use the __[parse_args method](https://docs.python.org/3/library/argparse.html#the-parse-args-method)__. The code below demonstrates how to access the arguments through the argparse extending the example above.

To begin, you will need to assign a variable to __parse_args__ and then use that variable to access the arguments of your argparse object. If you are creating the argparse object within a function, you will need to return __parse_args__ instead of assigning a variable to it. Also, note that the variable in_args points to a collection of the command line arguments.

This means to access the one we created in the code above, we have to reference the collection variable name __in_args__ then specify the command line argument variable name `dir`. For this example, it would be __in_args.dir__, where _in_args_ is the collection variable name and _dir_ refers to the command line argument variable name. Notice that you need a dot (.) separating the two variable names. The code below shows the assignment of __in_args__ to our parser and then accessing the value of __in_args.dir__ with the print statement.

```
# Assigns variable in_args to parse_args()
in_args = parser.parse_args()

# Accesses values of Argument 1 by printing it
print("Argument 1:", in_args.dir)
```

## Running a Program using command line arguments

To run a program like __check_images.py__, first, open a terminal window within the Project Workspace. Next, type the following and hit enter to run the program (this example - check_images.py). Because no command line arguments are specified after the program name (this example - check_images.py) this will use the default command line arguments that have been defined.

```
python check_images.py 
```
To run a program like __check_images.py__ using the command line argument `--dir`, first, open a terminal window within the Project Workspace. Next, type the following and hit enter to run the program (this example - check_images.py). Notice that all command line arguments are specified after the program name (this example - check_images.py) and they are indicated by the -- that proceeds their variable name (this example: dir) with the value following the variable name (in this example the string: pet_images/).

```
python check_images.py --dir pet_images/
```

If you are having difficulty running check_images.py with command line arguments, see the example program call on line 23 of the program.


