def entry_exit(f):
    def new_f():
        t = input('something: ')
        print(t)
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f

@entry_exit
def func1():
    print("inside func1()")

#func1()

import toolkit
import validators


def ping_handler(f):
    #def wrapper():
    hostname = input('Hostname > ')
    echos = input('Enter number of echo requests [25] > ')
    if echos == '':
        echos = '25'
    return f(hostname, echos)
    #return wrapper


@ping_handler
def get_ping(node, count='25'):
    try:
        print(toolkit.check_ping(node, count=count))
    except AttributeError:
        print('Unable to ping {}; check its syntax'.format(node))


get_ping()