from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AztecMatch backend is running"

@app.route("/register", methods=["POST"]) # this is the post request like how we access the email to see if its valid or not.
def post():
    data = request.get_json() 
    email = data["email"] #set the email to the data of the email
    
    if not email.endswith("@sdsu.edu"):
        return "Only SDSU emails allowed"
    else:
        return "Email verified!"

print("app.py started")

if __name__ == "__main__":
    print("starting flask server...")
    app.run(debug=True , port = 5001)



