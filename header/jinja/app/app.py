from flask import Flask, render_template
from flask_cors import CORS

import config

app = Flask(__name__, template_folder='templates')

# enable  Cross Origin Resource Sharing for use by materials cloud
#TODO: restrict this at some point
CORS(app)

# Support also routes with trailing slashes
app.url_map.strict_slashes = False

@app.route('/')
def index():
    template_vars = { name: getattr(config, name) for name in dir(config) if not name.startswith('_') } 
    return render_template('header.html', **template_vars)

if __name__ == '__main__':
    app.run(debug=True)
