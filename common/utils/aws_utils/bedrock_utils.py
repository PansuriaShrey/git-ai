import json
import os

import boto3

from common.constants import AWSConstants
from common.prompts import COMMIT_MESSAGE_PROMPT


def suggest_commit_message(diff_text):
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    prompt = COMMIT_MESSAGE_PROMPT.format(diff_text=diff_text)

    response = bedrock_client.invoke_model(
        modelId=AWSConstants.BEDROCK_MODEL_ID,
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": AWSConstants.MAX_TOKENS,
                "temperature": 0,
                "messages": [
                    {"role": "user", "content": [{"type": "text", "text": prompt}]}
                ],
            }
        ),
    )

    response_body = json.loads(response["body"].read())
    return response_body["content"][0]["text"].strip()
