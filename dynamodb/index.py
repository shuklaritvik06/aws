import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'example_table'


def create_table():
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print("Table created successfully")


def put_item(item):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=item)
    print("Item added successfully", response)


def get_item(item_id):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'id': item_id})
    item = response.get('Item')
    if item:
        print("Retrieved item:", item)
    else:
        print("Item not found")


def update_item(item_id, update_expression_input, expression_attribute_values_input):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'id': item_id},
        UpdateExpression=update_expression_input,
        ExpressionAttributeValues=expression_attribute_values_input,
        ReturnValues="UPDATED_NEW"
    )
    print("Item updated successfully", response)


def delete_item(item_id):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={'id': item_id})
    print("Item deleted successfully", response)


if __name__ == "__main__":
    create_table()
    put_item({'id': 1, 'name': 'Item 1', 'description': 'Description of item 1'})
    get_item(1)
    update_expression = "set description = :desc_val"
    expression_attribute_values = {':desc_val': 'Updated description'}
    update_item(1, update_expression, expression_attribute_values)
    get_item(1)
    delete_item(1)
