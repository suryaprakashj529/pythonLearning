def caesar_cipher(string, offset):
    # Write your code here.
    new_str = ""
    new_ch =''
    for ch in string:
        new_ch = (chr( (ord(ch) - offset)))
        if new_ch < 'a':
            new_ch = chr((ord('z') - (ord('a') - ord(new_ch) ))+1)
            new_str += new_ch
        else:
            new_str += new_ch
                
    return str(new_str)

