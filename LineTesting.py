"""To test the method of extraction of points using python library ezdxf"""

#Extracting the ModelSpace
import ezdxf
dwg = ezdxf.readfile("House.dxf")
msp = dwg.modelspace()

#Initializing Variables
count=0
points = list(())
final_points = list(())

#Extracting all points in the modelspace from LINE endpoints
for line in msp.query('LINE') :
    start=line.dxf.start
    points.append(start)
    end=line.dxf.end
    points.append(end)
    
#Removing duplicates
for point in points: 
        if point not in final_points: 
            final_points.append(point)   
    
#Printing in the ModelSpace
for point in final_points :
    msp.add_text("P (%d)" % count,dxfattribs={'height': 12, 'width': 1}).set_pos((point), align='CENTER')    
    count=count+1
dwg.saveas("House_out.dxf")