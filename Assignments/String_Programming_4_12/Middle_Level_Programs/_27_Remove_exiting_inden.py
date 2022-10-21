# remove existing indentation from all of the lines in a given text
import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
print(sample_text,'\n')
text_without_Indentation = textwrap.dedent(sample_text) # remove the indentation from all of the lines.
print(text_without_Indentation )
print()

'''
for wrap the text using the this command
wrapper = textwrap.Textwrapped(width=50)
res = wrapper.wrap(text=value) # value means which string u r passing that one assign the text



'''