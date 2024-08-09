def reverse(string):
    """Reverse string

    >>> reverse('')
    ''

    >>> reverse('Korvo')
    'ovroK'
    """

    return string[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()