"""Given a list of digits, determine the integer that it represents."""


def list_to_number(lst: list) -> int:
    """This function inputs a list, and returnns the number in it.

    It reads each digit, and add the (digit*10^power) to the number(result).
    power is determined by len(lst) - i(where i is the python index of the digit in the list)

    Example:
    [8,5,3,1] should be 8531, which is also:
    
    8*1000 + 5*100 + 3*10 + 1*1
    
    also equal to:
    
    8*10^3 + 5*10^2 + 3*10^1 + 1*10^0
    and this code breaks the list into the above format and calculate it.

    This assumes there are no negative numbers there.
    """
    number = 0
    for i, digit in enumerate(lst):
        number += digit * 10 ** (len(lst) - (i+1))
    return number

if __name__ == "__main__":
    """These are testcases, assuming all intergers in lst are positive."""
    print(list_to_number([8,3,5,1]))
    print(list_to_number([1,4,6,2,5,2,1]))
    print(list_to_number([1]))
