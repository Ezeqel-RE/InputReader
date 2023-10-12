## InputReaderHelpers

This module contains several functions to read different types of values from user input.

## Installation

Use the following command to install the InputReader module:



## Usage

Here are some examples of using the functions from the input reader module:

```python
from input_reader.inputr import readFloat, readInt, readStr, readChar, readBool, readFile, readList

# Read a float
value = readFloat("Enter a decimal number: ")
print("You entered:", value)

# Read an integer
value = readInt("Enter an integer number: ")
print("You entered:", value)

# Read a string
value = readStr("Enter a string: ")
print("You entered:", value)

# Read a single character
value = readChar("Enter a character: ")
print("You entered:", value)

# Read a bool
value = readBool("Enter a true|1 or false|0: ")
print("You entered:", value)

# Read a list from user input (default separator = ',')
values = readInputList("Enter list chain with ',' separator ")
print(values)

# Read a list from user input with appropriate data type 
values = readInputList("Enter list chain with ',' separator ", appropriate_data = True, appropriate_bool_data = True)
print(values)


# Read the content of a file with callback
path = "example.txt"
def callback(error, data):
    if error:
        print("An error occurred:", error)
    else:
        print("File content:", data)

readFile(path, callback)

# Read the content of file without callback
path = "example.txt"
error, data = readFile(path)
if error is None:
    print(data)
else:
    print("Error:",error)
    
# parse string with appropriate data type
a = parse('123') # 123
b = parse('.123') # 0.123
c = parse('123.') # 123
d = parse('true') # 'true'
e = parse('true',appropriate_bool_data = True) # True
f = parse('0',appropriate_bool_data = True) # False

```

## Contribution

Contributions are welcome! 
If you would like to improve this module, 
please submit a pull request.
