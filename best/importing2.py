# Wrong: multiple libraries in one line
import sys, os

# Wrong: local imports before standard library
from my_project import utils
import math

# Wrong: unused aliases or unclear ones
import numpy as numpy_library   # "numpy" alias is "np"

# Wrong: wildcard imports 
from math import *

# Wrong: relative import 
from .utils import helpers
