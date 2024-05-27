# Imports
from ats.core.models.base.app import BaseApp
from flask import Flask


class WebApp(BaseApp):
    __server_ip: str
    __server_port: int

    def __init__(self, server_ip: str = "127.0.0.1", server_port: int = 5000):
        self.__server_ip = server_ip
        self.__server_port = server_port

        # Check the variables that have been passed
        self.check_parameters()

    def check_parameters(self) -> None:
        """Checks app parameters

        Check the variables that have been passed to the app

        Args:

        Returns:
            None
        """
        if not self.__server_ip or self.__server_ip == "":
            raise ValueError("Incorrect server ip")

        if not self.__server_port or self.__server_port <= 0:
            raise ValueError("Incorrect server port")

    def run(self) -> None:
        """Start the app instance

        Args:

        Returns:
            None
        """
        # Create a new flask app instance
        flask_app: Flask = Flask(__name__)

        # Register the default flask route
        # flask_app.route()

        # Start the flask app instance
        flask_app.run(
            host=self.__server_ip,
            port=self.__server_port,
            debug=False,
        )
