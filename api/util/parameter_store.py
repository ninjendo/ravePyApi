import boto3
import json
from collections import defaultdict


def load_ssm_parameter(ssm_key, is_encrypted=True):
    print(ssm_key)
    ssm = boto3.client('ssm')
    ssm_params = defaultdict()
    parameter = ssm.get_parameter(Name=ssm_key, WithDecryption=is_encrypted)
    if parameter:
        ssm_params = json.loads(parameter['Parameter']['Value'])
    return ssm_params
