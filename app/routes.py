from app import app

#home page
@app.route("/")
def home():
    return "<h1>MY BLOG!!!</h1>"

@app.route("/about")
def about():
    return "<h1>ABOUT ME!!!!!!!</h1>"

@app.route("/Messages")
def messages():
    return "<h1>YOU HAVE 0 MESSAGES IN YOUR INBOX!!!!!!!!!</h1>"

@app.route("/Friends")
def friends():
    return "<h1>YOU HAVE 0 FRIEND REQUESTS!!!!!!!</h1>"