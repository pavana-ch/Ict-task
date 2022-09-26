from flask import Flask,render_template,request,redirect
from flask import send_file
from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(f"/tts/{name}")
 
@app.route("/tts/<name>")
def perform_tts(name):
    tts = gTTS(name, lang='en')
    location = "./static/output.mp3"
    tts.save(location)
    return render_template("tts.html", fileloc=location)


  
if __name__ == '__main__':
   app.run(debug=True, port=8000)
