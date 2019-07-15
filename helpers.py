#! /usr/bin/env python

# load a csv file into a list of dictionaries

import csv
import itertools

from pprint import pprint # giza a look


# load csv file form local directory - in repo
def load_csv_data():
    file_name = './static/sql_recipe_data.csv'

    with open(file_name) as csv_to_sql_file:    
        csv_reader = csv.DictReader(csv_to_sql_file, delimiter=',')    
        
        pprint(csv_reader)
        
        local_store = './static/'
        image_path = 'recipe/'
        txt_path = image_path
        
        image_dictionary = {}
        text_dicionary = {}
    
        entries = 0
        
        for row in csv_reader:
            line = ''
            
            for col_key in csv_reader.fieldnames:
    
                if col_key == 'image_filename':
                    image_dictionary[entries] = f"{image_path}{row[col_key]}"
                    continue
    
                if col_key == 'txt_ingredient_file':
                    text_dicionary[entries] = f"{txt_path}{row[col_key]}"
                    continue
    
                line = line + " " + row[col_key]
    
            print(line)
            
            entries +=1
            
    
        entries -= 1
        
        print("----- image_dictionary")
        pprint(image_dictionary)
    
        print("----- text_dicionary")
        pprint(text_dicionary)
        
        return image_dictionary



    # for line in db_lines:
    #     #print(f" | {line.ndb_no} | {line.nutr_no} | {line.nutr_val} | {line.deriv_cd} | ")
    #     formatted_text = formatted_text + f" | {line.ndb_no} | {line.nutr_no} | {line.nutr_val} | {line.deriv_cd} | \n"
    # 
    # print(f"\n\nProcess Query {formatted_text}")
    #     
    # print(f"\n\nHello World > {engine}" <)


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


def get_nutrients_per_serving():
    info = get_nutridata()
    
    nutrient_keys = 'n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al'.split(',')
    
    multiplier = float( info['serving_size'] ) / 100.0
    
    b4 = 0
    
    for key in nutrient_keys:
        b4 = info[key]
        info[key] = str( round( ( float( info[key] ) * multiplier ), 1 ) )
        print(f"key:{key} - b4:{b4} - x:{multiplier} - conv:{info[key]}- conv:{info[key].__class__.__name__}")

    return info


def get_ingredients_from_recipe(recipe_name):
    print(f"{recipe_name}")
    
    ingredients = "50g	fennel\n46g	butter\n70g	leek".split("\n")
    
    return ingredients    
