from flask import Flask,request
from flask_cors import CORS
import seamcarve2

app = Flask(__name__)
CORS(app)



@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/seam/',methods=['POST'])
def removeseam():
    request_data = request.get_json()
    imageURI = request_data["imgData"]
    seams = request_data["seams"]
    print(seams)

    result = seamcarve2.reduce_seams(imageURI,seams)

    # f = open('image.txt','a')
    # f.write(result)
    return result



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105,debug=True)