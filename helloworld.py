from flask import Flask, render_template
import datetime
import http.client
import json
import os


app = Flask(__name__, template_folder='templates', static_folder='staticfiles')

@app.route('/ciel')
def ciel():
    return render_template('ciel.html')

@app.route('/snir')
def snir():
    connexion = http.client.HTTPSConnection('api.openweathermap.org')
    connexion.request("GET", "/data/2.5/weather?lat=" + str(48.3)+"&lon="+ str(4.08)+ "&APPID="+os.environ['CLEAPI_OWM']+"&mode=json&units=metric&lang=fr")
    rep = connexion.getresponse()
    rep_str=rep.read()
    jsonDico = json.loads(rep_str.decode('utf-8'))
    return render_template('snir.html',utc_dt=str(jsonDico["main"]["temp"]))

@app.route('/etudes-sup')
def etudes_sup():
    return render_template('etudes.html')

if __name__ == '__main__':
    app.run(debug=True)