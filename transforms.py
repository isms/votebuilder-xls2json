""" Supporting module for parse.py containing all desired transforms. To
    add a transform that takes a single dictionary and alters it, write
    the function and then add it (in the proper order) to DICT_TRANSFORMS.
    To operate on the entire list of dicts, add it to LIST_TRANSFORMS instead.
"""
from datetime import datetime, timedelta

DATE_FORMAT = '%m/%d/%y'
DESIRED_KEYS = ['ID', 'Date', 'Event', 'Time', 'Type']


def apply_transforms(dicts):
    """ Apply all desired transforms to the dictionaries """
    for transform in DICT_TRANSFORMS:
        dicts = [transform(d) for d in dicts]
    for transform in LIST_TRANSFORMS:
        dicts = [transform(d) for d in dicts]
    return dicts


def filter_dict(d_in):
    """ Get rid of all (k, v) pairs we don't care about """
    return dict({k: d_in[k] for k in DESIRED_KEYS})


def fix_date(d_in):
    """ Change dates from, e.g. '3/2/13' to '03/02/13' for better sorting """
    date_in = datetime.strptime(d_in['Date'].split()[0], DATE_FORMAT)
    d_in['Date'] = datetime.strftime(date_in, DATE_FORMAT)
    return d_in


def insert_region(d_in):
    """ Try to lookup a region """
    d_in['Region'] = '' # leave blank for now
    return d_in


def manual_tweak(d_in):
    """ Any one-off tweaks that don't make sense anywhere else """
    # one event displaying wrong
    if d_in['ID'] == '42645':
        d_in['Time'] = '12:30 PM - 4:00 PM'
    return d_in


def sort_by_date(dicts):
    """ Sort the list of dicts by the 'Date' field """
    return sorted(dicts, key=lambda d_in: d_in['Date'])

# Order matters; these will be applied in the order they appear
DICT_TRANSFORMS = [
    filter_dict,
    fix_date,
    manual_tweak,
    insert_region,
]

LIST_TRANSFORMS = [
    sort_by_date,
]