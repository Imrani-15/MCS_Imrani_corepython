try:
    #import textwrap
    sample_text = '''
                    Python is a widely used high-level, general-purpose, interpreted,
                    dynamic programming language. Its design philosophy emphasizes
                    code readability, and its syntax allows programmers to express
                    concepts in fewer lines of code than possible in languages such
                    as C++ or Java.
        '''
    text_without_Indentation = textwrap.dedent(sample_text)
    print()
    print(text_without_Indentation)
    print()
except NameError as ne:
     print("An exception Occure",ne)
finally:
    print("This is excuted")



