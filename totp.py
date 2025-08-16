import hmac, hashlib, time, struct, base64

def generate_totp(email):
    # Secret = email + fixed string
    secret = (email + "HENNGECHALLENGE004").encode()

    # Time counter
    timestep = 30
    T = int(time.time()) // timestep
    msg = struct.pack(">Q", T)

    # HMAC-SHA512
    hmac_hash = hmac.new(secret, msg, hashlib.sha512).digest()

    # Dynamic truncation
    offset = hmac_hash[-1] & 0x0F
    code = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF

    # 10 digits
    return str(code % (10**10)).zfill(10)

print(generate_totp("enioladejo1725@gmail.com"))
