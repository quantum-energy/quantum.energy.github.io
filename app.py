from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# Load sample sales data
def load_data():
    # Replace 'sales_data.csv' with your actual data file
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [200, 250, 300, 150, 400]
    })
    return data

@app.route('/')
def dashboard():
    data = load_data()
    fig = px.line(data, x='Month', y='Sales', title='Monthly Sales')
    graph_html = fig.to_html(full_html=False)
    return render_template('dashboard.html', graph_html=graph_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)