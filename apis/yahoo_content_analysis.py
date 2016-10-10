# -*- coding: utf-8 -*-
import json
import requests
from time import sleep

from . import Extractor, RequestError, NoResults


class YahooContentAnalysisExtractor(Extractor):

    def _make_request(self, tries=4):
        if not tries:
            raise RequestError
        d = {'q': "select * from contentanalysis.analyze where text='{text}'".format(
            text=self.text.replace("'", "\\\'"),
        )}
        response = requests.post(
            "http://query.yahooapis.com/v1/public/yql?format=json",
            data=d,
        )
        if response.status_code != 200:
            sleep(1)
            return self._make_request(tries=tries-1)
        return response
    
    @property
    def results(self):
        try:
            r = self.response.json()['query']['results']['entities']['entity']
        except (KeyError, TypeError):
            raise NoResults
        if not isinstance(r, list):
            return [r]
        return r

    def calculate_keywords_with_score(self):
        kws = []
        if not isinstance(self.results, list):
            self.results = [self.results]
        for result in self.results:
            if float(result['score']) >= self.min_score:
                kws.append((result['text']['content'], float(result['score'])))
        return kws

