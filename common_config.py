#coding:utf-8

import os
import json

#training
params_file = os.path.dirname(os.path.abspath(__file__)) + '/' + 'model/params.json'
#params_file = os.path.dirname(os.path.abspath(__file__)) + '/' + 'model/param15.json'
# citation prediction
params_json = {}
with open(params_file) as fr:
	params_json = json.load(fr)


train_count = 1
converge = 1e-1

# MySQLdb
import sqlite3

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

# database definition
dbfile = os.path.dirname(os.path.abspath(__file__)) + '/' + 'model/academic.db'
tables = [
	{
		'name':'paper',
		'fields':["id","original_title","normalized_title","publish_year",
			"publish_date","DOI","original_venue","normalized_venue",
			"journal_id","conference_series_id","paper_rank"],
		'file':dataset_dir + '/Papers.txt'
	},
	{
		'name':'paper_url',
		'fields':["paper_id","url"],
		'file':dataset_dir + '/PaperUrls.txt'
	},
	{
		'name':'paper_author_affiliation',
		'fields':['paper_id','author_id','affiliation_id','original_affiliation',
			'normalized_affiliation','author_sequence_number'],
		'file':dataset_dir + '/PaperAuthorAffiliations.txt'
	},
	{
		'name':'paper_keyword',
		'fields':['paper_id','keyword','study_field_id'],
		'file':dataset_dir + '/PaperKeywords.txt'
	},
	{
		'name':'paper_reference',
		'fields':['paper_id','reference_id'],
		'file':dataset_dir + '/PaperReferences.txt'
	},
	{
		'name':'affiliation',
		'fields':['id','name'],
		'file':dataset_dir + '/Affiliations.txt'
	},
	{
		'name':'author',
		'fields':['id','name'],
		'file':dataset_dir + '/Authors.txt'
	},
	{
		'name':'conference_series',
		'fields':['id','name','full_name'],
		'file':dataset_dir + '/ConferenceSeries.txt'
	},
	{
		'name':'journal',
		'fields':['id','name'],
		'file':dataset_dir + '/Journals.txt'
	},
	{
		'name':'study_field',
		'fields':['id','name'],
		'file':dataset_dir + '/FieldsOfStudy.txt'
	}
]

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


#create database
conn = sqlite3.connect(dbfile)

for table in tables:
	sql = "create table if not exists '" + table['name'] + "'("
	comma = 0
	for field in table['fields']:
		if comma == 0:
			comma = 1
		else:
			sql += ","
		sql += field + " varchar(255) "
	sql += ")"
	conn.execute(sql)
	conn.commit()
conn.close()








