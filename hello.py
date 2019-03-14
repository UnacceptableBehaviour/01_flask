from flask import Flask, render_template
app = Flask(__name__)

def get_nutridata():
             #  0          1              2             3             4    5    6    7    8    9
    header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al,serving_size'
    text = '1,20190306_145901_seabass kale and potato dinner.jpg,seabass kale and potato dinner,20190306_145901_seabass kale and potato dinner.txt,55,1.6,0.44,0.5,0.43,0.4,2.74,0.32,0.47,0.0,7.28,0.45,0.0,450.0'
    
    header_list = header.split(',') 
    rcp_list = text.split(',')

    info = {}
    
    for i in range( len(header_list) ):        
        info[ header_list[i] ] = rcp_list[i]
        #print(f"{ header_list[i] } = { info[ header_list[i] ] }")
    
    return info


# these execute templates stored in the directory templates (in project folder)
# this passes a veariable headline into the index.html template
# it replace {{ headline }} in the template
@app.route('/')
def index_f():
    headline_py = "Lick the Toad"
    return render_template("index.html", headline=headline_py)



@app.route('/nutrient_table')
def nutrient_table_f():
    headline_py = 'Nutrients Table'
    
    info = get_nutridata()
    
    return render_template("nutrients_traffic_lights.html", headline=headline_py, info=info)