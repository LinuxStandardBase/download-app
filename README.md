# LSB Download App

This app serves the LSB download page.  It's needed so that new
releases are automatically picked up without any more complication to
the release process than we already have.

The app is a Flask app, written in Python, and using Bootstrap for its
look and feel.  It's really nothing special; one runs this app along
with a copy of the "bundles" as served by the LSB project in the
"bundles" directory of the FTP site.  It then serves a download page
with the appropriate links and other info included.

Pull requests are welcome.
