from django.urls import reverse
from django.test import TestCase

from .models import Mineral
import courses.views


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Diamond",
            category="really hard",
            color="clear",
            group="Other"
        )
        self.mineral2 = Mineral.objects.create(
            name="Ruby",
            category="really hard and red",
            color="red",
            group="Carbon"
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

    def test_random_mineral(self):
        rand = courses.views.random_mineral_pk()
        self.assertGreaterEqual(rand, 0)
        count = Mineral.objects.latest('pk').pk
        self.assertLessEqual(rand, count)

    def test_single_letter(self):
        resp = self.client.get(reverse('courses:single_letter',
                                       kwargs={'pk': 'R'}))
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_single_group(self):
        resp = self.client.get(reverse('courses:single_group',
                                       kwargs={'pk': 'Other'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])

    def test_single_color(self):
        resp = self.client.get(reverse('courses:single_color',
                                       kwargs={'pk': 'red'}))
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_search(self):
        resp = self.client.get(reverse('courses:search') + "?q=Rub")
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
