"""Extract audio from all lecture videos in parallel."""
import subprocess, os, re, glob
from concurrent.futures import ThreadPoolExecutor, as_completed

FFMPEG = r"C:\Users\de8xh\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
SRC = r"Y:\Fehér Zsolt\Tananyagok\_Maidment_ GIS in Water Resources\Youtube"
DST = r"C:\maidment_hidroGIS\audio"

os.makedirs(DST, exist_ok=True)

def clean_name(fn):
    name = os.path.splitext(fn)[0]
    # Remove leading number+dot
    name = re.sub(r'^\d+\.\s*', '', name)
    # Replace non-ascii and special chars with underscore
    name = re.sub(r'[^a-zA-Z0-9 _.-]', '_', name)
    # Collapse multiple underscores/spaces
    name = re.sub(r'[_ ]+', '_', name).strip('_')
    # Truncate to reasonable length
    if len(name) > 120:
        name = name[:120]
    return name

def extract(src_path, dst_path):
    cmd = [
        FFMPEG, '-i', src_path,
        '-vn',          # no video
        '-ac', '1',     # mono
        '-ar', '16000', # 16kHz (optimal for speech recognition)
        '-ab', '64k',   # 64kbps (plenty for speech)
        '-y',           # overwrite
        dst_path
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    return r.returncode == 0

videos = sorted(glob.glob(os.path.join(SRC, '*.mp4')))
print(f"Found {len(videos)} videos\n")

jobs = []
for v in videos:
    base = os.path.basename(v)
    out_name = clean_name(base) + '.mp3'
    out_path = os.path.join(DST, out_name)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        print(f"  SKIP (exists): {out_name}")
        continue
    jobs.append((v, out_path, out_name))

print(f"\n{len(jobs)} files to extract, running 16 parallel jobs...\n")

done = 0
failed = []
with ThreadPoolExecutor(max_workers=16) as ex:
    futures = {ex.submit(extract, src, dst): name for src, dst, name in jobs}
    for f in as_completed(futures):
        name = futures[f]
        try:
            ok = f.result()
            if ok:
                done += 1
                print(f"  OK [{done}/{len(jobs)}]: {name}")
            else:
                failed.append(name)
                print(f"  FAIL: {name}")
        except Exception as e:
            failed.append(name)
            print(f"  ERROR: {name} - {e}")

print(f"\n=== DONE: {done} extracted, {len(failed)} failed ===")
if failed:
    print("Failed files:", failed)

# Show total size
total = sum(os.path.getsize(os.path.join(DST, f)) for f in os.listdir(DST) if f.endswith('.mp3'))
print(f"Total audio size: {total/1024/1024:.1f} MB")
