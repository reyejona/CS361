from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)


# Data to serve with our API
states =  [
    {   "name": "Alabama",
        "state": "AL",
        "tax":.04
    },
    {   "name": "Alaska",
        "state":"AK",
        "tax":0
    },
    {   "name": "Arizona",
        "state": "AZ",
        "tax":.056
    },
    {   "name": "Arkansas",
        "state": "AR",
        "tax":.065
    },
    {   "name": "California",
        "state": "CA",
        "tax":.0725
    },
    {   "name": "Colorado",
        "state": "CO",
        "tax":.029
    },
    {   "name": "Connecticut",
        "state": "CT",
        "tax":.06350
    },
    {   "name": "Delaware",
        "state": "DE",
        "tax":.0
    },
    {   "name": "District of Columbia",
        "state": "DC",
        "tax":.06
    },
    {   "name": "Florida",
        "state": "FL",
        "tax":.06
    },
    {   "name": "Georgia",
        "state": "GA",
        "tax":.04
    },
    {   "name": "Hawaii",
        "state": "HI",
        "tax":.04166
    },
    {   "name": "Idaho",
        "state": "ID",
        "tax":.06
    },
    {   "name": "Illinois",
        "state": "IL",
        "tax":.06250
    },
    {   "name": "Indiana",
        "state": "IN",
        "tax":.07
    },
    {   "name": "Kansas",
        "state": "KS",
        "tax":.065
    },
    {   "name": "Kentucky",
        "state": "KY",
        "tax":.06
    },
    {   "name": "Louisiana",
        "state": "LA",
        "tax":.0445
    },
    {   "name": "Maine",
        "state": "ME",
        "tax":.055
    },
    {   "name": "Maryland",
        "state": "MD",
        "tax":.06
    },
    {   "name": "Massachusetts",
        "state": "MA",
        "tax":.0625
    },
    {   "name": "Michigan",
        "state": "MI",
        "tax":.06
    },
    {   "name": "Minnesota",
        "state": "MN",
        "tax":.06875
    },
    {   "name": "Mississippi",
        "state": "MS",
        "tax":.07
    },
    {   "name": "Missouri",
        "state": "MO",
        "tax":.04225
    },
    {   "name": "Montana",
        "state": "MT",
        "tax":.0
    },
    {   "name": "Nebraska",
        "state": "NE",
        "tax":.055
    },
    {   "name": "Nevada",
        "state": "NV",
        "tax":.0685
    },
    {   "name": "New Hampshire",
        "state": "NH",
        "tax":.0
    },
    {   "name": "New Jersey",
        "state": "NJ",
        "tax":.06625
    },
    {   "name": "New Mexico",
        "state": "NM",
        "tax":.05125
    },
    {   "name": "New York",
        "state": "NY",
        "tax":.04
    },
    {   "name": "North Carolina",
        "state": "NC",
        "tax":.04750
    },
    {   "name": "North Dakota",
        "state": "ND",
        "tax":.05
    },
    {   "name": "Ohio",
        "state": "OH",
        "tax":.05750
    },
    {   "name": "Oklahoma",
        "state": "OK",
        "tax":.045
    },
    {   "name": "Oregon",
        "state": "OR",
        "tax":.0
    },
    {   "name": "Pennsylvania",
        "state": "PA",
        "tax":.06
    },
    {   "name": "Rhode Island",
        "state": "RI",
        "tax":.07
    },
    {   "name": "South Carolina",
        "state": "SC",
        "tax":.06
    },
    {   "name": "South Dakota",
        "state": "SD",
        "tax":.045
    },
    {   "name": "Tennessee",
        "state": "TN",
        "tax":.07
    },
    {   "name": "Texas",
        "state": "TX",
        "tax":.06250
    },
    {   "name": "Utah",
        "state": "UT",
        "tax":.05950
    },
    {   "name": "Vermont",
        "state": "VT",
        "tax":.06
    },
    {   "name": "Virginia",
        "state": "VA",
        "tax":.053
    },
    {   "name": "Washington",
        "state": "WA",
        "tax":.065
    },
    {   "name": "West Virginia",
        "state": "WV",
        "tax":.06
    },
    {   "name": "Wisconsin",
        "state": "WI",
        "tax":.05
    },
    {   "name": "Wyoming",
        "state": "WY",
        "tax":.04
    },
]


# Route for Home page
@app.route('/', methods=['GET'])
def my_form():
    return render_template('home.html')


# A route to return all of the available states in our catalog.
@app.route('/states/', methods=['GET'])
def api_all():
    return jsonify(states)

# GET request in the URL for specific state
@app.route('/states/<string:state>', methods=['GET'])
def returnOne(state):
    theOne = states[0]
    for i,q in enumerate(states):
        if q['state'] == state:
            theOne = states[i]
    return jsonify({'states':theOne})



# Route for form data handling
@app.route('/form', methods=['GET', 'POST'])
def form():
        # handle the POST request
    if request.method == 'POST':
        state = request.form.get("state")
        return redirect(url_for('returnOne', state=state))
    else:
        return render_template("form.html")

# Route for translation microservice
@app.route('/translate', methods=['GET'])
def translate():
    return render_template('translate.html')



if __name__ == '__main__':
    app.run(debug=True)
