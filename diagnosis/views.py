from django.shortcuts import render

# Create your views here.



def diagnosis(request):
	return render(request, 'diagnosis.html', {})

def diagnosisResult(request):
	return render(request, 'diagnosisResult.html', {})


