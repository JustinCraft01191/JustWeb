from flask import Flask, render_template, request, redirect, url_for
from articles_local_updater import Updater
from send_email import Send_Email

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html", palm_prev = Updater().palm_preview_update(), coco_prev = Updater().coconut_preview_update())

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/articles')
def articles():
    if len(Updater().palm_articles()) > 10:
        palm_quantity = 10
    else:
        palm_quantity = len(Updater().palm_articles())
    if len(Updater().coconut_articles()) > 10:
        coco_quantity = 10
    else:
        coco_quantity = len(Updater().coconut_articles())
    return render_template("articles.html", palm_articles = Updater().palm_articles(), coco_articles = Updater().coconut_articles(), palm_quantity=palm_quantity, coco_quantity=coco_quantity)

@app.route('/contact_us/<status>')
def contact_us(status):
    return render_template("contact_us.html", msg_sent=int(status))

@app.route('/form_entry', methods=["POST", "GET"])
def form_entry():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        msg = f"Name : {name}\nEmail : {email}\nMessege : {message}"
        email = Send_Email(subject=subject, msg=msg)
        print(msg)
        status = email.Send_Message()
        return redirect(url_for('contact_us', status=status))



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

