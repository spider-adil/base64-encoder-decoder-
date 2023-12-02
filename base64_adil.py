binaries=[]
six_bits=[]
string=[]
character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b64_encode(a):

    # making 8 bits binaries of every character of the input string
    for i in a:
        b = bin(ord(i))[2:].zfill(8)
        binaries.append(b)
    remainder = len(a) % 3 
    #print(len(binaries))
    binaries.append('00000000') if remainder == 2 else binaries.extend(['00000000', '00000000']) if remainder == 1 else binaries 
    #print(binaries)
    body = 'b'
    for i in binaries: body = body + i
    body = body[1:]
    #print(body)
    #print(body[:6])
    for i in range(0,len(body),6): six_bits.append(body[i:i+6])
    #print(six_bits)
    s = '@'
    for i in six_bits: s = s + character[int(i,2)]
    s = s[1:]
    [string.append(j) for j in s]
    #s = s[:len(s)-2] + '==' if remainder == 1 else s = s[:len(s)-1]+'=' if (remainder==2) else s
    if remainder == 1: s = s[:len(s)-2]+'=='
    elif remainder == 2: s = s[:len(s)-1]+'='
    else: s
    #[print(k,end='') for k in string]
    
    return s


def b64_decode(x):
    
    value = "@"
    for j,i in enumerate(x):
        if i == "=":
            value += "000000"
        else:
            a = bin(int(character.index(i)))[2:].zfill(6)
            #print(a)
            value += str(a)
    #print(len(value))
    #print(value)
    text = "*"
    for i in range(1,len(value),8):
        #binaries.append(value[i:i+8])
        #b = int(value[i:i+8],2)
        #binaries.append(b)
        text += chr(int(int(value[i:i+8],2)))   
    return text[1:]
    

y = int(input("Enter 1 to encode and 2 to decode : "))
x = input("Enter the expression: ")
print(b64_encode(x)) if y == 1 else print(b64_decode(x)) if y == 2 else print("Error")


