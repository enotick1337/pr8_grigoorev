import random
import string
def func(parol):
    st1 = string.ascii_lowercase
    st2 = string.ascii_uppercase
    st3 = string.digits
    for i in range(11):
            parol += parol.join(random.choices(st1+st2+st3))
    return parol
parol = ''
print(func(parol))
