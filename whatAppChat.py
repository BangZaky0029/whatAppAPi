import requests

API_KEY = "USiuXE5U1NjGKCTs5SLv"  # Ganti dengan API Key dari Fonnte
phone_numbers = ["6281809742506"]  # List nomor tujuan

message = """Yth. Kepada Calon Karyawan

Terima kasih telah melamar untuk posisi Staff Marketing di Manukashop melalui Loker.id. Kami telah menerima lamaran Anda dan saat ini sedang melakukan proses seleksi awal.

Sebagai langkah pertama, kami mohon kesediaan Anda untuk mengisi formulir rekrutmen melalui tautan berikut:

📌 https://forms.gle/jHZB4CJd7cY5fumR9

Formulir ini bertujuan untuk melengkapi data serta membantu kami memahami profil Anda dengan lebih baik. Harap mengisi formulir ini selambat-lambatnya HARI INI (Jam : 23.59).

Setelah Anda mengisi formulir, kami akan mengirimkan tautan untuk jadwal interview online. Pastikan nomor WhatsApp dan email yang Anda cantumkan aktif agar kami dapat menghubungi Anda dengan mudah.

Jika ada pertanyaan, jangan ragu untuk menghubungi kami. Kami menantikan respon Anda dan semoga kita dapat segera bertemu dalam tahap interview!

Salam,
Manukashop"""

def send_message(phone, message):
    url = "https://api.fonnte.com/send"
    headers = {
        "Authorization": API_KEY
    }
    data = {
        "target": phone,
        "message": message
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

for number in phone_numbers:
    response = send_message(number, message)
    print(f"Nomor: {number}, Response: {response}")
