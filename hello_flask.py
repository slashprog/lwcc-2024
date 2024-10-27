from flask import Flask, render_template
app = Flask("test-app")

@app.route("/")
def welcome():
    return "<h1>Welcome to Simple Web application!</h1>"

@app.route("/about")
def about():
    return "<h2>This is an about page</h2>"

@app.route("/time")
def print_time():
    from time import ctime
    return f"The time now is: {ctime()}"

@app.route("/status")
def show_status():
    from time import ctime
    return render_template("status.html", time=ctime(), title="Clock")

if __name__ == '__main__':
    app.run()

