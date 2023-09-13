from flask import Flask,render_template,request

app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template('home.html')

#about page
@app.route("/about")
def about():
    return render_template('about.html')

#gallery page
@app.route("/contact")
def contact():
    return render_template('contact.html')

#form
@app.route("/form", methods=['get','post'])
def form():
    if request.method=='GET':
         return render_template('home.html')
    else:
        math = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average = (math+science+history)/3

    return render_template('home.html',score=average)


if __name__ == "__main__":
    app.run(debug=True)








