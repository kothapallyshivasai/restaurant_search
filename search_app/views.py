from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Restaurant
import json

@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        query = request.POST.get('search_bar')
        matching_restaurant_items = {}

        if query:
            matching_restaurants = Restaurant.objects.filter(items__icontains=query)
        
        for restaurant in matching_restaurants:
            items = json.loads(restaurant.items)
            matching_items = {key: value for key, value in items.items() if query in key.lower()}

            if matching_items:
                matching_restaurant_items[restaurant.name] = matching_items        

        return render(request, 'index.html', {'matching_restaurant_items': matching_restaurant_items})

    return render(request, 'index.html', {})
