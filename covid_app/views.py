from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"x-rapidapi-key": "aa20156b73msh143c6a2607af8f9p16eb5bjsn5fb2089c8859",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()
print("response is: ", response)


# Create your views here.
def helloworldview(request):
    mylist=[]
    noofresults=int(response['results'])
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                try:
                    new=response['response'][x]['cases']['new']
                except Exception as e:
                    new = 0
                try:
                    active=response['response'][x]['cases']['active']
                except Exception as e:
                    active = 0
                try:
                    critical=response['response'][x]['cases']['critical']
                except Exception as e:
                    critical = 0
                try:
                    recovered=response['response'][x]['cases']['recovered']
                except Exception as e:
                    recovered = 0
                try:
                    total=response['response'][x]['cases']['total']
                except Exception as e:
                    total = 0
                
                if total == None:
                    total = 0
                if active == None:
                    active = 0
                if recovered == None:
                    recovered = 0
                    
                deaths=int(total)-int(active)-int(recovered)
                
        context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
        return render(request,'index.html',context)
    
    
    context={'mylist':mylist}
    return render(request,'index.html',context)
