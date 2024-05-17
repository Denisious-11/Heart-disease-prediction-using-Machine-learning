from django.shortcuts import render
from .models import *

from django.views.decorators.cache import cache_control
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
import json
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import joblib
from datetime import datetime
from datetime import date
from django.views.decorators.csrf import ensure_csrf_cookie
import pickle
import numpy as np
import os
model = joblib.load("DNNmodel.h5")
datas=""


def display_login(request):
    return render(request, 'login.html', {})


def admin1(request):
    return render(request, 'home_admin.html', {})


def show_register(request):
    return render(request, 'register.html', {})


def view_users_admin(request):
    ob = Patients_table.objects.all()
    return render(request, 'view_users_admin.html', {"data": ob})


def manage_users_admin(request):
    return render(request, 'manage_users_admin.html', {})


def user(request):
    return render(request, 'home_user.html', {})


def doctor_home(request):
    return render(request, 'home_doctor.html', {})


def Reg_doctor(request):
    return render(request, 'Doctor_reg.html', {})


def Add_product(request):
    return render(request, 'admin_add_product.html', {})


def Prediction(request):
    return render(request, 'prediction3.html',)


def view_doctors_admin(request):
    ob = Doctor_table.objects.all()
    return render(request, 'view_doctors_admin.html', {"data": ob})



def Doctor_list_pats(request):
    ob = Patients_table.objects.all()
    return render(request, 'doctor_view_users.html', {"data": ob})


def check_login(request):
    var1 = request.GET.get("uname")
    var2 = request.GET.get("password")
    utyp = request.GET.get("utyp")
    print(var1, var2, utyp)
    data = {}
    if(utyp == "doc"):
        try:
            Doctor_table.objects.get(username=var1, password=var2)
            request.session["username"] = var1
            data["msg"] = "doc"
            print("login")
            return JsonResponse(data, safe=False)
        except:
            data["msg"] = "no"
            return JsonResponse(data, safe=False)
    else:
        try:
            Patients_table.objects.get(username=var1, password=var2)
            request.session["username"] = var1
            data["msg"] = "pat"
            print("login")
            return JsonResponse(data, safe=False)
        except:
            data["msg"] = "no"
            return JsonResponse(data, safe=False)


def register(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    age = request.GET.get("age")
    gender = request.GET.get("gender")
    phone = request.GET.get("phone")
    password = request.GET.get("password")
    username = request.GET.get("username")
    try:
        ob = Patients_table(name=name, age=age, gender=gender, email=email,
                            phone=phone, username=username, password=password)

        ob.save()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except:

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def doctor_reg(request):
    print("yes")
    name = request.GET.get("name")
    email = request.GET.get("email")
    place = request.GET.get("place")
    phone = request.GET.get("phone")
    password = request.GET.get("password")
    username = request.GET.get("username")
    print(name, email, place, phone, password, username)
    try:
        ob = Doctor_table(name=name, place=place, email=email,
                          phone=phone, username=username, password=password)

        ob.save()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def edit_doctor(request):
    uid = request.GET.get("uid")
    name = request.GET.get("name")
    email = request.GET.get("email")
    place = request.GET.get("place")

    phone = request.GET.get("phone")
    password = request.GET.get("password")
    username = request.GET.get("username")
    print("userid==", uid)
    try:
        ob = Doctor_table.objects.get(id=int(uid))
        ob.name = name
        ob.place = place
        ob.email = email
        ob.phone = phone
        ob.username = username
        ob.password = password

        ob.save()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def edit_patient(request):
    uid = request.GET.get("uid")
    name = request.GET.get("name")
    email = request.GET.get("email")
    age = request.GET.get("age")
    gender = request.GET.get("gender")
    phone = request.GET.get("phone")
    password = request.GET.get("password")
    username = request.GET.get("username")
    print("userid==", uid)
    try:
        ob = Patients_table.objects.get(id=int(uid))
        ob.name = name
        ob.age = age
        ob.gender = gender
        ob.email = email
        ob.phone = phone
        ob.username = username
        ob.password = password

        ob.save()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def deletepatient(request):
    uid = request.GET.get("uid")

    print("userid==", uid)
    try:
        ob = Patients_table.objects.get(id=int(uid))

        ob.delete()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def deletedoctor(request):
    uid = request.GET.get("uid")

    print("userid==", uid)
    try:
        ob = Doctor_table.objects.get(id=int(uid))

        ob.delete()
        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def handle_uploaded_file(f, name):
    print(name)
    filename = 'F:/Project 2021-22/Cardiovascular/hp_app/static/images/' + \
        str(name)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)




