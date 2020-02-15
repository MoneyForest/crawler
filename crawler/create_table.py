from __future__ import print_function
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Players',
    KeySchema=[
        {
            'AttributeName': 'npb_id',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'team_en',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'npb_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'team_en',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
