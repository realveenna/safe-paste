# Safe Paste

Safe Paste is a small personal project I created to help prevent accidentally sharing sensitive information when copying and pasting text.

It detects and redacts common sensitive values such as:

- Passwords
- API keys
- Tokens and secrets
- Database connection strings

## How It Works

Safe Paste uses **Ctrl + Shift + V** as a safe paste shortcut instead of the normal **Ctrl + V**.

For example:

```text id="q2uhqp"
password=mySecretPassword
```

becomes:

```text id="fnwmn8"
password=<PASSWORD_REDACTED>
```

The original clipboard content is restored after the safe version is pasted.

## How to Use

1. Download `SafePaste.exe` from the latest GitHub Release.
2. Double-click `SafePaste.exe`.
3. Leave the Safe Paste window open.
4. Copy text normally.
5. Press **Ctrl + Shift + V** to safely paste.
6. Press **Esc** to stop Safe Paste.

Normal **Ctrl + V** will still paste the original clipboard content.

> The Windows `.exe` does not require Python or uv to be installed.

## Running from Source

Install dependencies:

```bash id="bipns1"
uv sync
```

Run Safe Paste:

```bash id="y5kyb4"
uv run python safe_paste.py
```

Then use **Ctrl + Shift + V** to safely paste.

## Privacy

Safe Paste does not collect, store, transmit, or share personal information.

Clipboard content is processed locally on your device and is not sent to the developer or any external service.

See [`PRIVACY.md`](PRIVACY.md) for the full privacy policy.

## Disclaimer

Safe Paste is a personal project and is still a work in progress. It is intended to reduce the risk of accidentally sharing sensitive information, but **it does not guarantee that all passwords, API keys, tokens, credentials, or other sensitive data will be detected or redacted**.

Always review your content before sharing or publishing it. Do not rely on Safe Paste as your only method of protecting sensitive information.

Use at your own risk.
