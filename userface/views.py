from django.shortcuts import render,redirect
from django.views import generic
from .models import User,Vehicle, ParkingSpot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import RegisterForm,VehicleForm,ParkingSpaceForm
#from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geos import fromstr
from geopy.geocoders import  Nominatim
from geopy.exc import GeocoderTimedOut


def words_to_point(q):
    geolocator = Nominatim(user_agent = "driveways")
    location = geolocator.geocode(q)
    point = Point(location.latitude, location.longitude)
    return point

def index(request):

    return render(request, 'userface/index.html')






def search(request):

    if request.method == "GET":
        resultss = request.GET.get('results', False)
        if not resultss:
            resultss = ""

        try:

            destination = words_to_point(resultss)

        except (GeocoderTimedOut, AttributeError) as e:
            request.session['location'] = "Location cannot be determined"
            return render(request, 'userface/search.html', {'resultss': resultss})

        request.session['location'] = "unknown"
        if request.user.is_authenticated:
            request.session['location'] = []
            near_spots = ParkingSpot.objects.filter(location__distance_lt=(destination, Distance(km=3)))
            for spot in near_spots:
                request.session['location'].append(spot.address)
    return render(request, 'userface/search.html', {'resultss':resultss})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/userface")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})



class VehicleListView(LoginRequiredMixin,generic.ListView):
    model = Vehicle
    #context_object_name = 'vehicles'
    template_name = 'userface/user_vehicle_list.html'
    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)[:5]


def registervehicle(response):
    if response.method == "POST":
        form = VehicleForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/userface")
    else:
        form = VehicleForm()

    return render(response, "userface/register_vehicle.html", {"form": form})








