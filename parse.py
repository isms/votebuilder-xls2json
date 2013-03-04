#!/usr/bin/env python
""" Take the spreadsheet file exported from Votebuilder xls and output well
    formed JSON.
"""
import sys
import simplejson
from lxml.html import fromstring

TR_CLASS_NAMES = ['ResultsHeaderStyle', 'ResultsRowStyle',
    'ResultsAlternateRowStyle']

def get_lists_from_html(html):
    """ Parse the file to find the headers and all content rows of the
        table. Returns a tuple of (headers, all other rows) """
    doc = fromstring(html)
    # get all the tr elements, headers will always be first
    trs = []
    for class_name in TR_CLASS_NAMES:
        trs += doc.find_class(class_name)
    # extract the contents of all of the td (or th, for headers) children
    rows = [[td.text_content() for td in tr.getchildren()] for tr in trs]
    return (rows[0], rows[1:]) # (headers, all other rows)

def get_dicts_from_lists(headers, contents):
    """ Take all rows as lists turn them into dictionaries with the headers
        as keys for all dicts and the values in each row as values in each
        corresponding dictionary """
    size = range(len(headers))
    return [dict((headers[i], row[i]) for i in size) for row in contents]

def get_dicts_from_html(html):
    """ Higher level function to go straight from HTML to list of row
        dictionaries by combining other functions """
    headers, contents = get_lists_from_html(html)
    return get_dicts_from_lists(headers, contents)

def get_json_from_dicts(dicts):
    """ Given list of row dictionaries, return pretty printed JSON """
    return simplejson.dumps(dicts, sort_keys=True, indent=4)

def get_json_from_html(html):
    """ Higher level function to go straight from HTML to JSON by combining
        other functions """
    dicts = get_dicts_from_html(html)
    return get_json_from_dicts(dicts)

def read_html_from_file(filename):
    """ Opens the file and returns the contents """
    return open(filename, 'r').read()

def main(filename):
    """ Open the desired file, parse html, and output json """
    html = read_html_from_file(filename)
    json = get_json_from_html(html)
    print(json)

if (__name__ == '__main__'):
    if not len(sys.argv) == 2:
        print('Usage: python parse.py <filename>')
        sys.exit(1)
    main(sys.argv[1])