
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


def open_url(url):https://www.netflix.com/unsupported?nftoken=BgjCwOvcAxLCAcxAVkuctlRvVlA2/NQljes3Q0AKA7kgbCvfmWEbHcfloMQD/T5PWylgGfvRqdGGix6xTshNpFTtnnUTcw41dahPXA1wXLsaBExHCPAJDGssU0xASzp4GPwNUIBICeQZx89T9oHdmUYRMhZfJGZdUHJhsO8JvKKTpkQH1ujCayhkzVDag3kiXfVAZS+VfrtiuCB0nYfhRA9TSSlXNi4HRxk1Cmh5e7rs9q/FNEuDly1uK6D/PuycRRYqh0Agty3bz/AhGAYiDgoMs8OQKf8ZWlqRE3fr
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

             RED VERSION
""" + RESET)
    print(WHITE + "=" * 55 + RESET)


def verify_key():
    banner()
    print("Owner: t.me/nikaascorner")
    print("Enter the access key.")

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
        print("[1] Generate Netflix Email")
        print("[2] Generate Cookie")
        print("[3] Open Custom HTTPS Link")
        print("[4] Contact Owner on Telegram")
        print("[0] Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            number = random.randint(1000, 9999)
            print(f"\nEmail: 123{tunax}@gmail.com")

        elif choice == "2":
            token = secrets.tokenx(12)
            print(f"\n Cookie { NetflixId=v%3D3%26ct%3DBgjHlOvcAxLsAzspCE2wYQo3Qu5GvEPVBeEZsXNZRJ4kc8VIdH11eQGGxbuczGw9culnUeBLJlG6HLgrQtkAa166NeRch6t2r0YAp6x_nrq2uUy56b53O99R3OEdpOgPbH5MNgmzpzISove7xIrGLhFaAsUTvCqIYdDf4Gg05iiZSEWql5919MK509EB5ficSRPAGah-oqWggOcMZCfk86hZFeZvWrByZmIZ7zZv0pg2XKM2ELseV8j9B_k5PPNdCJHoO4nZcfXNlBEFqaYC8mfuPBEwLkxF4cGLPLEE4pzXOcXE4028IscWu14KFYCXzyH__iAXKIlivbLziuZgLzhlpA3LZFifckDkJV8HdfdnKmR0sWJ9J_jcZVPeK1whA_4BN_7pz2VjL1PGaRn-3sCHpxEAHZt820_AEGSxxb6T9QQ6y0tTtuFpKqKfb3g4gdRVcb3g0HbrW2OC1N_NxMbOocungrrOUrPe6zFr8MDk_04yzR25nqduIAEZOG5HYOp0e97qp9s3ydwWkTUkyd_yCxwwj2me5VUFqrC-Trd4cUx-hZFZZY36eSvM1oI7-wZ-Do1Y9thn_Seh3jYyLGk7orjMSyF4Dtnmhwsc6ZFg4DUrkmnBgtIFlOaSCxlWp2R_333YcPt1Kty7grsFTDxI4e2jwRgGIg4KDGjlfWvEn4ou35FM0w..%26pg%3DOORL6G3H5BDIFCO7ZUNB27GTUE%26ch%3DAQEAEAABABRLJEubVLE6D5vBG_xWi6yx5CM_Cp0hhYU. }")
            print("This is real Netflix session cookie.")

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
            print("Exiting.")
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
      menu()
if __name__ == "__main__":
    try:
        main()
except Keyboard Interrupt:
        print("\nExiting...")
