import functools

def repeatTwice(func):
    @functools.wraps(func)
    def wrapper(*args):
        func(*args)
        return func(*args)
    return wrapper





# @repeatTwice
def sayHello(*name):
    print(f'Hi {name[0]}')
    return 'Printed Twice'

Hi = repeatTwice(sayHello)
print(Hi)

# sayHello('anish')