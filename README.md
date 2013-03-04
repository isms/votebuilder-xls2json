# votebuilder-xls2json

Takes an `xls` file exported from certain sections of Votebuilder (a product of NGP VAN, Inc.) and outputs well-formed JSON.

Usage: `python parse.py <exported xls>`

Not all Votebuilder exports are set up the same way. This file works for exported files (such as Events List, Counts and Crosstabs, etc) which are actually an HTML fragment of the following form:

```html
<div>
  <table class="ResultsGridViewControlStyle" [...] >
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