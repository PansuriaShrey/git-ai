import subprocess

from dotenv import load_dotenv

from common.utils import get_diff, suggest_commit_message

load_dotenv()


def main():
    diff = get_diff()
    if not diff:
        print("No changes detected.")
        return

    print("🔍 Generating commit message...")
    message = suggest_commit_message(diff)
    print(f"\n💡 Suggested commit message:\n{message}\n")

    confirm = input("Commit with this message? (y/N): ").strip().lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", message])
        print("✅ Commit created.")
    else:
        print("❌ Commit canceled.")


if __name__ == "__main__":
    main()
