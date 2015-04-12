
from flask import Flask
import time
app = Flask(__name__)

dict_devices=dict()
#def status(device_id):
#	return dict_devices[device_id]
list_current_link=[]
list_link=["https://45.33.89.37:8443/share/svtZz","https://s3.amazonaws.com/ribytests3/google.pdf","TRUE"]

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/ping/<string:device_id>",methods=['GET', 'POST'])
def register(device_id):
	if device_id in dict_devices:
		dict_devices[device_id]=time.time()
		print dict_devices[device_id]
		return device_id+" added to list"+str(dict_devices[device_id])
	else:
		dict_devices[device_id]=time.time()
		return device_id+"added"
	print dict_devices

@app.route("/update/<string:uop>",methods=['GET', 'POST'])
def update(uop):
	list_current_link.append(uop)
	return "TRUE"
'''def route_machine():
        m=0
        d_l=None
        for d in dict_devices:
                if dict_devices[d]>m:
                        m=dict_devices[d]
                        d_l=d
        return d_l
'''
@app.route("/status/<string:device_id>",methods=['GET', 'POST'])
def status(device_id):
#	if list_current_link==None:
	if device_id==route_machine():
		return "Good"#,None
	else:
		return "Bad"#,None
#	else:
#		if device_id==route_machine():
#			return "Good",str(list_current_link.pop())
#		else:
#			return "Bad",None
@app.route("/getlaststate",methods=['GET', 'POST'])
def get_last_state():
	return list_current_link.pop()
def route_machine():
        m=0
        d_l=None
        for d in dict_devices:
                if dict_devices[d]>m:
                        m=dict_devices[d]
                        d_l=d
        return d_l

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

