from flask import Flask, render_template, request, json, jsonify
from fl1 import read_file, write_file
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route("/about")
def getAbout():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template('contact.html', phone = 87654321)

@app.route("/params")
def params():
  return request.args

@app.route("/post_req" , methods=['POST'])
def post_req():
  return request.args

@app.route("/read_file")
def read_from_file():
  content = read_file()
  return content

@app.route("/write_file", methods=['POST'])
def write_to_file():
  if request.content_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"Add line {contentJSON['data']} to file"
  else:
    return f"Invalid request {request.content_type} not allowed"

@app.route('/file', methods = ['GET', 'POST'])
def filework():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Invalid request{request.method} not allowed"

@app.route('/json')
def json_get():
  list = []
  list.append('value1')
  list.append('value2')
  list.append('value3')
  return jsonify({'data': list})

  
if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000, debug=True)