# def check_my_heart1(request):
#     hdata = request.GET.get("val")

#     try:
#         print("hdata", hdata)
#         hlist = hdata.split(",")
#         feats = [float(x) for x in hlist]
#         ytest = [feats]
#         ypred = model.predict(ytest)
#         print(ypred)
#         if(ypred[0] == 0):
#             res = "Normal Condition"
#         else:
#             res = "Presence of heart disease,Please consult a doctor immediately"
#         data = {"status": res}
#         print("result", res)
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         print(e)

#         data = {"status": 0}
#         return JsonResponse(data, safe=False)


def check_my_heart(request):
    # try:
        # Get data from the request
    age = float(request.GET.get("age"))
    sex = float(request.GET.get("sex"))
    chest_pain_type = float(request.GET.get("chest_pain_type"))
    resting_blood_pressure = float(request.GET.get("resting_blood_pressure"))
    cholesterol = float(request.GET.get("cholesterol"))
    fasting_blood_sugar = float(request.GET.get("fasting_blood_sugar"))
    resting_ecg = float(request.GET.get("resting_ecg"))
    max_heart_rate = float(request.GET.get("max_heart_rate"))
    exercise_induced_angina = float(request.GET.get("exercise_induced_angina"))
    oldpeak = float(request.GET.get("oldpeak"))
    slope = float(request.GET.get("slope"))
    num_vessels = float(request.GET.get("num_vessels"))
    thal = float(request.GET.get("thal"))
    
    # Create feature vector
    features = np.array([[age, sex, chest_pain_type, resting_blood_pressure, cholesterol,
                          fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_induced_angina,
                          oldpeak, slope, num_vessels, thal]])
    
    # Use your model to predict
    y_pred = model.predict(features)
    
    # Determine result based on prediction
    if y_pred[0] == 0:
        result = "Normal Condition"
    else:
        result = "Presence of heart disease. Please consult a doctor immediately."
    
    # Prepare response
    response_data = {"status": result}
    
    return JsonResponse(response_data, safe=False)
    
    # except Exception as e:
    #     print(e)
    #     # If an error occurs during processing, return status 0
    #     response_data = {"status": 0}
    #     return JsonResponse(response_data, safe=False)



def check_heart(request):
    age = request.GET.get("age")
    sex = request.GET.get("sex")
    cp = request.GET.get("cp")
    rbp = request.GET.get("rbp")
    schol = request.GET.get("schol")
    fbs = request.GET.get("fbs")
    recg = request.GET.get("recg")
    maxhr = request.GET.get("maxhr")
    exang = request.GET.get("exang")
    opk = request.GET.get("opk")
    spk = request.GET.get("spk")
    nmv = request.GET.get("nmv")
    thal = request.GET.get("thal")
    hlist=[age,sex,cp,rbp,schol,fbs,recg,maxhr,exang,opk,spk,nmv,thal]
    print(hlist)
    try:
        # print("hdata", hdata)
        
        feats = [float(x) for x in hlist]
        ytest = [feats]
        ypred = model.predict(ytest)
        
        print(ypred)
        if(ypred[0] == 0):
            res = "Normal Condition"
        else:
            res = "Presence of heart disease,Please consult a doctor immediately"
        data = {"status": res}
        print("result", res)
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)

def selectuser2(request):
    uid = request.GET.get("uid")
    utyp = request.GET.get("utyp")

    print("userid==", uid)

    print("utyp==", utyp)
    try:
        if(utyp == 'doc'):
            ob = Doctor_table.objects.get(id=int(uid))
            unm = ob.username
            request.session["user2"] = unm
        else:
            ob = Patients_table.objects.get(id=int(uid))
            unm = ob.username
            request.session["user2"] = unm

        data = {"status": 1}
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)

        data = {"status": 0}
        return JsonResponse(data, safe=False)


def Chatpage(request):
    return render(request, 'Chatpage.html', {})

def view_doctors_user(request):
    ob = Doctor_table.objects.all()
    return render(request, 'user_view_doctors.html', {"data": ob})

def Getallchats(request):
    sndr = request.session["username"]
    rcvr = request.session["user2"]

    ob = Chat_table.objects.filter(
        From=sndr, To=rcvr) | Chat_table.objects.filter(From=rcvr, To=sndr)
    mylist = []
    for i in ob:
        li1 = []
        if(i.From == sndr):
            li1.append("You")
        else:
            li1.append(rcvr)
        li1.append(i.chat)
        mylist.append(li1)
    print(mylist)

    resp = {}
    resp["datalist"] = mylist
    return JsonResponse(resp, safe=False)


