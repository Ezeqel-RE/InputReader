from typing import Optional, Tuple, List

def readFloat(message: str, error_message: str = "Please enter a float value!") -> float:
    """
    Reads a float value from user input.

    Args:
        message (str): The message to display to the user.
        error_message (str, optional): The error message to display if the input is not a float. Defaults to "Please enter a float value!".

    Returns:
        float: The read float value.
    """
    floatNumber = parse(readStr(message))
    if isinstance(floatNumber, (float, int)):
        return float(floatNumber)
    else:
        print(error_message)
        return readFloat(message, error_message)
    

def readInt(message: str, error_message: str = "Please enter an integer value!") -> int:
    """
    Reads an integer value from user input.

    Args:
        message (str): The message to display to the user.
        error_message (str, optional): The error message to display if the input is not an integer. Defaults to "Please enter an integer value!".

    Returns:
        int: The read integer value.
    """
    intNumber = parse(readStr(message))
    if isinstance(intNumber, int):
        return intNumber
    else:
        print(error_message)
        return readInt(message, error_message)


def readStr(message: str) -> str:
    """
    Reads a string value from user input.

    Args:
        message (str): The message to display to the user.

    Returns:
        str: The read string value.
    """
    return input(message)


def readChar(message: str, error_message: str = "Please enter a single character!") -> str:
    """
    Reads a single character from user input.

    Args:
        message (str): The message to display to the user.
        error_message (str, optional): The error message to display if the input is not a single character. Defaults to "Please enter a single character!".

    Returns:
        str: The read character.
    """
    char = readStr(message)
    if len(char) == 1:
        return char
    else:
        print(error_message)
        return readChar(message, error_message)


def readFile(pathToFile: str, callback=None) -> Tuple[Optional[Exception], str]:
    """
    Reads the content of a file.

    Args:
        pathToFile (str): The path to the file.
        callback (Optional[Callable[[Optional[Exception], str], None]], optional): A callback function to be called with the error and data. Defaults to None.

    Returns:
        Tuple[Optional[Exception], str]: A tuple containing the error (or None if no error occurred) and the data read from the file.
    """
    data = ""
    error = None
    try:
        with open(pathToFile, 'r') as file:
            data = file.read()
    except Exception as e:
        error = e
    if callback is not None:
        callback(error, data)
    return error, data


def readInputList(message: str, separator: str = ',', appropriate_data: bool = False, appropriate_bool_data: bool = False) -> List[Optional[str]]:
    """
    Reads a string input from the user and converts it into a list of elements.
    
    Args:
        message (str): The message to display when prompting the user for input.
        separator (str, optional): The separator used to split the input string into elements. Defaults to ','.
        appropriate_data (bool, optional): Whether to parse the elements into appropriate data types. Defaults to False.
        appropriate_bool_data (bool, optional): Whether to parse boolean elements into appropriate data types. Defaults to False.
    
    Returns:
        List[Optional[str]]: A list of elements converted from the input string.
    """
    print("Separator (" + separator + ")")
    chain = readStr(message)
    return _split(chain, separator, appropriate_data, appropriate_bool_data)
    
    
def _split(chain: str, separator: str = ',', appropriate_data: bool = False, appropriate_bool_data: bool = False) -> List[Optional[str]]:
    if len(chain) == 0:
        return []
    chains = chain.split(separator)
    if not appropriate_data:
        return chains
    else:
        for i, e in enumerate(chains):
            chains[i] = parse(e, appropriate_bool_data)
        return chains


def readList(path: str, separator: str = ',', appropriate_data: bool = False, appropriate_bool_data: bool = False) -> List[Optional[str]]:
    """
    Reads a list of elements from a file.

    Args:
        path (str): The path to the file.
        separator (str, optional): The separator used to split the elements in the file. Defaults to ','.
        appropriate_data (bool, optional): Whether to parse the elements into appropriate data types. Defaults to False.
        appropriate_bool_data (bool, optional): Whether to parse boolean elements into appropriate data types. Defaults to False.

    Returns:
        List[Optional[str]]: A list of elements read from the file.
    """
    error, data = readFile(path)
    if error is None:
        return _split(data, separator, appropriate_data, appropriate_bool_data)
    else:
        print("Error:", error)
        return []


def parse(expression: str, appropriate_bool_data: bool = False) -> Optional:
    """
    Parses the given expression to its appropriate data type.
        
    Args:
        expression (str): The expression to be parsed.
        appropriate_bool_data (bool, optional): Whether to parse boolean expressions into appropriate data types. Defaults to False.
        
    Returns:
        Optional: The parsed element.
    """
    
    def parseAppropriateNumber(strNumber: str) -> Optional:
        try:
            floatNumber = float(expression)
            intNumber = int(floatNumber)
            return floatNumber if floatNumber != intNumber else intNumber
        except Exception:
            return strNumber
    
    def parseAppropriateBool(strBool: str) -> Optional:
        if strBool.lower() in ['true', '1']:
            return True
        elif strBool.lower() in ['false', '0']:
            return False 
        else:
            return parseAppropriateNumber(strBool)
    
    if appropriate_bool_data:
        return parseAppropriateBool(expression)
    else:
        return parseAppropriateNumber(expression)


def readBool(message: str, error_message: str = "Please enter true|1 or false|0") -> bool:
    """
    Reads a boolean value from user input.

    Args:
        message (str): The message to display when asking the user to enter a boolean value.
        error_message (str, optional): The error message to display if the user enters an invalid value. Defaults to "Please enter true|1 or false|0".

    Returns:
        bool: The boolean value read from the user input.
    """
    boolean = parse(readStr(message), True)
    if isinstance(boolean, bool):
        return boolean
    else:
        print(error_message)
        return readBool(message, error_message)