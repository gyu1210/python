from flask import Flask, render_template, request, redirect
import random

## Flask 클래스 생성
##__name__: 파일의 이름
app = Flask(__name__)

# @ : 네비게이터 : 바로 아래에 있는 함수 실행
# route(주소) : 주소에 요청을 하면 아래의 함수를 실행
# @app.route('/'): 127.0.0.1:5000/ 로 요청하는 경우 아래의 함수를 실행
@app.route('/')
def index():
    return 'Hello World'

# 127.0.0.1 = localhost
# 127.0.0.1:5000/main 이라는 주소로 요청을 하는 경우 아래의 함수를 생성
#  5000: python 에서 연것 5500:live server에서 연것

@app.route('/main')
def main():
    return render_template('main.html')

# 명령프롬프트 열어서 수정된것 다시 실행시킬때 Ctrl + 화살표 위 + enter

# 새로운 api 생성
# localhost:5000/login 주소로 생성
@app. route("/login")
def login():
    # main.html에서 데이터를 보내는 형식
    # {id: xxxx, pass:xxxx}
     _id = request.args.get("id")
     _pass = request.args.get("pass") 
     print(_id, _pass)
     if (_id == 'test') & (_pass == '1234'):
         return render_template('second.html')
     else:
         # 로그인 실패시  localhost:5000/main으로 이동: redirect
         return redirect("/main")
         return(_id, _pass)
     
# localhost:5000/data api 생성
# post형태로 요청시
@app.route('/data', methods=['post'])
def data():
    _use = request.form['use']
    _list = ['바위', '가위', '보']
    choice_list =random.choice(_list)
    
    # 무승부인경우               #_use :유저  #_choice_list :컴퓨터
    if _use == choice_list:
        return '무승부'
    
    elif _use == '바위':
        if choice_list == '가위':
            result = '승'
        else:
            result = '패'

    elif _use == '가위':
        if choice_list == '보':
            result = '승'
        else:
            result = '패'

# elif 를 써도됨 :'보' ,하지만 남은것은 '보' 밖에 없기 때문에 굳이안써됨
    else:
        if choice_list == '바위':
            result = '승'
        else:
            result = '패'
    return render_template('result.html', res = result)


app.run()
# app.run(port.8080) 내가 코드가 클리지 않았는데 결과가 안나오면 포트번호바꾸기