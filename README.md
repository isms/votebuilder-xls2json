# votebuilder-xls2json

Takes an `xls` file exported from certain sections of Votebuilder (a product of NGP VAN, Inc.), applies desired transforms to the data, and outputs well-formed JSON to stdout.

## Usage

On the command line: `python parse.py <exported xls>`

Typical use might entail saving the output, e.g.: `python parse.py Report.xls > events.json`

## Use as module

It is also possible to use the intermediate functions within the module. For example:

```python
from parse import read_html_from_file, get_dicts_from_html

# read an exported events list
html = read_html_from_file('Report.xls')
dicts = get_dicts_from_html(html)
dicts[0]
```

Which would print a result like this:
```python
{'Scheduled': '6', 'Confirmed': '0', 'Completed': '0', 'Tentative': '0', 'Invited': '0', 'Walk In': '0', 'Conf Twice': '0', 'Paid': '0', 'ID': '55555', 'Wait List': '0', 'Cancelled': '0', 'Left Msg': '0', 'Time': '10:00 AM - 4:00 PM', 'Date': '1/1/13', 'No Show': '0', 'Type': 'Canvassing', 'Event': 'Anytown Canvass', 'Declined': '0'}
```

## Transforms

Before printing the JSON, you can apply specific transforms to the entire list of dictionaries or each dictionary. This makes it possible to, e.g., add fields, remove fields, sort the list of dictionaries, etc. *Note: specific transforms relevant to the 'Event List' export are left in as examples and will be applied by default. You may want to remove these before use.*

To remove transforms, simply delete them from the `DICT_TRANSFORMS` and `LIST_TRANSFORMS` lists at the end of `transforms.py`.

To add a transform that operates on each specific dictionary (to remove or add values, for example), write a function that takes a dictionary as its argument and returns the modified dictionary, then add that function to `DICT_TRANSFORMS`.

To add a transform that operates on the entire list of dictionaries (to sort, for example), write a function that takes a list of dictionaries as its argument and returns the modified list, then add that function to `LIST_TRANSFORMS`.

## Notes

Not all Votebuilder exports are set up the same way. This file works for exported files (such as Events List, Counts and Crosstabs, etc) which are actually an HTML fragment of the following form:

```html
<div>
  <table class="ResultsGridViewControlStyle">
    <tr class="ResultsHeaderStyle">
      <th scope="col"> [...] </th>
      [...]
    </tr>
    <tr class="ResultsRowStyle">
      <td> [...] </td>
      [...]
    </tr>
    <tr class="ResultsAlternateRowStyle"> [...]
      <td> [...] </td>
      [...]
    </tr>
  </table>
</div>
```