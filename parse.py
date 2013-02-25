#!/usr/bin/env python
""" Take the spreadsheet file exported from Votebuilder xls and output well
    formed JSON.
"""
import sys
import simplejson
from lxml.html import fromstring

ROW_CLASS_NAMES = ['ResultsHeaderStyle', 'ResultsRowStyle',
    'ResultsAlternateRowStyle']

def get_lines_from_html(html):
    """ Parse the file to find the headers and all content rows of the
        table.

        Returns a tuple of (headers, all other lines)
    """
    doc = fromstring(html)
    # get all the table rows, headers should always be first
    rows = []
    for name in ROW_CLASS_NAMES:
        rows += doc.find_class(name)
    lines = [[child.text_content() for child in row.getchildren()]
        for row in rows]
    return (lines[0], lines[1:]) # (headers, all other lines)

def get_row_dicts(headers, lines):
    """ Take all lines as lists read in from the file and put the
        row fields in the right order and sort lines by date """
    return [dict((headers[i], line[i]) for i in range(len(headers)))
        for line in lines]

def main(filename):
    """ Open the desired file, parse html, and output json """
    xls_file = open(filename, 'r')
    html = xls_file.read()
    xls_file.close()
    headers, lines = get_lines_from_html(html)
    rows = get_row_dicts(headers, lines)
    json = simplejson.dumps(rows, sort_keys=True, indent=4)
    print(json)

if (__name__ == '__main__'):
    if not len(sys.argv) == 2:
        print('Usage: python parse.py <filename>')
        sys.exit(1)
    main(sys.argv[1])