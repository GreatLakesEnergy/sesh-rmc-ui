import os
import redis
import rmc_data_file

from flask import Flask ,render_template 
from flask.ext.bower import Bower
from redis import Redis

app=Flask(__name__)
Bower(app)

app.config.from_pyfile('config.cfg')


r = redis.Redis(host='localhost', port=6379, db=0)

content_dict={}
content_dict['UPTIME'] ={'UPTIME':r.get('uptime')}
content_dict['ETHERNET_STATUS'] ={'Ethernet_Status':r.get('eth:active')}
content_dict['ETHERNET_IP'] ={'Ethernet_IP':r.get('eth:ip')}
content_dict['WLAN_STATUS'] ={'Wlan_Status':r.get('wlan:active')}
content_dict['WLAN_IP'] ={'Wlan_ip':r.get('wlan:ip')}
content_dict['WLAN_STRENGTH'] ={'Wlan_Stength':r.get('wlan:signlalevel')}
content_dict['BASE_DATA'] ={'Basedata':r.get('msg')}


@app.route("/")
def main():
    rmc_elements = content_dict.values()
    return render_template('base.html',rmc_elements=rmc_elements)


if __name__=="__main__":
    port = int(os.environ.get('FLASK_PORT', 5000))
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(host=host,port=port)

