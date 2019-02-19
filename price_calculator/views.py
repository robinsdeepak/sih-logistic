from django.shortcuts import render
from django.http import JsonResponse
from price_calculator.models import PricingModel


def Calculate(request):
    pricing_obj = PricingModel.objects.all()[0]
    tax = pricing_obj.service_tax

    # Posted form data
    time = request.POST['time']
    volume = request.POST['volume']
    weight = request.POST['time']
    distance = request.POST['distance']

    delivery_price = (time * pricing_obj.price_per_time + volume * pricing_obj.price_per_volume +
                      distance * pricing_obj.price_per_distance + weight * pricing_obj.price_per_weight)

    total_price = delivery_price * (1 + tax)

    return JsonResponse({"total_price": total_price})
