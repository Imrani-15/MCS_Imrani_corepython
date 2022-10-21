# display formatted text (width=50) as output
'''
The textwrap module can be used for wrapping and formatting of plain text.
This module provides formatting of text by adjusting the line breaks in
the input paragraph.
'''

import textwrap
value = """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""
print(value,"\n")
wrapper = textwrap.TextWrapper(width=70)
word_list = wrapper.wrap(text=value)
for ele in word_list:
    print(ele)