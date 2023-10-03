class TestClass:
    var = 2

    def __str__(self):
        return "Nice TestClass!"


print(TestClass.var)

t = TestClass()
print(t.var)

TestClass.var = 3

t2 = TestClass()
print(t2.var)

print(t)
print(t2)


# You can use functions as objects
variable = print
variable("Hello ?")
