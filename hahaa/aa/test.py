import hashlib
m = hashlib.md5()
m.update('password')
print m.hexdigest()