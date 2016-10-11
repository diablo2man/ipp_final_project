import os
from flask import Flask, render_template, request
import giphypop
import requests


app = Flask(__name__)

@app.route("/")
def index():
	ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	try:
		ip_location = requests.get('https://ipapi.co/'+ip+'/city/').text
	except:
		ip_location = "Mars"

	if ip_location == "Undefined":
		ip_location = "Mars"
	return render_template("index.html", ip_location=ip_location)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/results")
def results():
	keyword = request.args.get('keyword', '')
	g = giphypop.Giphy()
	error_msg = ""
	if keyword == '':
		gif_list = []
		error_msg = "No keywords entered"
	else:
		gif_list = g.search_list(keyword)
	return render_template("results.html", gif_list = gif_list, error_msg=error_msg)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

