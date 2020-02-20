import json
from . import utils


def parse_stats_p(player, response):
    arr = []
    for i in range(1, player['seasons'] + 1):
        BASE_XPATH = "//*[@id='tablefix_p']/tbody/tr[@class='registerStats'][" + \
            str(i) + "]"
        with open('crawler/xpath/stats_p.json', 'r') as f:
            stats_p_json = json.load(f)
            dic = dict()
            for key in stats_p_json.keys():
                if key == 'ip1':
                    continue
                if key == 'ip2':
                    ip = response.xpath(BASE_XPATH + stats_p_json['ip1']).extract() + \
                        response.xpath(
                            BASE_XPATH + stats_p_json['ip2']).extract()
                    dic['ip'] = utils.stlip_space_crlf(''.join(ip))
                    continue
                dic[key] = utils.stlip_space_crlf(''.join(response.xpath(
                    BASE_XPATH + stats_p_json[key]).extract()))

        arr.append(dic)
    player['stats_p'] = arr


def parse_stats_b(player, response):
    arr = []
    for i in range(1, player['seasons'] + 1):
        BASE_XPATH = "//*[@id='tablefix_b']/tbody/tr[@class='registerStats'][" + \
            str(i) + "]"
        with open('crawler/xpath/stats_b.json', 'r') as f:
            stats_b_json = json.load(f)
            dic = dict()
            for key in stats_b_json.keys():
                dic[key] = utils.stlip_space_crlf(''.join(response.xpath(
                    BASE_XPATH + stats_b_json[key]).extract()))

        arr.append(dic)
    player['stats_b'] = arr
