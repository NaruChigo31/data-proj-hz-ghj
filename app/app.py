# import libraries
from flask import Flask, render_template, request
import json
import pandas as pd

# Get the dataset to work with
dataFrame = pd.read_csv("../cleaned_and_parsed_dataset.csv")
dataFrame = dataFrame.rename(columns={"duration_mm/ss":"duration_mm_ss"})

client_formData = None
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
    analyticResponse = {
        "text": "You haven't rated any genre yet, please fill the form to get some suggestions!",
        "dbHead":None,
        "hasData": False
    }
    if request.cookies.get('data') not in [None, ""]:
        analyticResponse['hasData'] = True
        client_formData = json.loads(request.cookies.get('data'))
        print(client_formData)
        dataToSuggest = dataFrame[dataFrame['track_genre'] == client_formData['music-genre']]
    
        meanRateByDataset = dataToSuggest['popularity'].mean()

        if client_formData["rate"]*10 < meanRateByDataset:
            analyticResponse['text'] = "Your rate for this genre is lower than mean value of popularity in dataset, maybe you would like to check out the most popular songs from it to change your opinion?"
            analyticResponse['dbHead'] = dataToSuggest.sort_values(by='popularity', ascending=False).head(5)
        else:
            if client_formData["rate"]*10 > 80:
                analyticResponse['text'] = "Your rate for this genre is quite high, maybe you would like to check out the least popular songs from it, you may like them too!"
                analyticResponse['dbHead'] = dataToSuggest.sort_values(by='popularity', ascending=True).head(5)
            else:
                analyticResponse['text'] = "Your rate for this genre is mid by the dataset, here are some random songs from this genre you may like!"
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