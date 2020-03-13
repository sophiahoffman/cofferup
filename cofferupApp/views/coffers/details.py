import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from cofferupApp.models import Library

def get_coffer(coffer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT l.id, l.title, l.address
        FROM cofferapp_coffer l
        WHERE l.id = ?
        """,
        (coffer_id,))

        coffer_to_view = db_cursor.fetchone()

        return coffer_to_view

@login_required
def coffer_details(request, coffer_id):
    if request.method == 'GET':
        coffer = get_coffer(coffer_id)

        template = 'libraries/detail.html'
        context = {'coffer': coffer}

        return render(request, template, context)

class Coffers(ViewSet):
    """Orders view for Bangazon API"""
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Order instance
        """
        # Start by creating a new instance of the Order model
        new_coffer = Coffer()
        # The request.data["str"] expression evaluates the key names from your models and saves those values in your new model instance.
        new_coffer.name = request.data["name"]
        new_coffer.description = request.data["description"]  
        new_coffer.save() # saves your instance to the db

        # Pass the new model instance into the serializer, while declaring the context object as request serialized instance
        serializer = OrderSerializer(new_coffer, context={'request': request})
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single order

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            order_to_delete = Order.objects.get(pk=pk)
            order_to_delete.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except order_to_delete.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for a single itinerary item

        Returns:
            Response -- JSON serialized itinerary instance
        """
        try:
            single_order_record = Order.objects.get(pk=pk)
            serializer = OrderSerializer(single_order_record, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    
    # ! Ask why this one doesn't work but the other one does with a different naming convention
    # def retrieve(self, request, pk=None):
    #     """Handles the GET request for a single order
        
    #     Returns:
    #         -- A JSON serialized response object
    #     """
        
    #     try:
    #         # Store a ref to the specific resource in a variable
    #         order = Order.objects.get(pk=pk) # Call .objects on the model
    #         # Serialize the response and store it in a variable
    #         serializer = OrderSerializer(order, context={'request', request})
    #         # Return the serialized response object
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)
        
    def list(self, request):
        """Handles a GET request for all orders
        
        Returns:
            A serialized list of all orders
        """
        
        # Get all instances of orders from the db and store in the orders variable
        orders = Order.objects.all()

        serializer = OrderSerializer(
            orders,
            many=True,
            context={'request':request}
        )
        return Response(serializer.data)
        