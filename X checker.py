import os, sys, ctypes, time, random, string, warnings

required_libs = ["requests", "httpx", "colorama", "faker", "pycountry", "nltk"]
missing = []
for lib in required_libs:
    try:
        __import__(lib)
    except ImportError:
        missing.append(lib)
if missing:
    if os.path.exists("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        for lib in missing:
            os.system(f"pip install {lib}")

import requests, httpx
from colorama import Fore, init
init(autoreset=True)
Title = ctypes.windll.kernel32.SetConsoleTitleW
try:
    from faker import Faker
    _faker = Faker()
except:
    Faker = None
    _faker = None
try:
    import pycountry
except:
    pycountry = None
import nltk
from nltk.corpus import words

class TokenChecker:
    def selfcheck():
        return bool(open("token.txt").read().strip()) if __import__("os").path.exists("token.txt") else False
def word():
    result = requests.get('https://shdw.pythonanywhere.com/').text.strip()
    if not result:
        return "default"
    return result
def x_cookies():
    headers = {'accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://x.com','referer': 'https://x.com/i/flow/signup','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en'}
    req = requests.get("https://x.com", headers=headers)
    cookies = {}
    for cookie in req.cookies:
        cookies[cookie.name] = cookie.value
    return cookies
def get_random_token():
    try:
        with open('token.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
            
        if not tokens:
            return "Error: token.txt is empty"
            
        return random.choice(tokens)
    except FileNotFoundError:
        return "Error: token.txt not found"
    except Exception as e:
        return e
class Xchecker:
    def __init__(self):
        os.system('cls')
        TOKENCHECK = TokenChecker.selfcheck()
        if TOKENCHECK == False:
            print(f"{Fore.RED} token.txt is empty")
            input()
            exit()
        self.checked = 0
        self.user = ""
        self.available = 0
        self.unavailable = 0
        self.rl = 0
        self.run = True
        self.target_available = 1005
        print(f"{Fore.CYAN}===== Xchecker Username Checker =====")  
        print(f"{Fore.MAGENTA} Telegram @ytsof IG @shdw")
        self.mode = input(f"Choose mode:\n1. Check from file\n2. Check random usernames\n3. Check specific username\n4. Check with semi-username patterns\n5.meanings\n6. Check with common words\n7. Check with names (person/country/lands)\nEnter choice (1-7): ").strip()
        
        if self.mode == "1":
            self.file_path = input("Enter file path containing usernames: ").strip()
            self.usernames = self.load_usernames()
        elif self.mode == "2":
            self.length = int(input("Enter username length: ").strip())
        elif self.mode == "3":
            self.username = input("Enter username to check: ").strip()
        elif self.mode == "4":
            pass
        elif self.mode == "5":
            pass
        elif self.mode == "6":
            pass
        elif self.mode == "7":
            pass
        else:
            print(f"{Fore.RED}Invalid choice. Exiting.")
            exit()
        
        self.client = httpx.Client(http2=True, timeout=10.0)
        self.start()
    
    def load_usernames(self):
        try:
            with open(self.file_path, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}File not found. Exiting.")
            exit()
    
    def generate_random_username(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(self.length))
    
    def generate_semi_usernames(self):
        chars = string.ascii_lowercase + string.digits
        patterns = [
            lambda: f"{random.choice(chars)}_{random.choice(chars)}{random.choice(chars)}",
            lambda: f"{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}",
            lambda: f"{random.choice(chars)}_{random.choice(chars)}",
            lambda: f"{random.choice(chars)}-{random.choice(chars)}"
        ]
        return random.choice(patterns)()
    def generate_word_username(self):
        warnings.filterwarnings('ignore')
        try:
            nltk.data.find('corpora/words')
        except LookupError:
            nltk.download('words', quiet=True)

        word_list = [w.lower() for w in words.words() if len(w) == 6 and w.isalpha()] or [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()]
        return random.choice(word_list) if word_list else None

    def generate_name_username(self):
        generators = []
        if _faker:
            generators.append(lambda: _faker.first_name().lower())
            generators.append(lambda: _faker.last_name().lower())
            generators.append(lambda: _faker.country().lower())
            try:
                lands = [c for c in _faker.countries() if "land" in c.lower()]
                if lands:
                    generators.append(lambda: random.choice(lands).lower())
            except Exception:
                pass
        if pycountry:
            try:
                countries = [c.name.lower() for c in pycountry.countries]
            except Exception:
                countries = []

        if countries:
            generators.append(lambda: random.choice(countries))
            lands = [c for c in countries if "land" in c]
            if lands:
                generators.append(lambda: random.choice(lands))
        return random.choice(generators)()
    def check(self, username):
        token = get_random_token()
        resp_msg = requests.post('https://x.com/i/api/graphql/1bMz-9lPrmIXrhFmXntTHw/GetUsernameAvailabilityAndSuggestions',cookies =x_cookies(),headers ={'accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://x.com','referer': 'https://x.com/i/flow/signup','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36','x-twitter-auth-type': 'OAuth2Session','authorization': f'Bearer {token}','x-twitter-client-language': 'en'},json={'variables': {'include_suggestions': False,'session_token': '','username': f'{username}',},'queryId': '1bMz-9lPrmIXrhFmXntTHw',},).text
        return resp_msg


    def check_username(self, username, retries=1):
        for attempt in range(retries):
            try:
                self.user = username
                response_text = self.check(self.user)
                if '"available":true' in response_text:
                    self.available += 1
                    name = self.user
                    print(f"{Fore.GREEN} Good username @{name}")
                    with open("available_IG.txt", "a", encoding="utf-8") as file:
                        file.write(f"{name}\n")
                elif '"available":false' in response_text:
                    self.unavailable += 1
                    name = self.user
                    print(f"{Fore.RED} Bad username @{name}")
                    with open("notavailable_Xchecker.txt", "a", encoding="utf-8") as file:
                        file.write(f"{name}\n")
                else:
                    self.rl += 1
            except Exception as e:
                if attempt == retries - 1:
                    print(f"{Fore.YELLOW}[ERROR] {username}: {str(e)}")
                    try:
                        with open("error_X.txt", "a", encoding="utf-8") as errf:
                            errf.write(f"{username}: {str(e)}\n")
                    except:
                        pass

    def print_status(self):
        Title(f"Available: {self.available} | Unavailable: {self.unavailable} | unknown: {self.rl} | username :{self.user}")
    
    def start(self):
        print(f"{Fore.CYAN}Starting username checker...")
        
        try:
            if self.mode == "1":
                for username in self.usernames:
                    if not self.run or self.available >= self.target_available:
                        break
                    self.check_username(username)
                    self.print_status()
                    time.sleep(random.uniform(0.2, 0.6))
                print(f"\n{Fore.YELLOW}All usernames checked from file.")
                
            elif self.mode == "2":
                checked = 0
                while True:
                    username = self.generate_random_username()
                    self.check_username(username)
                    checked += 1
                    self.print_status()           
            elif self.mode == "3":
                self.check_username(self.username)
                self.print_status()
                print("\nUsername check completed.")
            elif self.mode == "4":
                checked = 0
                while True:
                    username = self.generate_semi_usernames()
                    self.check_username(username)
                    checked += 1
                    self.print_status()
            elif self.mode == "5":
                checked = 0
                while True:
                    username = word()
                    self.check_username(username)
                    checked += 1
                    self.print_status()
            elif self.mode == "6":
                checked = 0
                while True:
                    username = self.generate_word_username()
                    self.check_username(username)
                    checked += 1
                    self.print_status()
            elif self.mode == "7":
                checked = 0
                while True:
                    username = self.generate_name_username()
                    username = ''.join(ch for ch in username if ch.isalnum() or ch in "_-").lower()
                    self.check_username(username)
                    checked += 1
                    self.print_status()

        except KeyboardInterrupt:
            self.run = False
            print(f"\n{Fore.YELLOW}Interrupted by user. Stopping...")
        
        print(f"\n{Fore.CYAN}Final Results:")
        print(f"{Fore.GREEN}Available: {self.available} | {Fore.RED}Unavailable: {self.unavailable} | {Fore.YELLOW}unknown: {self.rl}")
        
        if self.available > 0:
            print(f"{Fore.GREEN}Available usernames saved in available_Xchecker.txt")
        try:
            self.client.close()
        except Exception:
            pass

if __name__ == "__main__":
    Xchecker()

