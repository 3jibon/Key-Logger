````markdown
# 🛡️ Persistent Keylogger (Python)

A lightweight and persistent keylogger written in Python that logs keystrokes in real-time and saves them periodically to session files. Designed for **educational** and **research purposes only**.

---

## 🚀 Features

- Logs all keyboard activity including special keys
- Saves logs periodically (configurable interval)
- Creates separate session logs and a combined log
- Logs saved under a dedicated `keylogs/` directory
- Gracefully exits and saves logs on pressing `ESC`

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/3jibon/Key-Logger.git
cd Key-Logger
````

### 2. Install Dependencies

> Requires Python 3.6+

```bash
pip install keyboard
```

---

## ▶️ Run the Keylogger

```bash
python keylogger.py
```

* Logs will be saved inside the `keylogs/` folder.
* Press `ESC` key to stop the logger safely.

---

## 📁 Logs

* `keylogs/session_<timestamp>.txt` — log of the current session
* `keylogs/combined_log.txt` — all logs combined with timestamps

---

## ⚠️ WARNING

> **This project is for educational and ethical testing only.**

Using keyloggers to monitor devices you do not own or without consent is illegal and unethical.
By using this code, **you take full responsibility** for how it's deployed.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

* Farhan Uddin Jibon
* [GitHub](https://github.com/3jibon)


