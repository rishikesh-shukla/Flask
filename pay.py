import os
from datetime import datetime
from flask import Flask, render_template
import datetime
import paypal as pp 
 

app = Flask(__name__)
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
	return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
app.run(debug=True)
