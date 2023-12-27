from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about_view, name="about"),
    path("contact", views.contact_view, name="contact"),
    path("product", views.product_view, name="product"),
    path("digital", views.digital_view, name="digital"),
    path("websitedesign", views.website_view, name="websitedesign"),
    path("graphic", views.graphic_view, name="graphic"),
    path("domain", views.domain_view, name="domain"),
    path("content", views.content_view, name="content"),
     path("application", views.application_view, name="application"),
     path("crm", views.crm_view, name="crm"),
     path("android", views.android_view, name="android"),
     path("corporate", views.corporate_view, name="corporate"),
     path("brochure", views.brochure_view, name="brochure"),
     path("pamphlets", views.pamphlets_view, name="pamphlets"),
     path("stationery", views.stationery_view, name="stationery"),
     path("tally", views.tally_view, name="tally"),
     path("webapplication", views.webapplications_view, name="webapplications"),
     path("hybrid", views.hybrid_view, name="hybrid"),
     path("windows", views.windows_view, name="windows"),
     path("customised", views.customised_view, name="customised"),
     path("ecommerce", views.ecommerce_view, name="ecommerce"),
     path("portals", views.portals_view, name="portals"),
     path("cms", views.cms_view, name="cms"),
     path("ui", views.ui_view, name="ui"),
     path("landing", views.landing_view, name="landing"),
     path("corporatewebsite", views.corporatewebsite_view, name="corporatewebsite"),
     path("enquiry", views.enquiry_view, name="enquiry"),
     path("vehicle", views.vehicle_view, name="vehicle"),
     path("astrology", views.astrology_view, name="astrology"),
     path("foodorder", views.foodorder_view, name="foodorder"),
     path("manufacture", views.manufacture_view, name="manufacture"),
     path("joinapp", views.joinapp_view, name="joinapp"),
     path("subscription", views.subscription_view, name="subscription"),
     path("community", views.community_view, name="community"),
     path("portfolio", views.portfolio_view, name="portfolio"),
     path("conceptuallogo", views.conceptuallogo_view, name="conceptuallogo")
    
     
]