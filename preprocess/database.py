# database definition
import sys, os
# reload(sys)
# sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/' + '..')

import pysolr
from common_config import dataset_dir
import json
import sqlite3

dbfile = os.path.dirname(os.path.abspath(__file__)) + '/' + 'preprocess/academic.db'
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