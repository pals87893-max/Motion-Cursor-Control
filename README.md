# 🎮 Motion Cursor Control

Control your PC mouse using your smartphone's motion sensors over Wi-Fi. Simply run the Python server on your computer, open the web app on your phone, connect both devices on the same network, and use your phone like an air mouse.

---

## ✨ Features

- 📱 Motion-based mouse control
- 🖱️ Left & Right click support
- ⚡ Real-time WebSocket communication
- 🌐 Works over local Wi-Fi
- 🔧 Adjustable sensitivity and axis inversion
- 💻 Cross-platform Python backend

---

## 📂 Project Structure

```
.
├── main.py              # Python WebSocket server
├── phone-sensor.html    # Mobile web application
└── README.md
```

---

## 🛠 Requirements

### PC

- Python 3.9+
- Windows/Linux/macOS

Install dependencies:

```bash
pip install pyautogui websockets
```

### Mobile

- Any Android phone with Chrome (or another browser supporting DeviceMotion API)
- Both phone and PC must be connected to the **same Wi-Fi network**

---

# 🚀 How It Works

The project consists of two parts:

### 1. Python Server (PC)

The Python application:

- Starts a WebSocket server on port **8080**
- Prints your PC's local IP address
- Receives motion data from your phone
- Converts phone rotation into mouse movement
- Handles left and right click events

---

### 2. Mobile Web App

The HTML page:

- Reads the phone's motion sensors
- Displays live sensor values
- Connects to the PC using WebSockets
- Sends sensor data at approximately **60 Hz**
- Includes Left Click and Right Click buttons

---

# ⚙️ Installation

## Step 1

Clone the repository.

```bash
git clone https://github.com/yourusername/motion-cursor-control.git
cd motion-cursor-control
```

---

## Step 2

Install dependencies.

```bash
pip install pyautogui websockets
```

---

## Step 3

Start the Python server.

```bash
python main.py
```

You will see something similar to:

```
your PC's local IP is:
192.168.1.25
```

Keep this terminal open.

---

## Step 4

Open `phone-sensor.html`.

You can:

- Host it using a local HTTP server
- Upload it to GitHub Pages
- Upload it to Netlify/Vercel
- Or serve it from any web server

> **Do not open it directly using `file://`** because motion sensors may not work correctly.

A simple local server:

```bash
python -m http.server
```

Then open

```
http://YOUR_PC_IP:8000/phone-sensor.html
```

on your phone.

---

## Step 5

Enter the IP address printed by the Python server.

Example:

```
192.168.1.25
```

Press **Submit**.

---

## Step 6

Press **Connect & Stream**.

Allow motion sensor permission if prompted.

Your phone is now controlling your PC cursor.

---

# 🎮 Controls

| Action | Description |
|---------|-------------|
| Tilt Phone | Move cursor |
| Left Click | Left mouse click |
| Right Click | Right mouse click |

---

# ⚙️ Configuration

Inside `main.py` you can customize:

```python
SENSITIVITY = 0.2
```

Increase for faster cursor movement.

---

Dead zone:

```python
DEADLOCK = 5.0
```

Ignores small movements to reduce cursor jitter.

---

Axis settings:

```python
INVERT_X = True
INVERT_Y = False
SWAP_AXES = False
```

Useful if movement feels reversed.

---

# 🧠 Communication Flow

```
Phone Motion Sensors
        │
        ▼
DeviceMotion API
        │
        ▼
WebSocket Client
        │
        ▼
Python WebSocket Server
        │
        ▼
PyAutoGUI
        │
        ▼
PC Mouse Cursor
```

---

# 📦 Dependencies

Python

- websockets
- pyautogui
- asyncio
- socket
- json

Browser

- DeviceMotion API
- WebSocket API

---

# 🐞 Troubleshooting

### Cursor doesn't move

- Make sure both devices are on the same Wi-Fi.
- Verify the IP address is correct.
- Ensure the Python server is running.
- Check that port **8080** isn't blocked.

---

### Motion permission denied

Grant Motion & Orientation permission in your browser:
On android:
- Open Chrome and tap the menu icon (three dots) in the top-right corner.
- Select Settings.
- Scroll down to the Advanced section and tap Site Settings.
- Scroll to the bottom, tap Additional permissions, and select Motion sensors.
- Toggle the setting to Sites can use motion sensors.
  
On iOS:
  - Open your iPhone Settings app.
  - Scroll down and tap Safari.
  - Ensure Motion & Orientation Access is toggled on (the switch should be green)

---

### Cursor moves the wrong way

Adjust:

```python
INVERT_X
INVERT_Y
SWAP_AXES
```

inside `main.py`.

---

### Connection failed

Make sure the firewall allows Python to accept incoming connections.

---

# 📈 Future Improvements

- Scroll support
- Drag & drop
- Multi-touch gestures
- Adjustable sensitivity from the phone
- Secure (WSS) connection

---
## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
