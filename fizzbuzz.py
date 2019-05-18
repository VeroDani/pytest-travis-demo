#na zaklade vstupu vrat retezec

def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError("n is not an int")
    if n <= 0:
        raise ValueError("n is not positive")
    if n % 15 == 0: #kdyz delitelne 15 = 3*5 delitelne 3 a 5 zaroven
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return str(n)
