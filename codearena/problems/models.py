from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    test_input = models.TextField()      # hidden input
    expected_output = models.TextField()  # hidden output

    def __str__(self):
        return self.title
