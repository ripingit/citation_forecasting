#coding:utf-8

import os
import json

params_file = os.path.dirname(os.path.abspath(__file__)) + '/' + 'service/params.json'
#params_file = os.path.dirname(os.path.abspath(__file__)) + '/' + 'service/param15.json'

# original dataset
dataset_dir = '/Volumes/exFAT/tmp/academic'
preprocessed_dataset_dir = os.path.dirname(os.path.abspath(__file__)) + '/../dataset/academic'
aln_seq = preprocessed_dataset_dir + '/aln_seq.csv'
aln_fea = preprocessed_dataset_dir + '/aln_fea.csv'
aln_vau = preprocessed_dataset_dir + '/aln_vau.csv'

# location of solr
#search_server = 'http://localhost:8983/solr/paper'
search_server = 'http://202.120.80.35:8983/solr/paper'
autocomplete_url_prefix = 'http://202.120.80.35:8983/solr/paper/select?rows=0&wt=json&q=*&'
autocomplete_url_prefix += 'facet=true&facet.limit=8&facet.field=normalized_title&'
autocomplete_url_prefix += 'facet.field=author&facet.mincount=1&facet.prefix='

#training
train_count = 1
converge = 1e-1

# citation prediction
params_json = {}
with open(params_file) as fr:
	params_json = json.load(fr)
