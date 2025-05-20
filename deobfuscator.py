import base64
import codecs

def deobfuscate_data(strings):
    results = []
    for s in strings:
        try:
            decoded = base64.b64decode(s).decode()
            results.append(("Base64", s, decoded))
        except:
            pass
        try:
            decoded = codecs.decode(s, 'rot_13')
            results.append(("ROT13", s, decoded))
        except:
            pass
        try:
            xor_key = 0x55
            decoded = ''.join([chr(ord(c) ^ xor_key) for c in s])
            if all(32 <= ord(c) <= 126 for c in decoded):
                results.append(("XOR", s, decoded))
        except:
            pass
    return results