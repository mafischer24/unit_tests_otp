# GOAL: Create a series of tests for each function in cipher.py.

from cipher import *


# test generatePad()
# ^ [https://stackoverflow.com/questions/62690654/oserror-pytest-reading-from-stdin-while-output-is-captured-consider-using-s].
# IMPORTANT: If using pad/message files, comment test_generatePad(). 
# def test_generatePad():
#     assert generatePad(padLength, ascii_pad) == ascii_pad

# test calcShift()
def test_calcShift():
    assert calcShift(message, ascii_message) == ascii_message

# test encipher()
# ^ [https://stackoverflow.com/questions/70414734/pytest-triggers-assertionerror].
def test_encipher():
    assert type(encipher(ascii_message, ascii_pad, new_message)) == str

# test decipher()
# decipher() takes two different inputs: 'message' and 'filename.' Need to test for both. 
# IMPORTANT: If using message and pad files, comment test_decipher_message(). 
def test_decipher_message():
    assert type(decipher(message, ascii_pad, old_message)) == str

# IMPORTANT: If generating random pad with user input, comment test_decipher_filename(). 
# def test_decipher_filename():
#     assert type(decipher(filename, ascii_pad, old_message)) == str