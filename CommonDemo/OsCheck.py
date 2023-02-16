import os
import sys

# Get current working folder

retval = os.getcwd()
print(f'Current working floder: {retval}')

# Modify current working folder

# os.chdir('abc')
# FileNotFoundError: [Errno 2] No such file or directory: '/home/123'
os.chdir('/home/edwin/Desktop/')


# Get working folder after modify
retval = os.getcwd()
print(f'Working floder after modify: {retval}')