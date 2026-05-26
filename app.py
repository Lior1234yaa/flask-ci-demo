from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "CI/CD Demo"}


@app.get("/health")
def health():
    return {"status": "ok12"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
