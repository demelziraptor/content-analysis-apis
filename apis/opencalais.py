# -*- coding: utf-8 -*-
import requests

from . import Extractor, RequestError, MissingCredentialsError


class OpenCalaisExtractor(Extractor):

    def __init__(self, text, key=None, **kwargs):
        if not key:
            raise MissingCredentialsError("Please pass key as argument")
        self.key = key
        super(OpenCalaisExtractor, self).__init__(text, **kwargs)

    def _make_request(self):
        headers = {'X-AG-Access-Token' : self.key, 'Content-Type' : 'text/raw', 'outputformat' : 'application/json'}
        response = requests.post(
            "https://api.thomsonreuters.com/permid/calais",
            data=self.text,
            headers=headers,
        )
        if response.status_code != 200:
            raise RequestError
        return response

    def _calculate_score(self, score, relevance, importance):
        return score or relevance or 1-(float(importance)/10)

    @property
    def results(self):
        return self.response.json()

    def calculate_keywords_with_score(self):
        grouptypes_to_ignore = ['language', 'versions']
        kws = []
        for k, v in self.results.iteritems():
            if k == 'doc':
                continue
            if v['_typeGroup'] in grouptypes_to_ignore:
                continue
            score = self._calculate_score(
                v.get('score'),
                v.get('relevance'),
                v.get('importance'),
            )
            kws.append((v['name'], score))
        return kws

