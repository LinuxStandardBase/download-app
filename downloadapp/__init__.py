from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from downloadapp import bundle_info

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html",
                           spec_url="http://refspecs.linuxbase.org/lsb.shtml",
                           sdks=bundle_info.get_sdks(),
                           appkits=bundle_info.get_appkits(),
                           dtks=bundle_info.get_dtks())
