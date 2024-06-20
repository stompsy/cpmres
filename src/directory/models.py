from django.db import models

from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class AgencyType(models.Model):
    """Model representing a type of Agency."""

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter an Agency type (e.g. General Hospital, Health Clinic, Assisted Living, Diagnostic Center, Treatment Center, Pharmacy, etc.)",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("agencytype-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="agencytype_name_case_insensitive_unique",
                violation_error_message="Agency type already exists (case insensitive match)",
            ),
        ]


class AgencyTag(models.Model):
    """Model representing a tag for an Agency."""

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter a tag for an Agency (e.g. Durable Medical Equipment, Dental, Dialysis, Naturopathic Health, SUD Treatment, Primary Care, Benefits Coordination, etc.)",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("agencytag-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="agencytag_name_case_insensitive_unique",
                violation_error_message="Agency tag already exists (case insensitive match)",
            ),
        ]


class Agency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        max_length=1500,
        unique=True,
        help_text="Enter a description of the Agency (e.g. Mission, Services, etc.)",
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    website = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    type = models.ManyToManyField(
        AgencyType, related_name="agencies", help_text="Select types for this Agency"
    )
    tag = models.ManyToManyField(
        AgencyTag, related_name="agencies", help_text="Select tags for this Agency"
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="agency_name_case_insensitive_unique",
                violation_error_message="Agency already exists (case insensitive match)",
            ),
        ]
        ordering = ["name"]

    def display_type(self):
        return ", ".join([type.name for type in self.type.all()[:3]])

    display_type.short_description = "Type"

    def display_tag(self):
        return ", ".join([tag.name for tag in self.tag.all()[:3]])

    display_tag.short_description = "Tag"

    def get_absolute_url(self):
        return reverse("agency-detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class ProviderType(models.Model):
    """Model representing a type of Provider."""

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a Provider type (e.g. Community Paramedic, Medical Doctor, Physician Assistant, Registered Nurse, Pharmacist, etc.)",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("providertype-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="providertype_name_case_insensitive_unique",
                violation_error_message="Provider type already exists (case insensitive match)",
            ),
        ]


class ProviderTag(models.Model):
    """Model representing a tag for a Provider."""

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter a tag for a Provider (e.g. Street Medicine, Dermatology, Psychiatry, Hospice Care, Family Practice, Wound Care, Investigator, etc.)",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("providertag-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="providertag_name_case_insensitive_unique",
                violation_error_message="Provider tag already exists (case insensitive match)",
            ),
        ]


class Provider(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(
        max_length=1500,
        unique=True,
        help_text="Enter a brief description or bio for the Provider (e.g. Mission, services provided, etc.)",
    )
    agency = models.ForeignKey(
        to=Agency,
        related_name="providers",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    email = models.EmailField(max_length=100)
    work_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    can_text = models.BooleanField()
    type = models.ManyToManyField(
        ProviderType,
        related_name="providers",
        help_text="Select types (title) for this Provider",
    )
    tag = models.ManyToManyField(
        ProviderTag, related_name="providers", help_text="Select tags for this Provider"
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("email"),
                name="provider_name_case_insensitive_unique",
                violation_error_message="Provider already exists (case insensitive match)",
            ),
        ]
        ordering = ["last_name", "first_name"]

    def display_type(self):
        return ", ".join([type.name for type in self.type.all()[:3]])

    display_type.short_description = "Type"

    def display_tag(self):
        return ", ".join([tag.name for tag in self.tag.all()[:3]])

    display_tag.short_description = "Tag"

    def get_absolute_url(self):
        return reverse("provider-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
