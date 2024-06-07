from django.db.models import Choices


class TaskChoices(Choices):
    in_work = 'In work'
    available = 'Available'
    on_review = 'On review'
    done = 'Done'
    cancelled = 'Cancelled'
