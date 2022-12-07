import random
import string
def func(parol):
    st1 = string.ascii_lowercase
    st2 = string.ascii_uppercase
    for i in range(11):
            parol += parol.join(random.choices(st1+st2))
    return parol
parol = ''
print(func(parol))
