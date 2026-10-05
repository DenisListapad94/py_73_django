from django.shortcuts import render, HttpResponse

def booking(request):
    template_name = "booking.html"
    test_go_to_template = 1
    test_list_to_template = ["python","go","ruby"]
    test_dict_to_templates = {
        "Jessi" : {
            "monday" : "9-18",
            "tuesday" :  "weekend",
            "wednesday": '11-19'
        },
        "Tom": {
            "monday": "weekend",
            "tuesday": "weekend",
            "wednesday": '9-21'
        }
    }
    context = {
        "test1": test_go_to_template,
        "test_list": test_list_to_template,
        "peoples": test_dict_to_templates
    }
    return render(request, template_name=template_name,context=context)


def about(request):
    template_name = "about.html"
    return render(request, template_name=template_name)

def home(request, home: int):
    template_name = "home.html"
    context = {
        "home": home
    }
    return render(request, template_name=template_name, context=context)