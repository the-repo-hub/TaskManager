from django.db.models import Choices


class TaskChoices(Choices):
    processing = 'Processing'
    available = 'Available'
    finished = 'Finished'
    error = 'Error'
    done = 'Done'
    cancelled = 'Cancelled'
