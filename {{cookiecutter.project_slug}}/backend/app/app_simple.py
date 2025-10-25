from flask import Flask, jsonify, render_template_string
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    pod_name = os.getenv('HOSTNAME', 'unknown')
    
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Backend - Kubernetes Challenge</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: white;
                    padding: 20px;
                }
                .container {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 50px 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                    backdrop-filter: blur(10px);
                    max-width: 800px;
                    width: 100%;
                }
                .emoji {
                    font-size: 4em;
                    text-align: center;
                    margin-bottom: 20px;
                    animation: bounce 2s infinite;
                }
                @keyframes bounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-20px); }
                }
                h1 {
                    font-size: 2.5em;
                    text-align: center;
                    margin-bottom: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }
                h2 {
                    font-size: 1.5em;
                    text-align: center;
                    margin-bottom: 30px;
                    opacity: 0.9;
                }
                .badge {
                    background: rgba(255, 255, 255, 0.2);
                    padding: 15px 30px;
                    border-radius: 25px;
                    text-align: center;
                    margin: 20px 0;
                    font-weight: bold;
                    border: 2px solid rgba(255, 255, 255, 0.3);
                }
                .pod-info {
                    background: rgba(0, 0, 0, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                    font-family: 'Courier New', monospace;
                }
                .pod-info h3 {
                    margin-bottom: 15px;
                    font-size: 1.2em;
                }
                .info-row {
                    display: flex;
                    justify-content: space-between;
                    padding: 8px 0;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                }
                .info-row:last-child { border-bottom: none; }
                .label { font-weight: bold; opacity: 0.8; }
                .value { color: #a0f0a0; }
                .tech-stack {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                    gap: 15px;
                    margin-top: 30px;
                }
                .tech-item {
                    background: rgba(255, 255, 255, 0.15);
                    padding: 15px;
                    border-radius: 15px;
                    text-align: center;
                    font-size: 0.9em;
                }
                .endpoints {
                    background: rgba(0, 0, 0, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                }
                .endpoints h3 {
                    margin-bottom: 15px;
                }
                .endpoint-item {
                    padding: 8px;
                    margin: 5px 0;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 5px;
                    font-family: 'Courier New', monospace;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="emoji">🚀</div>
                <h1>Flask Backend</h1>
                <h2>Kubernetes DevOps Challenge</h2>
                
                <div class="badge">
                    ✅ Successfully Deployed with 2 Replicas
                </div>
                
                <div class="pod-info">
                    <h3>📦 Pod Information</h3>
                    <div class="info-row">
                        <span class="label">Pod Name:</span>
                        <span class="value">{{ pod_name }}</span>
                    </div>
                    <div class="info-row">
                        <span class="label">Hostname:</span>
                        <span class="value">{{ hostname }}</span>
                    </div>
                    <div class="info-row">
                        <span class="label">Service Port:</span>
                        <span class="value">5000</span>
                    </div>
                    <div class="info-row">
                        <span class="label">NodePort:</span>
                        <span class="value">30007</span>
                    </div>
                </div>
                
                <div class="tech-stack">
                    <div class="tech-item">🐍 Python Flask</div>
                    <div class="tech-item">🐳 Docker</div>
                    <div class="tech-item">☸️ Kubernetes</div>
                    <div class="tech-item">🎯 Minikube</div>
                </div>
                
                <div class="endpoints">
                    <h3>🔗 Available API Endpoints</h3>
                    <div class="endpoint-item">GET / - Home Page</div>
                    <div class="endpoint-item">GET /api/health - Health Check</div>
                    <div class="endpoint-item">GET /api/info - System Information</div>
                    <div class="endpoint-item">GET /api/pod - Pod Details</div>
                </div>
            </div>
        </body>
        </html>
    ''', pod_name=pod_name, hostname=hostname)

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Backend Flask application is running',
        'service': 'flask-backend',
        'version': 'v1'
    }), 200

@app.route('/api/info')
def info():
    return jsonify({
        'application': 'Flask Backend DevOps Challenge',
        'framework': 'Flask',
        'python_version': os.sys.version,
        'hostname': socket.gethostname(),
        'pod_name': os.getenv('HOSTNAME', 'unknown'),
        'status': 'running',
        'port': 5000
    }), 200

@app.route('/api/pod')
def pod_info():
    return jsonify({
        'pod_name': os.getenv('HOSTNAME', 'unknown'),
        'hostname': socket.gethostname(),
        'node_name': os.getenv('NODE_NAME', 'unknown'),
        'pod_ip': os.getenv('POD_IP', 'unknown'),
        'namespace': os.getenv('POD_NAMESPACE', 'default')
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
