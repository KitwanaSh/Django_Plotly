from django.shortcuts import render

def index(request):
    '''
    Landing view for the BMI Calculator.
    '''

    if request.method == 'GET':
        
        # Template context date
        context: dict = { 'title': 'BMI Calculator'}
        
        # Return view
        return render(request, 'BMIapp/base.html', context)
