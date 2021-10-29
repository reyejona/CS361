from flask import Flask
import os
app = Flask(__name__) 
@app.route("/") 
def hello(): 
    return "A message from CS361" 
if __name__ == "__main__": 
    port = int(os.environ.get('PORT', 500)) 
    app.run()


