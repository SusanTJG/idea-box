import datetime
from django.test import TestCase
from idea import models, views

def get_relative_date(delta_days=0):
    return datetime.date.today() + datetime.timedelta(days=delta_days)

class BannerTest(TestCase):
    def test_timebound_banner(self):
        yesterday = get_relative_date(-1)
        tommorow = get_relative_date(+1)
        banner = models.Banner(title="How would you improve our vacation policy?",
                text="We would like to know what we can do to improve your work/life balance",
                start_date=yesterday, end_date=tommorow)
        banner.save()

        b = views.get_banner()
        self.assertIsNotNone(b)

    def test_indefinite_banner(self):
        yesterday = get_relative_date(-1)
        banner = models.Banner(title="How would you improve our vacation policy?", 
                text="We would like to know what we can do to improve your work/life balance",
                start_date=yesterday)
        banner.save()

        b = views.get_banner()
        self.assertIsNotNone(b)
        self.assertEquals(b.title, "How would you improve our vacation policy?")
        self.assertEquals(b.text, "We would like to know what we can do to improve your work/life balance")

    def test_timed_before_indefinite(self):
        yesterday = get_relative_date(-1)
        tommorow = get_relative_date(+1)

        timed_banner = models.Banner(title="How would you improve our vacation policy?", 
                text="We would like to know what we can do to improve your work/life balance",
                start_date=yesterday, end_date=tommorow)
        timed_banner.save()

        banner = models.Banner(title="How would you improve our promotion process?", 
                text="We would like to know what we can do to improve your work/life balance",
                start_date=yesterday)
        banner.save()

        b = views.get_banner()
        self.assertIsNotNone(b)
        self.assertEquals(b.title, "How would you improve our vacation policy?")
        self.assertEquals(b.text, "We would like to know what we can do to improve your work/life balance")

    def test_no_banner(self):
        b = views.get_banner()
        self.assertIsNone(b)

    def test_outside_timed(self):
        tommorow = get_relative_date(+1)
        end = get_relative_date(+5)
        banner = models.Banner(title="How would you improve our vacation policy?", 
                text="We would like to know what we can do to improve your work/life balance",
                start_date=tommorow, end_date=end)
        banner.save()
        b = views.get_banner()
        self.assertIsNone(b)
