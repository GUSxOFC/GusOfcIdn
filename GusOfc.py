import requests
import os
import time

API_KEY = "nfp_7dXycerH4AH8ktfuU7QpJAgiDvThUcKb10ad"

def anim(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

def garis():
    print("=" * 50)

def upload_html(nama, html_str):
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "name": nama,
        "description": f"Website HTML dari GUSxOFC",
        "content": html_str
    }
    try:
        res = requests.post("https://api.npoint.io/v1/pages", headers=headers, json=data)
        if res.status_code == 200:
            return res.json().get("url")
        else:
            return f"ERROR: Kode {res.status_code}"
    except Exception as e:
        return f"ERROR: {e}"

os.system("clear")
garis()
anim(">> GUSxOFC WEB MAKER - versi 1.0 <<")
garis()
print("Status: ngga tau, work apa kgk")
garis()

# Input nama & file HTML
nama_web = input("Masukkan nama web (tanpa spasi): ").strip().replace(" ", "_")
path_file = input("Masukkan path file HTML kamu: ").strip()

if not os.path.exists(path_file):
    print(f"[!] File tidak ditemukan: {path_file}")
    exit()

# Baca isi file HTML
with open(path_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Upload
anim("\n[+] Mengupload ke server npoint...")
link = upload_html(nama_web, html_content)

print("\nHasil:")
print(f"Nama Web : {nama_web}")
print(f"Link     : {link}")
