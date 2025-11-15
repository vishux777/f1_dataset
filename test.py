import time, os, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY = os.urandom(32)
aesgcm = AESGCM(KEY)
data = b"x"*200   # ~200 bytes payload

N = 2000
t0 = time.perf_counter()
for i in range(N):
    nonce = (i).to_bytes(4,'big') + b'\x00'*8
    ct = aesgcm.encrypt(nonce, data, None)
t1 = time.perf_counter()
print("AES-GCM encrypt avg (ms):", (t1-t0)/N*1000)

t0 = time.perf_counter()
for i in range(N):
    h = hashlib.sha256(data).digest()
t1 = time.perf_counter()
print("SHA256 avg (ms):", (t1-t0)/N*1000)
