from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkeyku2023"

# main_layout

@app.route('/')
def main_layout():
    return render_template('main_layout.html')


@app.route("/mainpage")
def mainpage():
    return render_template('main_page.html')


@app.route('/about')
def aboutku():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# parsing nilai interger
@app.route('/parsing/<int:nilaiku>')
def ayo_parsing(nilaiku):
    return "nilainya adalah : {} ".format(nilaiku)

# Parsing nilai string


@app.route('/parsing/<string:stringku>')
def ayo_string(stringku):
    return "nilainya adalah : {} ".format(stringku)

# parsing argument


@app.route('/parse_argument')
def parse_argument():
    data = request.args.get("nilai")
    return "parsing argumennya adalah {}".format(data)

# memparsing nilai dari url untuk mengeset nilai session


@app.route("/halaman/<int:nilai>")
def session_1(nilai):
    session["nilaiku"] = nilai
    return "berhasil mengeset nilai"


@app.route("/halaman/lihat")
def view_session_1():
    data = session["nilaiku"]
    return "nilai yang telah diset adalah = {}".format(data)

# redirect
@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for("aboutku"))

# login
@app.route('/login', methods=['POST','GET'])
def loginku():
    # jika tombol button diklik -> request POST
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'pass':
            session['email'] = email
            return redirect(url_for("sukses"))
        # jika salah email atau password
        else:
            return redirect(url_for("loginku"))
    return render_template("login.html")

# percobaan
@app.route("/yuki")
def yuki():
    return render_template('yuki.html') 
if __name__ == '__main__':
    app.run(debug=True)
