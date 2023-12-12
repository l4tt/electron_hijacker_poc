from __init__ import VERSION, API_ENDPOINT
import httpx, colorama
"""
Since, there API is gay make sure to use a VPN or a proxy, since they decide to ban your IP with CF WAF
"""

colorama.init()

class Messages:
    SUCCESS = f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] - " 
    ERROR = f"[{colorama.Fore.RED}-{colorama.Fore.RESET}] - "
    

class Hijack(Messages):
    def __init__(self):
        self.jwt_url = ""
        self.online_user_id = ""
        self.online_count = 0
# Please Replace the cookie agent with your own once it expires it will hit cloudflare
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "Cookie": "_ga=GA1.1.876850328.1700776169; _ga_7QWC8W9ECE=GS1.1.1701314942.3.0.1701314942.60.0.0; cf_clearance=Taau5bsIBXnQUpCrLrMny2RkF559DpWmPAASrhSY5oY-1702245863-0-1-c79ff041.fadb6de8.909eafa1-0.2.1702245863; __cf_bm=9NnkPnfLw15zTFxi.gkfYfXWZG9otIfYn9TTPyZaHpU-1702418509-1-AbLJ1a4IWnJZ+AXQaEe92iUZUUC3GeQdjK9UgITWk5m7XxtNUjW2vJWRKEdPudtjZzP/EmLfeZMnAO49PNElXa4="
        }

    def start_hijack(self):
        if not self.get_online_count():
            return print(f"{self.ERROR}Failed to get recent online user")

        print(f"{self.SUCCESS}Electron online user InstanceID: {self.online_user_id}")
        print(f"{self.SUCCESS}Electron online total users: {self.online_count}")
        
        if not self.gen_jwt():
            return print(f"{self.ERROR}Failed to gen an launch JWT token for electron")
        
        print(f"{self.SUCCESS}Electron Launch URL: {self.jwt_url}")
        print(f"{self.SUCCESS}Waiting for you to launch the URL...")
        
        
        
        
        while not self.get_jwt_status():
            print(f"{self.ERROR}Electron JWT token status is invalid, waiting to be authincated")
        
        print(f"{self.SUCCESS}Spoofed user ID to {self.online_user_id}")

    
    def get_jwt_status(self) -> bool:
        try:
            data = httpx.get(API_ENDPOINT + f"/94a055ed-d672-450c-94a9-1359c0510bfa/electron/launch/status?i={self.online_user_id}", headers=self.headers).json()
            get_status = data['success']
            get_auth = data['authorized']
        
            if get_status != True:
                return False
        
            if get_auth != True:
                return False
            
            return True
        except:
            return False
        
        
    
    def get_online_count(self) -> bool:
        try:
            data = httpx.get(API_ENDPOINT + "/site", headers=self.headers).json()
            
            visible_instances = data['cluster']['visibleInstances']
            first_instance_id = next(iter(visible_instances))
            connected_clients = visible_instances[first_instance_id]['connectedClients']

            self.online_user_id = first_instance_id
            self.online_count = connected_clients
            
            return True
        except Exception as e:
            
            return False
        
        

    def gen_jwt(self) -> bool:
        try:
            data = httpx.get(API_ENDPOINT + f"/94a055ed-d672-450c-94a9-1359c0510bfa/electron/launch/new?i={self.online_user_id}", headers=self.headers).json()
            launch_url = data['launchUrl']
            launchid = data['launchId']
            self.online_user_id = launchid
            self.jwt_url = launch_url
            

            return True
        except:
            return False
        
        

if __name__ == "__main__":
    Hijack().start_hijack()
