from astropy.coordinates import SkyCoord, AltAz, EarthLocation
from astropy.time import Time
import astropy.units as u
from datetime import datetime

import requests
import json

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


class finder(object):

    def __init__(self):
        self.refLoc=None
        self.refLocjson = None
        self.body = None
        self.xs = []
        self.ys = []
        self.fig = plt.figure()

    def getmylocation(self):
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip'] 

        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data = geo_request.json()

        self.refLocjson = {"longitude":float(geo_data["longitude"]),"latitude":float(geo_data["latitude"])}

        
    def fit(self,bodyName,refLoc=None,ret=False):
        
        if not refLoc is None:
            self.refLocjson = refLoc
        else:
            self.getmylocation()

        time = Time(datetime.now())
        self.body = SkyCoord.from_name(bodyName)
        self.refLoc = EarthLocation(lat=self.refLocjson["latitude"]*u.deg,lon=self.refLocjson["longitude"]*u.deg)
        self.frame = AltAz(obstime=time,location=self.refLoc)
        bodyAltaz = self.body.transform_to(self.frame)
        bodyAltaz.repesentation_type = "cartesian"

        self.cartCoord = [bodyAltaz.to_string(),time]

        if ret:
            return bodyAltaz

    def plotPoint(self,i):

        ax1 = self.fig.add_subplot(1,1,1)

        time = Time(datetime.now())
        frame = AltAz(obstime=time,location=self.refLoc)
        bodyHat = self.body.transform_to(frame)
        bodyHat.repesentation_type = "cartesian"
        x,y = map(float,bodyHat.to_string().split(" "))
        self.xs.append(x)
        self.ys.append(y)
        ax1.clear()
        ax1.scatter(self.xs,self.ys,color="black")
    
    def liveplot(self):
        anim = FuncAnimation(self.fig,self.plotPoint,interval=1000)
        plt.show()



        

    


