from django.shortcuts import render
from . models import Order

# Create your views here.
def index(request):
    return render(request, "website/index.html")



def about_view(request):
     return render(request, "website/about.html")


def contact_view(request):
     if request.method == 'GET':
          return render(request, "website/contact.html")
     else:
          if not request.POST['first_name'] or not request.POST['last_name'] or not request.POST['email'] or not request.POST['number'] or not request.POST['subject'] or not request.POST['message']:
               return render(request, "website/contact.html", {
               "error": "x"
               })
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          email = request.POST['email']
          phone = request.POST['number']
          sub = request.POST['subject']
          message= request.POST['message']

          var = Order(first_name=first_name, last_name=last_name, email=email, phone=phone, subject=sub, message=message)

          var.save()
          return render(request, "website/contact.html", {
               "bolt": "x",
               "first_name": first_name,
               "last_name": last_name,
          })

def product_view(request):
     return render(request, "website/product.html")


def digital_view(request):
     return render(request, "website/digital.html")

def graphic_view(request):
     return render(request, "website/graphic.html")

def website_view(request):
     return render(request, "website/websitedesign.html")


def content_view(request):
     return render(request, "website/content.html")


def domain_view(request):
     return render(request, "website/domain.html")

def application_view(request):
     return render(request, "website/application.html")

def crm_view(request):
     return render(request, "website/crm.html")

def android_view(request):
     return render(request, "website/android.html")


def tally_view(request):
     return render(request, "website/tally.html")

def corporate_view(request):
     return render(request, "website/corporate.html")

def brochure_view(request):
     return render(request, "website/brochure.html")


def pamphlets_view(request):
     return render(request, "website/pamphlets.html")


def stationery_view(request):
     return render(request, "website/stationery.html")

def webapplications_view(request):
     return render(request, "website/webapplications.html")


def hybrid_view(request):
     return render(request, "website/hybrid.html")


def windows_view(request):
     return render(request, "website/windows.html")


def customised_view(request):
     return render(request, "website/customised.html")


def cms_view(request):
     return render(request, "website/cms.html")



def ecommerce_view(request):
     return render(request, "website/ecommerce.html")


def corporatewebsite_view(request):
     return render(request, "website/corporatewebsite.html")



def portals_view(request):
     return render(request, "website/portals.html")



def ui_view(request):
     return render(request, "website/ui.html")


def landing_view(request):
     return render(request, "website/landing.html")


def enquiry_view(request):
     return render(request, "website/enquiry.html")

def vehicle_view(request):
     return render(request, "website/vehicle.html")

def astrology_view(request):
     return render(request, "website/astrology.html")

def foodorder_view(request):
     return render(request, "website/foodorder.html")

def manufacture_view(request):
     return render(request, "website/manufacture.html")

def joinapp_view(request):
     return render(request, "website/joinapp.html")

def subscription_view(request):
     return render(request, "website/subscription.html")

def community_view(request):
     return render(request, "website/community.html")

def portfolio_view(request):
     return render(request, "website/portfolio.html")

def conceptuallogo_view(request):
     return render(request, "website/conceptuallogo.html")



