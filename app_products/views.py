from rest_framework import views
from rest_framework.response import Response
from django.core.cache import cache
from .models import Products
from django.db.models import Avg, Sum, F

TTL = 60 * 5

class ProductsViewset(views.APIView):
    def get(self, request):
        try:
            category = request.query_params.get('category')
            min_price = request.query_params.get('min_price')
            max_price = request.query_params.get('max_price')
            
            # check if cache exists
            cache_key = f'products_analytics_{category}_{min_price}_{max_price}'
            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data)
            
            queryset = Products.objects.all()

            # Filtering
            if category:
                queryset = queryset.filter(category__iexact=category)
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
                
            # Aggregation
            total_products = queryset.count()
            average_price = queryset.aggregate(avg_price=Avg('price'))['avg_price'] or 0
            total_stock_value = queryset.aggregate(stock_value=Sum(F('stock') * F('price')))['stock_value'] or 0

            response_data = {
                "total_products": total_products,
                "average_price": round(average_price, 2),
                "total_stock_value": round(total_stock_value, 2),
            }
            # Setting cache
            cache.set(cache_key, response_data, TTL)
            return Response({'res': response_data})
        except Exception as e:
            print(f'Error {str(e)}')
    