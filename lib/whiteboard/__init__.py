from flask import Flask
import os.path

template_folder = os.path.normpath( os.path.join(__file__, "..", "..", "..", "templates") )

app = Flask(__name__, template_folder=template_folder)
