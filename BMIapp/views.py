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

    if request.method == 'GET':
        # BMI form
        bmi_form: BMIForm = BMIForm()
        context: dict = {'title': 'BMI Calculator',
                 'bmi_form': bmi_form}

    return render(request, 'BMIapp/base.html', context)
