from django.shortcuts import render

# Create your views here.
def blogdetails(request):
    return render(request, 'pagesapp/blogdetails.html')

def chackout(request):
    return render(request, 'pagesapp/checkout.html')

def shopdetails(request):
    return render(request, 'pagesapp/shopdetails.html')

def shopingcart(request):
    return render(request, 'pagesapp/shopingcart.html')