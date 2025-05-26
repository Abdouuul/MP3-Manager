from abc import ABC, abstractmethod
from flask import Blueprint

class BaseController(ABC):
    controller_bp = Blueprint('controller_bp', __name__)