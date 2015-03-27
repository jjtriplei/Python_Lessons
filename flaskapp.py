import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
import os

# Do not modify
app = Flask(__name__)
# End Do not Modify


# Index of the site (ie: The first page that will show up when the site is visited.
@app.route('/')
def minecraft_index():
    return render_template('Craft.html')

@app.route('/admin')
def admin_main():
    # Example of how to pass data to a template and loop over it
    return render_template('admin.html', names=["Josh", "Joe", "Scruffy"])

@app.route('/boogerballs')
def task_5():
    return render_template('task5.html')



@app.route('/find', methods=['POST'])
def find_overviewer():
    # Code here to start find overviewer process

    path = "/usr/bin/"
    dirs = os.listdir(path)

    if "overviewer.py" in dirs:
        print ("Yes")
    else:
       print ("No")

@app.route('/process', methods=["POST"])
def start_process():
    # Code here to start overviewer process
    print "Yup"



# This route is setup to serve static files (ie: Images, CSS, Video ... etc)
# Do not modify
@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

if __name__ == '__main__':
    app.run()
# End Do not modify