from django.db import models


# Create your models here.
class PatientData(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    jan_eating_behaviour = models.IntegerField(default=0)
    feb_eating_behaviour = models.IntegerField(default=0)
    mar_eating_behaviour = models.IntegerField(default=0)
    apr_eating_behaviour = models.IntegerField(default=0)
    may_eating_behaviour = models.IntegerField(default=0)
    jun_eating_behaviour = models.IntegerField(default=0)
    jul_eating_behaviour = models.IntegerField(default=0)
    jan_self_harm = models.IntegerField(default=0)
    feb_self_harm = models.IntegerField(default=0)
    mar_self_harm = models.IntegerField(default=0)
    apr_self_harm = models.IntegerField(default=0)
    may_self_harm = models.IntegerField(default=0)
    jun_self_harm = models.IntegerField(default=0)
    jul_self_harm = models.IntegerField(default=0)
    jan_mood = models.IntegerField(default=0)
    feb_mood = models.IntegerField(default=0)
    mar_mood = models.IntegerField(default=0)
    apr_mood = models.IntegerField(default=0)
    may_mood = models.IntegerField(default=0)
    jun_mood = models.IntegerField(default=0)
    jul_mood = models.IntegerField(default=0)
    jan_social_interactions = models.IntegerField(default=0)
    feb_social_interactions = models.IntegerField(default=0)
    mar_social_interactions = models.IntegerField(default=0)
    apr_social_interactions = models.IntegerField(default=0)
    may_social_interactions = models.IntegerField(default=0)
    jun_social_Interactions = models.IntegerField(default=0)
    jul_social_Interactions = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class CollectivePatientData(models.Model):
    name = models.CharField(max_length=255)
    severity_rate = models.IntegerField(default=0)
    months_of_treatment = models.IntegerField(default=0)

    def __str__(self):
        return self.name
