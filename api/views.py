from django.shortcuts import render
import requests
from .models import WowApiClientError, WowApiError
from auction.settings import WOW_API

def handle_request(url, params=None):
        try:
            response = requests.get(url, params=params)
        except requests.RequestException as e:
            raise WowApiClientError(e)

        try:
            json_data = response.json()
        except ValueError:
            raise WowApiClientError(
                '{} - Missing json - {}'.format(response.status_code, response.content))

        if not response.ok:
            if 'status' in json_data.keys():
                raise WowApiError(
                    response.status_code, json_data['status'], json_data.get('reason'))

            raise WowApiClientError(
                '{} - Something went wrong - {}'.format(
                    response.status_code, response.content))

        return json_data


def get_auction():
    print "Get Auction"
    response = handle_request("https://eu.api.battle.net/wow/auction/data/"+WOW_API['server']+"?locale="+WOW_API['locale']+"&apikey="+WOW_API['apikey'])
    return response['files'][0]['url']

def get_item(id):
    response = [];
    if id:
        print "https://eu.api.battle.net/wow/item/"+ id +"?locale="+WOW_API['locale']+"&apikey="+WOW_API['apikey']
        response = handle_request("https://eu.api.battle.net/wow/item/"+ id +"?locale="+WOW_API['locale']+"&apikey="+WOW_API['apikey'])
    return response;
