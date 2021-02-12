# Note friendly PDF

I want to print PDFs with enough blank space to write lots of notes. Margins are usually big enough! This tool can
- take a PDF file on your computer,
- insert a blank page in every other page, then
- write out the expanded document as a new PDf.
Now you can print the results out and have plenty of space to write notes.

Here is an example of an incredibly interesting math paper I downloaded from the arXiv. If I print it out -- double sided, with 2 sheets per page, I'll get this:
![Before](static/before.png)

The content of the paper appears dubious, so I'll want plenty of space to jot down my suspicions. I run the command...
```
python main.py ~/Downloads/2005.11428.pdf
```
which will create a new file, `~/Downloads/2005.11428_notes.pdf`. This new file has lots of space for me to write:
![After](static/after.png)


## Basic usage

After downloading the code, install the requirements within a virtual env:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now you are ready to use the tool. A help menu will guide you:
```
python main.py --help
```
