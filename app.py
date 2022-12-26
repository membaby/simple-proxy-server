from flask import Flask, render_template, request, url_for, redirect, abort
import requests
import sys
import logging

app = Flask(__name__, static_url_path='/')

ALLOWED_IPS = [

]

BLOCKED_IPS = [

]

PORT = 6405

@app.before_request
def limit_remote_addr():
    if len(ALLOWED_IPS):
        if (len(ALLOWED_IPS) and request.remote_addr not in ALLOWED_IPS) or request.remote_addr in BLOCKED_IPS:
            logger.info('Aborted IP: ' + request.remote_addr)
            abort(403)

@app.route('/')
def show_custom_homepage():
    url = request.args.get('url')
    if 'http' not in url:
        url = 'https://' + url
    try:
        response = requests.get(url, timeout=20)
    except:
        return 'Error: Could not connect to ' + url
    
    logger.info('Request: ' + url)
    return response.text

def initialize_logging():
    global logger
    logging.basicConfig(filename="logging.log", format='%(asctime)s [%(levelname)s] %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Scraper started.')

if __name__ == '__main__':
    logger = None
    initialize_logging()
    app.run(host='0.0.0.0', port=PORT)