from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<name>")
def name(name):
    image = name.lower() + ".png"  # Use lowercase for image filename
    display_name = name.capitalize()  # Capitalize for display
    return render_template('name.html', name=display_name, image=image)

@app.route("/abc")
def abc():
    return render_template("abc.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)