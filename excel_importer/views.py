from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tablib import Dataset
from .models import Phase1, Phase2, Phase3, Phase4, Phase5

def simple_upload(request):
    if request.method == 'POST':
        # Extract the selected phase from the form data
        phase = request.POST.get('phase')

        # Define a mapping from phase names to models
        phase_models = {
            'phase1': Phase1,
            'phase2': Phase2,
            'phase3': Phase3,
            'phase4': Phase4,
            'phase5': Phase5
        }

        # Get the model class for the selected phase
        model_class = phase_models.get(phase)

        if not model_class:
            return HttpResponse("Invalid phase selected", status=400)

        # Initialize a new dataset and load the uploaded file into it
        dataset = Dataset()
        new_file = request.FILES['myfile']
        imported_data = dataset.load(new_file.read(), format='xlsx')

        # Process each row in the imported data
        for data in imported_data:
            try:
                # Create an instance of the selected phase model
                if phase == 'phase1':
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        criteria_f=data[7],
                        score=data[8],
                        year=data[9],
                    )
                elif phase == 'phase2':
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        score=data[7],
                        year=data[8],
                    )
                elif phase == 'phase3':
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        score=data[7],
                        year=data[8],
                    )
                elif phase == 'phase4':
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        criteria_f=data[7],
                        score=data[8],
                        year=data[9],
                    )
                elif phase == 'phase5':
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        score=data[6],
                        year=data[7],
                    )
                
                value.save()

            except IndexError as e:
                print(f"Error processing row {data}: {e}")
                continue

        # Redirect to a success URL or display a success message
        return HttpResponseRedirect('/success-url/')  # Adjust this URL as needed

    # Render the upload form template if it's not a POST request
    return render(request, 'upload.html')
