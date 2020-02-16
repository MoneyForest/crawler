# -*- coding: utf-8 -*-
from . import player_utils


class CrawlerPipeline(object):

    def process_item(self, item, spider):
        table = player_utils.init_player_table()
        item = player_utils.replace_none_to_space(item)
        key = player_utils.table_keys(item)

        if 'Item' not in table.get_item(Key=key):
            table.put_item(Item=dict(item))
        return
