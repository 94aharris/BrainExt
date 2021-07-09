# Pandoc #

Overview of how I install and use Pandoc for Markdown -> whatever conversion.

## Resources ##

- [Pandoc Docs](1)
- [Install Tex](2)

## Usage ##

- Convert from markdown to format
  - `pandoc <file>.md -f markdown -t <destformat> -o <outputfilename><.extension>`

- PDF Specific Conversion
  - To convert to pdf, you'll need to install [tex](2) (Loooong time)
  - `pandoc .\PythonBasics.md -f markdown -t pdf -o ..\pandoc_output\Python.pdf --pdf-engine C:\texlive\2021\bin\win32\pdflatex.exe`

## Website Idea ##

- Markdown files / images are the backing
- When a commit occurs, files are pushed through pandoc to create static html files
- Updated files are pushed to a hosting app server
- Each page has a 'download as - docx, pdf, pptx, etc.' link at the bottom
- When a download is requested the backing .md is pushed through pandoc, the file returned, and the output placed in cache
- When updates occur to the backing .md, cached download versions are invalidated
- Some sort of search index for the output

## Link References ##

[1]: https://pandoc.org/MANUAL.html "Pandoc Documentation"
[2]: http://www.tug.org/texlive/acquire-netinstall.html "Install Tex"