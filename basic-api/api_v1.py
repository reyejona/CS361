from flask import Flask, jsonify, request

app = Flask(__name__)



states =  [
    {   'state': 'AL',
        'tax':.04
    },
    {   'state':'AK',
        'tax':0
    },
    {   'state': 'AZ',
        'tax':.056
    },
    {   'state': 'AR',
        'tax':.065
    },
    {   'state': 'CA',
        'tax':.0725
    },
    {   'state': 'CO',
        'tax':.029
    },
    {   'state': 'CT',
        'tax':.06350
    },
    {   'state': 'DE',
        'tax':.0
    },
    {   'state': 'DC',
        'tax':.06
    },
    {   'state': 'FL',
        'tax':.06
    },
    {   'state': 'GA',
        'tax':.04
    },
    {   'state': 'HI',
        'tax':.04166
    },
    {   'state': 'ID',
        'tax':.06
    },
    {   'state': 'IL',
        'tax':.06250
    },
    {   'state': 'IN',
        'tax':.07
    },
    {   'state': 'KS',
        'tax':.065
    },
    {   'state': 'KY',
        'tax':.06
    },
    {   'state': 'LA',
        'tax':.0445
    },
    {   'state': 'ME',
        'tax':.055
    },
    {   'state': 'MD',
        'tax':.06
    },
    {   'state': 'MA',
        'tax':.0625
    },
    {   'state': 'MI',
        'tax':.06
    },
    {   'state': 'MN',
        'tax':.06875
    },
    {   'state': 'MS',
        'tax':.07
    },
    {   'state': 'MO',
        'tax':.04225
    },
    {   'state': 'MT',
        'tax':.0
    },
    {   'state': 'NE',
        'tax':.055
    },
    {   'state': 'NV',
        'tax':.0685
    },
    {   'state': 'NH',
        'tax':.0
    },
    {   'state': 'NJ',
        'tax':.06625
    },
    {   'state': 'NM',
        'tax':.05125
    },
    {   'state': 'NY',
        'tax':.04
    },
    {   'state': 'NC',
        'tax':.04750
    },
    {   'state': 'ND',
        'tax':.05
    },
    {   'state': 'OH',
        'tax':.05750
    },
    {   'state': 'OK',
        'tax':.045
    },
    {   'state': 'OR',
        'tax':.0
    },
    {   'state': 'PA',
        'tax':.06
    },
    {'  state': 'RI',
        'tax':.07
    },
    {   'state': 'SC',
        'tax':.06
    },
    {   'state': 'SD',
        'tax':.045
    },
    {   'state': 'TN',
        'tax':.07
    },
    {   'state': 'TX',
        'tax':.06250
    },
    {   'state': 'UT',
        'tax':.05950
    },
    {   'state': 'VT',
        'tax':.06
    },
    {   'state': 'VA',
        'tax':.053
    },
    {   'state': 'WA',
        'tax':.065
    },
    {   'state': 'WV',
        'tax':.06
    },
    {   'state': 'WI',
        'tax':.05
    },
    {   'state': 'WY',
        'tax':.04
    },
]



@app.route('/', methods=['GET'])
def home():
    return "<h1>United States Tax Rates</h1><p>This site is a prototype API for finding US Sales Tax Rates.</p>"


# A route to return all of the available states in our catalog.
@app.route('/states/all', methods=['GET'])
def api_all():
    return jsonify(states)


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    state = request.args.get('state')

    return '''<h1>The state is: {}</h1>'''.format(state)


# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
        # handle the POST request
    if request.method == 'POST':
        state = request.form.get('state')
        tax = request.form.get('tax')
        return '''
                  <h1>The state value is: {}</h1>
                  <h1>The tax value is: {}</h1>'''.format(state, tax)
    return '''
              <form method="POST">
                  <div><label>State: <input type="text" name="State"></label></div>
                  <div><label>Tax: <input type="text" name="tax"></label></div>
                  <input type="submit" value="Submit">
              </form>'''


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    state = None
    tax = None

    if request_data: 
        if 'state' in request_data:
            state = request_data['state']

        if 'tax' in request_data:
            tax = request_data['tax']


    return '''
           The State is: {}
           The State Sales tax rate is: {}
           '''.format(state, tax)






@app.route('/states', methods=['GET'])
def api_id():
    # Check if an state was provided as part of the URL.
    # If state is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'state' in request.args:
        state = str(request.args['state'])
    else:
        return "Error: No state field provided. Please specify a state."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested state.
    # IDs are unique, but other fields might return many results
    for state in states:
        if state['state'] == state:
            results.append(state)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)