'''
    WRITING A FILE IN PYTHON
    => To write a file, you will still use the with open()
    => But instead of the open to have only the name of the file, we need to indicate which mode
       which is the writable.
    => When you write a file and the file contains, some text, it overides the file
    => In case you want to add some text after file has some text already in it, you use the 'a' mode
       which means append.

'''

text = "Hello dudes\nMy name is Maximus\nAnd this is a file\nI am writing to\n"

with open('Test1.txt', 'w') as file:
    file.write(text)

text1 = "I am a text that was appended at the end\nSorry if I am so cute\n"
with open('Test1.txt', 'a') as file:
    file.write(text1)


