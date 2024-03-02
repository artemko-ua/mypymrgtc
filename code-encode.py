import os
import pyAesCrypt 

def crypter(_mode, _file):
    password = input("Enter password for codeing and encoding files: ")
    buffer = 512 * 1024
    ext = _file.split('.')

    if(int(_mode) == 0) :
        pyAesCrypt.encryptFile(_file,  ext[0].lower() + '.art', password, buffer  )

    elif(int(_mode) == 1):
        _type = input("Enter type: ")
        pyAesCrypt.decryptFile(_file, ext[0].lower() + '.' + _type , password , buffer)

    os.remove(_file)

print("To code file: 0; to encode file 1:")
mode = input("Enter mode: ")


file = input("Please enter file name: ")

crypter(mode, file)