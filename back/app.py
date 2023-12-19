from flask import Flask , render_template , request
import json

app = Flask(__name__)
users= []






with open('login_data.json', 'r') as json_file:
    users = json.load(json_file)



@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/login', methods=['POST' , 'GET'])
def login():
    
    msg= 'Try again'
    if request.method == 'POST':
        userName = request.form.get('username')
        passWord = request.form.get('password')
        
        for user in users:
            
            if userName == user["username"] and passWord == user["password"]:
                return render_template('success.html')
        else:
            return render_template('login.html' , msg = msg)  
    return render_template('login.html')


@app.route('/signup' , methods = ['POST' , 'GET'])
def signup():
     if request.method == 'POST':
        newUsername = request.form.get('newUsername')
        newPassword = request.form.get('newPassword')

        newUser = {'username' : newUsername , 'password' : newPassword}

        users.append(newUser)
        print(users)

        with open('login_data.json', 'w') as json_file:
            json.dump(users , json_file)

        return render_template('success.html')
     return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)