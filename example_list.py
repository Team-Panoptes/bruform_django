words = ["Django", "is", "going", "to", "be", "fun"]
print(words[:3])
print(words[3:])

text = "My title"
print(text[3:])

words.append("soon")
words += ["!", "!", "!"]
print(words)

words.insert(2, "really")
print(words)

words.remove("!")
print(words)

removed = words.pop(0)
print(words)
print(removed)


words[0] = "New!"
print(words)

words_tuple = ("Can't", "touch", "this")
words_tuple = ("another", "tuple")
