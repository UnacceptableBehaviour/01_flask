from flask import Flask, render_template
app = Flask(__name__)

# importing files
# https://realpython.com/absolute-vs-relative-python-imports/
# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
# https://pep8.org/#imports
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
from .helpers import  load_csv_data, get_nutridata, get_nutrients_per_serving
#import helpers

# these execute templates stored in the directory templates (in project folder)
# this passes a veariable headline into the index.html template
# it replace {{ headline }} in the template
@app.route('/')
def index_f():
    headline_py = "Lick the Toad"
    #info = get_nutrients_per_serving() 
    return render_template("index.html", headline=headline_py) #, info=info)

@app.route('/nutrient_table')
def nutrient_table():
    headline_py = 'Nutrients Table'    
    info = get_nutrients_per_serving()    
    return render_template("nutrients_traffic_lights_w_buttons.html", headline=headline_py, info=info)


@app.route('/nutrient_table_dbl')
def nutrient_table_f():
    headline_py = 'Double Nutrients Table'    
    info = get_nutridata()    
    return render_template("nutrients_traffic_lights_w_buttons_dbl.html", headline=headline_py, info=info)


@app.route('/recipe_drop_down')
def recipe_drop_down():
    info = load_csv_data()
    headline_py = "Pick a Recipe"
    return render_template("recipe_dropdown.html", headline=headline_py, image_dict=info)

@app.route('/recipe_wb')
def recipe_wb():
    info = get_nutrients_per_serving()
    headline_py = "Lick the Buttons"
    return render_template("recipe_template_wb.html", headline=headline_py, info=info)
