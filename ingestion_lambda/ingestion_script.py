import json
import os
import requests
import boto3
import snowflake.connector
from snowflake.connector.errors import ProgrammingError
from cryptography.hazmat.primitives import serialization
from datetime import datetime

snowflake_connection = None

def get_secrets():

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name = )