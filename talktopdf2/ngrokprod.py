from pyngrok import ngrok
import yaml

# Terminate open tunnels if exist
ngrok.kill()

# Setting the authtoken
# Get your authtoken from `ngrok_credentials.yml` file
with open('ngrok_api_credentials.yml', 'r') as file:
    NGROK_AUTH_TOKEN = yaml.safe_load(file)
ngrok.set_auth_token(NGROK_AUTH_TOKEN['ngrok_key'])

# Open an HTTPs tunnel on port XXXX which you get from your `logs.txt` file
ngrok_tunnel = ngrok.connect(8501)
print("Streamlit App:", ngrok_tunnel.public_url)