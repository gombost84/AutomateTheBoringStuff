def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

def spam2():
    print(eggs)

def spam3():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42

spam()
spam2()
spam3()
