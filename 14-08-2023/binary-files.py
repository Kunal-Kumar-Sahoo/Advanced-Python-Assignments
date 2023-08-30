# Problem statement
# You have been given a set of tasks related to text encoding, file I/O with encoding, and buffering. Your goal is to complete each task following the provided examples. Each task requires you to write Python code to accomplish specific tasks.

# Example 1: Encoding and Decoding
# --------------------------------
# Python uses Unicode for handling text, and the 'encode()' and 'decode()' methods are used to convert text to bytes and vice versa.

text = "Hello, 你好, مرحبًا"
encoded_text = text.encode('utf-8')  
#Unicode is a list of characters with unique decimal numbers (code points).  A = 65, B = 66, C = 67, ..
# UTF-8 is a variable-length character encoding standard used for electronic communication.
print(f"Encoded Text: {encoded_text}") 

decoded_text = encoded_text.decode('utf-8')  # Decode bytes back to UTF-8 text
print(f"Decoded Text: {decoded_text}")

print ("Task1 is done")

# Example 2: File I/O with Encoding
# --------------------------------
# When reading from or writing to files, encoding should be specified to handle text in the desired character set.

# Writing to a file with specified encoding
with open("encoded_file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 你好, مرحبًا")
# Encoding ensures that the file can handle and correctly represent characters from different languages,
# like the English, Chinese, and Arabic characters in the provided string.
# Reading from the file with specified encoding
with open("encoded_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"File Content: {content}")
print("Task2: Reading from a file is done")

# Example 3: Writing Binary Files
# -------------------
# Python will encode the text based on the default text encoding. 
# Additionally, Python will convert line endings (\n) to whatever the platform-specific line ending is, 
# which would corrupt a binary file like an exe or png file.
# 'wb' mode is specifically designed for writing binary data, such as images, audio files, video files,
# and other non-textual data. When you open a file in binary write mode ('wb'), the data is written 
# as-is without any character encoding or interpretation.
binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # Binary representation of "Hello World"
with open('binary_file.bin', 'wb') as file:
    file.write(binary_data)
with open('binary_file.bin', 'rb') as file:
    content = file.read()
    print(f"File Content: {content}")
print("Task3: writing binary file is done")

# Example 4: Buffering
# -------------------
buffer_size = 10  # Set the buffer size 10 characters at a time
with open('buffered_example.txt', 'w', buffering=buffer_size) as file:
    for i in range(1, 6):
        file.write(f"This is line {i}\n")
print("Task4: Buffering is done")
# Buffering allows you to accumulate data in memory and then write it in larger chunks, reducing 
# the number of system calls required to write the data.

# Here's what happens in the loop:
# The loop iterates from 1 to 5.
# In each iteration, it writes a line of text to the file, and the data is buffered in memory.
# Once the buffer is filled with 10 characters (or a newline character \n is encountered), 
# the buffered data is flushed (written) to the file.

# The primary use of buffering is to improve the efficiency of data transfer, processing and improving latency.
# buffering can have performance implications and can affect the behavior of your code, 
# so it's important to choose an appropriate buffering strategy based on your specific requirements. 
# In real-world scenarios, you might choose a buffer size that balances performance and memory 
# consumption based on the nature of your application.
