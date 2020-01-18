#!/usr/bin/env python3
'''Passing singel arg, array or list and dictionary'''


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def f(pos1, pos2, pos_or_kwd, kwd1, kwd2):
    print('pos1=', pos1)
    print('pos2=', pos2)
    print('pos3=', pos_or_kwd)
    print('pos4=', kwd1)
    print('pos5=', kwd2)


def concat(*args, sep="/"):
    return sep.join(args)


# lambda function
def x(a, b): return a * b


# call it
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

f(1, 2, 3, {'kwd1': 4}, {'kwd2': 5})

print(concat('earth', 'mars', 'venus'))
print(concat('today', 'tomorrow', 'the day after', sep='|'))

print(x(5, 6))
