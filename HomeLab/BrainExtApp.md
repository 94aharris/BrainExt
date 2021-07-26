# BrainExt Application #

## Thoughts ##

- Utilize Python (Django) for the markdown conversion? Part of the build or dynamically at the app?
  - Deffinitely part of the build, dynamically would slow things down
- Need some sort of search index, Elasticsearch maybe?
- Not sure what I would use a Postgresql DB for other than user login, tbd I suppose
- Python would be good for doing DS / Graphs but would I need those other than the relationship graph?
- Angular w/ Typescript is still on the table, if nothing else since that is used heavily at work
- Backend?
  - Docker would be nice but may be overkill, other than to just learn it better
  - Heroku is an option, but what's the price look like on that? Heroku free nodes shutdown after 30 mins of inactivity
  - CloudFlare workers are different, thats V8 infra, like javascript
  - again, why would I need a DB? Search index is more of what I'm after
- I'm essentially designing a CMS that hooks up to github...
- I do want to tinker more with docker and such, the app is less important to me, I want to learn how to better deploy things

## Resources ##

- [Gatsby Digital Garden (example)](https://github.com/mathieudutour/gatsby-digital-garden#readme)
- [RoamSearch (example)](https://roamresearch.com/)
- [Gitbook(Example)](https://www.gitbook.com/)
- [Everything I Know (Example)](https://wiki.nikitavoloboev.xyz/)
  - [His other page](https://nikitavoloboev.xyz/)
  - [Learn-Anything](https://learn-anything.xyz/)


## Potential Design ##

- Frontend
  - Main Page with center content, sidebar on left side, top nav / search bar
  - Sidebar has everything organized by folder / files
  - Like the idea of the on-page graph to navigate by
- Build Process
  - Build service to translate .md files into content
  - Build service to create left side nav
  - Build service to generate graph
  - Appendix generator based on any links that are mentioned on pages
- Backend
  - FE web app
    - Converted .md to html file static content (for center pane)
    - Some way to update or respond to content
  - Downloader
    - click to download as pdf, txt, md, docx, pptx converted at runtime from pandoc, cached, invalidated when necessary
  - Backend Search Service
    - Search content for terms
  - Backend Graph Service
    - Discover relationships between content where mentioned in other documents
      - Don't key on every single word, maybe key terms? discovered by bold or headers?
- Mobile App Component
