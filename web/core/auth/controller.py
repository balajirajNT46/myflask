from flask import render_template, request, redirect, url_for, Blueprint,json
import requests

app = Blueprint('view_auth', __name__)


@app.route('/auth/welcome', methods=['GET']) 
def get_mobile():
	return render_template('welcome.html')

@app.route('/auth/welcome', methods=['POST'])
def post_mobile():	
	mobile		= request.form.get('mobile')

	URL = 'http://localhost:5001/user/mobile'
	data = { "mobile": mobile }
	print(">> DATA <<")
	print(data)
	headers = {'Content-Type': "application/json",}	
	response = requests.request("POST",URL, data=json.dumps(data), headers=headers)     	
	user_id = json.loads(response.text)	
	return redirect(url_for("view_auth.get_create",data=data,user_id=user_id))	

@app.route('/auth/create/<user_id>', methods=['GET']) 
def get_create(user_id):
	return render_template('register.html',user_id=user_id)


@app.route('/auth/profile/<data>', methods=['GET'])
def get_profile(data):
	username = request.args.get('username')
	user_id = request.args.get("user_id")	
	print(user_id)
	return render_template('profile.html',user_id=user_id)

@app.route('/auth/postprofile/<user_id>', methods=['POST'])
def post_profile(user_id):
	user_id	= user_id
	file	= request.files.get('profile_pic')
	print(file)
	path 	= '/static/fileupload/' + user_id
	file.save(path.filename)
	Success = 'Success'
	return redirect(url_for("view_auth.get_profile",Success=Success))

@app.route('/auth/create', methods=['POST'])
def post_create():	
	username	= request.form.get('username')
	email		= request.form.get('email')
	mobile		= request.form.get('mobile')
	city		= request.form.get('city')
	state		= request.form.get('state')
	affiliation	= request.form.get('affiliation') 
	
	URL = 'http://localhost:5001/user/create'
	data = { "username": username, "email": email, "mobile": mobile, "city": city, "state": state, "affiliation": affiliation }
	print(">> DATA <<")
	print(data)
	headers = {'Content-Type': "application/json",}	
	response = requests.request("POST",URL, data=json.dumps(data), headers=headers)     	
	data = json.loads(response.text)	
	return redirect(url_for("view_auth.get_profile",data=data))		

	

# @app.route('/auth/create', methods=['POST'])
# def post_create():	
# 	username	= request.form.get('username')
# 	email		= request.form.get('email')
# 	mobile		= request.form.get('mobile')
# 	city		= request.form.get('city')
# 	state		= request.form.get('state')
# 	affiliation	= request.form.get('affiliation') 
	
# 	URL = 'http://localhost:5001/user/create'
# 	data = { "username": username, "email": email, "mobile": mobile, "city": city, "state": state, "affiliation": affiliation }
# 	print(data)
# 	headers = {'Content-Type': "application/json",}	
# 	response = requests.request("POST",URL, data=json.dumps(data), headers=headers)     
# 	#print(response)
# 	users = json.loads(response.text)
# 	for user in users:
# 		id =str(user['user_id']) 
# 		user_mobile=str(user['mobile'])
# 	if user_mobile == request.form.get('mobile'):			
# 		return redirect(url_for("view_auth.get_profile",data=data,id=id))	
# 	else:
# 		return redirect(url_for("view_auth.get_create",response=response.text))
# 	return response.text