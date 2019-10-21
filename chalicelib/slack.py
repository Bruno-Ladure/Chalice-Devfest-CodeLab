# -*- coding: utf-8 -*-​
import logging
import os

import requests

REGION = os.environ['AWS_DEFAULT_REGION']
IDENTITY = os.environ['IDENTITY']
BUCKET_NAME = os.environ['BUCKET_NAME']
SLACK_MESSAGE_WH = os.environ['SLACK_MESSAGE_WH']

# TODO
# Declare the blueprint


__logger = logging.getLogger()
__logger.setLevel(logging.DEBUG)

# TODO
# Schedule this lambda
# see https://chalice.readthedocs.io/en/latest/topics/events.html#scheduled-events
# and
# https://docs.aws.amazon.com/fr_fr/AmazonCloudWatch/latest/events/ScheduledEvents.html
# for schedule expressions


def rocker_speak(event):
    """Post a random citation in slack

    Arguments:
        event {dict} -- a cloudwatch cron event
    """
    # TODO
    # Get a citation with the citation python module
    author, citation = ('auteur', 'citation',)
    slack_message = {
        "blocks": [{
            "type": "divider"
        }, {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": IDENTITY
            }
        }, {
            "type": "divider"
        }, {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": citation
            }
        }, {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_{}_".format(author)
            }
        }]
    }
    __logger.debug(slack_message)
    response = requests.post(url=SLACK_MESSAGE_WH, json=slack_message)
    __logger.info(response)

# TODO
# Trigger this lambda on S3 object creation event
# see https://chalice.readthedocs.io/en/latest/topics/events.html#s3-events


def rock_on_stage(event):
    """On image creation in S3, post a message in Slack

    Arguments:
        event {dict} -- and s3 event with bucket a key
    """
    if event.key[-4:] in ['.png', '.jpg']:
        file_path = "https://{}.s3-{}.amazonaws.com/{}".format(
            event.bucket, REGION, event.key)
        # TODO
        # Get Tags from Rekognition
        # use the rekognition python module
        tags = "tag1 tag2"
        slack_message = {
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": IDENTITY
                }
            }, {
                "type": "divider"
            }, {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "A new picture was uploaded"
                },
                "block_id": event.key,
                "image_url": file_path,
                "alt_text": "images"
            }, {
                "type": "divider"
            }, {
                "type":
                "context",
                "elements": [{
                    "type":
                    "mrkdwn",
                    "text":
                    "Tags: *{}*".format(tags)
                }]
            }]
        }
        __logger.debug(slack_message)
        # response = requests.post(url=SLACK_MESSAGE_WH, json=slack_message)
        # __logger.info(response)