def Addchat(request):
    msg = request.GET.get("qstn")
    sndr = request.session["username"]
    rcvr = request.session["user2"]
    ob = Chat_table(From=sndr, To=rcvr, chat=msg)
    ob.save()
    data = {"msg": "yes"}

    return JsonResponse(data, safe=False)



def User_view(request):
    try:
        v1 = Patients_table.objects.all()
        print(v1, "d")
        data = {}
        if v1:
            valu = serializers.serialize("json", v1)
            data['d1'] = json.loads(valu)
            return JsonResponse(data, safe=False)
        else:
            return HttpResponse("no data")
    except Exception as e:
        print(e)
        return HttpResponse("error")


def view_upload_file(request):
    return render(request, 'upload_record.html', {})


def upload_content(request):
    username=request.session["username"]
    
    f2= request.FILES["file"]
    file_name=str(f2.name)


    print("f2: ",f2)
    print("file_name: ",file_name)

    if Files.objects.filter(filename=file_name).exists():
        return HttpResponse("<script>alert('File with this name already exists');window.location.href='/view_upload_file/'</script>")

    else:

        fs1 = FileSystemStorage("hp_app/static/files/"+username)#%username
        fs1.save(file_name, f2)

        f1=open("hp_app/static/files/"+username+"/"+file_name,'rb')
        content=f1.read()
        f1.close()
        print("Content : ",content)

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("Current Time =", time)

        today = date.today()
        current_date = today.strftime("%d/%m/%Y")
        print("date =",current_date)

        obj1=Files(filename=file_name,username=username,date=current_date,time=time)
        obj1.save()

        return HttpResponse("<script>alert('File Uploaded Successfully');window.location.href='/view_upload_file/'</script>")


def get_records(request):
    req_list=Files.objects.all()
    return render(request,'all_files_view.html',{'req': req_list}) 



def download(request):
    f_id=request.POST.get("f_id")
    filename=request.POST.get("filename")
    username=request.POST.get("username")
    print("**************")
    print(filename)
    print(username)

    if True:
        
        file1_path = "hp_app/static/files/"+username+"/"+filename
        print(os.path.exists(file1_path))
        print(file1_path)

        if os.path.exists(file1_path):
            with open(file1_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file1_path)
                return response
        raise HttpResponse("<script>alert('File does not exists');window.location.href='/get_records/'</script>")
    return HttpResponse("<script>alert('File Downloaded Successfully');window.location.href='/get_records/'</script>")

# def edit(request):
#     user_id = request.GET.get("id2")
#     user_name = request.GET.get("uname")
#     phone = request.GET.get("phone")

#     e = Users.objects.get(user_id=int(user_id))
#     e.user_name=user_name
#     e.phone = phone
#     e.save()

#     return HttpResponse("edited successfully")


# def block(request):
#     user_name = request.GET.get("uname")
#     id2 = request.GET.get("id2")
#     v = Users.objects.get(user_id=id2)
#     v.flag = '1'
#     v.save()
#     return HttpResponse("successfully blocked")


# def Block_un(request):
#     user_name = request.GET.get("uname")
#     id2 = request.GET.get("id2")
#     v = Users.objects.get(user_id=id2)
#     v.flag = '0'
#     v.save()
#     return HttpResponse("successfully unblocked")


# def get_emotion_user(request):
#     return render(request, "get_emotion_user.html", {})


# def insert(request):
#     image = request.POST.get("img")
#     img = request.FILES["img"]
#     fs = FileSystemStorage("hp_app\\static")
#     fs.save(image, img)

#     return render(request, 'get_emotion_user.html', {'image': img})


# def get_emotion(request):
#     path = request.GET.get("path")

#     a = "hp_app/"
#     final_path = a+path
#     print(final_path)

#     # analysing image using DeepFace
#     face_analysis = DeepFace.analyze(img_path=final_path)
#     # print("Face Analysis :",face_analysis)

#     print("Emotion :", face_analysis["dominant_emotion"])
#     my_emotion = face_analysis["dominant_emotion"]
#     return HttpResponse(my_emotion)


# def get_water_info(request):
#     return render(request, 'get_water_info_user.html', {})


# def consultant(request):
#     return render(request, 'home_consultant.html', {})


# def psychologist(request):
#     return render(request, 'home_psychologist.html', {})


# def Bot_response(request):
#     qstn = request.GET.get("qstn")
#     print(qstn)

#     response = chatbot.get_response(qstn)
#     print("bot-->", response)
#     print(str(response))
#     data = {"msg": str(response)}
#     return JsonResponse(data, safe=False)


# def surveypage(request):
#     return render(request, 'survey.html', {})
