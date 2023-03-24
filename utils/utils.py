from userInformation.models import Profile
from systemModules.models import Company, Module


def userCompany(pk):
    user = Profile.objects.get(pk=pk)
    company_pk = Company.objects.get(pk=user.company.pk)
    return company_pk

