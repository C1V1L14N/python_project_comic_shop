
from flask import Flask, render_template
from controllers.comics_controller import comic_blueprint
from controllers.publishers_controller import publishers_blueprint

app = Flask(__name__)
app.register_blueprint(comic_blueprint)
app.register_blueprint(publishers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)