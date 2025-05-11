import os
import json
import urllib.request
import requests
from datetime import datetime
import time
import webbrowser
import re
import platform
import sys

class UsernameSearch:
    """Main class for searching username information across platforms"""
    
    def __init__(self):
        self.platforms = {
            "instagram": self.search_instagram,
            "twitter": self.search_twitter,
            "tiktok": self.search_tiktok,
            "github": self.search_github,
            "linkedin": self.search_linkedin,
            "facebook": self.search_facebook
        }
        
        # Common headers for scraping
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
        
        # Initialize with default proxy settings
        self.proxy = None
        self.proxy_settings = {
            'http': None,
            'https': None
        }
    
    def clear_screen(self):
        """Clear terminal screen based on OS"""
        os_name = platform.system().lower()
        if os_name == 'windows':
            os.system('cls')
        else:  # For Linux and MacOS
            os.system('clear')
    
    def create_report_folder(self, username):
        """Create report folder if it doesn't exist"""
        username = username.replace(" ", "_")
        folder = f"Reports/{username}/"
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        return folder, username
    
    def create_report_file(self, folder, username):
        """Create and initialize report file"""
        report_path = f"{folder}{username}.txt"
        if os.path.exists(report_path):
            os.remove(report_path)
        
        with open(report_path, "a") as f:
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"SOCIAL SEARCHER REPORT\n")
            f.write(f"=====================\n\n")
            f.write(f"Username: {username}\n")
            f.write(f"Date: {date_string}\n")
            f.write(f"--------------------------------------\n\n")
        
        return report_path
    
    def configure_proxy(self):
        """Configure proxy settings"""
        self.clear_screen()
        
        print("\n[+] Proxy Configuration\n")
        print("[1] Use default system settings")
        print("[2] Enter custom proxy")
        print("[3] No proxy")
        
        choice = input("\n[?] Choose option (1-3): ")
        
        if choice == '1':
            return None
        elif choice == '2':
            proxy_ip = input("\nEnter proxy address (format: ip:port): ")
            if proxy_ip:
                self.proxy = proxy_ip
                self.proxy_settings = {
                    'http': f'http://{proxy_ip}',
                    'https': f'http://{proxy_ip}'
                }
                return proxy_ip
        
        self.proxy = None
        self.proxy_settings = {'http': None, 'https': None}
        return None
    
    def make_request(self, url):
        """Make HTTP request with configured proxy"""
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxy_settings, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"[-] Error accessing {url}: Status code {response.status_code}")
                return None
        except Exception as e:
            print(f"[-] Error accessing {url}: {str(e)}")
            return None
    
    def search_instagram(self, report_path, username, proxy=None):
        """Search for Instagram profile information"""
        print(f"[+] Searching Instagram for: {username}")
        
        url = f"https://www.instagram.com/{username}/"
        
        with open(report_path, "a") as f:
            f.write("\n=== INSTAGRAM RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            
            response = self.make_request(url)
            if response:
                if "The link you followed may be broken" in response.text:
                    f.write("Status: Profile NOT FOUND\n")
                    print(f"[-] Instagram profile not found")
                else:
                    f.write("Status: Profile FOUND\n")
                    print(f"[+] Instagram profile found!")
                    
                    # Extract basic information
                    followers_match = re.search(r'"followedBy":{"count":(\d+)}', response.text)
                    if followers_match:
                        followers = followers_match.group(1)
                        f.write(f"Followers: {followers}\n")
                        print(f"[i] Followers: {followers}")
            else:
                f.write("Status: Error accessing profile\n")
    
    def search_twitter(self, report_path, username, proxy=None):
        """Search for Twitter profile information"""
        print(f"[+] Searching Twitter for: {username}")
        
        url = f"https://twitter.com/{username}"
        
        with open(report_path, "a") as f:
            f.write("\n=== TWITTER RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            
            response = self.make_request(url)
            if response:
                if "This account doesn't exist" in response.text:
                    f.write("Status: Profile NOT FOUND\n")
                    print(f"[-] Twitter profile not found")
                else:
                    f.write("Status: Profile FOUND\n")
                    print(f"[+] Twitter profile found!")
            else:
                f.write("Status: Error accessing profile\n")
    
    def search_tiktok(self, report_path, username, proxy=None):
        """Search for TikTok profile information"""
        print(f"[+] Searching TikTok for: {username}")
        
        url = f"https://www.tiktok.com/@{username}"
        
        with open(report_path, "a") as f:
            f.write("\n=== TIKTOK RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            
            response = self.make_request(url)
            if response:
                if "Couldn't find this account" in response.text:
                    f.write("Status: Profile NOT FOUND\n")
                    print(f"[-] TikTok profile not found")
                else:
                    f.write("Status: Profile FOUND\n")
                    print(f"[+] TikTok profile found!")
            else:
                f.write("Status: Error accessing profile\n")
    
    def search_github(self, report_path, username, proxy=None):
        """Search for GitHub profile information"""
        print(f"[+] Searching GitHub for: {username}")
        
        url = f"https://github.com/{username}"
        
        with open(report_path, "a") as f:
            f.write("\n=== GITHUB RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            
            response = self.make_request(url)
            if response:
                if response.status_code == 404:
                    f.write("Status: Profile NOT FOUND\n")
                    print(f"[-] GitHub profile not found")
                else:
                    f.write("Status: Profile FOUND\n")
                    print(f"[+] GitHub profile found!")
                    
                    # Extract repositories count
                    repos_match = re.search(r'(\d+) repositories available', response.text)
                    if repos_match:
                        repos = repos_match.group(1)
                        f.write(f"Public repositories: {repos}\n")
                        print(f"[i] Public repositories: {repos}")
            else:
                f.write("Status: Error accessing profile\n")
    
    def search_linkedin(self, report_path, username, proxy=None):
        """Search for LinkedIn profile information"""
        print(f"[+] Searching LinkedIn for: {username}")
        
        url = f"https://www.linkedin.com/in/{username}"
        
        with open(report_path, "a") as f:
            f.write("\n=== LINKEDIN RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            f.write("Note: LinkedIn requires authentication for detailed results\n")
            f.write(f"Status: URL generated for manual verification\n")
    
    def search_facebook(self, report_path, username, proxy=None):
        """Search for Facebook profile information"""
        print(f"[+] Searching Facebook for: {username}")
        
        url = f"https://www.facebook.com/{username}"
        
        with open(report_path, "a") as f:
            f.write("\n=== FACEBOOK RESULTS ===\n")
            f.write(f"Username searched: {username}\n")
            f.write(f"Profile URL: {url}\n")
            f.write("Note: Facebook requires authentication for detailed results\n")
            f.write(f"Status: URL generated for manual verification\n")
    
    def search_dorks(self, username, report_path):
        """Search for Google and Yandex dorks"""
        print(f"[+] Generating dork search links for: {username}")
        
        with open(report_path, "a") as f:
            f.write("\n=== DORK SEARCH LINKS ===\n")
            
            # Google dorks
            f.write("Google Dorks:\n")
            google_dorks = [
                f"site:twitter.com {username}",
                f"site:facebook.com {username}",
                f"site:instagram.com {username}",
                f"site:linkedin.com {username}",
                f"site:github.com {username}",
                f"site:youtube.com {username}",
                f"\"{username}\" email",
                f"\"{username}\" contact",
                f"\"{username}\" phone",
                f"\"{username}\" address"
            ]
            for dork in google_dorks:
                f.write(f"- {dork}\n")
                search_url = f"https://www.google.com/search?q={urllib.parse.quote(dork)}"
                f.write(f"  URL: {search_url}\n")
            
            # Yandex dorks
            f.write("\nYandex Dorks:\n")
            yandex_dorks = [
                f"site:twitter.com {username}",
                f"site:facebook.com {username}",
                f"site:instagram.com {username}",
                f"site:linkedin.com {username}",
                f"site:github.com {username}",
                f"\"{username}\" email"
            ]
            for dork in yandex_dorks:
                f.write(f"- {dork}\n")
                search_url = f"https://yandex.com/search/?text={urllib.parse.quote(dork)}"
                f.write(f"  URL: {search_url}\n")
    
    def search_selected_platforms(self, username, platforms):
        """Search username on selected platforms"""
        folder, username_safe = self.create_report_folder(username)
        report_path = self.create_report_file(folder, username_safe)
        
        print(f"\n[+] Starting search for: {username}")
        print(f"[i] Proxy: {'Enabled: ' + self.proxy if self.proxy else 'Disabled'}")
        
        # Search across selected platforms
        for platform in platforms:
            if platform in self.platforms:
                self.platforms[platform](report_path, username, self.proxy)
                time.sleep(1)  # Small delay to avoid rate limiting
        
        # Generate dork search links if requested
        if 'dorks' in platforms:
            self.search_dorks(username, report_path)
        
        print(f"\n[+] Search completed!")
        print(f"[+] Report saved to: {report_path}")
        
        return report_path
    
    def search_all_platforms(self, username):
        """Search username across all platforms"""
        platforms = list(self.platforms.keys())
        platforms.append('dorks')
        return self.search_selected_platforms(username, platforms)
    
    def view_report(self, report_path):
        """View generated report"""
        if os.path.exists(report_path):
            try:
                with open(report_path, 'r') as f:
                    print(f.read())
            except Exception as e:
                print(f"[-] Error reading report: {str(e)}")
        else:
            print(f"[-] Report file not found: {report_path}")
    
    def main_menu(self):
        """Display main menu and handle user input"""
        last_report = None
        
        while True:
            self.clear_screen()
            
            print("\n[+] MAIN MENU")
            print("\n[1] Quick Search (All Platforms)")
            print("[2] Custom Search (Select Platforms)")
            print("[3] Configure Proxy")
            print("[4] View Last Report")
            print("[0] Exit")
            
            choice = input("\n[?] Select an option: ")
            
            if choice == '1':
                self.clear_screen()
                username = input("\n[?] Enter username to search: ")
                if username:
                    last_report = self.search_all_platforms(username)
                    input("\n[i] Press Enter to continue...")
            
            elif choice == '2':
                self.clear_screen()
                username = input("\n[?] Enter username to search: ")
                if username:
                    print("\n[i] Select platforms to search (y/n):")
                    selected_platforms = []
                    
                    for platform in self.platforms.keys():
                        if input(f"  {platform.capitalize()} (y/n): ").lower() == 'y':
                            selected_platforms.append(platform)
                    
                    if input(f"  Dork Search (y/n): ").lower() == 'y':
                        selected_platforms.append('dorks')
                    
                    if selected_platforms:
                        last_report = self.search_selected_platforms(username, selected_platforms)
                    else:
                        print("[-] No platforms selected.")
                        
                    input("\n[i] Press Enter to continue...")
            
            elif choice == '3':
                self.configure_proxy()
                input("\n[i] Press Enter to continue...")
            
            elif choice == '4':
                self.clear_screen()
                if last_report:
                    self.view_report(last_report)
                else:
                    print("\n[-] No reports have been generated yet.")
                input("\n[i] Press Enter to continue...")
            
            elif choice == '0':
                self.clear_screen()
                print("\n[+] Thank you for using Social Searcher!")
                sys.exit(0)
            
            else:
                print("[-] Invalid option. Please try again.")
                time.sleep(1)


# Main execution
if __name__ == "__main__":
    searcher = UsernameSearch()
    try:
        searcher.main_menu()
    except KeyboardInterrupt:
        print("\n[-] Program interrupted. Exiting...")
        sys.exit(0)