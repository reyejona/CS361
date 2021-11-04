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
