from django.shortcuts import render
from .models import Agency, Provider, AgencyType, ProviderType, AgencyTag, ProviderTag

# Create your views here.


def index(request):

    # Generate counts of some of the main objects
    num_agencies = Agency.objects.count()
    num_agency_types = AgencyType.objects.count()
    num_agency_tags = AgencyTag.objects.count()
    num_providers = Provider.objects.count()
    num_provider_types = ProviderType.objects.count()
    num_provider_tags = ProviderTag.objects.count()

    context = {
        "num_agencies": num_agencies,
        "num_agency_types": num_agency_types,
        "num_agency_tags": num_agency_tags,
        "num_providers": num_providers,
        "num_provider_types": num_provider_types,
        "num_provider_tags": num_provider_tags,
    }

    return render(request, "pages/index.html", context=context)
