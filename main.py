def check_isbn13(isbn):
    isbn_str = f'{isbn}'
    print(isbn_str)
    list(isbn_str)
    '''last idx should be 12'''
    sum_even = 0
    sum_odd = 0
    my_list= list(isbn_str)
    print(my_list)
    i = len(my_list) - 1
    while i >= 0:
      if i % 2 == 0:
        sum_odd += int(my_list[i])
      elif i % 2 >= 1:
        sum_even += int(my_list[i])
      i -= 1
    print(sum_odd, sum_even)
# This prints 34, 22 which is correct
    total = sum_odd + 3 * sum_even
    print(total)
#     This prints 100 which is correct!
check_isbn13(9780306406157)
