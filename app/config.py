import sys
import os
from dotenv import load_dotenv
import logging


def load_configurations(app):
    load_dotenv()
    app.config["ACCESS_TOKEN"] = 'EAAN3F5PZBnXIBO1iIQjR7ZC1lh5ZApSX9xVJW2Xmk6ZCVOYKA5kkMWUz5BzzAxxensaTt6bqlP9aHW8SQb5Ggdk2HEqa18VZAS4icbqYZCQ7K8bZAO7FhXvSh6ZC5YM8jZANpZB9pXCb9lgPiqvLfgGruiRoECBkJZCG5iOuX1Mpp92gEguM3ZAswXh5bPOfy2ESRhFjIrRkPRdM33NMRUtjN7jSXGOzZC6HZBeTAOi7AZD'
    app.config["YOUR_PHONE_NUMBER"] = os.getenv("YOUR_PHONE_NUMBER")
    app.config["APP_ID"] = '975368081022322'
    app.config["APP_SECRET"] = 'f778d98308586b573c76e6cd1f25ad2c'
    app.config["RECIPIENT_WAID"] = '541140962011'
    app.config["VERSION"] = 'v20.0'
    app.config["PHONE_NUMBER_ID"] = '472273505962341'
    app.config["VERIFY_TOKEN"] = 'Pepu06112006'


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
