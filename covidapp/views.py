from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "54bd57f751mshf6d3f35c74b518bp1c153bjsn29f1fdf85bf1"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
	mylist = []
	noofresults = int(response['results'])
	for x in range(0,noofresults):
		
		mylist.append(response['response'][x]['country'])
		mylist.sort()
	if request.method=="POST":
		selectedcountry = request.POST['selectedcountry']
		
		noofresults = int(response['results'])
		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country']:
				new = response['response'][x]['cases']['new']
				active = response['response'][x]['cases']['active']
				critical = response['response'][x]['cases']['critical']
				recovered = response['response'][x]['cases']['recovered']
				total = response['response'][x]['cases']['total']
				deaths = response['response'][x]['deaths']['new']
		context = {'selectedcountry' : selectedcountry,'mylist' : mylist,'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'total' : total,'deaths' : deaths}
		return render(request, 'helloworld.html',context)

				

	
	noofresults = int(response['results'])
	mylist = []
	for x in range(0,noofresults):
		
		
		mylist.append(response['response'][x]['country'])
		mylist.sort()

	context = {'mylist' : mylist}
	return render(request, 'helloworld.html',context)
	



