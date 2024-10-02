#COMMIT 9/18/2024  


#File structure of the computerized growing chamber (CGC) repository (MVP) is as follows  

#MVP  

  #data: currently hosts no logs or files  
  
  #logs: holds logs for couchdb, cron, heartbeat, mvp, server, and startup. These files are specific
                  #to each machine. Might not be created automatically by their corresponding script  
                  
  #pictures: holds photos from two webcams in separate folders  
  
    #cam1Left: holds pictures from left camera  
    
    #cam2Right: holds pictures from right camera  
    
  #python: holds python scripts for basic CGC functionality  
  
    #__pycache__: holds .pyc files from logData and si7021  
    
  #scripts: holds bash scripts for basic and some advanced CGC functionality such as couchDB and cron  
  
  #setup: holds bash scripts for other services, primarily for initializing and updating cron (NEED NOTE)  
  
  #web: holds sub-repository for web service python scripts  
  
    #cgi-bin holds aforementioned web service python scripts  
    
  
#COMMIT 10/2/24
#LOCAL CHANGE: TGCA FOURTH FLOOR
#REMOVED REFERENCES TO COUCHDB FROM NECESSARY CGC FUNCTIONS:
#LightOn.py and LightOff.py
#Fan.py
