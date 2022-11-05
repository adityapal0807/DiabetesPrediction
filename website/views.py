from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
import joblib
import numpy as np

LOCATION = {
    'red':['Russia','India','Pakistan','China','United States of America','Indonesia'],
    'orange':['Brazil','Egypt','Italy','Germany','United Kingdom','Iran','Turkey','Japan','Bangladesh','Vietnam','Philippines','Malta'],
    'yellow':['Canada','Mexico','Colombia','Venezuela','Chile','Peru','Argentina','South Africa','Angola','Democratic Republic of the Congo',
                                'Uganda','Tanzania','Kenya','Sudan','Ethiopia','Ghana','Nigeria','Algeria','Morocco','Yemen','Saudi Arabia',
                                'Iraq','Syria','Spain','Portugal','France','Belgium','Netherlands','Greece','Romania','Ukraine','Sweden','Kazakhstan',
                                'Uzbekistan','Afghanistan','Nepal','Sri Lanka','Malaysia','Myanmar (formerly Burma)','Australia','North Korea','South Korea','Andorra',
                                'Cabo Verde','Cyprus','Czechia (Czech Republic)','Holy See','Hungary','Lebanon','Singapore','Switzerland','Liechtenstein',
                                'Luxembourg','Monaco','Poland'],
    'green':['Antigua and Barbuda','Bahamas','Barbados','Cuba','Dominica','Dominican Republic','Grenada','Haiti','Jamaica','Saint Kitts and Nevis',
                                'Saint Lucia','Saint Vincent and the Grenadines','Trinidad and Tobago','Ecuador','Bolivia',"CÃ´te d'Ivoire'",'Burkina Faso',
                                'Libya','Senegal','Gambia','Zambia','Zimbabwe','Malawi','Mozambique','Madagascar','Somalia','Jordan','United Arab Emirates',
                                'Azerbaijan','Bulgaria','Belarus','Norway','Ireland','Tajikistan','Cambodia','Papua New Guinea','Austria','Brunei',
                                'Cameroon','Comoros','Finland','Israel','Thailand','Mali','Mauritius','Niger'],
    'purple':['Denmark','Marshall Islands'],
    'dark blue':['Iceland','Guyana','Suriname','Guinea-Bissau','Equatorial Guinea','Djibouti','Eswatini (fmr. "Swaziland")','Bhutan','Bosnia and Herzegovina'],
    'light blue':['Uruguay','Paraguay','Namibia','Botswana','Rwanda','Burundi','Eritrea','Oman','Qatar','Kuwait','Liberia','Sierra Leone',
                                    'Guinea','Gabon','Congo (Congo-Brazzaville)','Central African Republic','Chad','South Sudan','Lesotho','Estonia',
                                    'Latvia','Lithuania','Georgia','Turkmenistan','Kyrgyzstan','Mongolia','Laos','Fiji','New Zealand','Albania','Armenia','Bahrain',
                                    'Belize','Benin','Costa Rica','Croatia','El Salvador','Guatemala','Kiribati','Maldives','Mauritania','Moldova']
}

color_weight = {
    'red' : 1.177,
    'orange': 0.132,
    'yellow': 0.065,
    'green' : 0.013,
    'light blue' : 0.006,
    'dark blue' : 0.001,
    'purple' : 0
}
        

def index(request):
    return render(request,'website/index.html')

def location(request):
    if request.method == 'GET':
        all_countries=[]
        for a in LOCATION.values():
            for b in a:
                all_countries.append(b)

            
        return render(request,'website/location.html',{
            'countries': sorted(all_countries)
        })
    else:
        global user_location
        global location_numb 
        user_location = request.POST['country']
        for loc in LOCATION:
            if user_location in LOCATION[loc]:
                location_numb = color_weight[loc]
        return redirect(predict)
        

