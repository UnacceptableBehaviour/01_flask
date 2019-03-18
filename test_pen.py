#! /usr/bin/env python

from pprint import pprint # giza a look

import glob
import re           # regex

#from helpers import *
# call get_nutridata()
#
# or 
#
#import helpers
# call helpers.get_nutridata()

#from helpers import *
import helpers


def main():
    print(f"RUNNING TEST PEN")
    
    info = helpers.get_nutridata()
 
    #pprint(info)
 
    for k,v in info.items():        
        print(f"{ k } = { v }")
        
    print(f"__name__ is: {__name__}")
    print(f"__file__ is: {__file__}")
    print(f"__loader__ is: {__loader__}")
    print(f"__package__ is: {__package__}")
        
    info['n_EnkJ'] = str( round( float( info['n_En'] ) * 4.184 ) )
    info['serving_size'] = str( round( float( info['serving_size'] ) ) )
    
    print(f"n_EnkJ:       {info['n_EnkJ']}")
    print(f"serving_size: {info['serving_size']}")
    
    print(f"{1}")
    
    helpers.get_nutrients_per_serving()
    
    helpers.load_csv_data()



#def get_ingredients_from_recipe(name):
    print( helpers.get_ingredients_from_recipe('') )

    requested_recipe = 'mushroom rissotto'

    print( glob.glob('./static/recipe/*.txt') )
    
    recipe_ref = {}
    for recipe_file in glob.glob('./static/recipe/*.txt'):
        print(recipe_file)
        #print(re.search(r'\d{8}_\d{6}_(.*).txt', './static/recipe/20190301_145910_mushroom rissotto.txt') )
        print(re.search(r'\d{8}_\d{6}_(.*).txt', recipe_file).group(0) )
        print(re.search(r'\d{8}_\d{6}_(.*).txt', recipe_file).group(1) )
        recipe_name = re.search(r'\d{8}_\d{6}_(.*).txt', recipe_file).group(1)
        recipe_ref[recipe_name] = recipe_file
        
    print(f"Looking for: {requested_recipe} <")
    print(f"Found: {recipe_ref[requested_recipe]} <")
    
    recipe_file ="./static/recipe/20190301_145910_mushroom rissotto.txt"
    
    # with open(recipe_file) as f:
    #    content = [line.rstrip() for line in f]
    # print( content.__class__.__name__ )            # list
    # 
    # for l in content:
    #     print( l )
                                         # match
    # ^-+- for the (.*) \((\d+)\)        # 1.name (2.portions)
    # (.*)                               # 3. ingredients
    # ^\s+Total \((.*?)\)                # 4. yield
    # need DOTALL so multiline works
    # https://www.thegeekstuff.com/2014/07/advanced-python-regex/
    # all together
    # ^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)
    #
    
    with open(recipe_file) as f:
        content = "".join(f.readlines())
                        
    print( content.__class__.__name__ )
    print( ' - - - recipe text' )
    print( content )
    
    #match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', content, re.DOTALL )
    #match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', content, re.MULTILINE )
    
    match = re.search( r'^-+- for the (.*) \((\d+)\)', content, re.DOTALL )
    r_name = match.group(1)
    r_portions = match.group(2)
    
    match = re.search( r'\)(.*)^\s+T', content, re.MULTILINE )
    #r_ingredients = match.group(1)
    r_ingredients = 'ingredients'
    #r_yield = match.group(4)
    r_yield = '1kg'
    
    print(f" - - - recipe: {r_name} <\n{r_ingredients}\nmakes {r_yield} which is {r_portions} portions" )
    
    this_is_multiline = \
'''
------------------ for the mushroom rissotto (3)
50g	fennel
46g	butter
70g	leek
20g	green pepper
16g	garlic
88g	white mushrooms
80g	sauteed mushrooms
100g	white wine
10g	chicken stock cube
490g	water
40g	peas
80g	cream cheese
100g	arborio rice
								Total (900g)
'''
    
    print(f" - - -  - - -  this_is_multiline \n{this_is_multiline}\n - - - - - ")
    
    #match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', this_is_multiline, re.DOTALL )
    #match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', this_is_multiline, re.MULTILINE )
    r_name = 'No Match'
    r_portions = 'No Match'
    r_ingredients = []
    r_yield = 'No Match'

    # name and portions
    match = re.search( r'^-+- for the (.*) \((\d+)\)', this_is_multiline, re.MULTILINE )
    #match = re.search( r'^-+- for the (.*) \((\d+)\)', this_is_multiline, re.DOTALL )
    if match:
        r_name = match.group(1)
        r_portions = match.group(2)
    else:
        print("name and portions NO MATCH")
        
    
    # ingredients
    #match = re.search( r'^(\d+)g\s+([a-zA-Z ]+)$', this_is_multiline, re.MULTILINE )
    match = re.findall( r'^(\d+)g\s+([a-zA-Z ]+)$', this_is_multiline, re.MULTILINE )
    #match = re.search( r'\)(.*)^\s+T', this_is_multiline, re.DOTALL )
    if match:
        #pprint(match)
        print(f"ingredients: {match.__class__.__name__}") # - {match.size}")
        for i in match:
            r_ingredients.append( f"{i[0]}g\t{i[1]}" )
            print( f"{i[0]}g\t{i[1]}" )
    else:
        print("ingredients NO MATCH")
    
    # yield
    match = re.search( r'^\s+Total \((.*?)\)', this_is_multiline, re.MULTILINE )
    #match = re.search( r'^\s+Total \((.*?)\)', this_is_multiline, re.DOTALL )
    if match:
        r_yield = match.group(1)
    else:
        print("yield NO MATCH")

    print(f" - - - recipe ML: {r_name} <\n{r_ingredients}\nmakes {r_yield} which is {r_portions} portions" )
    
    match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', this_is_multiline, re.MULTILINE | re.DOTALL )
    #match = re.search( r'^-+- for the (.*) \((\d+)\)', this_is_multiline, re.MULTILINE )
    #match = re.search( r'\).*?^(.*)^\s+Total \((.*?)\)', this_is_multiline, re.MULTILINE )
    #match = re.search( r'^\s+Total \((.*?)\)', this_is_multiline, re.MULTILINE )
    r_ingredients = match.group(3).strip()
    print(f"{r_ingredients.__class__.__name__}")
    print(f"{r_ingredients}")
    print(f"{match.group(3)}")


    get_ingredients_from_recipe('mushroom risotto')

if __name__ == '__main__':
    main()                      # call main if this is being executed directly 
