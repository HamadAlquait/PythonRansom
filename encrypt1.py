#Gain access to operating system & using random IV later in code
import os, random

from Crypto.Cipher import AES

#Hashing algorithm
from Crypto.Hash import SHA256


def encrypt(key, filename):
    
    #Chunks that will be pulled out of the file
    chunksize = 64*1024
    
    #Name of the file once it has been encrypted
    outputFile = "(encrypted)"+filename
    
    #Filesize of the current file thats being encrypted; Fills file with 16 bytes and fills left hand side of string with zero's
    filesize = str(os.path.getsize(filename)).zfill(16)
    
    #Generate random IV
    IV = ''

    for i in range(16):
        #Random integer between 0-0xFF, IV generates 16 characters
        IV += chr(random.randint(0,0xFF))
    
    #Take the key thats passed in the function using Cipher Block Chaining (CBC); Insert IV for the AES
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    #Opening file we want to encrypt in read binary, calling that file an "infile:
    with open(filename, 'rb') as infile:
        
        #Take the output file in write binary
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                #Read the chunksize that was specified above
                chunk = infile.read(chunksize)

            #If chunk has nothing inside of it, break   
            if len(chunk) == 0:
                    break
                #Grab the remainder
                elif len(chunk) % 16 !=  0:
                    
                    #Padding the chunk with spaces, 16 minus the remainder of the length of the chunksize
                    chunk += ' ' *  (16 - (len(chunk) % 16))
                
                #Writes out the encrypted chunksize
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64*1024
    
    #Grabbing everything after the first 11 characters, since everything after the first 11 characters is the filename
    outputFile = filename[11:]

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                #Decrypt the chunk that is in the encrypted file
                outfile.write(decryptor.decrypt(chunk))
                
               #Reduces all of the padding added above, reducing to the original filesize before encryption
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    
    #Returns the hash of the password being created
    return hasher.digest()

def Main():
    choice = raw_input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    if choice == 'E':
        filename = raw_input("File to encrypt: ")
        password = raw_input("Password: ")
        encrypt(getKey(password), filename)
        print "Done."
    elif choice == 'D':
        filename = raw_input("File to decrypt: ")
        password = raw_input("Password: ")
        decrypt(getKey(password), filename)
        print "Done."
    else:
        print "No option selected. Closing..."

if __name__ == '__main__':
    Main()


