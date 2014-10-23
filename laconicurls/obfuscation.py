#The base27 idea comes from this guy who was using base31 to cut out vowels.
#I've also removed the 4 numbers that look like vowels to prevent any unintentional calculator gags
#http://jeffreypratt.net/safely-base-36-encoding-integers.html
BASE27_ALPHABET = '256789BCDFGHJKLMNPQRSTVWXYZ'

def base27_encode(n):
    """Encode a number in the unoffensive base 27 format
    >>> base27_encode(0)
    '2'
    >>> base27_encode(26)
    'Z'
    >>> base27_encode(27)
    '52'
    """
    if n == 0:
        return BASE27_ALPHABET[0]

    result = ""

    while (n > 0):
        result = BASE27_ALPHABET[n % len(BASE27_ALPHABET)] + result
        n = int(n / len(BASE27_ALPHABET))

    return result

def base27_decode(encoded):
    """Decode a number from the unoffensive base27 format
    >>> base27_decode('2')
    0
    >>> base27_decode('Z')
    26
    >>> base27_decode('52')
    27
    >>> base27_decode('ZZZZ')
    531440
    """
    result = 0

    for i in range(len(encoded)):
        place_value = BASE27_ALPHABET.index(encoded[i])
        result += place_value * (len(BASE27_ALPHABET) ** (len(encoded) - i - 1))

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
