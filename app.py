from flask import Flask, render_template

app = Flask(__name__)

app.name = "Flask Pertama saya sebagai mahasiswa BISNIS DIGITAL (Variabel Global)"
user = {
        "nama": "Nadyah",
        "age": 18,
        "hobby": "nonton"
    }

#1 App Route Hello World
@app.route("/")
def hello_world():
    return "<p>Hello, World!  I am a Python Flask App, Selamat Pagi..</p>"

#2 App Route Aplikasi ke halaman pertama 
@app.route('/about/')
def about():
    return "<p> Ini Flask Pertama saya sebagai mahasiswa BISNIS DIGITAL</p>"

#3 App Route Halaman HTML FlaskLand
@app.route("/lembar/flaskland/")
def lucu():
    return render_template("flaskland.html")


#4 App Route Halaman HTML FlaskLand_2 Full menghubungkan ke static CSS
@app.route("/lembar/flaskland/full/")
def flaskland_halaman():
    return render_template("flaskland_2.html")


#5 App Route Dinamis
@app.route("/lembar/flaskland/<string:nama>")
def get_name(nama):
    return f"Halaman ini adalah {app.name}".format(nama)



@app.route("/lembar/flasklands/")
def get_name2():
    return f"Nama saya adalah {user}"


#6 App Route Variabel Global
@app.route("/global/")
def global_name():
    return f"nama aplikasi {app.name}"


#7 App Route Variabel Lokal
@app.route("/lokal/")
def lokal_nama():
    user = {
        "nama": "Nadyah",
        "age": 18,
        "hobby": "nonton"
    }
    return render_template("lokal.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)

