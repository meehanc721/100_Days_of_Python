from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "codechad721@gmail.com"
PASSWORD = "suckalemon"

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()


app = Flask(__name__)

@app.route('/')
def start():
    return render_template("index.html", all_posts=posts)

@app.route('/index.html')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form["name"]
        email = request.form["email"]
        cell = request.form["cell"]
        message = request.form["message"]


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="codechad721@yahoo.com",
                msg=f"Subject: New User Message\n\nName: {name}\nEmail: {email}\nCell Number: {cell}\n\n{message}"
            )

        return render_template("contact.html", msg_sent=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)