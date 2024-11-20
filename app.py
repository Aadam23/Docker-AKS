# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Docker and AKS!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Flask on AKS!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f4f9;
            }
            h1 {
                color: #333;
                font-size: 3em;
            }
            p {
                color: #555;
                font-size: 1.2em;
            }
            footer {
                margin-top: 50px;
                font-size: 0.9em;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask on AKS!</h1>
        <p>This web application is containerized with Docker and deployed on Azure Kubernetes Service.</p>
        <footer>&copy; 2024 Your Name</footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
