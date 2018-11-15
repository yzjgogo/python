from flask import Flask,jsonify
from flask import request
from flask import make_response
from flask import abort

'''
diy function toDict used to convert obj to dict,then let the dict transfer into jsonify(dict),so we can convert obj to json.
''' 
class Student:
	def __init__(self, name, age, pen):
		self.name = name
		self.age = age
		self.pen = pen
	def toDict(self):
		stuDict = self.__dict__
		kvList = stuDict.items()
		for k,v in kvList:
			if isinstance(v,Pen):
				stuDict[k] = v.__dict__
		return stuDict			

class Pen:
	def __init__(self, color, size):
		self.color = color
		self.size = size
		
 









'''
使用ngrok或pagekite让你的本地Flask程序外网可访问
主要通过监听局域网服务器端口，实现外部访问
http://greyli.com/use-ngrok-to-expose-your-local-application/
http://pagekite.net/  官网会识别你的系统显示使用方法。
推荐pagekite,因为对于免费用户ngrok的链接是动态的，而pagekite可以自定义
'''

app = Flask(__name__)

'''
request.args --> get request have no requestBody,just contain get request's paras.
request.form --> post request's requestBody,jsut contain post request's paras.
request.values --> contain all get request and post request's paras.

request.headers --> request header.
request.url
request.base_url,if get type,then no paras.
request.host
request.method


rep = make_response('response_body',response_code,new_added_head_dict)  --> the second para can ignore,the third para can ignore too,you can add response header in there.
eg:make_response("response_body",200,{'Name':'Jack','Age':'30'})

rep.mimetype = 'text/plain'
rep.headers['head_name'] = 'head_value' --> reset head k-v or add head k-v
rep.status_code = 404 --> set response code.


'''
@app.route('/', methods=['GET', 'POST'])
def home():
	'''
return response way 1:
	#return response body , response code,new_added_head_dict.
	#return "request result",400,{'Name':'Jack','Age':'30'}
	#return "result ok"  if response is 200,you can omit it. equals "return 'result ok',200"
	'''

	'''
return response way 2:

	rep = make_response('HelloKitty',400,{'name':'jack','age':'20'})
	rep.mimetype = 'text/plain'
	rep.headers['Date'] = 'Mon, 31 Oct 2018 09:09:09 GMT'
	rep.headers['YinMiao'] = 'Home'
	rep.status_code = 440
	return rep
	'''

	'''
return response way 3:
	abort(404)
	return 'result'
	
	the program stop run at 'abort',and throw http status code,attention is just can throw http official status, the code afer 'abort' will never run.eg:"return 'result'" will never run.
	
	you can through errorhandler(status_code) catch the error,then the client will never get the status_code.the client will get response through errorhandler(status_code).	
	'''

	'''
return response way4:json
	use jsonify will auto modify response head's 'Content-Type' as 'application/json'
	'''
	mydict = {'name':'Jack','age':'18','home':{'addr':'Anhui','Num':1202}}
	mydict2 = {'name':'Lulu','age':'28','home':{'addr':'HeNan','Num':1404}}
	mydict3 = {"errorCode": 1000,"errorMessage": "操作成功","data": [{"functionId": 61,"functionName": "我的欢迎语","groupId": 1100},{"functionId": 2,"functionName": "首页添加病人","groupId": 200}]}
	jlist = [mydict,mydict2]
	
	pen = Pen('White',4.5)
	stu = Student('ZhangSan',65,pen)
	#return jsonify(jlist) #jsonify can convert list to json
	#return jsonify(mydict3) # jsonify can convert dict to json
	return jsonify(stu.toDict())#stu.toDict() is a dict

'''
	return ('Flask_get:\nFlask-request.url:%s\n'+
'Flask-request.method：%s\n'+
'Flask-request.args.to_dict()：%s\n'+
'Flask-request.values.to_dict()：%s\n'+
'Flask-request.data:%s\n'+
'Flask-request.headers:%s\n'+
'Flask-request.form:%s\n'+
'Flask-request.base_url:%s\n'+
'Flask-request.host:%s\n')%(request.url,request.method,str(request.args.to_dict()),str(request.values.to_dict()),str(request.data),str(request.headers),str(request.form.to_dict()),request.base_url,request.host)
'''

'''
if errorhandler intercept a status_code,it means that the errorhandler will rehandle the request,the errorhandler will return the final response body,response code,response header to client.
'''
@app.errorhandler(404)
def page_not_find(e):
	return 'the fianl response given to client',888,{'Name':'Jack','Age':'30'}

@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''



@app.route('/signin', methods=['POST'])
def signin():
	#需要从request对象读取表单内容：
#	if request.form['username']=='admin' and request.form['password']=='password':
#		return '<h3>Hello, admin!</h3>'
#	return '<h3>Bad username or password.</h3>'

	#return 'Flask-request.form:%s'%request.form.to_dict()
	return ('Flask_post:\nFlask-request.url:%s\n'+
'Flask-request.method：%s\n'+
'Flask-request.args.to_dict()：%s\n'+
'Flask-request.values.to_dict()：%s\n'+
'Flask-request.data:%s\n'+
'Flask-request.headers:%s\n'+
'Flask-request.form:%s\n'+
'Flask-request.base_url:%s\n'+
'Flask-request.host:%s\n')%(request.url,request.method,str(request.args.to_dict()),str(request.values.to_dict()),str(request.data),str(request.headers),str(request.form.to_dict()),request.base_url,request.host)



if __name__ == '__main__':
	#192.168.190.134 is this computer's ip,through  this we can visit the flask server on out internet.attention is you should close the firewall of the computer.
	#app.run(host='192.168.190.134', port=8000,debug=True)
	app.run()#default port is 5000

