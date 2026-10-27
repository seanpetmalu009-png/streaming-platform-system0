
import os
import random
import secrets
import subprocess
import webbrowser
from urllib.parse import urlparse

KEY = "nikaaclients"
TELEGRAM = "https://t.me/nikaascorner"

RED = "\033[91m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"


def open_url(url):
    try:
        subprocess.run(
            ["termux-open-url", url],
            check=True
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        webbrowser.open(url)


def banner():
    os.system("clear")
    print(RED + r"""
 _   _ _____ _____ _____ _____ _     ___ __  __
| \ | | ____|_   _|  ___|_   _| |   |_ _|  \/  |
███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝
██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝
██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗
██║ ╚████║███████╗   ██║   ███████╗███████╗██║██╔╝ ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

             DEMO VERSION
""" + RESET)
    print(WHITE + "=" * 55 + RESET)


def verify_key():
    banner()
    print("Owner: t.me/nikaascorner")
    print("Enter the demo access key.")

    for _ in range(3):
        entered = input("\nLicense Key: ").strip()

        if entered == KEY:
            print(GREEN + "\nAccess Granted!" + RESET)
            input("Press Enter to continue...")
            return True

        print(RED + "Invalid Key!" + RESET)

    print("Access denied.")
    return False


def demo_menu():
    while True:
        banner()
        print("[1] Generate Mock Email")
        print("[2] Generate Dummy Cookie")
        print("[3] Open Custom HTTPS Link")
        print("[4] Contact Owner on Telegram")
        print("[0] Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            number = random.randint(1000, 9999)
            print(f"\nMock Email: demo_{number}@example.com")

        elif choice == "2":
            token = secrets.token_hex(12)
            print(f"\nDummy Cookie: DEMO_{token}")
            print("This is not a real Netflix session cookie.")

        elif choice == "3":
            url = input("Enter HTTPS URL: ").strip()
            parsed = urlparse(url)

            if parsed.scheme == "https" and parsed.hostname:
                open_url(url)
                print("Opening link...")
            else:
                print("Please enter a valid HTTPS URL.")

        elif choice == "4":
            open_url(TELEGRAM)

        elif choice == "0":
            print("Exiting demo.")
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")


def main():
    banner()
    print("Opening owner Telegram...")
    open_url(TELEGRAM)
    input("\nReturn to Termux and press Enter...")

    if verify_key():
        demo_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
