from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='staticfiles')

@app.route('/ciel')
def ciel():
    return render_template('ciel.html')

@app.route('/snir')
def snir():
    return render_template('snir.html')

@app.route('/etudes-sup')
def etudes_sup():
    return render_template('etudes.html')

if __name__ == '__main__':
    app.run(debug=True)