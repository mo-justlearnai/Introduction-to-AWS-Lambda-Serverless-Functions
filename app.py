# ==================================================
# Title: Lambda function
# Author: Mattithyahu
# Created Date: 26/06/2023
# ==================================================

# Imports test block
# ==================================================
try:
    import json
    import pandas as pd
    import sklearn
    import requests
    import numpy as np

    from warnings import filterwarnings
    filterwarnings('ignore')

except Exception as e:
    print(f"Errors : {e} ")


# Lambda function
# ==================================================
def lambda_handler(event, context):

    print("\n[INFO]: Starting Lambda function..")
    
    NAME = event['name']
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'My name is {NAME}')
    }
