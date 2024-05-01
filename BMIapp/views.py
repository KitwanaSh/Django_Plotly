from django.shortcuts import render
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Figure
import plotly.graph_objs as ob

from .form import BMIForm

def index(request):
    '''
    Landing view for the BMI Calculator.
    '''
    # x_values = ["May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"] 

    # y_values = [5, 15, 10, 5, 8, 6, 10]
    # # Create the plot
    # bar_plot = Figure(data=[ob.Bar( x = x_values, 
    #                                y = y_values,
    #                                textposition = 'auto',)])

    # Embed the plot in an HTML div tag
    # bar_plot_div: str = plot(bar_plot, output_type="div")

    context = {'title': 'BMI Calculator'}

    if request.method == 'POST':
        # BMI form
        bmi_form: BMIForm = BMIForm()
        height: str = request.POST['height']
        weight: str = request.POST['weight']

        bmi_result: float = float(weight)/(float(height)*float(height))

        if bmi_result < 18.5:
            result: str = 'Underweight'

        elif (bmi_result >= 18.5) and (bmi_result < 25):
            result: str = 'Healthy Weight'

        elif (bmi_result >= 25) and (bmi_result < 30):
            result: str = 'Overweight'

        elif (bmi_result >= 30) and (bmi_result < 35):
            result: str = 'Obessity class I'

        elif (bmi_result >= 35) and (bmi_result < 40):
            result: str = 'Obessity class II'

        elif (bmi_result >= 40):
            result: str = 'Obessity class III'

        # Create bar plot
        bmi_plot: Figure = px.bar(x = ["Height", "Weight", "BMI index"], 
                                    y = [float(height), float(weight), bmi_result])

        # Embed the plot in a div tag
        bar_plot_div: str = plot(bmi_plot, output_type="div")

        context.update({
            'bmi_form': bmi_form,
            'bmi_plot': bar_plot_div,
            'result': result
        })
    else:
        # Initialize form for GET request
        context['bmi_form'] = BMIForm()

    return render(request, 'BMIapp/base.html', context)
