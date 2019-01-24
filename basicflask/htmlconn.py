from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    #name = "harshita"
    #list1 = ['komal','harshita','aarti']
    #dict1 = {
     #         'fname' : 'Harshita',
      #        'lname' : 'Raj'
       #     }
    dict2 = {
              'Harshita': 90,
              'Komal' : 80,
              'Aarti' : 90
            }
    #return render_template('tmp.html',name = name, list1 = list1,dict1 = dict1)
    return render_template('table.html',dict2=dict2)
    
if __name__ == "__main__":
    app.run(debug=True)
