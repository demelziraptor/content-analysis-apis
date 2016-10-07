Content Analysis APIs
=====================
Super basic helper classes to use free content analysis / keyword extraction APIs.

Currently supports:

- Yahoo Content Analysis
- OpenCalais (requires API key)

To use
------
Set up the extractor:

    text = """
    Sajid Javid has overturned Lancashire council's rejection of a fracking site, paving the way for shale company Cuadrilla to drill in the county next year and provoking outrage from local groups, environmentalists and politicians.
    """
    extractor = OpenCalaisExtractor(text, key='YOURKEY')

Then there are 4 output options:

    extractor.keywords
    [u'Hydraulic fracturing in the United Kingdom', u'Anti-frackin
    g movement', u'Government of the United Kingdom', u'Sajid Javid', u'Lancashire council', u'local grou
    ps', u'Cuadrilla', u'Cuadrilla Resources', u'Natural environment', u'Balcombe drilling protest']

    extractor.keywords_with_score
    [(u'Hydraulic fracturing in the United Kingdom', 0.9), 
    (u'Anti-fracking movement', 0.9), (u'Government of the United Kingdom', 0.9), (u'Sajid Javid', 0.8), 
    (u'Lancashire council', 0.8), (u'local groups', 0.8), (u'Cuadrilla', 0.8), (u'Cuadrilla Resources', 0
    .8), (u'Natural environment', 0.8), (u'Balcombe drilling protest', 0.8)]

    extractor.results
    {u'http://d.opencalais.com/pershash-1/6bfab1a6-cc29-3756-ba86-535f5f
    929fdd': {u'_typeReference': u'http://s.opencalais.com/1/type/em/e/Person', u'_type': u'Person', u'na
    me': u'Sajid Javid', u'firstname': u'Sajid', u'lastname': u'Javid', u'commonname': u'Sajid Javid', u'
    confidence': {u'aggregate': u'0.98', u'resolution': u'0.0', u'statisticalfeature': u'0.97', u'dblooku
    p': u'0.95'}, u'_typeGroup': u'entities', u'instances': [{u'detection': u"[]Sajid Javid[ has overturn
    ed Lancashire council's rejection of]", u'length': 11, u'exact': u'Sajid Javid', u'suffix': u" has ov
    erturned Lancashire council's rejection of", u'offset': 0}], u'confidencelevel': u'0.98', u'relevance
    ': 0.8, u'nationality': u'N/A', u'forenduserdisplay': u'true', u'persontype': u'N/A'}...

    extractor.raw
    <Response [200]>

There are options to restrict the results, `max_results` (default `10`) and `min_score` (default `0.8`).
    
    extractor = OpenCalaisExtractor(text, key='YOURKEY', max_results=3)
    [(u'Hydraulic fracturing in the United Kingdom', 0.9), (u'Anti-fracking movement', 0.9), (u'Government of the United Kingdom', 0.9)]


