#Write a function that repeats the process of
#giving a coconut away and then taking one
#fifth of the remaining coconuts away.


def f(n):
    return (n - 1) / 5 * 4


def f6(n):

    # Enter code here
    for i in range(6):
        n = f(n)
    return n


print f6(96.)
