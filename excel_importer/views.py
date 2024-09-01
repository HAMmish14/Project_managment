from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tablib import Dataset
from .models import Phase1, Phase2, Phase3, Phase4, Phase5
from django.shortcuts import render, get_object_or_404, Http404

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
        return HttpResponseRedirect('retrieve-data')  # Adjust this URL as needed

    # Render the upload form template if it's not a POST request
    return render(request, 'upload.html')

from django.shortcuts import render, get_object_or_404
from .models import Phase1, Phase2, Phase3, Phase4, Phase5, Criteria1

def get_data_by_usn(request):
    if request.method == 'POST':
        if 'usn' in request.POST:
            usn = request.POST.get('usn')
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
                return render(request, 'retrieve_data.html', {"error": "Invalid phase selected"})

            # Retrieve the data for the given USN
            data = get_object_or_404(model_class, usn=usn)

            # Pass the data to the template
            context = {
                "data": {
                    "usn": data.usn,
                    "name": data.name,
                    "criteria_a": data.criteria_a,
                    "criteria_b": data.criteria_b,
                    "criteria_c": data.criteria_c,
                    "criteria_d": data.criteria_d,
                    "criteria_e": data.criteria_e,
                    "criteria_f": getattr(data, 'criteria_f', None),  # criteria_f might not exist in some phases
                    "score": data.score,
                    "year": data.year,
                }
            }
            return render(request, 'retrieve_data.html', context)

        elif 'criteriaName' in request.POST and 'criteriaPhase' in request.POST:
            criteria_name = request.POST.get('criteriaName')
            phase_number = request.POST.get('criteriaPhase')

            # Retrieve the criteria data based on name and phase number
            criteria_data = get_object_or_404(Criteria1, criteria_name=criteria_name, phase_number=phase_number)

            # Pass the criteria data to the template
            context = {
                "criteria_data": {
                    "criteria_id": criteria_data.criteria_id,
                    "criteria_name": criteria_data.criteria_name,
                    "description": criteria_data.description,
                    "max_marks": criteria_data.max_marks,
                    "phase_number": criteria_data.phase_number,
                }
            }
            return render(request, 'retrieve_data.html', context)

    return render(request, 'retrieve_data.html')
