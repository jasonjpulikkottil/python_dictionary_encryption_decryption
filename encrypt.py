encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

orig_file = open('Plain_Text_File.txt','r')
file_read = orig_file.read()    
orig_file.close()
encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','w')

for ch in file_read:
    if ch in encryption_library:
        encrypt_file.write(encryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('Plain_Text_File.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()
codes_items = encryption_library.items()

for ch in file_read:
    if not ch in encryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')


