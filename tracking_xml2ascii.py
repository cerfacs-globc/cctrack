from xml.dom import minidom
import sys
 
doc = minidom.parse(sys.argv[1])
filename_out = sys.argv[2]
fout = open(filename_out, 'w+', encoding='ascii')
 
disturbanceNodes=doc.getElementsByTagName("disturbance")
for i in disturbanceNodes:
  cycloneNumberNodes=i.getElementsByTagName("cycloneNumber")
  cycloneNumber=cycloneNumberNodes[0].firstChild.nodeValue
  fixNodes=i.getElementsByTagName("fix")
  for j in fixNodes:
 
     validTimeNodes=j.getElementsByTagName("validTime")
     validTime=validTimeNodes[0].firstChild.nodeValue
     aaaammjj=validTime.split("T")[0].replace("-","")
     aaaa=validTime[0:4]
     mm=validTime[5:7]
     jj=validTime[8:10]
     hh=validTime.split("T")[1][0:2]
 
     longitudeNodes=j.getElementsByTagName("longitude")
     longitude=longitudeNodes[0].firstChild.nodeValue
     eastOrWest=longitudeNodes[0].getAttribute("units")
     lonSign=""
     if eastOrWest == "deg W":
       lonSign="-"
       longitude=str(-float(longitude)+360.0)
       
 
     latitudeNodes=j.getElementsByTagName("latitude")
     latitude=latitudeNodes[0].firstChild.nodeValue
     northOrSouth=latitudeNodes[0].getAttribute("units")
     latSign=""
     if northOrSouth == "deg S":
       latSign="-"
 
     pressureNodes=j.getElementsByTagName("pressure")
     pressure=pressureNodes[0].firstChild.nodeValue

     vorticityNodes=j.getElementsByTagName("vorticity")
     vorticity=vorticityNodes[0].firstChild.nodeValue

     circulationNodes=j.getElementsByTagName("circulation")
     circulation=circulationNodes[0].firstChild.nodeValue

     print ("%s %s%s %s %s %s %s %s %s %s" % (cycloneNumber,latSign,latitude,longitude,vorticity,pressure,hh,jj,mm,aaaa), file=fout)

fout.close()
