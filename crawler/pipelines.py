# -*- coding: utf-8 -*-
import boto3


class CrawlerPipeline(object):

    def process_item(self, item, spider):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('player')
        if 'Item' not in table.get_item(Key={'npb_id': item['npb_id'], 'team_en': item['team_en']}):
            table.put_item(Item=dict(item))
        return
