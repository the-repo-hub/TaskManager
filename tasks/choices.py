from django.db.models import Choices


class TaskChoices(Choices):
    available = 'Available'
    in_work = 'In work'
    on_review = 'On review'
    done = 'Done'
    cancelled = 'Cancelled'
