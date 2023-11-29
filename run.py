from flask import Flask, render_template, request

app = Flask(__name__, template_folder='static/html', static_folder='static')

@app.route('/')
def homepage():
    # 我的html路径为static\html\index.html

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
