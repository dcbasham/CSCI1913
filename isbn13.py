def check_isbn13(isbn):
    '''Check the isbn is valid and return a boolean,
    use algorithm to check the check digit'''
    if 0 <= isbn <= 9999999999999:
       if len(isbn) < 13:
            new_isbn= make_isbn13(isbn)
            return new_isbn
       elif len(isbn) == 13:


def make_isbn13(number):
    ''' compute the check digit (last digit) from the book number,
    returning the new isbn as an integer'''
