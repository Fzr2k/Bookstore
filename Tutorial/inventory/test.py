from inventory_pb2 import BookCategory, InventoryRequest

request = InventoryRequest(user_id=1, category=BookCategory.SCIENCE_FICTION)
print(request)