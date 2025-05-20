import re
from math import log2

def extract_strings(data, min_length=4):
    pattern = rb'[\x20-\x7E]{%d,}' % min_length
    return [s.decode() for s in re.findall(pattern, data)]

def extract_entropy_sections(data, chunk_size=256):
    def shannon_entropy(chunk):
        freq = [0] * 256
        for b in chunk:
            freq[b] += 1
        entropy = -sum((f / len(chunk)) * log2(f / len(chunk)) for f in freq if f)
        return entropy

    results = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        ent = shannon_entropy(chunk)
        if ent > 7.5:
            results.append((i, ent))
    return results