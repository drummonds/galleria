from django.core.urlresolvers import reverse
from django_webtest import WebTest
from model_mommy import mommy
from artists.models import Artist


class ArtistTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Artist)
        self.assertTrue(isinstance(instance, Artist))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Artist)
        response = self.app.get(reverse('artist_list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('artist_create'))
        new_biography = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Artist.objects.filter(name=new_name).exists())

        # This was the code but it isn't the form name
        # form = response.forms['artist_form']
        # So using the more ugly indexing by number here and in test_update_view
        form = response.forms[0]
        form['name'] = new_name
        form.submit().follow()

        instance = Artist.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Artist)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Artist)
        response = self.app.get(reverse('artist_update', kwargs={'pk': instance.pk, }))

        form = response.forms[0]
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Artist.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Artist)
        pk = instance.pk
        response = self.app.get(reverse('artist_delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Artist.objects.filter(pk=pk).exists())
