decryption_library = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',
                      ')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R',
                      '}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a',
                      '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j',
                      'b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s',
                      'k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}

orig_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = orig_file.read()
orig_file.close()
encrypt_file = open('DECRYPTED_Plain_Text_File.txt','w')

for ch in file_read:
    if ch in decryption_library:
        encrypt_file.write(decryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()    
codes_items = decryption_library.items()

for ch in file_read:
    if not ch in decryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')
