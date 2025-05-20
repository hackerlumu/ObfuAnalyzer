from deobfuscator import deobfuscate_data
from extractor import extract_strings, extract_entropy_sections
from report_generator import generate_report

def main():
    filepath = "samples/sample_obfuscated.dll"

    with open(filepath, 'rb') as f:
        data = f.read()

    entropy_hits = extract_entropy_sections(data)
    strings = extract_strings(data)
    deobfuscated = deobfuscate_data(strings)

    generate_report(strings, deobfuscated, entropy_hits, filepath)

if __name__ == "__main__":
    main()