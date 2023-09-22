#DaurieBasham_Lab01_CSCI1913-004
def check_isbn13(isbn):
    """ A function for validating if the check-digit of an ISBN13 is correct. Takes an
integer argument and returns a boolean indicating whether true or false
:rtype: boolean"""
    if 0 <= isbn <= 9999999999999:
        string_isbn= str(isbn)
        odds = 0
        evens = 0
        if len(string_isbn) < 13:
            string_isbn= string_isbn.zfill(13)
        for odd in range(0,13,2):
            odds += int(string_isbn[odd])
        for even in range(1,12,2):
            evens += int(string_isbn[even])
        total = odds + 3 * evens
        is_divisible = total % 10
        if is_divisible == 0:
            return True
        else:
            return False
    else:
        return False



def make_isbn13(number):
    """This function should take a single integer and convert it to an equivalent valid
    ISBN 13, returning the new isbn13 as an integer
    :rtype: int"""
    sum_odd= 0
    sum_even= 0
    num_str= f'{number}'
    if 0 <= number <= 9999999999999:
        num_str = num_str.zfill(12)
        i = 0
        while i < len(num_str):
            if i % 2 == 0:
                sum_odd += int(num_str[i])
            elif i % 2 >= 1:
                sum_even += int(num_str[i])
            i += 1
        total = sum_odd + 3 * sum_even
        last_digit = total % 10
        if last_digit == 0:
            check_digit = 0
        else:
            check_digit = 10 - last_digit
        new_num_str= f'{num_str}{check_digit}'
        new_number = int(new_num_str)
        return new_number
    else :
     return -1

def secret_words():
    """This function should take no input and return only a string. The string returned should contain the
    secret words posted to Piazza and slack.
    :rtype: str"""
    return 'notebook', 'sector'
