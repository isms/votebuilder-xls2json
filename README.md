# votebuilder-xls2json

Takes an `xls` file exported from certain sections of Votebuilder and outputs well-formed JSON.

Usage: `python parse.py <exported xls>`

Not all Votebuilder exports are set up the same way. This file works for exported files (such as Events List, Counts and Crosstabs, etc) which are actually an HTML fragment of the following form:

```
            <div>
              <table class="ResultsGridViewControlStyle" [...] >
                <tr class="ResultsHeaderStyle">
                  <th scope="col"> [...] </th>
                  [...]
                </tr>
            /   <tr class="ResultsRowStyle">
            |     <td> [...] </td>
            |     [...]
(repeating) |   </tr>
            |   <tr class="ResultsAlternateRowStyle"> [...]
            |     <td> [...] </td>
            |     [...]
            \   </tr>
              </table>
            </div>
```

Votebuilder is a product of NGP VAN, Inc.