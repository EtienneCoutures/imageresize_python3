import requests
from flask import Flask, request, send_file, make_response 
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/resize", methods=['POST'])
def resize(scale=0):
    try:
        scale = float(request.args.get('scale', scale))
    except:
        return (make_response("", 400))
    if (scale < 0):
        return (make_response("", 400))
    data = request.get_data()
    try:
        img = Image.open(BytesIO(data))
    except:
        return (make_response("", 400))
    size = img.size
    format = str(img.format).lower()
    img = img.resize((int(size[0] * scale), int(size[1] * scale)))
    img.save("name." + format, format=format)
    final= "name." + format
    return send_file("name." + format, attachment_filename=final, as_attachment=True, mimetype='application/binary')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)#, debug=True)

