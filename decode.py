import base64
import json
def decode(s):
    key = "key"
    t = base64.b64decode(s.encode('utf-8'))
    print(t)
    out=""
    for i in range(len(t)):
        out += chr(t[i] ^ ord(key[i % 3]))
    return out
f=open("E:\\Project\\lib\\saves\\IRONCLAD.autosave")
out=open("E:\\Project\\lib\\saves\\IRONCLAD.json",'w')
s=f.read()
o=decode(s)
print(o)
out.write(o)
#json.dump(o,out)
