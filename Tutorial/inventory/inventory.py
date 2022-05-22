from concurrent import futures

import grpc

from inventory_pb2 import (
    BookCategory,
    Book,
    InventoryResponse,
)
import inventory_pb2_grpc

books_by_category = {
    BookCategory.MYSTERY: [
        Book(id=1, title="The Maltese Falcon"),
        Book(id=2, title="Murder on the Orient Express"),
        Book(id=3, title="The Hound of the Baskervilles"),
        Book(id=4, title="Da Vinci Code"),
    ],
    BookCategory.SCIENCE_FICTION: [
        Book(id=5, title="The Hitchhiker's Guide to the Galaxy"),
        Book(id=6, title="Ender's Game"),
        Book(id=7, title="The Dune Chronicles"),
        Book(id=8, title="Frankenstien"),
    ],
    BookCategory.SELF_HELP: [
        Book(id=9, title="The 7 Habits of Highly Effective People"),
        Book(id=10, title="How to Win Friends and Influence People"),
        Book(id=11, title="Man's Search for Meaning"),
        Book(id=12, title="When Breath Becomes Air"),
    ],
}


class InventoryService(inventory_pb2_grpc.InventoryBooksServicer):
    def Inventory(self, request, context):

       mystery_books = books_by_category[BookCategory.MYSTERY]

       science_fiction_books = books_by_category[BookCategory.SCIENCE_FICTION]

       self_help_books = books_by_category[BookCategory.SELF_HELP]

       all_books = mystery_books + science_fiction_books + self_help_books

       return InventoryResponse(books=all_books)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryBooksServicer_to_server(
        InventoryService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
