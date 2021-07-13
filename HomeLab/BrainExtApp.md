# BrainExt Application #

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
