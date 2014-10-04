"""
Takes an input CSV file with columns of logitude and lattitude. 
Adds javascript/geojson language and spits it out as a js file. 

Required inputs: 
  * the input csv file (all non-float columns will be ignored)
  * the name for your feature

Output:
  * Points for your features. TODO: make this optional! 
"""

import sys

infile = sys.argv[1]
feature_name = sys.argv[2]

### print out the prelim stuff
outfile = open(feature_name+'.js','w')
print >> outfile, "var", feature_name, '= {'
print >> outfile, '\t "type":"FeatureCollection",'
print >> outfile, '\t \t "features": ['


for line in open(infile,'r'):
    cols = line.split(',')
    try:
        long = float(cols[0])
        lat = float(cols[1])
    except:
        print "not numbers!", line
        continue

    print >> outfile, '\t \t \t {'
    print >> outfile, '\t \t \t \t "geometry": {'
    print >> outfile, '\t \t \t \t \t "type":"Point",'
    print >> outfile, '\t \t \t \t \t "coordinates":[', cols[0], ',', cols[1][:-1], ']' ## To avoid the end-of-line character
    print >> outfile, '\t \t \t },'

    print >> outfile, '\t \t \t "type":"Feature",'
    print >> outfile, '\t \t \t "properties": {'
    print >> outfile, '	\t \t \t "popupContent": "SPRINT mast"'
    print >> outfile, '\t \t \t },'

    print >> outfile, '\t \t },'
print >> outfile, '\t', ']'
print >> outfile, '};'

outfile.close()
