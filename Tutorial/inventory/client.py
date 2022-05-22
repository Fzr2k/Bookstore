import grpc
from inventory_pb2 import InventoryRequest
from inventory_pb2_grpc import InventoryBooksStub

channel = grpc.insecure_channel("localhost:50051")
client = InventoryBooksStub(channel)
request = InventoryRequest(user_id=1)
print(client.Inventory(request))
