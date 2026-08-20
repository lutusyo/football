from django.test import TestCase
from apps.reference.models.event_type import EventType
from apps.reference.models.event_category import EventCategory
from apps.reference.models.event_outcome import EventOutcome
from apps.reference.models.body_part  import BodyPart


class EventModelTests(TestCase):

    def test_event_category(self):
        category = EventCategory.objects.create(name="Possession", code="POS")
        self.assertEqual(str(category), "Possession")

    def test_event_type(self):
        category = EventCategory.objects.create(name="Possession", code="POS")
        event = EventType.objects.create(category=category, name="Pass", code="PASS")
        self.assertEqual(str(event), "Pass")

    def test_event_outcome(self):
        outcome = EventOutcome.objects.create(name="Successful", code="SUCCESS")
        self.assertEqual(str(outcome), "Successful")

    def test_body_part(self):
        body_part = BodyPart.objects.create(name="Right Foot", code="RIGHT_FOOT")
        self.assertEqual(str(body_part), "Right Foot")