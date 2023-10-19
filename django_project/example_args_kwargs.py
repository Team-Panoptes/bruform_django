def func(first, *args):
    print(args)

func("hello", "world", "extra")


def func2(a, b, c):
    print(a)
    print(b)
    print(c)

mylist = [1, 2]
func2(42, *mylist)


def somme(*args):
    total = 0
    for number in args:
        total += number
    
    print(total)

print("----Somme----")
somme(1, 2, 3, 4, 5)


def func3(a, b=2, c=0):
    print(a * b + c)

func3(5)
func3(5, 4)
func3(5, c=10)

print("----Kwargs----")

def func4(**kwargs):
    print(kwargs)

func4(first=1, another=2, last=3)

def func5(user="Anonymous", page="index.html", id=3):
    print(f"User {user} requesting page {page} for object {id}.")

mydict = {
    "id":42,
    "user": "Bastien",
}

func5(**mydict)