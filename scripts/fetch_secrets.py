import requests
import os

URL = "https://raw.githubusercontent.com/Mddoha/Jan-AI-Secrets/main/raw/.secrets"
OUTDIR = "secrets"

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    resp = requests.get(URL)
    lines = resp.text.strip().split("\n")
    for line in lines:
        key, val = line.split("=", 1)
        with open(f"{OUTDIR}/{key.strip()}.txt", "w") as f:
            f.write(val.strip())

if __name__ == "__main__":
    main()
