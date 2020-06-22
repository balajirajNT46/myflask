from flask import request,Blueprint,jsonify
from core.auth.model import UserModel

app = Blueprint('view_auth',__name__)


@app.route("/user/mobile", methods=['POST']) 
def mobile():
	print(">> API <<")
	r = request.json
	data = [ 
			{ 'mobile':r.get('mobile') }
		   ]
	new_dict={item['mobile'] for item in data}	
	u = UserModel()
	existingdata = u.checkmobile(new_dict)	
	if existingdata == []:
		temp = u.create(data)
		return jsonify(temp)
	else:
		return jsonify(existingdata)
	return "success"


@app.route("/user/create", methods=['POST'])
def create():
	print(">> API <<")
	r = request.json
	data = [
				{'username':r.get('username'),
				'email':r.get('email'),
				'mobile':r.get('mobile'),
				'city':r.get('city'),
				'state':r.get('state'),
				'affiliation':r.get('affiliation')}
		   ]

	print(data)
	existingdata = [
					{'mobile': r.get('mobile')}
		   ]		   
	new_dict={item['mobile'] for item in existingdata}	
	u = UserModel()
	temp1=u.check(new_dict)	
	if temp1 == []:
		temp = u.create(data)				
		return jsonify(temp)
	else:
		return jsonify(temp1)
	return "success"
	

	