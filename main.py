from analysis.file_analysis import analyze_file
from utils.logger import log_activity

def display_menu():
    print("\n========== CryptoLabX ==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")
    print("================================")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            log_activity("Encrypt")
            print("\n[Encrypt] Coming Soon...")

        elif choice == "2":
            log_activity("Decrypt")
            print("\n[Decrypt] Coming Soon...")

        elif choice == "3":
            log_activity("Attack")
            print("\n[Attack] Coming Soon...")

        elif choice == "4":
            log_activity("Analyze")
            analyze_file("datasets/sample.txt")

        elif choice == "5":
            log_activity("Exit")
            print("\nThank you for using CryptoLabX!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()