from hashids import Hashids
hashids = Hashids()

hash_str = hashids.encrypt(123)
print('Encrypt(123) -> %s' % hash_str)

x = hashids.decrypt(hash_str)
print('decrypt(%s) -> %d' % (hash_str, x[0])) 
