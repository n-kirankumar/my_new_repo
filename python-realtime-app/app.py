from flask import Flask, Response, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask Real-Time App!"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    message = data.get("message", "")
    return jsonify({"echo": message})

@app.route('/stream')
def stream():
    def event_stream():
        count = 0
        while True:
            count += 1
            yield f"data: Message {count}\n\n"
            time.sleep(2)  # send message every 2 seconds
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
