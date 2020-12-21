# Lab: Web Scraping
## Overview
It’s wonderful when someone has gone to the effort to expose their site’s data through an API.

But not everyone can (or wants to) do that.

No problem. Let’s code up a web scraper that can automate the process of manually using the site.

## Feature Tasks and Requirements
* a Wikipedia page and record which passages need citations.
E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
 web scraper is reported the number of citations needed.
* web scraper is identified those cases AND include the relevant passage.
E.g. Citation needed for “lorem spam and impsum eggs”
**note **the “relevant passage” to be the parent element that contains the passage, often a paragraph element.
## Implementation Notes
* Count function must be named get_citations_needed_count
* get_citations_needed takes in a url and returns an integer
* Report function must be named get_citations_needed_report
* get_citations_needed_report takes in a url and returns a string
* string should be formatted with each citation needed on own line, in order found.

### [The link of repository](https://github.com/Sajanader/web-scraper)
