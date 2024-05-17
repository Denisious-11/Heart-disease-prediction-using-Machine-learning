"""hp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hp_app.views import *


urlpatterns = [
    url(r'admin/', admin.site.urls),

##################################
    url(r'^$',display_login),
    url(r'^show_register',show_register,name='show_register'),
    url(r'^register',register,name='register'),
    url(r'^display_login',display_login,name='display_login'),
    url(r'^check_login',check_login,name='check_login'),
########################################

###################################
    url(r'^view_users_admin',view_users_admin,name="view_users_admin"),
    url(r'^manage_users_admin',manage_users_admin,name="manage_users_admin"),
    url(r'^admin1',admin1,name='admin1'),
    url(r'^User_view',User_view,name='User_view'),
    # url(r'^edit',edit,name="edit"),
##############################################

##############################

##############################

##############################
    url(r'^user',user,name='user'),
######################################

##############################
    url(r'^edit_patient',edit_patient,name="edit_patient"),
    url(r'^deletepatient',deletepatient,name="deletepatient"),
    url(r'^Reg_doctor',Reg_doctor,name="Reg_doctor"),
    url(r'^doctor_reg',doctor_reg,name="doctor_reg"),
    url(r'^view_doctors_admin',view_doctors_admin,name="view_doctors_admin"),
    url(r'^edit_doctor',edit_doctor,name="edit_doctor"),
    url(r'^deletedoctor',deletedoctor,name="deletedoctor"),
    url(r'^Prediction',Prediction,name="Prediction"),
    url(r'^check_heart',check_heart,name="check_heart"),
    url(r'^doctor_home',doctor_home,name="doctor_home"),
    url(r'^Chatpage',Chatpage,name='Chatpage'),
    url(r'^Doctor_list_pats',Doctor_list_pats,name="Doctor_list_pats"),
    url(r'^check_my_heart',check_my_heart,name="check_my_heart"),
    url(r'^view_doctors_user',view_doctors_user,name="view_doctors_user"),
    url(r'^Addchat',Addchat,name='Addchat'),
    url(r'^Getallchats',Getallchats,name='Getallchats'),
    url(r'^selectuser2',selectuser2,name="selectuser2"),
    url(r'^view_upload_file',view_upload_file,name="view_upload_file"),
    url(r'^upload_content',upload_content,name="upload_content"),
    url(r'^get_records',get_records,name="get_records"),
    url(r'^download',download,name="download"),
##############################
    ]
