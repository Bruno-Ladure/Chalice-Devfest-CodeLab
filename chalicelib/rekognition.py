# -*- coding: utf-8 -*-​
import os

import boto3

__REGION = os.environ['AWS_DEFAULT_REGION']
__MAX_LABELS = int(os.getenv('MAX_LABELS', '10'))
__MIN_CONFIDENCE = int(os.getenv('MIN_CONFIDENCE', '90'))


def analyse(bucket, key, region='eu-west-'):
    """Analyse an image with AWS Rekognition service and return analys

    Arguments:
        bucket {str} -- the bucket where the image is
        key {str} -- the key path to the images

    Returns:
        str -- the image tags with space separator
    """
    rekognition = boto3.client("rekognition", __REGION)
    response = rekognition.detect_labels(
        Image={"S3Object": {
            "Bucket": bucket,
            "Name": key,
        }},
        MaxLabels=__MAX_LABELS,
        MinConfidence=__MIN_CONFIDENCE,
    )
    rekos = [reko.get('Name') for reko in response['Labels']]
    return ' '.join(rekos)