def predict(request):
    if request.method == 'POST':
        user = Info()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        sex = request.POST['sex_input']
        pregnancies = request.POST['pregnancy_input']
        glucose = request.POST['glucose_input']
        blood_pressure = request.POST['bp_input']
        skin_thickness = request.POST['skin_input']
        insulin = request.POST['insulin_input']
        bmi = request.POST['bmi_input']
        dpf = request.POST['dpf_input']
        age = request.POST['age_input']

        user.first_name = first_name
        user.last_name = last_name
        user.sex = sex
        user.glucose = glucose
        user.blood_pressure = blood_pressure
        user.skin_thickness = skin_thickness
        user.insulin = insulin
        user.bmi = bmi
        user.dpf= dpf
        user.location = user_location
        user.age = age



        if request.POST['sex_input'] == 'Female':
            if not request.POST['pregnancy_input']:
                return render(request,'website/predict.html',{
                    'error': 'Since You Selected Female, Please select this field'
                })
            else:
                user_values = np.array([pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]).reshape(1,-1)
                model = joblib.load('website/static/website/models/RFR_model_Female.sav')
                result = model.predict(user_values)

                user.pregnancies = pregnancies
                user.result = result[0]
                user.save()

                return render(request,'website/result.html',{
                    'sex': sex,
                    'first_name': first_name,
                    'last_name':last_name,
                    'result': (float(result[0])*100)+location_numb,
                    'location_weight': location_numb,
                    'result_brand': int((float(result[0])*100)+location_numb),
                    'country':user_location
                })
                
        else:
            user_values = np.array([glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]).reshape(1,-1)
            model = joblib.load('website/static/website/models/RFR_model_Male.sav')
            result = model.predict(user_values)

            user.result = result[0]
            user.save()

            return render(request,'website/result.html',{
                'sex': sex,
                'first_name': first_name,
                'last_name':last_name,
                'result': (float(result[0])*100)+location_numb,
                'location_weight': location_numb,
                'result_brand': int((float(result[0])*100)+location_numb),
                'country':user_location
            })

        
    else:
        return render(request,'website/predict.html',{
            'message': user_location
        })

def dpf(request):
    if request.method == "POST":
        global no_of_siblings
        no_of_siblings = [i for i in range(int(request.POST['no_of_siblings']))]
        print(no_of_siblings)
        return redirect(family)
    else:
        return render(request,'website/sibling_input.html')

def family(request):
    if request.method == 'POST':
        parent_m = request.POST["parent_m"]
        parent_f = request.POST["parent_f"]
        age_diagnosed_m = int(request.POST["age_diagnosed_m"])
        age_diagnosed_f = int(request.POST["age_diagnosed_f"])
        age_m = int(request.POST["age_m"])
        age_f = int(request.POST["age_f"])
        grandmother = request.POST["grandmother"]
        grandfather = request.POST["grandfather"]
        age_diagnosed_gm = int(request.POST["age_diagnosed_gm"])
        age_diagnosed_gf = int(request.POST["age_diagnosed_gf"])
        age_gm = int(request.POST["age_gm"])
        age_gf = int(request.POST["age_gf"])
        

        family = {}

        family["mother"] = [ parent_m , age_diagnosed_m , age_m]
        family["father"] = [ parent_f , age_diagnosed_f , age_f]
        family["grandfather"] = [grandfather , age_diagnosed_gf , age_gf]
        family["grandmother"] = [grandmother , age_diagnosed_gm , age_gm]
        family["sibling"] = {}

        

        for sibling_no in range(len(no_of_siblings)):
            sib = 'sibling'
            age_diagnosed_s = 'age_diagnosed_s'
            age_s = 'age_s'
            s = sib + str(sibling_no)
            s_answer = s + 'answer'
            s_age_diagnosed = age_diagnosed_s + str(sibling_no) 
            s_age = age_s + str(sibling_no)
            s_answer = request.POST["{}".format(s_answer)]
            s_age_diagnosed= int(request.POST["{}".format(s_age_diagnosed)])
            s_age = int(request.POST["{}".format(s_age)])

            family["sibling"][s] = [s_answer , s_age_diagnosed , s_age]
            
            

        #main calculation

        yes = []
        no = []

        for relation in family:
            if relation != "sibling":
                if family[relation][0] == "Yes":
                    yes.append((relation , family[relation][1]))
                elif family[relation][0] == "No":
                    no.append((relation ,family[relation][2]))
            else:
                for sibling in family[relation]:
                    if family[relation][sibling][0] == "Yes":
                        yes.append((sibling , family[relation][sibling][1]))
                    elif family[relation][sibling][0] == "No":
                        no.append((sibling ,family[relation][sibling][2]))

        sigma_yes = 0
        sigma_no = 0

        for data in yes:
            if data[0] == "grandfather" or data[0] == "grandmother":
               sigma_yes += 0.25*( 88 - data[1])
            else:
                sigma_yes += 0.5*(88 - data[1])

        for data in no:
            if data[0] == "grandfather" or data[0] == "grandmother":
                sigma_no += 0.25*(data[1] - 14)
            else:
                sigma_no += 0.5*(data[1] - 14)

        global dpf_value
        dpf_value = (sigma_yes + 20)/(sigma_no + 50)

        return render(request,'website/dpf_result.html',{
            'dpf':dpf_value
        })
    else:
        return render(request,'website/dpf_calc.html',{
            'siblings': no_of_siblings,
            'len_siblings':len(no_of_siblings)
        })

def ml_model(request):
    return render(request,'website/model.html')

