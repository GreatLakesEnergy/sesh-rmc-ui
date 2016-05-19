from redis import Redis
import redis

r=redis.Redis(host="localhost",port="6379",db=0)

seconds='30s'
ethactive='1'
eth0ip='127.0.0.1'
active='1'
ip='192.168.7.2'
signallevel='0'
msg='message on load'

r.set("uptime",seconds)
r.set("eth:active",ethactive)
r.set("eth:ip",eth0ip)
r.set("wlan:active",active)
r.set("wlan:ip",ip)
r.set("wlan:signallevel",signallevel)
r.set("basedata",msg)
    


