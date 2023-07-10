from flask import Flask, request,jsonify,render_template
from utils import MedicalInsurance
import traceback

import config


app =Flask(__name__)

@app.route('/medical_insurance')
def home1():
      

    return render_template('medical_insurance.html')


@app.route('/test')

def test():
    print('testing of html page')

    return """ <html>
                <!DOCTYPE html> 
            <html>
            <body>

            <h1>My First Heading</h1>
            <p>My first paragraph.</p>

            </body>
            </html>"""


@app.route('/home')

def home():
    print('testing of page API')


    return render_template('index.html')

@app.route('/medical_insurance/predict_charges', methods = ['GET', 'POST'])

def predict_charges():

    try:
        

        if request.method == 'GET':

            data = request.args.get
            print('*'*50)
            print("Data :",data)
            age      = int(data('age'))
            gender   = data('gender')
            bmi      = int(data('bmi'))
            children = int(data('children'))
            smoker   = data('smoker')
            region   = data('region')

            Obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
                

            #return jsonify({"Result":f"Predicted Medical Charges == {round(pred_price,3)}"})
            return render_template('medical_insurance.html', prediction = pred_price)

        elif request.method=='POST':
            data = request.form.get
            print("Data",data)
            age      = int(data('age'))
            gender   = data('gender')
            bmi      = int(data('bmi'))
            children = int(data('children'))
            smoker   = data('smoker')
            region   = data('region')

            Obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
                

            #return jsonify({"Result":f"Predicted Medical Charges == {round(pred_price,3)}"})
            return render_template('medical_insurance.html', prediction = pred_price)
    except:
        print(traceback.print_exc())
        return redirect(url_for('medical_insurence'))


    
    


if __name__== "__main__":
    app.run(host='0.0.0.0', port = config.PORT_NUMBER)
