# 🔥 scarface966 – Discord Nitro Code Checker

**By: scarface966 (Termux Edition)**  
**Do NOT steal or reupload without credit**  
All rights reserved © 2025 by scarface966

---

## 🛠️ What is this?

A simple, slow, and safe Discord Nitro code checker script made for educational purposes only.

This script:

- Generates random Nitro links (`discord.gift/<code>`)
- Checks if they are valid using Discord’s API
- Waits between requests to avoid IP bans or rate limits
- Saves working codes to `valid_nitros.txt`
- Works on **Termux**, **Linux**, or **Python3 systems**

---

## 🚀 How to run

### 1. Install dependencies (for Termux):

```bash
pkg update && pkg upgrade
pkg install python -y
pip install requests colorama
