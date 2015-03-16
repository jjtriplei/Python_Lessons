import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

# Do not modify
app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
# End Do not Modify


# Index of the site (ie: The first page that will show up when the site is visited.
@app.route('/')
def minecraft_index():
    return render_template('Craft.html')






# This route is setup to server static files (ie: Images, CSS, Video ... etc)
# Do not modify
@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

if __name__ == '__main__':
    app.run()
# End Do not modify