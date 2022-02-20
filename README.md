# Exerimenting with Unit Tests. 

Welcome to my unit tests for the One Time Pad Cipher! 

---

To get started, the first thing to note is that the cipher.py program takes in _two_ different tyes of inputs: 

1. **User inputs** (if you want to generate your own messages and pads).
    * message = user's message
    * pad = user's desired pad length


2. **Files** (if you have a message and a pad in files).
    * filename = name of file with message
    * filenamePAD = name of file with pad


Depending on the type of input you want to use, you will need to comment out certain chunks of code in the `cipher.py` file. The same concept applies if you want to also test the functions in `cipher.py` via `cipher_test.py`. Be sure to check that you have made the necessary comments in **both** files!

Look for comments that start with 'IMPORTANT.' Those are the chunks of code that will need to be commented/uncommented. 

---

_Referenced the following site for how to create a Markdown file:_

^ [https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f#:~:text=Below%20are%20the%20steps%20to%20create%20a%20markdown,click%20the%20%E2%80%98open%20preview%20to%20the%20side%E2%80%99%20icon.].