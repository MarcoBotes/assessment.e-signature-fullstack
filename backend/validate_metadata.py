"""
Simple script iterates through the save directory and just prints the output for validating the results
"""
import os
from PyPDF2 import PdfReader

from Utilities.config import Constants

for file in os.listdir(Constants.directory):
    reader = PdfReader(os.path.join(Constants.directory, file))
    print(file, reader.metadata)