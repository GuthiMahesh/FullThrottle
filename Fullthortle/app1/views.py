from django.shortcuts import render
from django.http import HttpResponse


def autocomplete(request):
    # return render(request,"base.html")
    if request.is_ajax():
        q = request.GET.get('term', 'procrastination').capitalize()
        search_qs = model.objects.filter(name__startswith=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def search(request):
    return render(request, "base.html")
