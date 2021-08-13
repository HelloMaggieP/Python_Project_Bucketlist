from flask import Flask, render_template
#import from controllers 
app = Flask(__name__)

#blueprints

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)