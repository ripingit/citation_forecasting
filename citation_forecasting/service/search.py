#coding:utf-8

import os
import sys
import json
import urllib

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/' + '..')
from common_config import common_config

autocomplete_url_prefix = common_config.search_server
autocomplete_url_prefix += '/select?rows=0&wt=json&q=*&'
autocomplete_url_prefix += 'facet=true&facet.limit=8&facet.field=normalized_title&'
autocomplete_url_prefix += 'facet.field=author&facet.mincount=1&facet.prefix='

# solr search

field_weights = [
	('normalized_title',10),
	('author',3),
	('keyword',3),
	('publish_year',2),
]

boosting_function = []

highlight_params = [
	('fragsize',10),
]

paging_size = 5

import pysolr

def autocomplete(prefix):
    if isinstance(prefix,list):
        prefix = prefix[0]
    search_url = urllib.urlopen(autocomplete_url_prefix + prefix)
    result = json.loads(search_url.read())
    return result

def search_paper(search_words,start):
    search_text = ''
    for weight in field_weights:
        for w in search_words:
            search_text += weight[0] + ':*' + w + '*^%d '%weight[1]
    for w in search_words:
        search_text += w + ' '

    solr = pysolr.Solr(common_config.search_server)
    results = solr.search(search_text, **{'start':start,'rows': paging_size})
    return results