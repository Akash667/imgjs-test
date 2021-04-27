from flask import Flask,request
from flask_cors import CORS
import seamcarve2
# import seamcar as seamcarve2
import time
import base64
app = Flask(__name__)
CORS(app)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    # time.sleep(10)
   return "hello"


@app.route('/seam/',methods=['POST'])
def removeseam():

    request_data = request.get_json()

    imageURI = request_data["imgData"]

    seams = request_data["seams"]

    # print(seams)

    result = seamcarve2.reduce_seams(imageURI,seams)

    # f = open('image.txt','a')
    # f.write(result)
    return result


@app.route('/illuminate/',methods=['POST'])
def illuminate():

    request_data = request.get_json()

    imageURI = request_data["imgData"]
 
    encoded_data = imageURI

    if imageURI[:4] != "data":
        encoded_data = imageURI
    else:
        encoded_data = imageURI.split(',')[1]
        # pass
    
    with open("result.jpg",'wb') as f:
        f.write(base64.b64decode(encoded_data))


    return "success"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105,debug=True)