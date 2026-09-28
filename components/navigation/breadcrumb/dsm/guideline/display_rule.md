The general display rule is: Depending on the screen width (breakpoint), we hierarchically hide page names by prioritizing the display of the currently viewed page back to the homepage.
We prioritize displaying the name of the currently viewed page, then the previous page, and so on, up to displaying the homepage name if the screen width allows it.

At a minimum, and for all breakpoints, the currently viewed page and page n-1 (the page preceding the currently viewed page) are always displayed.
Depending on the breakpoints, the number of pages shown or hidden changes:
- 2xs, xs, sm: 2 names max -> Previous / Current
- md: 3 names max -> Previous / Previous / Current
- lg: 4 names max -> Previous / Previous / Previous / Current
- xl, 2xl, 3xl: The entire hierarchy is displayed

Note that technically (CSS helper classes) and depending on the breakpoint, it is possible to force the specific display of a page that is not shown by default, and vice versa.

Except for the name of page n-1, which is never truncated, the names of the other pages may be truncated (from the homepage to the currently viewed page inclusive).
Note that technically (CSS helper classes), we retain the ability not to truncate the display of a specific page (for example, we prefer not to truncate the homepage name).