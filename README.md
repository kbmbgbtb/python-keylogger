# python-keylogger
A Python keylogger that logs keystrokes in batches of 200 characters
This is a Python-based keylogger that captures keyboard input in real time and stores it in **batches of 200 characters**. It logs each batch with a timestamp and writes the data to a JSON file inside a dated folder.

DISCLAIMER: This tool is for educational, ethical testing, and cybersecurity training purposes only. Do not use this on any system or person without explicit, informed consent.

Features

- Real-time keystroke capture using `pynput`
- Groups every 200 characters into a single JSON log entry
- Automatically creates a folder named with the current date (`DDMMYYYY`)
- Saves logs in JSON format with timestamps
- Lightweight and cross-platform (Windows/Linux/macOS)

Project Structure

```
keylogger_project/
├── keylogger_batching.py
└── README.md
```

Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-keylogger.git
cd python-keylogger
```

2. Install Dependencies

```bash
pip install pynput
```

> Optional for window tracking:  
> `pip install pywin32` (Windows only)

How It Works

- The script listens for keyboard input.
- Every time 200 characters are captured, it creates a **new log batch** and appends it to a JSON file.
- The logs are stored in a folder named after the current date (e.g., `01072025`) in the same directory as the script.

Example Output (JSON)

```json
[
  {
    "timestamp": "2025-07-01 17:35:02",
    "batch": "the quick brown fox jumps over the lazy dog... (200 chars)"
  },
  {
    "timestamp": "2025-07-01 17:37:12",
    "batch": "next 200 characters typed..."
  }
]
```

Customization

You can tweak the following:

| Option | Description |
|--------|-------------|
| `200` | Change the character batch size |
| `log_dir` | Modify the destination folder |
| `json` | Change output format (CSV or TXT with minor edits) |

Legal & Ethical Notice

This tool must **only be used**:

- In your own virtual machines or test environments
- With **informed consent** from all participants
- For learning, awareness, or cybersecurity training

**Unauthorized use of keyloggers is illegal and unethical.**

License

MIT License — Free to use, modify, and distribute with credit.
