## TUPLES
Tuple is a datatype for immutable ordered sequence of elements. Similar to list as it has ordered collection of objects and can be accesses by indices.
Unlike lists, Tuples are immutable i.e, we cannot sort the elements in it or add or remove elements. 

- Why do we have tuples if they are like lists but with fewer features?
Tuples are useful when we have two or more values which are so closely related such that they will be always be used together. 
Eg: (lattitude, longtitude) coordinates. Tuples can also be used to assign multiple variables in compact ways.

```
l,b,h = 1,2,3
print("The dimensions are {} x {} x {}".format(l,b,h))
```

Tuple unpacking is a way via which we assign multiple values to different variables as shown above.

## SET
A data type for mutable unordered collection of unique elements.

## Identity operators - `is` and `is not`
- `is` evaluates if both sides have the same identity.
- `is not` evaluates if both sides have different identities.

`is` operator can also be used with dictionaries to check if the key is valid or whether on being called the key has returned None or not.

```
elements = {'hydrogen': 1, 'helium': 2, 'carbon':6}
x = elements.get('delithium')
is_null = x is None
print(is_null) 
>> True

not_null = x is not None
print(not_null)
>> False
```
```
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

True
True
True
False
```
That's correct! List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. That is the difference between checking for equality vs. identity.

## Dictionary

`.get()` function returns None if the key is not available or the value you want to return must be specified.

```
>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"
```

## Compound Data structures

```
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
```


We can access elements in this nested dictionary like this.
```
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
```

## zip and enumerate
`zip` and `enumerate` are useful built-in functions that can come in handy when dealing with loops.

#### zip
`zip` returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing

`list(zip(['a', 'b', 'c'], [1, 2, 3]))` would output `[('a', 1), ('b', 2), ('c', 3)]`.

Like we did for `range()` we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this.

```
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
```

In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.
```
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```
This would create the same letters and nums tuples we saw earlier.

Zip Lists to a Dictionary

```
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)
```

#### enumerate
`enumerate` is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.
```
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
```

This code would output:

```
0 a
1 b
2 c
3 d
4 e
```

## Functions
Functions are useful blocks of code that allow you to encapsulate a task. Encapsulation allows us to carry out a whole series of steps with one simple command. You can think about functions as a way to take what you have already learned how to do and put it in an easy-to-use container that allows you to use it over and over again.

## Variable Scope
Variable scope refers to which parts of a program a variable can be referenced, or used, from.

It's important to consider scope when using variables in functions. If a variable is created inside a function, it can only be used within that function. Accessing it outside that function is not possible.

__Good practice:__ It is best to define variables in the smallest scope they will be needed in. While functions can refer to variables defined in a larger scope, this is very rarely a good idea since you may not know what variables you have defined if your program has a lot of variables.

What is the result of running this code? 
```
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
```
This code causes an `UnboundLocalError: local variable 'egg_count' referenced before assignment`, because the variable egg_count in the first line has global scope. Note that it is not passed as an argument into the function, so the function assumes the egg_count being referred to is the global variable.

You saw that within a function, we can print a global variable's value successfully without an error. This worked because we were simply accessing the value of the variable. If we try to change or reassign this global variable, however, as we do in this code, we get an error. __Python doesn't allow functions to modify variables that aren't in the function's scope.__

A better way to write this would be:

```
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
```

Note a similar code:

```
str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
```

__Output:__ It will print 'Variable scope is an important concept.'

If we tweak the code little bit:
```
str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
```

When we comment out str1 = 'Variable scope is an important concept,' the str1 variable being referenced inside the function becomes the one with the global scope from line 1. So the value of that variable with global scope is printed out inside the function.

### Importing Local Scripts

We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where you want to organize your code into multiple files and reuse code in those files. If the Python script you want to import is in the same directory as your current script, you just type `import` followed by the name of the file, without the .py extension.

```
import useful_functions
```

It's the standard convention for `import` statements to be written at the top of a Python script, each one on a separate line. This `import` statement creates a __module__ object called `useful_functions`. Modules are just Python files that contain definitions and statements. To access objects from an imported module, you need to use dot notation.

```
import useful_functions
useful_functions.add_five([1, 2, 3, 4])
```

We can add an alias to an imported module to reference it with a different name.

```
import useful_functions as uf
uf.add_five([1, 2, 3, 4])
```

#### Using a main block

To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an `if __name__ == "__main__"` block. Or alternatively, include them in a function called main() and call this in the `if main` block.

Whenever we run a script like this, Python actually sets a special built-in variable called `__name__` for any module. When we run a script, Python recognizes this module as the main program, and sets the `__name__` variable for this module to the string `"__main__"`. For any modules that are imported in this script, this built-in `__name__ `variable is just set to the name of that module. Therefore, the condition `if __name__ == "__main__"`is just checking whether this module is the main program.


#### Try It Out!
Here's the code I used in the video above. Create these scripts in the same directory and run them in your terminal! Experiment with the `if main` block and accessing objects from the imported module!

```
# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)
```

```
# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
```

