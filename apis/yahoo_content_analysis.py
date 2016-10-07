# -*- coding: utf-8 -*-
import json
import requests

from . import Extractor, RequestError


class YahooContentAnalysisExtractor(Extractor):

    def _make_request(self):
        d = {'q': "select * from contentanalysis.analyze where text='{text}'".format(
            text=self.text.replace("'", "\\\'"),
        )}
        response = requests.post(
            "http://query.yahooapis.com/v1/public/yql?format=json",
            data=d,
        )
        if response.status_code != 200:
            raise RequestError
        return response
    
    @property
    def results(self):
        r = self.response.json()['query']['results']['entities']['entity']
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

