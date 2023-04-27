import pytest
import json
import sys, os, inspect
from src.app import app

from pprint import pprint

cmd_folder = os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../.."))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


@pytest.mark.unittest
class TestUnitPy:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass