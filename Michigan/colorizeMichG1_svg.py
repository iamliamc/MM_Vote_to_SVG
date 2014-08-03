### colorize_svg.py
 
import csv
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
 
# Read in unemployment rates
unemployment = {}
min_value = 100; max_value = 0
reader = csv.reader(open('medicalmarijuana2008.csv'), delimiter=",")
for row in reader:
    try:
        full_fips = row[0]
        rate = float( row[4].strip() )
        unemployment[full_fips] = rate
    except:
        pass
 
 
# Load the SVG map
svg = open('List_of_michigan_counties_ID.svg', 'r').read()
 
# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
 
# Find counties
paths = soup.findAll('path')
 
# Map colors 0xEDF8FB; 0xCCECE6; 0x99D8C9; 0x66C2A4; 0x2CA25F; 0x006D2C; 
#colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
#colors = ["#7fa04b", "#7f8a45", "#7f7f42", "#7f743f", "#7f693c", "#804733"]
colors = ["#008600", "#00c900", "#FFC300", "#FF7400", "#FF0D00", "#990000"]
 

# County style
path_style ='fill-opacity:1;fill-rule:evenodd;stroke:#d0c0a0;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1'
 
# Color the counties based on unemployment rate
for p in paths:
    #print(p['id'])
    if p['id'] not in ["State_Lines", "separator", "tspan", "text", "text2295"]:
        # pass
        try:
            rate = unemployment[p['id']]
        except:
            continue
 
 
        if rate > 65:
            #print('five')
            color_class = 0
        elif rate > 60 :
            #print('four')
            color_class = 1
        elif rate > 58:
            #print('three')
            color_class = 2
        elif rate > 56:
            #print('two')
            color_class = 3
        elif rate > 53:
            #print('one')
            color_class = 4
        else:
            #print('zero')
            color_class = 5
 
 
        color = colors[color_class]
        p['style'] = 'fill:' + color + ';' + path_style
 
print(soup.prettify())