from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello_world():
	return "Hello from git + docker + jenkins"


