from django.test import TestCase
from .factories import OrganizationFactory
from .models import Organization


class TDDTestOrganization(TestCase):
    def setUp(self):
        self.organization = OrganizationFactory(name='Toxzen')

    def test_org_exists(self):
        """
        Test organizations
        """
        org = Organization.objects.get(name='Toxzen')
        org_count = Organization.objects.all().count()
        self.assertIsNotNone(org)
        self.assertEqual(org_count, 1)
        self.assertEqual(str(org), 'Toxzen')
