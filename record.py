import json
import time
import os
import twisted.python.logfile
from ConfigParser import SafeConfigParser


class JsonLog(object):
    def __init__(self):
        dire = os.path.dirname('info')
        name = os.path.basename('info')
        self.outfile = twisted.python.logfile.DailyLogFile(name, dire, defaultMode=0o664)

    def get_log(self, command, rhost, rport):
        data = {}
        parse = SafeConfigParser()
        parse.read('info')
        dst_ip = parse.items('IP')
        data['timestamp'] = time.strftime("%Y-%m-%d %X", time.localtime())
        data['dst_ip'] = dst_ip[0][1]
        data['dst_port'] = 6379
        data['src_ip'] = rhost
        data['src_port'] = rport
        data['command'] = command
        json.dumps(data)
        self.outfile.write(data+"\n")
        self.outfile.flush()



