from import_export import resources

from core.models import PatientData, CollectivePatientData


class PatientDataResource(resources.ModelResource):
    class Meta:
        model = PatientData
        # skip_unchanged = True
        # report_skipped = True
        fields = ['Name',
                  'Age',
                  'jan_eating_behaviour',
                  'feb_eating_behaviour',
                  'mar_eating_behaviour',
                  'apr_eating_behaviour',
                  'may_eating_behaviour',
                  'jun_eating_behaviour',
                  'jul_eating_behaviour',
                  'jan_self_harm',
                  'feb_self_harm',
                  'mar_self_harm',
                  'apr_self_harm',
                  'may_self_harm',
                  'jun_self_harm',
                  'jul_self_harm',
                  'jan_mood',
                  'feb_mood',
                  'mar_mood',
                  'apr_mood',
                  'may_mood',
                  'jun_mood',
                  'jul_mood',
                  'jan_social_interactions',
                  'feb_social_interactions',
                  'mar_social_interactions',
                  'apr_social_interactions',
                  'may_social_interactions',
                  'jun_social_Interactions',
                  'jul_social_Interactions']
        # exclude = ('id',)
        import_id_fields = ['Age']
        # export_order = ('id', 'price', 'author', 'name')
        # exclude = ('id',)


class CollectivePatientDataResource(resources.ModelResource):
    class Meta:
        model = CollectivePatientData
        # skip_unchanged = True
        # report_skipped = True
        # exclude = ('id',)

        fields = ['name', 'severity_rate', 'months_of_treatment']
        import_id_fields = ['severity_rate']
