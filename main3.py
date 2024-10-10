from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
from Inter import main_encrypt,bit2str,integrity

import time
import hashlib
from gmssl.sm3 import sm3_hash
from subkey import get_Kn
from flask import session, redirect
from flask import url_for

from config import APP_STATIC_TXT

app = Flask(__name__)

# 设置文件上传保存路径
app.config['UPLOAD_FOLDER'] = 'static/upload/'
# MAX_CONTENT_LENGTH设置上传文件的大小，单位字节
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # q=0
    if(request.method == 'GET'):
        return render_template('index.html');
    else:
        f = request.files['file'];
        data = {}
        hashh = request.form['text']  # 后面这个name和前端的name保持一致
        passwd = request.form['password']
        fname = secure_filename(f.filename);
        ext = fname.rsplit('.')[-1];
        # 生成一个uuid作为文件名
        fileName = str(uuid.uuid4()) + "." + ext;
        # fileName = "output" +str(q)+ "." + ext;
        # q=q+1;
        # os.path.join拼接地址，上传地址，f.filename获取文件名
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        # f1 = open("static/upload/"+fileName, 'w', encoding='utf-8')
        # message=f1.read()
        # message=main_encrypt(message,"dddddddddd",0)
        # message=bit2str(message)
        with open(os.path.join(APP_STATIC_TXT, fileName)) as f1:
            s = f1.read()  # 读取前五个字节
            s = main_encrypt(s, passwd, int(hashh))
            # f1.write(s)
            f1.close()
        f2 = open("static/upload/" + fileName, 'w', encoding='utf-8')
        s = bit2str(s)
        fileHash = integrity(s, int(hashh))  # 获取文件hash
        f2.write("[ciphertext " + fileHash + "]\n")
        # f2.write(hashh + "\n")
        # f2.write(passwd + "\n")
        f2.write(s)
        f2.close()
        # qq=q-1;
        aaa_address="http://127.0.0.1:5000/download/"+fileName
        return render_template('index1.html',downloadAddress=aaa_address);
        # return "http://127.0.0.1:5000/download/"+fileName;

# 文件下载
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        path = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename));
        if path:
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
