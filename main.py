from flask import Flask, request
from flask import render_template
import json
import anydbm
gdb = anydbm.open('./gdbm.dbm', 'c')
app = Flask(__name__)

@app.route("/")
def main():
  return "This is main"

@app.route("/node")
def node():
  return render_template('index.html')

@app.route("/push",methods=['POST'])
def push():
    content = request.json
    #print content
    #print content[0]
    if not gdb.get(str(content[0])):
      gdb[str(content[0])] = json.dumps([content[1:]])
    else: 
      buff = json.loads(gdb[str(content[0])])
      buff.append(content[1:])
      gdb[str(content[0])] = json.dumps(buff)
    
    print 'aaa', gdb[str(content[0])]
    return json.dumps("helloworld")

# retrun must be json
@app.route("/pullGPS",methods=['POST'])
def pullGPS():
    content = request.json
    key = '_'.join(content).encode('utf-8')
    print key
    #return json.dumps('some')
    if not gdb.get(key):
      return json.dumps([None])
    else: 
      return gdb[key]
    
import os
@app.route('/lib/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(os.path.join('lib', path))

if __name__ == "__main__":
  app.run(debug=True, host='192.168.15.10')
  gdb.close()
