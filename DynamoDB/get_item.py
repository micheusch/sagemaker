import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
table = dynamodb.Table('Books')

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})

print(resp['Item'])
