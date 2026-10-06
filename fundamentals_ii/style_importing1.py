# Standard library imports come first
import os
import sys

# Then third-party imports
import requests
import numpy as np

# Finally local application imports
from my_project import utils
from my_project.models import User

# Grouped imports are okay if they’re from the same package
from collections import defaultdict, namedtuple
