from parser_net import parser_net_func
#import parser_web
import packege_class

def main():
    ip_net = '127.1.1.'
    mac_list = []

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

    parser_net_func(ip_net, mac_list)

    pass

if __name__ == '__main__':
    
    main()

    pass