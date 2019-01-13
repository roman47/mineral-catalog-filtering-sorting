from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral

class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Diamond",
            category="really hard"
        )
        self.mineral2 = Mineral.objects.create(
            name="Ruby",
            category="really hard and red"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'courses/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('courses:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
