from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def comment():
     user = {'username':'Harshita'}
     post = [ {'name':{'uname':'John'},{'comment':'Its a beauriful day'}]
             
     return render_template()
    
if __name__ == "__main__":
    app.run(debug=True)
