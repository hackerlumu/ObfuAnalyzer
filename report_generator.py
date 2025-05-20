from datetime import datetime

def generate_report(strings, deobf, entropy_hits, filename):
    report = f"# ObfuAnalyzer Report\n\n**File:** `{filename}`\n**Time:** {datetime.now()}\n\n"
    report += "## 🔍 Extracted Strings\n"
    report += "\n".join([f"- {s}" for s in strings[:50]]) + "\n\n"

    report += "## 🧪 Deobfuscated Content\n"
    for mtype, original, result in deobf:
        report += f"- **{mtype}**: `{original}` → `{result}`\n"

    report += "\n## ⚠️ High Entropy Sections\n"
    for offset, ent in entropy_hits:
        report += f"- Offset `{offset}` → Entropy: `{ent:.2f}`\n"

    output_path = "outputs/reports/report.md"
    with open(output_path, "w") as f:
        f.write(report)
    print(f"[+] Report generated: {output_path}")