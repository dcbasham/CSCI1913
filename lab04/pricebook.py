# Daurie Basham
def is_sorted(pricebook):
    """takes a list of tuples and checks if it is
    sorted ascending by name (string), which is the
    second element in the tuple pair. O(N) run time required
    :rtype bool """
    last_idx = len(pricebook) - 1
    i = 0
    while i < last_idx:
        temp = pricebook[i][1]
        next_el = pricebook[i + 1][1]
        if temp > next_el:
            return False
        else:
            i += 1
    return True


def price_average(pricebook):
    """get the average price of the list of tuples, price is the first
    element in each tuple pair
    :rtype float"""
    sum_pb = 0.0
    items = len(pricebook)
    for i in range(len(pricebook)):
        sum_pb += pricebook[i][0]
    if sum_pb == 0.0:
        return 0.0
    else:
        return sum_pb / items


def unsorted_get(pricebook, name):
    """Search pricebook by name and return its price. If name not found,
    return None
    O(N)"""
    for i in range(len(pricebook)):
        if pricebook[i][1] == name:
            return pricebook[i][0]
    return None


def unsorted_put(pricebook, name, price):
    """pricebook is an unsorted list of tuples (name, price).
    The function replicates a dictionary assignment with key: name and
    value:price.
    Update pricebook with the new price of the product name
    or add a new element (stored as a tuple) to the list.
    """
    new_tuple = (price, name)
    if len(pricebook) < 1:
        pricebook.append(new_tuple)
    else:
        for i in range(len(pricebook)):
            if pricebook[i][1] == name:
                pricebook.insert(i, new_tuple)
                pricebook.pop(i + 1)
            elif i == len(pricebook) - 1:
                pricebook.append(new_tuple)


def sorted_get(pricebook, name):
    """Search pricebook by name and return its price. If name not found,
    return None
     O(N)"""
    high = len(pricebook) - 1
    low = 0
    if len(pricebook) >= 1:
        while high >= low:
            mid = (low + high) // 2
            if pricebook[mid][1] == name:
                return pricebook[mid][0]
            elif pricebook[mid][1] < name:
                low = mid + 1
            elif pricebook[mid][1] > name:
                high = mid - 1
    else:
        return None


def sorted_put(pricebook, name, price):
    """takes a sorted pricebook (list of tuples). each tuple is 2 elements:
    a price and name. Update pricebook to reflect the new price
    and keep in sorted order"""
    j = len(pricebook) - 1
    if len(pricebook) >= 1:
        for i in range(len(pricebook)):
            if name == pricebook[i][1]:
                pricebook.pop(i)
                pricebook.insert(i, (price, name))
                break
            elif name < pricebook[i][1]:
                pricebook.insert(i, (price, name))
                break
            elif i == j:
                pricebook.append((price, name))
                break
    else:
        pricebook.append((price, name))