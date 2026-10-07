# Safe Paste

Safe Paste is a small personal project I created to help prevent accidentally sharing sensitive information when copying and pasting text.

It detects and redacts common sensitive values such as:

- Passwords
- API keys
- Tokens and secrets
- Database connection strings

## How It Works

Run Safe Paste and use:

```text
Ctrl + Shift + V
```

instead of the normal paste shortcut.

For example:

```text
password=mySecretPassword
```

becomes:

```text
password=<PASSWORD_REDACTED>
```

The original clipboard content is restored after the safe version is pasted.


# 🔐 Safe Paste

Safe Paste is a small personal project I created to help prevent accidentally sharing sensitive information when copying and pasting text.

It currently detects and redacts:

- Passwords
- API keys
- Tokens and secrets
- Database connection strings

## How to Run

Clone the repository and open the project folder.

Install the dependencies:

```bash
uv sync
```

Run Safe Paste:

```bash
uv run python safe_paste.py
```

You should see:

```text
Safe Paste is running. Press Ctrl+Shift+V to paste redacted content.
Press Esc to stop.
```

## How to Use

Copy text normally, then use:

```text
Ctrl + Shift + V
```

instead of `Ctrl + V`.

For example:

```text
password=hello123
```

will be pasted as:

```text
password=<PASSWORD_REDACTED>
```

Press `Esc` to stop Safe Paste.


## Disclaimer

Safe Paste is a personal project and is still a work in progress. It is intended to reduce the risk of accidentally pasting sensitive information, but it does not guarantee that all passwords, API keys, tokens, credentials, or other sensitive data will be detected or redacted.

Always review your content before sharing or publishing it. Do not rely on Safe Paste as your only method of protecting sensitive information.

Use at your own risk.