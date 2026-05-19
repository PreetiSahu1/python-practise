#----1----# 


import time
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("start time : ",time.ctime())
        result = func(*args,**kwargs)
        print(result)

        print("complete time : ", time.ctime())

    return wrapper


@my_decorator
def task():
    add= 5+6
    print("execution")
    return add



result=task()