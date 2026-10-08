import os
import subprocess
import sys

# ─────────────────────────────────────────────────────────────
# AYTRO GEN
# ─────────────────────────────────────────────────────────────

TITLE = r"""
 █████╗ ██╗   ██╗████████╗██████╗  ██████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔══██╗██╔═══██╗
███████║ ╚████╔╝    ██║   ██████╔╝██║   ██║
██╔══██║  ╚██╔╝     ██║   ██╔══██╗██║   ██║
██║  ██║   ██║      ██║   ██║  ██║╚██████╔╝
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝
"""

# Folder containing the generator scripts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_DIR = os.path.join(BASE_DIR, "gens")

# Menu options
OPTIONS = {
    "1": os.path.join(GEN_DIR, "generator10.py"),
    "2": os.path.join(GEN_DIR, "generator20.py"),
    "3": os.path.join(GEN_DIR, "generator50.py"),
    "4": os.path.join(GEN_DIR, "generator100.py"),
}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def run_script(script_path):
    if not os.path.isfile(script_path):
        print("\n[!] Generator file not found.")
        input("\nPress Enter to continue...")
        return

    clear_screen()
    print(TITLE)
    print("─" * 55)
    print("                    AYTRO GEN")
    print("─" * 55)
    print("\n[+] Starting generator...\n")

    try:
        subprocess.run(
            [sys.executable, script_path],
            check=False
        )
    except KeyboardInterrupt:
        print("\n\n[!] Generator stopped.")

    input("\nPress Enter to return to the menu...")


def menu():
    while True:
        clear_screen()

        print(TITLE)
        print("─" * 55)
        print("                    AYTRO GEN")
        print("─" * 55)
        print()
        print("[1] Generate 10")
        print("[2] Generate 20")
        print("[3] Generate 50")
        print("[4] Generate 100")
        print()
        print("[0] Exit")
        print()

        choice = input("AYTRO GEN > ").strip()

        if choice == "0":
            clear_screen()
            print(TITLE)
            print("\nThanks for using AYTRO GEN!")
            break

        if choice in OPTIONS:
            run_script(OPTIONS[choice])
        else:
            print("\n[!] Invalid option.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    menu()