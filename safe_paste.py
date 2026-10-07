import re
import pyperclip
import keyboard
import time


def redact_text(text : str) -> str:
    """
    Redacts sensitive keys in the clipboard by replacing them with '<REDACTED_VALUE>'.
    
    Args:
        text (str): The input text to be redacted.
        
    Returns:
        str: The redacted text.
    """

    # PASSWORD
    text = re.sub(
        r'(?i)(pwd|password|pass|passwd)\s*[=:]\s*[^\s]+',
        r'\1=<PASSWORD_REDACTED>',
        text
    )

    # API KEYS
    text = re.sub(
        r'(?i)(api[_-]?key|secret|token)\s*[=:]\s*[^\s]+',
        r'\1=<API_KEY_REDACTED>',
        text
    )

    # DATABASE CONNECTION STRINGS
    text = re.sub(
        r'(postgres|mysql|mongodb|sqlite|mssql|oracle)\s*://[^\s]+',
        r'\1=<DATABASE_CONNECTION_REDACTED>',
        text
    )

    return text


def safe_paste():
    """
    Monitors the clipboard for sensitive information and redacts it when detected.
    """

    original = pyperclip.paste()

    safe_text = redact_text(original)

    pyperclip.copy(safe_text)

    keyboard.press_and_release('ctrl+v')

    time.sleep(0.1)  # Small delay to ensure the paste operation completes
    pyperclip.copy(original)  # Restore the original clipboard content


print('Safe Paste is running. Press Ctrl+Shift+V to paste redacted content.')
print('Press Ctrl + Shift + V to safely paste')
print('Press Esc to stop.')

keyboard.add_hotkey('ctrl+shift+v', safe_paste)
keyboard.wait('esc')
