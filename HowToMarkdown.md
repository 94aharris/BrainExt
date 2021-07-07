# How to Markdown #

## Useful Markdown Links ##

* [MarkdownCheatSheet](https://www.markdownguide.org/cheat-sheet/)
* [Full Markdown Guide](https://markdown-guide.readthedocs.io/en/latest/basics.html)

- [x] This is done
- [ ] This is Not Done :(

## Images ##

![demo screenshot](Images/SCS.png)

## Table ##

| Assesment |  Q1   |  Q2   |   Q3 |
| :-------- | :---: | :---: | ---: |
| RT        |   1   |   1   |    2 |
| ER        |   2   |   3   |    3 |
| MM        |   1   |   2   |    2 |


## In Document Links to Headers ##

The IDs are generated from the content of the header according to the following rules:

- All text is converted to lowercase.
- All non-word text (e.g., punctuation, HTML) is removed.
- All spaces are converted to hyphens.
- Two or more hyphens in a row are converted to one.
- If a header with the same ID has already been generated, a unique incrementing number is appended, starting at 1.

[link](this-is-my-header)

## This is my Header ##

From time to time I have encountered a unique header which is converted into an ID in some non-obvious way. A quick way to work out the ID is to use your browser's view source and/or inspect tools to view the HTML source code. For example, you might find the following HTML for your example:

    <h3 id="1-this-is-my-header">1. This is my Header</h3>

Then just use the contents of the id attribute with a hash to link to that header: #1-this-is-my-header.