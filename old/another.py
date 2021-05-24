from flask import Flask
app = Flask("__main__")

@app.route("/")
def index():
    return "Another Page"


if __name__ == "__main__":
    app.run(debug=True)  