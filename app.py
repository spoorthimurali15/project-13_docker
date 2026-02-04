from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hiii :)!! Your app is running inside Docker and published to ECR 🚀"

if __name__ == "__main__":
    # Run the app on port 5000
    app.run(host="0.0.0.0", port=5000)
