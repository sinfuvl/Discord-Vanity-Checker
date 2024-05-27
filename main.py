import tls_client, asyncio, threading, colorama, time; from tls_client import Session; from colorama import Fore, Style

class Main():
  def __init__(self):
    self.session = Session(client_identifier="chrome_108", random_tls_extension_order=True)

  def fetchvanities(self):
    with open("data/vanities.txt", "r") as f:
      return f.read().splitlines()

  def istaken(self, vanity):
    r = self.session.get(f"https://discord.com/api/v9/invites/{vanity}")
    if r.status_code in (200, 201, 204):
      print(f"{Fore.RED}[+]{Style.RESET_ALL} {vanity} is taken")
      return True
    elif r.status_code in (404, 405, 429):
      print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {vanity} is available")
      return False
    else:
      return None

  def addvanity(self, vanity):
    with open("data/available.txt", "a") as f:
      f.write(vanity + "\n")

  def main(self):
    while True:
      vanities = self.fetchvanities()
      for vanity in vanities:
        process = self.istaken(vanity)
        if process == True:
          pass
        elif process == False:
          self.addvanity(vanity)
        else:
          pass
      time.sleep(1)

  def run(self):
    threading.Thread(target=self.main).start()

if __name__ == "__main__":
  Main().run()
