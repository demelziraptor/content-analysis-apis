# -*- coding: utf-8 -*-

class Extractor(object):

    max_results = 10
    min_score = 0.8

    def __init__(self, text, **kwargs):
        self.text = text.strip().decode('utf-8')
        self.response = self._make_request()
        if kwargs:
            for k, v in kwargs.iteritems():
                setattr(self, k, v)

    def _make_request(self):
        """ return Request """
        raise NotImplementedError

    def _trim_sort_keywords_with_score(self, kws):
        kws = sorted(kws, key=lambda x: x[1], reverse=True)
        return kws[:self.max_results]

    @property
    def raw(self):
        return self.response

    @property
    def results(self):
        """ return better formatted response data """
        raise NotImplementedError

    def calculate_keywords_with_score(self):
        """ return list of (keyword,score) tuples """
        raise NotImplementedError

    @property
    def keywords_with_score(self):
        return self._trim_sort_keywords_with_score(self.calculate_keywords_with_score())

    @property
    def keywords(self):
        return [v for v, _ in self.keywords_with_score]


class NotImplementedError(Exception):
    pass


class RequestError(Exception):
    pass

class MissingCredentialsError(Exception):
    pass

