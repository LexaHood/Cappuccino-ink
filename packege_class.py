class net_packege_printer (object):
    status: bool

    def __init__(self, ip = None, mac = None, toner = None, name = None):
        if ip != None: self.ip = ip
        else: self.ip = '127.0.0.1'
        if mac != None: self.mac = mac
        else: self.mac = '00:00:00:00:00:00'
        if toner != None: self.toner = toner
        else: self.toner = -1
        if name != None: self.name = name
        else: self.name = 'no name'
        self.status = True

    def add_ip (self, ip):
        self.ip = ip

    def add_mac (self, mac):
        self.mac = mac

    def add_toner (self, toner):
        self.toner = toner

    def get_ip (self):
        return self.ip

    def get_mac (self):
        return self.mac

    def get_toner (self):
        return self.toner

    def get_status (self):
        return self.status

    def switch_status(self):
        self.status != self.status

    def print_packege (self):
        print ('ip adress: ', self.ip, '\tmac: ', self.mac, '\ttoner: ', self.toner, '%')

    def get_string_to_write (self):
        return ('ip adress: ' + self.ip + '\tmac: ' + self.mac + '\ttoner: ' + str(self.toner))

    pass