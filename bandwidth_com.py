import sys,os # Importing standard system and os python library 
import speedtest # Importing Bandwidth python library (ref : https://github.com/sivel/speedtest-cli)
import time # Importing standard time python library
import datetime # Importing standard date python library
import os.path # Make sure os.path is imported 



s = speedtest.Speedtest() # Speedtest object definition
s.get_best_server() # Best evaluation server selection for dummy package download
print(s.best) # Showing Best server paramters

### Preparing Output file
compt=1
filename="internet_bandwidth_"+str(compt)+".log"
while os.path.isfile(filename):
    compt+=1
    filename="internet_bandwidth_"+str(compt)+".log"
    
savefile=open(filename,'w')
savefile.write(s.best["url"]+" "+s.best["name"]+" "+s.best["country"]+"\n")
###

nb_mesure=5 # Number of mesures to take (the average speed will be used as final result)
sampling_time=3600 # Take one sample every hours (3600 seconds)

now = datetime.datetime.now() # Sample Date 

# Getting output file ready to receive data
savefile.write("Nombre de mesure / Echantillonnage: %d\n"%(nb_mesure))
savefile.write("Temps d'echantillonnage: %d sec\n"%(sampling_time))
savefile.write(now.strftime("%Y-%m-%d %H:%M")+"\n\n")
savefile.write("Date\tDownload Speed (Mbits/s)\tDownload Speed (Mbytes/s)\tUpload Speed (Mbits/s)\tUpload Speed (Mbytes/s)\n")

print("Sampling Launched")
while True:
    try:
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M"))
        mesure_d=0.0
        mesure_u=0.0
        
        print("Mesuring Download")
        for i in range(0,nb_mesure):
            mesure_d+=s.download() # Download speed mesurement (will be executed 5 times)
        print("Mesuring Upload")
        for i in range(0,nb_mesure):
            break # THIS LINE PREVENT UPLOAD MESUREMENT, not useful for bandwidth evaluation
            mesure_u+=s.upload()
            
        mesure_d=mesure_d/nb_mesure # Average speed calculation
        mesure_u=mesure_u/nb_mesure # Not used
        savefile.write(str(now.strftime("%Y-%m-%d %H:%M"))+"\t"+str(mesure_d/1024/1024)+"\t"+str(mesure_d/1024/1024/8)+"\t"+str(mesure_u/1024/1024)+"\t"+str(mesure_u/1024/1024/8)+"\n")
        savefile.flush() # Force program to write the results in the output file (program will not use internal buffers)
        os.fsync(savefile.fileno()) # IDEM ^
        print("Sleep")
        time.sleep(sampling_time) # Program wait before next sampling
    except KeyboardInterrupt: # If CTRL-C is pressed, stop the sampling and quit the program
        print("Manual Interrupt Detected")
        break
savefile.close() # Make sure all informations are in the file and close it
