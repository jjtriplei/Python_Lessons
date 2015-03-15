from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Josh is a douche! That should offend less people'

@app.route('/Craft/') # 
def Cool_shit():
    return render_template('Craft.html')



if __name__ == '__main__':
    app.run()