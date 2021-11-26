import boto3
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
table = dynamodb.Table('Books')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
# to equal "John Grisham" by using the ".eq()" method.
resp = table.query(KeyConditionExpression=Key('Author').eq('John Grisham'))

print("The query returned the following items:")
# for item in resp['Items']:
#     print(item)
print(resp)

# {'Items': [
#     {'Title': 'The Firm', 'Formats': {'Hardcover': 'Q7QWE3U2', 'Paperback': 'ZVZAYY4F', 'Audiobook': 'DJ9KS9NM'}, 
#      'Author': 'John Grisham', 'Category': 'Suspense'}, 
#     {'Title': 'The Rainmaker', 'Formats': {'Hardcover': 'J4SUKVGU', 'Paperback': 'D7YF4FCX'}, 
#      'Author': 'John Grisham', 'Category': 'Suspense'}
#     ], 
# 'Count': 2,
# 'ScannedCount': 2, 
# 'ResponseMetadata': 
#     {'RequestId': '0BDR8QTQ02NTSOSNT774HI9ORBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 
#     'HTTPHeaders': {'server': 'Server', 'date': 'Wed, 24 Nov 2021 19:37:16 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '394', 'connection': 'keep-alive', 'x-amzn-requestid': '0BDR8QTQ02NTSOSNT774HI9ORBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2191835166'}, 
#     'RetryAttempts': 0}
# }