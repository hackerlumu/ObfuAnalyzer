# ObfuAnalyzer

ObfuAnalyzer is a malware analysis tool for deobfuscating encoded strings and identifying suspicious patterns in obfuscated PE files (DLL/EXE). It helps malware analysts detect base64, ROT13, XOR patterns, and high-entropy blobs in binary data.

## Features
- Extracts and deobfuscates obfuscated strings
- Detects entropy spikes (packed or encrypted blobs)
- Generates Markdown reports for offline analysis

## Usage
1. Place your sample in `samples/` directory (e.g., sample_obfuscated.dll)
2. Run:

```bash
python main.py
```

3. Report will be generated in `outputs/reports/`

## Requirements
No external dependencies. Pure Python 3.x code.