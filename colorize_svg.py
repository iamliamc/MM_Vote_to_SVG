import csv
from BeautifulSoup import BeautifulSoup

unemployment = {}

reader = csv.reader(open('unemployment09.csv'), delimiter=",")

for row in reader:
	try:
        full_fips = row[1] + row[2]
        rate = float( row[8].strip() )
        unemployment[full_fips] = rate
    except:
        pass


		
svg = open('counties.svg', 'r').read()

soup = BeautifulSoup(svg, selfClosingTags=['defs', 'sodipodi:namedview'])

paths = soup.findAll('path')

colors = ["0xEDF8FB", "0xCCECE6", "0x99D8C9", "0x66C2A4", "0x2CA25F", "0x006D2C"]

for p in paths:
 
    if p['id'] not in ["State_Lines", "separator"]:
        # pass
        try:
            rate = unemployment[p['id']]
        except:
            continue
 
        if rate > 10:
            color_class = 5
        elif rate > 8:
            color_class = 4
        elif rate > 6:
            color_class = 3
        elif rate > 4:
            color_class = 2
        elif rate > 2:
            color_class = 1
        else:
            color_class = 0
 
        color = colors[color_class]
        p['style'] = path_style + color
		
print soup.prettify()