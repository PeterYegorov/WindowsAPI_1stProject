import ctypes
from ctypes import wintypes

user_handle = ctypes.WinDLL("user32.dll")           # handle to user32.dll
kernel_handle = ctypes.WinDLL("kernel32.dll")       # handle to kernel32.dll

ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF)     # Setting up access rights

dwDesiredAccess = ALL_ACCESS
bInheritHandle = False
dwProcessId = ctypes.wintypes.DWORD(int(input("Input a PID: ")))                        # Asking for a PID to get a handle to
    
acq_handle = kernel_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)    # Acquiring a handle

# Error check
error = ctypes.get_last_error()
if error != 0:
    print("Failed to create a handle")
    print(f"Error code {error}")
    exit(1)

if acq_handle < 0:
    print("Failed to create a handle")
else:                                       # Message box setup
    hWind = None
    lpText = f"Raw value: {acq_handle}"
    lpCaption = "Handle created"
    uType = 0x00000000 | 0x00000040
    response = user_handle.MessageBoxW(hWind, lpText, lpCaption, uType)     # Show a message box and get a response code

# Error check
error = kernel_handle.GetLastError()
if error != 0:
    print(f"Error code: {error}")
    exit(1)
exit(0)
