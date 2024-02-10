from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

def user_profile(req):
    return JsonResponse(
        {
         "Name": "Ibukun Ayomide-Baafog",
         "Email": "ibukun.baafog@meltwater.org", 
         "Phone-no": "+233535320858"
         
         }
        )

def filter_queries(req, query_id):
    return JsonResponse(
        {
        "ID": query_id,
        "Title": "Filtering",
        "Description": "How to filter your queries",
        "Status": "ongoing",
        "Submitted by": "Ibukun Ayomide-Baafog"
    }
        )

class Queryview(View):
    queries = [
        {"id": 1, "title": "Adama declined"},
        {"id": 2, "title": "Shots fired"}
        ]
   
    def get(self, request):
        
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse ({"status": "ok"})

