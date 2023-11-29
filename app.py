from flask import Flask, render_template, request

app = Flask(__name__, template_folder='static/html', static_folder='static')

@app.route('/')
def homepage():
    # 我的html路径为static\html\index.html

    return render_template('index.html')

if __name__ == '__main__':
    # BEGIN: ed8c6549bwf9
    app.run(port=80, host='101.42.151.208', ssl_context='adhoc')
    # END: ed8c6549bwf9
    app.run(port=80)
