# SOLUTION ---------------------------------

def launcher(my_callable, *args, **kwargs):
    return my_callable(*args, **kwargs)

# END SOLUTION -----------------------------

def test_function1():
    return "Hello!"

def test_function2(number1, number2):
    return number1 * number2

def test_function3(text, uppercase=False, excited=False):
    result = text

    if uppercase:
        result = result.upper()
    if excited:
        result += "!!!!"

    return result

test_result = launcher(test_function3, "Python", excited=True)
print(test_result)