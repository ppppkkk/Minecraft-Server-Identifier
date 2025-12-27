import time, threading
from flask import Flask, render_template, jsonify, request
from mcstatus import JavaServer

app = Flask(__name__)

# This will now store the "Active" server being watched
current_server = {"ip": "mc.hypixel.net"}
latest_data = {"mc_ping": 0, "players": 0, "max_players": 0, "status": "Offline"}

def background_logger():
    global latest_data
    while True:
        try:
            # Always pings whatever is in current_server['ip']
            server = JavaServer.lookup(current_server['ip'])
            status = server.status()
            latest_data = {
                "mc_ping": round(status.latency),
                "players": status.players.online,
                "max_players": status.players.max,
                "status": "Online"
            }
        except:
            latest_data["status"] = "Offline"
            latest_data["mc_ping"] = 0
        time.sleep(3)

@app.route('/')
def home():
    # A list of cool servers to show on the landing page
    featured_servers = [
        {"name": "Hypixel", "ip": "mc.hypixel.net", "desc": "The largest minigame server."},
        {"name": "PikaNetwork", "ip": "play.pika-network.net", "desc": "Popular cracked server."},
        {"name": "Complex Gaming", "ip": "hub.mc-complex.com", "desc": "Pixelmon and Survival."},
        {"name": "DonutSMP", "ip": "donutsmp.net", "desc": "Hardcore Lifesteal SMP."}
    ]
    return render_template('home.html', featured=featured_servers)

@app.route('/monitor')
def monitor():
    # Get the IP from the URL (e.g., /monitor?ip=play.pika.net)
    target_ip = request.args.get('ip', 'mc.hypixel.net')
    current_server['ip'] = target_ip
    return render_template('index.html', ip=target_ip)

@app.route('/data')
def data():
    return jsonify(latest_data)

if __name__ == '__main__':
    threading.Thread(target=background_logger, daemon=True).start()
    app.run(debug=True, port=5000)