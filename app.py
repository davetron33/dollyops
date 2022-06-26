import redis
import os
from flask import Flask

# This is your standard Flask application that writes a key/value pair to redis, and then reads it right back to the user.
app = Flask(__name__)

# On the one hand, we're not committing a password to git in the application code.
# On the other, it's still easily readable in the docker-compose file.
#
# A better option for this, IMO would be to utilize a key store, and templatize the redis configuration.
REDIS_PASS = os.environ['REDIS_PASS']
@app.route('/')


# dolly_ctf() takes no arguments, simply returns the value of the 'dolly_ctf' variable.
def dolly_redis():

    # Initilize the 'dolly_ctf' variable (ctf for 'capture the flag')
    dolly_ctf = ""

    # Establish a connection to the redis docker image.
    r = redis.Redis(host='redis', port=6379,  charset="utf-8", decode_responses=True, db=1, password=REDIS_PASS)

    # Write the 'dolly_ctf' key and set it's value to a nice message for Mr. Jarvis.
    r.set('dolly_ctf','Hello Mr. Jarvis. The Redis DB sends its regards.')

    # Get the response and store it as the value to a variable so we can print it later.
    response = r.get('dolly_ctf')

    # Convert the response to a string, otherwise expect DataType exceptions and assign the result to the 'dolly_ctf' variable.
    dolly_ctf = str(response)
    return dolly_ctf

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9001)
