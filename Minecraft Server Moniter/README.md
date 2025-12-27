# Minecraft Server Monitor Pro

A high-performance, real-time web dashboard designed to monitor Minecraft server telemetry. This project provides live-scrolling "Task Manager" style visualizations for latency and player population.

## Key Features
* **Real-Time Streaming Graphs:** Smooth, animated line charts for Ping and Player counts that update every 2 seconds without page refreshes.
* **Dual-Page Navigation:** * **Home:** A searchable landing page with "Quick Connect" buttons for major networks.
    * **Monitor:** A dedicated dashboard with glassmorphism UI and big-number stat cards.
* **Smart Telemetry Thread:** A background Python thread handles all server communication, ensuring zero lag on the web interface.
* **Persistent Logging:** Automatically records every status update to `server_log.csv` for historical tracking.
* **Optimized Handshake:** Uses a refined status protocol to provide the most accurate "in-game" latency feel.

---

## Setup & Installation

### 1. Install Required Libraries
You will need Python 3.8+ installed. Use the following command to install dependencies:

pip install flask mcstatus

### 2. Project Directory Structure
For the app to run correctly, ensure your folder is organized as follows:

/minecraft-monitor
├── run_monitor.py      # Main Python Application
├── server_log.csv      # Auto-generated Data Log
└── /templates
      ├── home.html     # Search & Landing Page
      └── index.html    # Live Graph Dashboard

### 3. Running the Application
Launch the monitor from your terminal:

python run_monitor.py

Then, access the dashboard at: http://localhost:5000

---

## Technical Breakdown

### The Backend (Python + Flask)
* **Threading:** Uses Python's threading module to run a background monitor that pings the server independently of the web server. This prevents the website from freezing while waiting for a server response.
* **MCStatus:** Utilizes the SLP (Server List Ping) protocol to query the Java Edition server port (25565).
* **JSON API:** Serves data through a /data endpoint, allowing the frontend to pull updates asynchronously.

### The Frontend (AJAX + Chart.js)
* **Streaming Plugin:** Uses chartjs-plugin-streaming to create the "Task Manager" look where data slides smoothly across the screen in real-time.
* **Luxon Adapter:** Handles high-precision time-scaling and date formatting for the X-axis.
* **Bootstrap 5:** Provides the responsive, dark-mode professional grid layout and "Glassmorphism" card styles.

---


## Customization
You can update the "Featured Servers" list by modifying the featured_servers array in run_monitor.py. 

featured_servers = [
    {"name": "Hypixel", "ip": "mc.hypixel.net", "desc": "The gold standard of minigames."},
    {"name": "PikaNetwork", "ip": "play.pika-network.net", "desc": "Top-tier cracked server."},
]