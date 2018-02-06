# coding: utf-8

# https://github.com/jedie/django-tools
from django_tools.unittest_utils.unittest_base import BaseTestCase
from django_tools.unittest_utils.user import TestUserMixin

# The Forms-Builder Project
from forms_builder.forms.models import Form


class FormsAdminTests(TestUserMixin, BaseTestCase):
    def test_create_forms(self):
        self.login(usertype="superuser")

        self.assertEqual(Form.objects.all().count(), 0)

        response = self.client.post(
            path="/en/admin/forms/form/add/",
            data={
                "title": "The Form 1 in english",
                "status": "2",
                "intro": "This is the first form in the base language 'english'",
                "button_text": "submit",
                "response": "Thanks!",
                "redirect_url": "/en/",
                "sites": "1",

                "fields-TOTAL_FORMS": "3",
                "fields-INITIAL_FORMS": "0",
                "fields-MIN_NUM_FORMS": "0",
                "fields-MAX_NUM_FORMS": "1000",

                "fields-0-label": "Does it worked?!?",
                "fields-0-field_type": "4",
                "fields-0-required": "on",
                "fields-0-visible": "on",
                "fields-0-choices": "yes,no,maybe",
                "fields-0-default": "maybe",
                "fields-0-placeholder_text": "the placeholder text",
                "fields-0-help_text": "Just click on ckeckbox",

                "fields-1-required": "on",
                "fields-1-visible": "on",

                "fields-2-required": "on",
                "fields-2-visible": "on",

                "fields-__prefix__-required": "on",
                "fields-__prefix__-visible": "on",

                "_save": "Sichern",
            },
            HTTP_ACCEPT_LANGUAGE="en"
        )
        self.assertRedirects(response, expected_url="/en/admin/forms/form/")

        self.assertEqual(Form.objects.all().count(), 1)

        form = Form.objects.all()[0]
        url = form.get_absolute_url()
        self.assertEqual(url, "/forms/the-form-1-in-english/")

        response = self.client.get(url, HTTP_ACCEPT_LANGUAGE="en")
        self.assertResponse(response,
            must_contain=(
                "<h1>Die Form 1 in deutsch</h1>",
                "<p>Die erste Form übersetzt ins deutsche</p>",
                '<form action="/forms/die-form-1-in-deutsch/" method="post">',

            ),
            html=True,
            messages=[],
            must_not_contain=("error", "traceback"),
            template_name="admin/index.html",
        )
#
#
# text = '''
# curl 'http://127.0.0.1:8000/de/admin/forms/form/add/' -H 'Host: 127.0.0.1:8000' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' --compressed -H 'Referer: http://127.0.0.1:8000/de/admin/forms/form/add/' -H 'Content-Type: multipart/form-data; boundary=---------------------------175709242120618184301141493923' -H 'Cookie: sessionid-ZQLVV=J6QKQzdn2bKbhNMjm3e7JghWHLmtygop; CSRF-Token-ZQLVV=bVgbzRKYmMYoQ9Khad5Fyx25ifLXN6C7; djdt=hide; csrftoken=Rp10VXj0UbjFVBu1luv0CoDEoDk3ongQF2kOmlvD9EMJtIkdp8OjvUpCycJ5r3Tn; django_language=de; sessionid=m9dm7yqnjbbz1fkbr34l85h67dxlw9ko' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data ''
# csrfmiddlewaretoken=7onTfOLa1hwmHHormQD7RPYIJxjTLQn7V1GHGcXNgKZqfOeDquWqKlKGT6IVOw0E
# title=Die+Form+1+in+deutsch
# intro=Die+erste+Form+übersetzt+ins+deutsche
# button_text=Senden
# response=Danke!
# redirect_url=/de/
# email_from
# email_copies
# email_subject
# email_message
# fields-TOTAL_FORMS=1
# fields-INITIAL_FORMS=1
# fields-MIN_NUM_FORMS=1
# fields-MAX_NUM_FORMS=1
# fields-0-label=Funktioniert+es?!?
# fields-0-choices=ja,nein,vielleicht
# fields-0-default=vielleicht
# fields-0-placeholder_text=Der+Platzhaltertext
# fields-0-help_text=Einfach+auf+eine+Checkbox+klicken
# _sa
