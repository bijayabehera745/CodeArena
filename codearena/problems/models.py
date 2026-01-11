from django.db import models
from djongo import models


class Problem(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    # For test case checking internally
    test_input = models.TextField()      # hidden input
    expected_output = models.TextField()  # hidden output

    @property
    def id(self):
        return str(self._id)

    def __str__(self):
        return self.title
