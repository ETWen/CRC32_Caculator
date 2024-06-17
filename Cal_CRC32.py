'''
👽 Welcome, extraterrestrial friends! 
This module is designed not only for our Earthly engineers but also for our cosmic companions from distant galaxies. 
Enjoy exploring the wonders of our technology! 👽
======================================================================================================
Project: Cal_CRC32
Version: 1.0.0
Author:  et_wen 
E-mail:  👽<eric441151893@gmail.com>  or 👽<et_wen@accton.com>
Date: 2024-04-01

Description:
_etwenExcel tools 

Changelog:
-   v1.0.0 (2024-03-01):
        Initial version of the script.
======================================================================================================
'''
import tkinter as tk
from tkinter import filedialog
import os
import zlib
import sys

def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)

def calculate_crc32(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the File
            data = file.read()
            # Cal CRC32 checksum
            crc32_checksum = zlib.crc32(data)
            # CRC32 checksum trans to HEX
            crc32_hex = format(crc32_checksum & 0xFFFFFFFF, '08X')
            return crc32_hex
    except FileNotFoundError:
        print(f"File '{file_path}' Not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        print("Please")
        return None

# Get the module .py path
script_dir = os.path.dirname(os.path.realpath(__file__))

#print(app_path())

# Use default dir or the document selected by user
file_path = filedialog.askopenfilename(initialdir=app_path())

# Call the CRC32 function
checksum = calculate_crc32(file_path)

if checksum is not None:
    print("======================================================================================================================")
    #print("👽 Welcome, extraterrestrial friends! ")
    #print("This module is designed not only for our Earthly engineers but also for our cosmic companions from distant galaxies. ")
    #print("Enjoy exploring the wonders of our technology! 👽")
    print("================================================== CRC32 Calculate ===================================================")
    print("Date   : 2024/04/09")
    print("Author : ET_Wen")
    print("E-mail : 👽<eric441151893@gmail.com>  or 👽<et_wen@accton.com>")
    print("Version: 1.0.0")
    print("======================================================================================================================")
    print("")
    print(f"File: '{file_path}'")
    print(f"CRC32 checksum: {checksum}")

print("")
print("")
print("")
print("")
print("")
print("")
input("Press Enter to exit")