from flask import Flask, render_template
from flask_cors import CORS

from config import mcloud_base_url

app = Flask(__name__, template_folder='templates')

# enable  Cross Origin Resource Sharing for use by materials cloud
#TODO: restrict this at some point
CORS(app)

# needed for flask.flash
app.secret_key = 'Materials Cloud header template'

# Use this to change prefix on apache
#app.config['APPLICATION_ROOT'] = '/flask'

# Support also routes with trailing slashes
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template('header.html', mcloud_base_url=mcloud_base_url)

if __name__ == '__main__':
 app.run(debug=True)