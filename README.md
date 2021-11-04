# CS361
CS361 Repository
Test Commit


How to run:
## Make sure you have python3 installed on your computer.


1. Open terminal and type 
```cd /Users/Documents``` (or wherever else you want to save the project)
2. Then type 
```git clone https://github.com/reyejona/taxrateAPI.git ```
to clone the project into that folder

3. move to the taxrateAPI folder in the directory
 ```cd taxrateAPI```

5. To install dependencies (Mac OS) type 
```python3 -m pip install -r requirements.txt```

4. To install virtual enviornment Run 
```pip3 install virtualenv``` 

5. Then run 
```python3 -m venv ./venv```

6. Now, activate the virtual environment by running 
```source ./venv/bin/activate```

7. Finally, run 
``` export FLASK_APP=api```

8. then 
``` flask run``` 
and Boom! It should run on port 5000


## Running the application
To search for a state using a POST request
1. Click on > "search for a state sales tax rate" 
2. Type in 2 letter state abbreviation i.e. "CA" = California
3. State should be displayed as a json object


To translate a language
1. Click on  > "translate text to a different language"
2. Type in your language as a string "FR" for french, "ES" for spanish, "CH" for Chinese etc.
3. Type in the text you want to translate.
4. Hit the submit button!
5. It should return translated text.

To display all states
1. Go to ```http://127.0.0.1:5000/states/```
2. It will display all states as a json dictionary

To search for 1 state using a GET request through the URL
1. Type in ```http://127.0.0.1:5000/states/<state_abbreviation>```
2. Where <state_abbreviation> is a 2 letter state abbreviation ie Texas is "TX"
3. It will display state information as a json object.
