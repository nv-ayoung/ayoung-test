from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# HTML template with a modern, distinctive design
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ayoung-test</title>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #0a0a0f;
            --accent: #ff6b35;
            --accent-glow: rgba(255, 107, 53, 0.3);
            --text-primary: #f0f0f0;
            --text-muted: #6b6b7b;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Syne', sans-serif;
            background: var(--bg-dark);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }
        
        body::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 80%, var(--accent-glow) 0%, transparent 25%),
                radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 25%),
                radial-gradient(circle at 40% 40%, rgba(16, 185, 129, 0.1) 0%, transparent 20%);
            animation: drift 20s ease-in-out infinite;
        }
        
        @keyframes drift {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            33% { transform: translate(2%, -2%) rotate(1deg); }
            66% { transform: translate(-1%, 1%) rotate(-1deg); }
        }
        
        .container {
            position: relative;
            z-index: 1;
            text-align: center;
            padding: 3rem;
        }
        
        .logo {
            font-size: 5rem;
            font-weight: 800;
            color: var(--text-primary);
            letter-spacing: -0.03em;
            margin-bottom: 1rem;
            animation: fadeInUp 0.8s ease-out;
        }
        
        .logo span {
            color: var(--accent);
        }
        
        .tagline {
            font-size: 1.25rem;
            color: var(--text-muted);
            font-weight: 400;
            margin-bottom: 3rem;
            animation: fadeInUp 0.8s ease-out 0.1s both;
        }
        
        .status {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 100px;
            padding: 0.75rem 1.5rem;
            animation: fadeInUp 0.8s ease-out 0.2s both;
        }
        
        .status-dot {
            width: 10px;
            height: 10px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
            50% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
        }
        
        .status-text {
            color: var(--text-muted);
            font-size: 0.9rem;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .endpoints {
            margin-top: 3rem;
            animation: fadeInUp 0.8s ease-out 0.3s both;
        }
        
        .endpoints a {
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
            margin: 0 1rem;
            transition: opacity 0.2s;
        }
        
        .endpoints a:hover {
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="logo">Hello<span>.</span>World</h1>
        <p class="tagline">Flask application up and running</p>
        <div class="status">
            <div class="status-dot"></div>
            <span class="status-text">Server online</span>
        </div>
        <div class="endpoints">
            <a href="/api/health">/api/health</a>
            <a href="/api/info">/api/info</a>
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    """Render the home page."""
    return render_template_string(HOME_TEMPLATE)


@app.route("/api/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "message": "Service is running"})


@app.route("/api/info")
def info():
    """Application info endpoint."""
    return jsonify({
        "name": "ayoung-test",
        "version": "1.0.0",
        "description": "A Flask application"
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
