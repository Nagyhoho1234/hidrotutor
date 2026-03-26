"""Run GPT-5.4 Hungarian lector via OpenAI API on chapters, in chunks."""
import os, json, sys, time
sys.stdout.reconfigure(encoding='utf-8')
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("hu_lector_prompt.md", encoding="utf-8") as f:
    PROMPT = f.read()

CHUNK_SIZE = 200  # lines per chunk
START = int(sys.argv[1]) if len(sys.argv) > 1 else 1
END = int(sys.argv[2]) if len(sys.argv) > 2 else 25

for ch in range(START, END + 1):
    chf = f"ch{ch:02d}"
    chapter_path = f"chapters_hu/{chf}.md"
    fixes_path = f"lector_fixes/{chf}_fixes.json"

    if not os.path.exists(chapter_path):
        print(f"SKIP {chf}: file not found")
        continue

    with open(chapter_path, encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    all_fixes = []
    print(f"=== {chf} ({total_lines} lines) ===")

    for offset in range(0, total_lines, CHUNK_SIZE):
        chunk_lines = lines[offset:offset + CHUNK_SIZE]
        chunk_text = "".join(chunk_lines)
        end_line = min(offset + CHUNK_SIZE, total_lines)

        # Skip chunks that are mostly empty/formatting
        real_lines = [l for l in chunk_lines if l.strip() and not l.startswith('#') and not l.startswith('<!--') and not l.startswith('**Figure') and not l.startswith('**')]
        if len(real_lines) < 10:
            print(f"  chunk {offset+1}-{end_line}: skipped (mostly formatting)")
            continue

        print(f"  chunk {offset+1}-{end_line}: sending...", end="", flush=True)

        try:
            response = client.chat.completions.create(
                model="gpt-5.4",
                messages=[
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": f"Lektoráld a következő szövegrészletet ({chf}, {offset+1}-{end_line}. sor):\n\n{chunk_text}"},
                ],
                temperature=0.3,
                max_completion_tokens=8000,
            )
            result = response.choices[0].message.content

            try:
                data = json.loads(result)
                fixes = data.get("fixes", [])
                # Adjust line numbers to absolute
                for fix in fixes:
                    fix["line_approx"] = fix.get("line_approx", 0) + offset
                all_fixes.extend(fixes)
                print(f" {len(fixes)} fixes")
            except json.JSONDecodeError:
                print(f" JSON parse error, skipped")

        except Exception as e:
            print(f" ERROR: {e}")
            if "rate_limit" in str(e).lower() or "429" in str(e):
                print("  Rate limited, waiting 60s...")
                time.sleep(60)
            continue

        time.sleep(1)  # Small delay between chunks

    # Save all fixes
    combined = {"chapter": chf, "total_issues": len(all_fixes), "fixes": all_fixes}
    with open(fixes_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)

    # Apply fixes
    with open(chapter_path, "r", encoding="utf-8") as f:
        text = f.read()

    applied = 0
    for fix in all_fixes:
        orig = fix.get("original", "")
        sugg = fix.get("suggested", "")
        if orig and orig in text:
            text = text.replace(orig, sugg, 1)
            applied += 1

    with open(chapter_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"  TOTAL: {len(all_fixes)} fixes found, {applied} applied")
    print()

print("=== DONE ===")
