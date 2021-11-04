# CS361
CS361 Repository
Test Commit


How to run:

1. Open terminal and type 
```cd /Users/Documents``` (or wherever else you want to save the project)
2. Then type 
```git clone https://github.com/reyejona/cs361-project.git ```
to clone the project into that folder

3. to install dependencies (Mac OS) type 
```python3 -m pip install -r requirements.txt```

4. Run 
```pip3 install virtualenv``` 
to install the virtual environment

5. Then run 
```python3 -m venv ./venv```

6. Now, activate the virtual environment by running 
```source ./venv/bin/activate```

7. Run 
```source ./venv/bin/activate``` 
again to activate the virtual environment

8. Finally, run 
``` export FLASK_APP=api```

9. then 
``` flask run``` 
and Boom! It should run on port 5000
