from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, get_object_or_404
from django.views import generic
from directory.models import Agency, Provider, AgencyType, AgencyTag

# Create your views here.


def index(request):

    # Generate counts of some of the main objects
    num_agencies = Agency.objects.count()
    num_providers = Provider.objects.count()

    context = {
        "num_agencies": num_agencies,
        "num_providers": num_providers,
    }

    return render(request, "pages/index.html", context=context)


class AgencyListView(generic.ListView):
    model = Agency
    template_name = "pages/agencies.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["agencies"] = Agency.objects.all()
        return context


class AgencyDetailView(generic.DetailView):
    model = Agency
    template_name = "pages/agency_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agencies"] = Agency.objects.all()
        context["providers"] = Provider.objects.all()
        context["agency_types"] = AgencyType.objects.all()
        context["agency_tags"] = AgencyTag.objects.all()
        return context


def login_user(request):
    pass


def logout_user(request):
    pass


def register_user(request):
    pass
