import subprocess


def get_diff(staged_only=True):
    """
    Returns git diff as text.
    staged_only=True -> only staged changes
    staged_only=False -> unstaged + staged changes
    """
    cmd = ["git", "diff", "--cached"] if staged_only else ["git", "diff"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()
