from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def createCompany(request):
    # TODO
    # - User must be logged in to create a company
    # - User must not have a company already
    return render(request, "company/createCompany.html")
def companyProfile(request):
    # TODO
    # - User must be logged in to view a company
    return render(request, "company/companyProfile.html")
def companyJobList(request):
    # TODO
    # - User must be the owner of the company to view this page
    return render(request, "company/companyJobList.html")

def companyApplicants(request):
    # TODO
    # - User must be the owner of the company to view this page
    return render(request, "company/companyApplications.html")
def companyProfileSettings(request):
    # TODO
    # - User must be the owner of the company to view this page
    # - If user doesn't have a company, redirect to createCompany
    return render(request, "company/companySettings.html")
def createJob(request):
    # TODO
    # - User must be the owner of the company to view this page
    # - If user doesn't have a company, redirect to createCompany
    return render(request, "company/createJob.html")