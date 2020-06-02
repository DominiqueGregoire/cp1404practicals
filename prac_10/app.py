from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! :)'


# # add the greet function
# @app.route('/greet')
# def greet():
#     return 'Hello'

# add the greet name function
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return 'Hello {}'.format(name)


# convert between Fahrenheit and Celsius
@app.route('/convert_celsius_to_fahrenheit/<celsius>')
def convert_celsius_to_fahrenheit(celsius=''):
    #   version 1
    # return str(float(celsius) * 1.8 + 32)
    #   version 2
    fahrenheit = float(celsius) * 1.8 + 32
    return '{} degrees Celsius converts to {} degrees Fahrenheit'.format(celsius, str(fahrenheit))



# def convert_celsius_to_fahrenheit(celsius=''):
#     celsius = "37"
#     return float(celsius) * 1.8 + 32


if __name__ == '__main__':
    app.run()
