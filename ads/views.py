from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from ads.models import Category, Ads
import json
from django.views.decorators.csrf import csrf_exempt


def status(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for cat in categories:
            response.append({
                "id": cat.id,
                "name": cat.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)

    def post(self, request):
        cat_data = json.loads(request.body)

        category = Category()
        category.name = cat_data["name"]

        category.save()

        return JsonResponse(cat_data)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()

        response = []
        for a in ads:
            response.append({
                    "id": a.id,
                    "name": a.name,
                    "author": a.author,
                    "price": a.price,
                    "description": a.description,
                    "address": a.address,
                    "is_published": a.is_published
                })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ads()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse(ad_data)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
                "id": cat.id,
                "name": cat.name
            }, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published
                }, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)
