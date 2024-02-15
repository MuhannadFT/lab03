def repeat(function):
    def wrapper():
        for _ in range(x):
            function()
    return wrapper

x = int(input("Enter a number of repetitions: "))

@repeat
def hello():
    print ('Hello')

hello()