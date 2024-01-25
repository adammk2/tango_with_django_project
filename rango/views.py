from django.shortcuts import render
from rango.models import Category
from rango.models import Page

# Create your views here.

from django.http import HttpResponse

def index(request):
    # Query the database for a list of all categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in out context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Get category from slug, if not exists, throws error.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all pages in category
        pages = Page.objects.filter(category=category)

        # Add results list to template context under name pages.
        context_dict['pages'] = pages

        # Add category from database to context dict, use this in template to verify it exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # If don't find category, do nothing.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Render response and return it to the client
    return render(request, 'rango/category.html', context=context_dict)
