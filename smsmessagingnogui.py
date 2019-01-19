from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from string import digits as string_digits
from random import choice as random_choice
from devicefunctions import unlockDevice

def run():
      random_num = ''.join(random_choice(string_digits) for i in range(5))
      print(random_num)
      loop_active = True
      while loop_active:
          user_input = 0
          if user_input == 0:
              loop_active = False
              app = Flask(__name__)
              account_sid = 'AC42e108b0ca9beea35600b65013bc3d95'
              auth_token = '0cb8be0e4d5c9438cac8896e09e8e4dd'
              client = Client(account_sid, auth_token)
              message = client.messages \
                  .create(
                  body="New device detected; please type in the code displayed on your screen.",
                  from_='+17747736090',
                  to='+14017719495'
              )
              print(message.sid)

              def shutdown_server():
                  func = request.environ.get('werkzeug.server.shutdown')
                  if func is None:
                      raise RuntimeError('Not running with the Werkzeug Server')
                  func()

              @app.route("/sms", methods=['GET', 'POST'])
              def incoming_sms():
                  """Send a dynamic reply to an incoming text message"""
                  messagereply = request.values.get('Body', None)

                  resp = MessagingResponse()

                  if messagereply == str(random_num):
                      resp.message("Thank you!")
                      print(resp)
                      unlockDevice('*')
                      shutdown_server()
                      return str(resp)

                  elif messagereply != str(random_num):
                      resp.message("Nice Try.")
                      print(resp)
                      return str(resp)  
          app.run()
        

if __name__ == "__main__":
  run()
