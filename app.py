from flask import Flask, render_template, request
app = Flask(__name__)

REGISTERS = []

CLASSES = ["Coding", "Music", "Martial Arts", "Yoga", "Biology"]


@app.route("/")
def home():
    return render_template("index.html", classes=CLASSES)


@app.route("/classes", methods=["POST"])
def classes():
    name = request.form.get("name")
    extra_class = request.form.get("class")
    if not name or not extra_class in CLASSES:
        return render_template("failure.html")
    reg = {}
    reg["name"] = name
    reg["class"] = extra_class
    REGISTERS.append(reg)
    return render_template("classes.html")


@app.route("/registers")
def registers():
    return render_template("registers.html", registers=REGISTERS)


if __name__ == "main":
    app.run()
