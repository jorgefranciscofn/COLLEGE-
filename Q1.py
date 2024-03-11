import sys
import hashlib
if len(sys.argv) < 2:
    print(f"uso: {sys.argv[0]}nomearq")
    print('esse prog clacula o hash ')
    sys.exit


fd=open(sys.argv[1],"rb")
h=hashlib.sha256()
h.update(fd.read())
fd.close()
print(h.hexdigest())





