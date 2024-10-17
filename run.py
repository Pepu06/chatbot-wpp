import logging

from app import create_app


app = create_app()

# hello world route
@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000)
