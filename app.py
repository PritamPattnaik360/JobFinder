from flask import Flask, render_template, request
import pandas as pd
from Scraper import scrape  
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        times = int(request.form['times'])
        
        # Call the scrape method
        scrape(title, location, times)
        
        # Read the data from CSV
        data = pd.read_csv('Data.csv')
        
        # Prepare data for visualization
        job_title_counts = data['job_title'].value_counts()
        
        # Create Plotly bar chart
        trace = go.Bar(
            x=job_title_counts.index,
            y=job_title_counts.values,
            marker=dict(color='rgb(26, 118, 255)')
        )
        layout = go.Layout(
            title='Distribution of Job Titles',
            xaxis=dict(title='Job Title'),
            yaxis=dict(title='Count')
        )
        fig = go.Figure(data=[trace], layout=layout)
        plot_div = fig.to_html(full_html=False)
        
        # Pass data to HTML template
        return render_template('index.html', plot_div=plot_div, table=data.to_html(index=False))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
