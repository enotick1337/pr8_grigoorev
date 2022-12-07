import random
import string
def func(parol):
    st1 = string.ascii_lowercase
    for i in range(11):
            parol += parol.join(random.choices(st1))
    return parol
parol = ''
print(func(parol))