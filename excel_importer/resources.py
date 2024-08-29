from import_export import resources
from .models import Phase1,Phase5,Phase4,Phase2,Phase3

class Phase1Resource(resources.ModelResource):
    class Meta:
        model = Phase1
        fields = (
            'usn', 'name', 'criteria_a', 'criteria_b', 
            'criteria_c', 'criteria_d', 'criteria_e', 
            'criteria_f', 'score', 'year'
        )

class Phase2Resource(resources.ModelResource):
    class Meta:
        model = Phase2
        fields = (
            'usn', 'name', 'criteria_a', 'criteria_b', 
            'criteria_c', 'criteria_d', 'criteria_e', 
            'score', 'year'
        )

class Phase3Resource(resources.ModelResource):
    class Meta:
        model = Phase3
        fields = (
            'usn', 'name', 'criteria_a', 'criteria_b', 
            'criteria_c', 'criteria_d', 'criteria_e', 
            'score', 'year'
        )

class Phase4Resource(resources.ModelResource):
    class Meta:
        model = Phase4
        fields = (
            'usn', 'name', 'criteria_a', 'criteria_b', 
            'criteria_c', 'criteria_d', 'criteria_e', 
            'criteria_f', 'score', 'year'
        )

class Phase5Resource(resources.ModelResource):
    class Meta:
        model = Phase5
        fields = (
            'usn', 'name', 'criteria_a', 'criteria_b', 
            'criteria_c', 'criteria_d', 'score', 'year'
        )