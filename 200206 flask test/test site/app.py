from flask import Flask, render_template, request, jsonify
#from werkzeug import secure_filename
#import keras
import json
import pymysql
app = Flask(__name__)


db = pymysql.connect(host="127.0.0.1", user="ad",passwd="1234", db='tests', port=3306)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html')


#업로드 HTML 렌더링
@app.route('/container')
def container():
    cursor = db.cursor()
    # 데이터베이스에서 사용자 이미지 가져오기
    item_sql = "select * from USER_ITEM"
    cursor.execute(item_sql)
    rows=cursor.fetchall() 
    row_headers=[x[0] for x in cursor.description]
    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    #print(json_data)
    # json_return=json.dumps(json_data[0]) 
    # print(json_return)
    
    cursor.close()
    return render_template('container.html',json_data = json_data)





#파일 업로드 처리
@app.route('/image', methods = ['GET', 'POST'])
def image():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        print(data[0])
        for i in data:
            i = json.loads(i)
            item_name = i['item']
            x = i['x']
            y = i['y']
            z = i['z']
            cursor = db.cursor()
            item_sql = f"UPDATE USER_ITEM SET X_ITEM = {x}, Y_ITEM = {y}, Z_ITEM = {z} where ITEMID = '{item_name}'"
             
            cursor.execute(item_sql)
            cursor.fetchall() 
            
            
            

    return jsonify(data)
        # return render_template('/container.html')



#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(type(f.filename))
        #저장할 경로 + 파일명
        f.save('temp/'+ 'uploaded_img' + '.' + f.filename.split('.')[-1]) # secure_filename(f.filename)
        return render_template('/index.html')



@app.route('/analysis')
def analysis():
    return 0

@app.route('/waiting')
def wait():
    return 0





 
if __name__ == '__main__':
    #서버 실행
    app.run(debug = True,host='0.0.0.0')