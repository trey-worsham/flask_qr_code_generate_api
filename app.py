#apt install pip
#pip install flask
#pip install pyqrcode
#pip install pypng
from flask import Flask, request, make_response, send_file
import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime

app = Flask(__name__)

@app.route('/generate_qr_code', methods=['GET','POST'])
def generate_qr_code():    
 if request.method == 'GET':
    #get the text for the qr_code
    data = request.get_json()
    word = data["url"]

    #make the qr_code
    string = pyqrcode.create(word)

    #get time and date in string
    now = datetime.now()
    date_time = now.strftime("%m#%d#%Y#%H#%M#%S")

    #make the file name for the qr_code
    qr_code_file_name = date_time +"_qr_code.svg"
    #write the qr_code to disk
    string.svg(qr_code_file_name, scale = 8)

    #send the qr_code to the user
    return send_file(qr_code_file_name, mimetype='image/svg+xml')

app.run(host='0.0.0.0', port=81)

