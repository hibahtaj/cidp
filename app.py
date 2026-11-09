import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def registration():
    return render_template('reg.html')

@app.post('/submit')
def submit():
    name = request.form.get('name', '').strip()
    password = request.form.get('password', '')
    if not name or not password:
        return render_template('reg.html', error='Name and password are required.'), 400
    return render_template('succ.html', name=name)

@app.get('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5055')), debug=False)
