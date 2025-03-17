# Ubisoft Offline Locker

Ubisoft Offline Locker is a simple tool that allows users to easily block the internet connection of **Ubisoft Connect**, forcing the launcher into **offline mode**. This is useful for users who want to prevent Ubisoft Connect from accessing the internet while keeping their games playable.

## Features

✅ **Block Ubisoft Connect**: Prevents the launcher from connecting to Ubisoft servers.  
✅ **Allow Ubisoft Connect**: Restores internet access to the launcher.  
✅ **Persistent Configuration**: Saves the selected executable path for future use.  
✅ **Simple UI**: A lightweight and user-friendly interface.  

## Screenshots
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/screenshot.png?raw=true)

## How It Works

The software modifies the **Windows Firewall rules** to either block or allow internet access for `UplayWebCore.exe`, which is the core network component of Ubisoft Connect. It creates **both inbound and outbound rules** to ensure complete disconnection when blocking.

## Requirements

- Windows 10 / 11
- Python 3.x (for manual build)
- `pyinstaller` (for EXE generation)

## Installation

### 🔹 Using Prebuilt EXE

1. Download `UbisoftOfflineLocker.exe` from the [Releases](https://github.com/RK-Game-Pass/UbisoftOfflineLocker/releases) page.
2. Run it **as Administrator** (Right-click → "Run as administrator").
3. Select the **`UplayWebCore.exe`** file from the Ubisoft Connect installation folder.
4. Click **"Block connection"** to disable online access.
5. Click **"Allow connection"** to restore internet access.

### 🔹 Building from Source

1. **Clone the repository:**
   ```sh
   git clone https://github.com/RK-Game-Pass/UbisoftOfflineLocker.git
   cd UbisoftOfflineLocker
   ```
2. **Install dependencies:**
   ```sh
   pip install pyinstaller
   ```
3. **Build the executable:**
   ```sh
   pyinstaller --onefile --noconsole --icon=icon.ico --name=UbisoftOfflineLocker --uac-admin main.py
   ```
4. The compiled `.exe` file will be in the `dist/` folder.

## 🛠️ Usage Instructions

### 1️⃣ **Launching the Application**
- **Option 1:** Download the EXE from [Releases](https://github.com/RK-Game-Pass/UbisoftOfflineLocker/releases/latest).
- **Option 2:** Build the EXE from the source code (see "Installation" section).
- **IMPORTANT:** **Run as Administrator**  
  → **Right-click** on `UbisoftOfflineLocker.exe` → **Select "Run as administrator"**  

### 2️⃣ **Selecting Ubisoft Connect’s Network File**
1. The app requires selecting the **`UplayWebCore.exe`** file.
2. By default, this file is located in:  
   ```
   C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UplayWebCore.exe
   ```
3. If a path has already been saved, it will be pre-filled automatically.

### 3️⃣ **Blocking Ubisoft Connect’s Internet Access**
- Click **"Block connection"**  
- This creates **Windows Firewall rules** to **block all inbound and outbound traffic**.  
- **Use Case:**  
  ✅ You want to force Ubisoft Connect into **offline mode**.  
  ✅ You want to prevent updates or online authentication while keeping your games playable.  

🚨 **IMPORTANT:** After blocking the connection, Ubisoft Connect **must be restarted**. Even if offline mode appears active, you still need to **restart the launcher and log in again**.

### 4️⃣ **Restoring Ubisoft Connect’s Internet Access**
- Click **"Allow connection"**  
- This removes the firewall rules, allowing Ubisoft Connect to go online again.  
- **Use Case:**  
  ✅ You need to download a game or update.  
  ✅ You want to switch back to online multiplayer mode.  

### 5️⃣ **Checking Firewall Rules**
If you want to verify that the firewall rules were applied, run the following command in the **Command Prompt** (`cmd`):  
```sh
netsh advfirewall firewall show rule name=all
```

## Troubleshooting

- **"Firewall modification failed. Try running as administrator."**  
  → Right-click on `UbisoftOfflineLocker.exe` and select **"Run as Administrator"**.

- **"Invalid file selected."**  
  → Ensure you selected `UplayWebCore.exe` from the correct installation folder.

- **"Firewall rules not applied."**  
  → Check your Windows Firewall settings manually using:
  ```sh
  netsh advfirewall firewall show rule name=all
  ```

## Contributing

Pull requests and issues are welcome! Feel free to fork the repository and submit improvements.

## License

This project is licensed under the **MIT License**.

## Disclaimer

This tool is **not affiliated with Ubisoft**. Use at your own risk.

---