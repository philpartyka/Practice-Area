def outer(msg):
    lang = 'Python'
    def inner():
        print(lang, msg)
    return inner

myfunc = outer('is fun!')
myfunc()

def outer(msg):
    lang = 'Python'
    print(lang, msg)
    #return inner

myfunc = outer('is fun!')
myfunc



import re

print(re.findall(r"ana", "banana"))
