'''

This is the main file of the application.
It is responsible for rendering the HTML templates and handling the user input for feedbacks.
The application uses Flask to create a web server and serve the HTML templates.

'''

# import libraries
from flask import Flask, render_template, request
import json
import pandas as pd
import os

# Get the dataset to work with
dataFrame = pd.read_csv(os.path.abspath("cleaned_and_parsed_dataset.csv"))
dataFrame = dataFrame.rename(columns={"duration_mm/ss":"duration_mm_ss"})

client_formData = None

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    print(client_formData)
    return render_template('form.html')

@app.route("/analytics")
def analytics():

    # Create a response object
    analyticResponse = {
        "text": "You haven't rated any genre yet, please fill the form to get some suggestions!",
        "dbHead":None,
        "hasData": False
    }

    # Check if the user has rated any genre
    if request.cookies.get('data') not in [None, ""]:
        analyticResponse['hasData'] = True

        # Get the feedback from the cookie
        client_formData = json.loads(request.cookies.get('data'))


        tagsToGroup = ["energy", "tempo", "danceability"]
        tagsDirection = [False, False, False]

        for i in client_formData["tag"]:
            if i == "energetic":
                tagsDirection[0] = (True)
            elif i == "happy":
                tagsDirection[1] = (True)
            elif i == "active":
                tagsDirection[2] = (True)

        # Get the data for the genre the user rated
        dataToSuggest = dataFrame[dataFrame['track_genre'] == client_formData['music-genre']]
        # get the mean rate for the genre
        meanRateByDataset = dataToSuggest['popularity'].mean()

        analyticResponse['text'] += f" Your rate for this genre is {client_formData['rate']*10} and the mean rate for this genre is {meanRateByDataset:.2f}"

        tagsToGroup.append("popularity")

        if client_formData["rate"]*10 < meanRateByDataset:
            tagsDirection.append(False)
            analyticResponse['text'] += "\n\nYour rate for this genre is lower than mean value of popularity in dataset, maybe you would like to check out the most popular songs from it to change your opinion?"
            analyticResponse['dbHead'] = dataToSuggest.sort_values(by=tagsToGroup, ascending=tagsDirection).head(5)
            analyticResponse['text'] += f"\n\nAlso this suggestion is based on your tags: {', '.join(client_formData['tag'])}."
        else:
            if client_formData["rate"]*10 > 80:
                tagsDirection.append(True)
                analyticResponse['text'] += "\n\nYour rate for this genre is quite high, maybe you would like to check out the least popular songs from it, you may like them too!"
                analyticResponse['dbHead'] = dataToSuggest.sort_values(by=tagsToGroup, ascending=tagsDirection).head(5)
                analyticResponse['text'] += f"\n\nAlso this suggestion is based on your tags: {','.join(client_formData['tag'])}."
            else:
                analyticResponse['text'] += "\n\nYour rate for this genre is mid by the dataset, here are some random songs from this genre you may like!"
                analyticResponse['dbHead'] = dataToSuggest.sample(n=5)
        
        analyticResponse['dbHead'] = analyticResponse['dbHead'].to_dict('records')
        # for i in analyticResponse['dbHead'].to_dict('records'):
        #     print(i)
    return render_template('analytics.html', **analyticResponse)

@app.route("/graphs")
def about():
    return render_template('graphs.html')

if __name__ == '__main__':
    app.run(debug=True)