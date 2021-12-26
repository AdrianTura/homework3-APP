import urllib.request

'''Helper function to download a file from a specified url'''
def download_file(url, file_name):
    urllib.request.urlretrieve(url, file_name)

'''Helper function to decript a string that was encoded using caesar algorithm'''
'''
    Obs: 105 = 97 + 8
    97 = ASCII code for 'a'
    8 = caesar length
'''
def decript_using_caesar(encripted):
    decripted = ''

    for letter in encripted:
        if letter.isalpha():
            converted = chr((ord(letter) - 105) % 26 + 97)
        else:
            converted = letter
        
        decripted += converted

    return decripted + '\n' + '\n'