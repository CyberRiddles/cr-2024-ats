"""oss.core.models.base.app"""

# Imports
from abc import ABC, abstractmethod


class BaseApp(ABC):
    """The base class for an app."""

    @abstractmethod
    def __init__(self, server_ip: str, server_port: int) -> None:
        """Initializes an BaseApp class instance.

        Args:
            server_ip (str): The ip the server is hosted on.
            server_port (int): The port the server listens on.
        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def check_parameters(self) -> None:
        """Check the run parameters

        Check the parameters the run function will use to start the BaseApp.

        Args:

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        """Starts the BaseApp implementation.

        Args:

        Returns:
            None
        """
        raise NotImplementedError
