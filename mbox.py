import ctypes

user_handle = ctypes.WinDLL("user32.dll")       # handle to user32.dll
kernel_handle = ctypes.WinDLL("kernel32.dll")   # handle to kernel32.dll

'''
set up for a message box
'''
hWind = None
lpText = "Hello, I will install a virus"
lpCaption = "Warning"
uType = 0x00000001 | 0x00000030

response = user_handle.MessageBoxW(hWind, lpText, lpCaption, uType)     # Show a message box and get a response code

'''
Error check
'''
error = kernel_handle.GetLastError()
if error != 0:
    print(f"Error code: {error}")
    exit(1)

'''
Print the result, depending on a button clicked
'''
if response == 1:
    print("You shouldn't have done it!")
elif response == 2:
    print("Good. Don't trust suspicious message boxes.")
