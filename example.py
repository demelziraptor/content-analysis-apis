# -*- coding: utf-8 -*-
from apis.yahoo_content_analysis import YahooContentAnalysisExtractor
from apis.opencalais import OpenCalaisExtractor


text = """
Sajid Javid has overturned Lancashire council's rejection of a fracking site, paving the way for shale company Cuadrilla to drill in the county next year and provoking outrage from local groups, environmentalists and politicians.
"""

print "For the text:"
print text

extractor = YahooContentAnalysisExtractor(text)
print "Result for Yahoo (keywords only): " + str(extractor.keywords)

OPENCALAIS_KEY = 'YOURKEY'
extractor = OpenCalaisExtractor(text, OPENCALAIS_KEY)
print "Result for Opencalais (keywords only): " + str(extractor.keywords)
print "Result for Opencalais (keywords with scores): " + str(extractor.keywords_with_score)
print "Result for Opencalais (results): " + str(extractor.results)
print "Result for Opencalais (raw): " + str(extractor.raw)

extractor = OpenCalaisExtractor(text, OPENCALAIS_KEY, max_results=3)
print "Top 3 results for Opencalais: " + str(extractor.keywords_with_score)

