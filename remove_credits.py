import os

# أي سطر فيه واحد من النصوص دي هيتمسح
PATTERNS = ["Special Thanks to:", "Designed by:"]

changed = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d != ".git"]
    for name in files:
        if not name.lower().endswith(".html"):
            continue
        path = os.path.join(root, name)
        with open(path, "r", encoding="utf-8", errors="surrogateescape", newline="") as f:
            lines = f.readlines()
        kept = [l for l in lines if not any(p in l for p in PATTERNS)]
        if len(kept) != len(lines):
            with open(path, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                f.writelines(kept)
            print(f"تم التعديل: {path} (اتمسح {len(lines) - len(kept)} سطر)")
            changed += 1

print(f"\nخلص. عدد الملفات اللي اتعدلت: {changed}")
