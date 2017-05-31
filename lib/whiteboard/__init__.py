from flask import Flask
import os.path

project_base_dir = os.path.normpath( os.path.join(__file__, "..", "..", ".." ) )
template_folder = os.path.join(project_base_dir, "templates")
static_folder = os.path.join(project_base_dir, "static")

app = Flask(__name__, template_folder=template_folder, 
                      static_folder=static_folder)
app.secret_key = 'c315a37bbd3c49da980bf4f70c450e53c1eb4ed6'
