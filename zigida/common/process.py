
def exec_binary_search(countries, country):

    left, right = 0, len(countries) - 1

    while left <= right:

        middle = left + (right - left) // 2

        # Check if country is present at mid
        if countries[middle] == country:
            return middle

        # If country is greater, ignore left half
        elif countries[middle] < country:
            left = middle + 1

        # If country is smaller, ignore right half
        else:
            right = middle - 1

    return False
