from flask import Flask
from flask import request

app = Flask(__name__) #__name__ means this current file


@app.route('/postjson', methods=['POST'])
def postJsonHandler:
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'

@app.route('/')
def hello_world():
    return 'Hello World!'

'''when you run your python script, python assign the name __main__ to the script when executed
if statement prevents other script from runningWhen we run main.py, it will change its name to 
__main__ and only then will that if statement activate.'''
if __name__ == '__main__':
    app.run()
