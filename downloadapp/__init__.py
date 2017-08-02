from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    sdks = [{"name": "IA32 SDK",
             "fn": "lsb-sdk-5.0.0-3.ia32.tar.gz",
             "url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/sdk/lsb-sdk-5.0.0-3.ia32.tar.gz"}]
    appkits = [{"name": "IA32 App Checker",
                "pkg_fn": "lsb-app-checker-5.0.0-3.ia32.tar.gz",
                "pkg_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ia32.tar.gz",
                "local_fn": "lsb-app-checker-local-5.0.0-3.ia32.tar.gz",
                "local_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ia32.tar.gz"}]
    dtks = [{"name": "IA32 Distribution Test Kit",
             "mgr_fn": "lsb-dist-testkit-manager-5.0.0-2.ia32.tar.gz",
             "mgr_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/dist-testkit/lsb-dist-testkit-manager-5.0.0-2.ia32.tar.gz",
             "full_fn": "lsb-dist-testkit-5.0.0-2.ia32.tar.gz",
             "full_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/dist-testkit/lsb-dist-testkit-5.0.0-2.ia32.tar.gz"}]

    return render_template("index.html",
                           spec_url="http://refspecs.linuxbase.org/lsb.shtml",
                           sdks=sdks,
                           appkits=appkits,
                           dtks=dtks)
