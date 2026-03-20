from django.shortcuts import render, redirect

def sales(request):
    return render(request, "formApp/Biodata.html")


def sales_output(request):
    if request.method == "POST":
        context = {
            "name": request.POST.get("name"),
            "dob": request.POST.get("dob"),
            "gender": request.POST.get("gender"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "address": request.POST.get("address"),
            "qualification": request.POST.get("qualification"),
            "skills": request.POST.get("skills"),
        }
        return render(request, "formApp/Biodata_output.html", context)

    return redirect("Biodata")