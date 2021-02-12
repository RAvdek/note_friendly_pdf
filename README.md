# Note friendly PDF

["...I have discovered a truly marvelous proof of this, which this margin is too narrow to contain."](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem)

I want to print PDFs with enough blank space to write lots of notes. Margins are usually too tiny to write out a complete thought! This tool can

- take a PDF file on your computer,
- insert a blank page in every other page, then
- write out the expanded document as a new PDF.

Now you can print the results out and have plenty of space to write notes.

Here is an example of an incredibly interesting math paper I downloaded from the arXiv. If I print it out -- double sided with 2 sheets per page -- I'll get the following print preview:
![Before](static/before.png)

The content of the paper appears dubious, so I'll want plenty of space to jot down my suspicions. The margins don't provide me enough space.
I run the following command to make an edited file with lots of blank space...
```
python main.py ~/Downloads/2005.11428.pdf
```
which will create a new file, `~/Downloads/2005.11428_notes.pdf` which looks like this:
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
