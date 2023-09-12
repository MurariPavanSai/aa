from flask import Flask, render_template, request
import sklearn

app = Flask(__name__)

import pickle

model = pickle.load(
    open(
        "C:\\Users\\pavan\\Machine learning projects\\Insta reach analysis\\Vs Flask\\codey.pkl",
        "rb",
    )
)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/services.html")
def services():
    return render_template("services.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/guest", methods=["POST", "GET"])
def guest():
    fe = request.form["explore"]
    fh = request.form["home"]
    fhas = request.form["hashtags"]
    oth = request.form["other"]
    l = request.form["likes"]
    s = request.form["saves"]
    c = request.form["comments"]
    sh = request.form["shares"]
    pv = request.form["profile_visits"]
    f = request.form["follows"]
    data = [[fe, fh, fhas, oth, l, s, c, sh, pv, f]]
    data = [
        [
            float(fe),
            float(fh),
            float(fhas),
            float(oth),
            float(l),
            float(s),
            float(c),
            float(sh),
            float(pv),
            float(f),
        ]
    ]
    pre = model.predict(data)
    kick = {
        "From explore": fe,
        "from home": fh,
        "from hastag": fhas,
        "others": oth,
        "likes": l,
        "saves": s,
        "comments": c,
        "shares": sh,
        "profile_visits": pv,
        "follows": f,
        "Impressions": int(pre),
    }
    return render_template("service-details.html", y=kick)


if __name__ == "__main__":
    app.run(debug=True)
