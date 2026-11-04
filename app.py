import os, uuid
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=20*1024*1024
UPLOAD=os.path.join(os.path.dirname(__file__),"uploads")
os.makedirs(UPLOAD,exist_ok=True)
ALLOWED={"txt","md","pdf","png","jpg","jpeg","webp","py","html","css","js","json","zip"}
@app.get("/")
def home(): return render_template("index.html")
@app.get("/api/status")
def status(): return jsonify({"name":"MADARA AI Studio","status":"online","ai_configured":bool(os.getenv("AI_API_KEY"))})
@app.post("/api/upload")
def upload():
 f=request.files.get("file")
 if not f or not f.filename: return jsonify(error="Choose a file"),400
 name=secure_filename(f.filename)
 if name.rsplit(".",1)[-1].lower() not in ALLOWED: return jsonify(error="Unsupported file type"),400
 saved=uuid.uuid4().hex[:10]+"_"+name
 f.save(os.path.join(UPLOAD,saved))
 return jsonify(name=name,saved_as=saved,size=os.path.getsize(os.path.join(UPLOAD,saved)))
@app.get("/uploads/<path:name>")
def download(name): return send_from_directory(UPLOAD,name,as_attachment=True)
if __name__=="__main__": app.run(host="0.0.0.0",port=int(os.getenv("PORT",5000)))
