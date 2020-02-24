from flask_pymongo import PyMongo
from flask import Flask,request
import os
import monog
from bson import ObjectId
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/payment"
mongo = PyMongo(app)
User_id="Rishi"

@app.route("/")
def home_page():
	user_id = request.form.get("user_id") #getting useer id from the cart 
	monog.insert_data( { User_id: user_id })# finding the user id in userid
	online_users = monog.get_single_data(ObjectId({user_id:user_id}))
	if (online_users == True):
		port = int(os.environ.get("PORT", 5000))
		app.run(host='127.0.0.1', port=port)
		return redirect(url_for("pay"))
	return render_template("pay", online_users=online_users)

#app = Flask(__name__)
@app.route("/pay", methods=["GET", "POST"])
def payment():
	if request.method == "POST":
		user_id = request.form.get("user_id")
		product_id = request.form.get("product_id")
		total_amout	=request.form.get("total_amout")
	if userid in user_id and productid[product_id][1] == product_id:
		session[""] = pp
		app.permanent_session_lifetime = datetime.timedelta(hours = 0.166667)
		return redirect(url_for("pay"))
	else:
		os.system('python errors.py')
	return render_template('payment.html')


@app.route("/pay/")
def about():
	return render_template('pay.py')


@app.route("/contact")
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000, debug=True)