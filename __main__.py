from parser_net import parser_net_func
from parser_web import parcer_web_brother, check_web_conection
from packege_class import net_packege_printer

def write_file_printer_list():
    size = len(printers_list)
    if size <= 0: 
        print("printer list has size 0") 
        return -2
    
    try: 
        file_printer_list = open('printer list.data', 'w', 1, 'UTF-8')
    except OSError as e: 
        print ("Cant create printer list.data")
        return -1
    
    for i in range(size):
        file_printer_list.write(printers_list[i].get_string_to_write() + '\n')
        pass
    
    file_printer_list.close()
    pass

def initialization():
    global ip_net
    global mac_list
    global printers_list

    ip_net = '127.1.1.'
    mac_list = []
    printers_list = []

    try:
        conf_file = open('config.conf', 'r', 1, 'UTF-8')
    except OSError as e:
        print ("Cant open config")
        return 1
    
    config = conf_file.read()
    conf_file.close()

    index_ip_start = config.find("network") + 8
    index_ip_end = config.find("\n", index_ip_start)
    ip_net = config[index_ip_start : index_ip_end]
    print (ip_net)

    index_mac = config.find("mac list") + 9
    def mac_separator_of_conf(index_start, index_end):
        index_start = config.find("[", index_start) + 1
        index_end = config.find("]", index_start)

        mac_list.append(config[index_start : index_end])

        if config.find("[", index_end) != -1:
            mac_separator_of_conf(index_start, index_end)
        else:
            return 0
        pass

    mac_separator_of_conf(index_mac, 1)
    print (mac_list)

    printers_list = parser_net_func(ip_net, mac_list)

    for i in range(len(printers_list)):
        if printers_list[i].get_mac().find(mac_list[0]) != -1:
            printers_list[i].add_toner = parcer_web_brother(printers_list[i])
            pass
        printers_list[i].print_packege()
        pass
    
    write_file_printer_list()
    pass

if __name__ == '__main__':
    
    initialization()


    pass