Sales Data Analysis Dashboard

Welcome to the Sales Data Analysis Dashboard project! This project is designed to provide an interactive dashboard for analyzing sales data, built using Flask, Pandas, and Plotly for data visualization.

Project Overview

This project allows users to:
	•	View sales data trends through interactive charts.
	•	Edit and customize the data source as needed.
	•	Access the dashboard easily via a browser on port 8080.

Key Technologies

	•	Flask: Backend web framework.
	•	Pandas: Data analysis library.
	•	Plotly: Visualization library for creating interactive charts.

Getting Started

Prerequisites

Make sure you have the following tools installed or set up:
	•	GitHub Codespaces for development.
	•	Working Copy and Textastic (optional for iOS editing).
	•	Python 3.x and Pip (if running locally).

1. Clone the Repository

First, clone the repository to your environment. This can be done in GitHub Codespaces or locally.

git clone https://github.com/quantum-energy/quantum-energy.github.io.git
cd quantum-energy.github.io

2. Set Up the Environment

In GitHub Codespaces (or your local environment), install dependencies and activate the virtual environment:

# Install pipenv if not installed
pip install pipenv

# Create and activate a virtual environment
pipenv install flask pandas plotly
pipenv shell

3. Project Structure

The project is structured as follows:

quantum-energy.github.io/
├── app.py                # Main Flask application
└── templates/
    └── dashboard.html    # HTML template for the dashboard

4. Run the Application

In GitHub Codespaces, you can run the Flask application as follows:

flask run --host=0.0.0.0 --port=8080

	Note: Ports 5000 and 5050 are already taken, so we use port 8080.

Once the app is running, you should see output indicating the server is running on http://localhost:8080. In GitHub Codespaces, this port should be available for preview.

5. Edit the Application

Using Working Copy and Textastic on iOS

If you’d like to edit the application on iOS:
	1.	Open Working Copy and clone this repository using the URL https://github.com/quantum-energy/quantum-energy.github.io.git.
	2.	Link Working Copy to Textastic for easy editing of project files.
	3.	After making edits, commit and push your changes back to GitHub directly from Working Copy.

Usage

By default, the dashboard displays sample monthly sales data. You can customize app.py to load your own sales data from a CSV file or other sources.

Example Code Snippets

Loading Custom Data

Replace the load_data function in app.py with the following code to load data from a CSV file:

def load_data():
    data = pd.read_csv('your_sales_data.csv')  # Ensure this file is in the project root
    return data

Sample Data Visualization

The dashboard currently displays a line chart of monthly sales. Modify the chart type or data as needed in the dashboard function in app.py:

@app.route('/')
def dashboard():
    data = load_data()
    fig = px.bar(data, x='Month', y='Sales', title='Monthly Sales')  # Change to bar chart
    graph_html = fig.to_html(full_html=False)
    return render_template('dashboard.html', graph_html=graph_html)

Deployment

Deploy to GitHub Pages (Optional)

To deploy this project as a static website on GitHub Pages, you would need to convert it to static HTML. Note that Flask requires a server to run, so GitHub Pages might not support dynamic Flask apps directly. Consider exporting the dashboard as static HTML if deployment is necessary.

Contributing

If you’d like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome contributions that improve functionality or add features.

License

This project is open-source and available under the MIT License.

Quick Commands Reference

Here’s a quick reference for commands in this project:
	•	Clone the repository:

git clone https://github.com/quantum-energy/quantum-energy.github.io.git


	•	Set up environment:

pip install pipenv
pipenv install flask pandas plotly


	•	Run Flask app on port 8080:

flask run --host=0.0.0.0 --port=8080


Happy coding with your Sales Data Analysis Dashboard! Feel free to reach out if you have questions or suggestions.
