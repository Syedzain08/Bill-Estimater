from flask import Flask, render_template, request
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask('Test', template_folder=os.path.join(base_dir, 'templates'))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
           
            watts = float(request.form['watts'])
            hours_used = float(request.form['hours_used'])
            fixed_tax = float(request.form['fixed_tax'])
            electricity_cost = float(request.form['electricity_cost'])

        
            kw = watts / 1000
            hours_in_months = 30 * hours_used
            kwh_or_unit = kw * hours_in_months
            estimated_cost = kwh_or_unit * electricity_cost
            estimated_cost_without_tax = (estimated_cost + fixed_tax).__round__(3)
            total = estimated_cost.__round__(3)


            return render_template('index.html', result=f"Estimated Cost W Tax: PKR:{total} \n Estimated Cost WO Tax: PKR:{estimated_cost_without_tax} \n Units Consumed:{kwh_or_unit}")
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")
    return render_template('index.html', result=None)

@app.route("/ampsandvolts.html", methods=["GET", "POST"])
def ampsandvolts():
    if request.method == "POST":
        try:
            amps = float(request.form["amps"])
            volts = float(request.form["volts"])
            hours_used = float(request.form['hours_used'])
            fixed_tax = float(request.form['fixed_tax'])
            electricity_cost = float(request.form['electricity_cost'])

            watts = amps * volts
            kw = watts / 1000
            hours_in_months = 30 * hours_used
            kwh_or_unit = kw * hours_in_months
            estimated_cost = kwh_or_unit * electricity_cost
            estimated_cost_without_tax = (estimated_cost + fixed_tax).__round__(3)
            total = estimated_cost.__round__(3)

            return render_template('ampsandvolts.html', result=f"Estimated Cost WO Tax: PKR:{total} \n Estimated Cost W Tax: PKR:{estimated_cost_without_tax} \n Units Consumed: PKR:{kwh_or_unit}")
        except Exception as e:
            return render_template("ampsandvolts.html", results=f"Error: {str(e)}")
    return render_template("ampsandvolts.html", results=None)
            
@app.route("/kwatt.html", methods=["GET", "POST"])
def kwatts():
    if request.method == "POST":
        try:
            kwatt = float(request.form['kwatt'])
            hours_used = float(request.form['hours_used'])
            fixed_tax = float(request.form['fixed_tax'])
            electricity_cost = float(request.form['electricity_cost'])

            hours_in_months = 30 * hours_used
            kwh_or_unit = kwatt * hours_in_months
            estimated_cost = kwh_or_unit * electricity_cost
            estimated_cost_without_tax = (estimated_cost + fixed_tax).__round__(3)
            total = estimated_cost.__round__(3)

            return render_template('kwatt.html', result=f"Estimated Cost W Tax: PKR:{total} \n Estimated Cost WO Tax: PKR:{estimated_cost_without_tax} \n Units Consumed: PKR:{kwh_or_unit}")
        except Exception as e:
            return render_template("kwatt.html", results=f"Error: {str(e)}")
    return render_template("kwatt.html", results=None)

app.run(host='0.0.0.0', port=80)
