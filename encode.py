import base64
import json
def encode(t):
    key = "key"
    out=""
    for i in range(len(t)):
        out += chr(ord(t[i]) ^ ord(key[i % 3]))
    s = base64.b64encode(out.encode('utf-8'))
    return s
f=open("E:\\Project\\lib\\saves\\IRONCLAD.json",encoding="utf-8")
out=open("E:\\Project\\lib\\saves\\IRONCLAD.autosave",'w',encoding='UTF-8')
s=f.read()
o=encode(s).decode("ascii")
print(o)
out.write(str(o))
f.close()
out.close()
