strange = print

strange("Hello, world!")

def gimme_a_function():

    def internal(value):
        print(f"Value is {value}")
    
    return internal


oulah = gimme_a_function()
oulah(42)
