from random import *
def empty(stack):
    return stack["cnt"]>0
def push(stack,inp):
    stack["data"].append(inp)
    stack["top"]+=1
    stack["cnt"]+=1
def pop(stack):
    if empty(stack):
        stack["data"].pop()
        stack["top"] -= 1
        stack["cnt"] -= 1
        return True
    else:
        return False
def top(stack):
    if empty(stack):
        return tuple((stack["data"][stack["top"]],True))
    else:
        return tuple((0, False))
if __name__ == '__main__':

    print("PyCharm")
    stack = {
        "data":[],
        "top":-1,
        "bot":0,
        "cnt":0
    }
    for i in range(30):
        push(stack,randint(1,50))
    print(stack)
    for i in range(15):
        pop(stack)
    print(stack)
    if top(stack)[1]:
        print(top(stack)[0])
    else:
        print("Top element not found")
    for i in range(20):
        if not pop(stack):
            print("No more elements")
    print(stack)