from django.db import models
from django.contrib.auth.models import User


class OrganizationMember(models.Model):
    """
    Organization Members.  Those belonging to the organization.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trustee = models.BooleanField()

    def __str__(self):
        return self.user.email


class Organization(models.Model):
    """
    Organizations and communities
    """
    name = models.CharField(max_length=150, db_index=True, help_text="The name of your community or organization")
    code = models.CharField(max_length=10)
    members = models.ManyToManyField(OrganizationMember, help_text="Users who belong to this organization")

    objects = models.Manager()

    def __str__(self):
        return self.name
