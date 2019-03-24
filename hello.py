from flask import Flask, render_template, request
app = Flask(__name__)

# importing files
# https://realpython.com/absolute-vs-relative-python-imports/
# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
# https://pep8.org/#imports
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
from .helpers import  load_csv_data, get_nutridata, get_nutrients_per_serving, get_ingredients_from_recipe
#import helpers

ingredient_text_list = get_ingredients_from_recipe('mushroom rissotto')

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


@app.route('/recipe_drop_down', methods=["GET", "POST"])
def recipe_drop_down():
    if request.method =='GET':
        info = load_csv_data()
        image_file = ''
        headline_py = "Pick a Recipe"
        return render_template("recipe_dropdown.html", headline=headline_py, recipe_image=image_file, image_dict=info)
    else:
        info = load_csv_data()
        headline_py = "Pick a Recipe"        
        image_file = request.form.get("recipe_image_list_drop_down")
        return render_template("recipe_dropdown.html", headline=headline_py, recipe_image=image_file, image_dict=info)
        

@app.route('/drop_down_action', methods=["GET", "POST"])
def drop_down_action():
    if request.method =='GET':
        return "THIS IS A GET REQUEST"
    else:            
        image_file = request.form.get("recipe_image_list_drop_down")
        return render_template("show_image.html", recipe_image=image_file)

@app.route('/ingredients', methods=['GET','POST'])
def ingredient_list():
    header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al,serving_size'
    info = {}
    recipe_name = 'mushroom rissotto'
    info['recipe_title'] = recipe_name
    info['ingredient_list'] = get_ingredients_from_recipe(recipe_name)
    #info['image_filename'] = get_image_for_recipe(recipe_name)
    info['image_filename'] = './static/recipe/20190301_145910_mushroom rissotto.jpg'
    
    if request.method =='GET':      # arrive at page
        return render_template("ingredients_list.html", info=info, ingredient_list=ingredient_text_list)
    else:                           # page updating with user input request.method = 'POST' 
        new_ingredient = request.form.get("form_ingredients_list")
        ingredient_text_list.append(new_ingredient)
        return render_template("ingredients_list.html", info=info, ingredient_list=ingredient_text_list)

    

@app.route('/recipe_wb')
def recipe_wb():
    info = get_nutrients_per_serving()
    headline_py = "Lick the Buttons"
    return render_template("recipe_template_wb.html", headline=headline_py, info=info)



# app.run(host='0.0.0.0', port= 8090)
