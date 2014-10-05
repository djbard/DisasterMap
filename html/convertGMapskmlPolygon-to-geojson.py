### Converts a Google maps kml file that contains only polygons, into a geojson file of polygons. 



lats = []
longs = []
np =-1
for line in open('SanFranciscoSeismicHazardZonesLiquefaction.kml','r'):
    if '<Polygon>' in line:
        np+=1
        lats.append([])
        longs.append([])
    if '-122' in line and '37' in line:
        cols = line.split(',')
        lats[np].append(float(cols[0]))
        longs[np].append(float(cols[1]))

print len(lats), len(lats[0])

## ok, now I have my lists of lats and longs, I need to put them into the file. 

outfile = open('Liq.js','w')
print >> outfile, 'var Liquifaction = { \n','    "type": "Feature", \n','    "properties": { \n','        "popupContent": "Liquifaction zone! Run!", \n','        "style": { \n','            weight: 2, \n','            color: "#999", \n','            opacity: 1, \n','            fillColor: "#B0DE5C", \n','            fillOpacity: 0.8  \n','        } \n','    }, \n','    "geometry": { \n','        "type": "MultiPolygon", \n','        "coordinates": [ \n',


for i in range(len(lats)):
    if i==0:
        print >> outfile, '\t \t ['
    else:
        print >> outfile, '\t\t ],['
    print >> outfile, '\t\t\t ['
    for j in range(len(lats[i])):
        if j==len(lats[i])-1:
            print >> outfile, '\t\t\t\t [', str(lats[i][j]), ',', str(longs[i][j]), ']'
        else:
            print >> outfile, '\t\t\t\t [',str(lats[i][j]), ',', str(longs[i][j]), '],'
    print >> outfile, '\t\t\t ]'

print >> outfile, '\t\t ]'
print >> outfile, '\t ]'
print >> outfile, '   }'
print >> outfile, '};'
