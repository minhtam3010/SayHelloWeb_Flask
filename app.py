from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "leminhtam"

@app.route("/hello")
def index():
    flash("Mời Bạn Điền Tên Vào Đây hihi")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Xin chào " + str(request.form['name_input']) + ". Chào mừng bạn đến với lớp Python NC")
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()