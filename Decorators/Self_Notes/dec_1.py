# Sort a dictionary by key python
def upp_text(text):
    return text.upper()
def low_text(text):
    return text.lower()

def greet(func):
    greet = func("Hi this is decorator")
    print(greet)

greet(upp_text)
greet(low_text)