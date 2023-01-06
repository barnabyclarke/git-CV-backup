import smtplib

from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "seoifnoseinfiosefhosue"
Bootstrap(app)


PASSWORD = "qocdlolkqxdyivsu"
MY_GMAIL = "hlangmore420@gmail.com"
MY_YAHOO_MAIL = "barnabyclarke@yahoo.co.uk"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=MY_YAHOO_MAIL,
                msg=f"Subject: New Message from GitHub Contact\n\n"
                    f"FROM:  {request.form['name']}\n"
                    f"MESSAGE:  {request.form['message']}\n\n"
                    f"CONTACT DETAILS\n"
                    f"EMAIL:  {request.form['email']}\n"
                    f"PHONE:  {request.form['phone-number']}"
            )
        return render_template("email_confirm.html"), {"Refresh": f"3 url={url_for('home')}"}
    return render_template("contact.html")


@app.route('/cv/')
def cv():
    return render_template("cv.html")


if __name__ == "__main__":
    # from elsa import cli
    # cli(app, base_url='https://barnabyclarke.com')
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

# TODO: look at setting info as environment variables before github run
# TODO: maybe make blog private on github
