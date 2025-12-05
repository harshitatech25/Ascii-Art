import os
import msvcrt as msv
from colorama import init, Fore, Back, Style

init(autoreset=True)

def fill_background():
    print(Back.BLACK + " " * 200)

ascii_rows = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

def print_char(row, col):
    print(Fore.CYAN + Style.BRIGHT + row[col], end="")

def print_title(text):
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + text.center(70))
    print()

def char_index(ch):
    if ch.isdigit():
        return (ord(ch) - 17) * 6
    if ch == " ":
        return 26 * 6
    if ch == "@":
        return 27 * 6
    if ch == "_":
        return 28 * 6
    if ch == "-":
        return 29 * 6
    if ch == ".":
        return 30 * 6
    return ((ord(ch) - 64) - 1) * 6

def show_single_char():
    os.system("cls")
    fill_background()
    print_title(" ONE CHARACTER ")

    ch = input(Fore.YELLOW + "Enter One Character: ").upper()
    if len(ch) != 1:
        show_single_char()
        return

    n = char_index(ch)

    for row in ascii_rows:
        for col in range(n, n + 6):
            print_char(row, col)
        print()

def show_words():
    os.system("cls")
    fill_background()
    print_title(" ALPHA NUMERIC WORDS ")

    text = input(Fore.YELLOW + "Enter String (<=15): ").upper()
    if not (1 <= len(text) <= 15):
        show_words()
        return

    for row in ascii_rows:
        for ch in text:
            n = char_index(ch)
            for col in range(n, n + 6):
                print_char(row, col)
        print()

def show_range():
    os.system("cls")
    fill_background()
    print_title(" ALPHA RANGE ")

    r = input(Fore.YELLOW + "Enter Range (A-D): ").upper()
    if len(r) != 3:
        show_range()
        return

    start = ord(r[0]) - 64
    end = ord(r[2]) - 64
    if start > end or abs(end - start) >= 15:
        show_range()
        return

    for row in ascii_rows:
        for i in range(start, end + 1):
            n = (i - 1) * 6
            for col in range(n, n + 6):
                print_char(row, col)
        print()

def show_alpha():
    os.system("cls")
    fill_background()
    print_title(" ONLY ALPHABETS ")

    text = input(Fore.YELLOW + "Enter Alphabets (<=15): ").upper()
    if not (1 <= len(text) <= 15) or not text.isalpha():
        show_alpha()
        return

    for row in ascii_rows:
        for ch in text:
            n = ((ord(ch) - 64) - 1) * 6
            for col in range(n, n + 6):
                print_char(row, col)
        print()

def show_numbers():
    os.system("cls")
    fill_background()
    print_title(" ONLY NUMBERS ")

    text = input(Fore.YELLOW + "Enter Numbers (<=15): ").upper()
    if not (1 <= len(text) <= 15) or not text.isnumeric():
        show_numbers()
        return

    for row in ascii_rows:
        for ch in text:
            n = (ord(ch) - 17) * 6
            for col in range(n, n + 6):
                print_char(row, col)
        print()

def menu():
    while True:
        os.system("cls")
        fill_background()
        print_title(" ASCII ART PROJECT ")

        print(Fore.CYAN + "1. One Character")
        print(Fore.MAGENTA + "2. Words")
        print(Fore.GREEN + "3. Range")
        print(Fore.YELLOW + "4. Only Alphabets")
        print(Fore.RED + "5. Only Numbers")
        print(Fore.WHITE + "6. Exit\n")

        choice = msv.getch().decode()

        if choice == "1": show_single_char()
        elif choice == "2": show_words()
        elif choice == "3": show_range()
        elif choice == "4": show_alpha()
        elif choice == "5": show_numbers()
        elif choice == "6": return

        print(Fore.GREEN + "\nPress Y to continue...")
        if msv.getch().decode().lower() != "y":
            break

menu()
