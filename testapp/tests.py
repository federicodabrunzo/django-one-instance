from django.test import TestCase, override_settings

from testapp.models import *
from one_instance.models import SingletonModelAlreadyExists


class SingletonQueriesTestCase(TestCase):

    def test_get(self):
        c1 = Config.objects.create(enabled=False)
        c2 = Config.objects.get()
        self.assertEqual(c1.pk, c2.pk)

    @override_settings(DJANGO_ONE_STRICT=True)
    def test_get_strict_enabled(self):

        Config.objects.create(enabled=False)
        with self.assertRaises(TypeError):
            Config.objects.get(pk=1)

    @override_settings(DJANGO_ONE_STRICT=False)
    def test_get_strict_disabled(self):

        c1 = Config.objects.create(enabled=False)
        c2 = Config.objects.get(pk=1)
        self.assertEqual(c1.pk, c2.pk)

    @override_settings(DJANGO_ONE_STRICT=True)
    def test_create_strict_enabled(self):

        Config.objects.create(enabled=False)
        with self.assertRaises(SingletonModelAlreadyExists):
            Config.objects.create(enabled=False)

    @override_settings(DJANGO_ONE_STRICT=False)
    def test_create_strict_disabled(self):

        c1 = Config.objects.create(enabled=False)
        c2 = Config.objects.create(enabled=False)
        self.assertEqual(c1.pk, c2.pk)

    def test_get_or_create(self):

        c1, created = Config.objects.get_or_create(defaults=dict(enabled=False))
        self.assertEquals(created, True)
        c2, created = Config.objects.get_or_create()
        self.assertEquals(created, False)
        self.assertEquals(c1.pk, c2.pk)

    @override_settings(DJANGO_ONE_STRICT=True)
    def test_get_or_create_strict_enabled(self):

        with self.assertRaises(TypeError):
            Config.objects.get_or_create(pk=1, defaults=dict(enabled=False))

    @override_settings(DJANGO_ONE_STRICT=False)
    def test_get_or_create_strict_disabled(self):

        c1, created = Config.objects.get_or_create(
            pk=1, defaults=dict(enabled=False))
        self.assertEquals(created, True)
        c2, created = Config.objects.get_or_create(
            pk=1, defaults=dict(enabled=False))
        self.assertEquals(created, False)
        self.assertEquals(c1.pk, c2.pk)

    def test_update_or_create(self):

        c1, created = Config.objects.update_or_create(
            defaults=dict(enabled=False))
        self.assertEquals(created, True)
        self.assertEquals(c1.enabled, False)

        c2, created = Config.objects.update_or_create(
            defaults=dict(enabled=True))
        self.assertEquals(created, False)
        self.assertEquals(c2.enabled, True)

        self.assertEquals(c1.pk, c2.pk)

    @override_settings(DJANGO_ONE_STRICT=True)
    def test_update_or_create_strict_enabled(self):

        with self.assertRaises(TypeError):
            Config.objects.update_or_create(pk=1, defaults=dict(enabled=False))

    @override_settings(DJANGO_ONE_STRICT=False)
    def test_update_or_create_strict_disabled(self):

        c1, created = Config.objects.update_or_create(
            pk=1, defaults=dict(enabled=False))
        self.assertEquals(created, True)

        c2, created = Config.objects.update_or_create(
            pk=1, defaults=dict(enabled=False))
        self.assertEquals(created, False)

        self.assertEquals(c1.pk, c2.pk)

    def test_first_equal_last(self):
        Config.objects.create(enabled=False)
        _first = Config.objects.first()
        _last  = Config.objects.last()
        self.assertEqual(_first.pk, _last.pk)
        

class SingletonNotSupportedTestCase(TestCase):

    def _test_not_supported(self, f_name):
        
        with self.assertRaises(TypeError):
            getattr(Config.objects, f_name)()

    def test_aggregate_not_supported(self):

        self._test_not_supported('aggregate')

    def test_bulk_create_not_supported(self):

        self._test_not_supported('bulk_create')

    def test_bulk_update_not_supported(self):

        self._test_not_supported('bulk_update')