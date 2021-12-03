
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import requests
from studentsapp.forms import StudentForm

# def StudentListView(request):
#     response = requests.get("http://127.0.0.1:7345/api/students/")
#
#     if response.status_code==200:
#         try:
#             dict_data = json.loads(response.text)
#         except ValueError:
#             return HttpResponse({"message" : "Sorry, you are not getting JSON response"})
#         else:
#             return HttpResponse(dict_data)
#     else:
#         return HttpResponse(response.text)


def StudentListView(request):
    response = requests.get("http://127.0.0.1:7345/api/students/")

    if response.status_code==200:
        try:
            student_list = json.loads(response.text)
            context = {
                "student_list" : student_list
            }
            return render(request,'studentsapp/student_list.html',context)

        except ValueError:
            context ={
                "error" : "Sorry, you are not getting JSON response"
            }
            return render(request, 'studentsapp/student_list.html', context)

    else:
        context = {
            "error" : "Requsted information not available"
        }
        return render(request, 'studentsapp/student_list.html', context)


def StudentDetailView(request,pk):
    response = requests.get("http://127.0.0.1:7345/api/students/"+str(pk)+'/')

    if response.status_code==200:
        try:
            student = json.loads(response.text)
            context = {
                "student" : student
            }
            return render(request,'studentsapp/student_detail.html',context)

        except ValueError:
            context ={
                "error" : "Sorry, you are not getting JSON response"
            }
            return render(request, 'studentsapp/student_detail.html', context)

    else:
        context = {
            "error" : "Requsted information not available"
        }
        return render(request, 'studentsapp/student_detail.html', context)


def StudentDeleteView(request,pk):
    if request.method=='POST':
        response = requests.delete("http://127.0.0.1:7345/api/students/" + str(pk) + '/')

        if response.status_code==204:
            return redirect('student_list')
        else:
            context = {
                "error" : "Some thing wrong. Record not deleted.Try Again"
            }
            return render(request, 'studentsapp/student_confirm_delete.html', context)

    else:
        response = requests.get("http://127.0.0.1:7345/api/students/" + str(pk) + '/')

        if response.status_code == 200:
            try:
                student = json.loads(response.text)
                context = {
                    "student": student
                }
                return render(request, 'studentsapp/student_confirm_delete.html', context)

            except ValueError:
                context = {
                    "error": json.loads(response.text)
                }
                return render(request, 'studentsapp/student_confirm_delete.html', context)

        else:
            context = {
                "error": json.loads(response.text)
            }
            return render(request, 'studentsapp/student_confirm_delete.html', context)


def StudentCreateView(request):
    if request.method=='POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            sno = request.POST.get('sno')
            sname = request.POST.get('sname')
            marks = request.POST.get('marks')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')

            payload = {
                "sno" : sno,
                "sname" : sname,
                "marks" : marks,
                "address" : address,
                "mobile" : mobile,
            }

            response = requests.post("http://127.0.0.1:7345/api/students/",data=payload)

            if response.status_code==201:
                return redirect('student_list')
            else:
                context ={
                    "error" : json.loads(response.text)
                }
                return render(request,'studentsapp/student_form.html',context)

        else:
            context = {
                "error" : "Please send proper data for all fields"
            }
            return render(request,'studentsapp/student_form.html',context)

    else:
        form = StudentForm()
        context = {'form' : form}
        return render(request,'studentsapp/student_form.html',context)



def StudentUpdateView(request,pk):
    if request.method=='POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            sno = request.POST.get('sno')
            sname = request.POST.get('sname')
            marks = request.POST.get('marks')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')

            payload = {
                "sno" : sno,
                "sname" : sname,
                "marks" : marks,
                "address" : address,
                "mobile" : mobile,
            }

            response = requests.put("http://127.0.0.1:7345/api/students/"+str(pk)+"/",
                                    data=payload)

            if response.status_code==200:
                return redirect('student_list')
            else:
                context ={
                    "error" : json.loads(response.text)
                }
                return render(request,'studentsapp/student_update.html',context)

        else:
            context = {
                "error" : "Please send proper data for all fields"
            }
            return render(request,'studentsapp/student_form.html',context)

    else:
        response = requests.get("http://127.0.0.1:7345/api/students/" + str(pk) + '/')

        if response.status_code == 200:
            try:
                student = json.loads(response.text)
                context = {
                    "student": student
                }
                return render(request, 'studentsapp/student_update.html', context)

            except ValueError:
                context = {
                    "error": json.loads(response.text)
                }
                return render(request, 'studentsapp/student_update.html', context)

        else:
            context = {
                "error": json.loads(response.text)
            }
            return render(request, 'studentsapp/student_update.html', context)






        form = StudentForm()
        context = {'form' : form}
        return render(request,'studentsapp/student_form.html',context)











