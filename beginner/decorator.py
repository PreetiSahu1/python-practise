#----1----# 


import time
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("start time : ",time.ctime())
        result = func(*args,**kwargs)
        for i in result:
            print(i)

        print("complete time : ", time.ctime())

    return wrapper


@my_decorator
def task():
    add= 5+6
    sub= 17-10
    tab = 5
    print("execution")
    return add,sub,tab


result=task()