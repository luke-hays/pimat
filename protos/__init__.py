# Make polynomial_pb2 available at package level
from . import polynomial_pb2
import sys

# Add the protos directory to sys.path so the generated files can find each other
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
