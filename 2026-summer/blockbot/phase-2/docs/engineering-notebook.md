# Phase 2 Engineering Notebook

## Date
**Date:** 2026-06-24
**Phase:** 2 — First Web Server

---

## What I built
A web server that has 3 pages, including: /, /telemetry, and /extra.
"/" displays HTML including fake telemetry data from app.py and a 
connection state indicator.


---

## How it works
A web server is like a helicopter trying to enter a giant building with thousands of landing pads, or ports. 
A Raspberry Pi is the building. Like in an airport, there needs to be someone to accept a plane landing, 
if there is no one there, the plane gets turned away. SSH works because there is a "person" standing at pad 22, 
I set it up in the Raspberry Pi Imager when I flashed the OS. The browser got rejected because there was no one 
waiting behind the web port to accept it. So, I use 0.0.0.0, which means "talk to anyone on the network."

---

## Problems I hit and how I fixed them

### Failure 1:
**Expected:** Web Server to Connect
**What happened:** Server refused to connect through the web.
**Cause:** I did not have a script yet to look for the web to connect.
**Fix:** Creating app.py
**Lesson:** For every port a programmer wants to use, you need a program waiting for something to connect to the port.

---

### Failure 2: 
**Expected:** A Web Server to Open
**What happened:** An error saying app.py does not exist.
**Cause:** I forgot to save it.😄
**Fix:** Pressed ctrl+s when I am on the file.
**Lesson:** Don't forget to save your files!

---

### Failure 3:
**Expected:** JSON Telemetry Test to Have Correct Syntax
**What happened:** "false" caused a syntax error in the VS Code editor.
**Cause:** "false" was not capitalized, and therefore, Python did not recognise it as boolean.
**Fix:** Changing from "false" to "False"
**Lesson:** Always check syntax for inconspicuous errors. "false" and "False" are naturally the same for a person, but completely different things for Python.

---

### Failure 4:
**Expected:** Repository to be Updated when I Ran Bash Terminal Commands to Make a New Commit to This Repository
**What happened:** Through terminal, Github told me that it found changes that were not on my Pi yet, and as a cherry on top, changes on my Pi that were not on Github
**Cause:** Made changes through browser, and then changes on VS Code terminal while the VS Code was SSH-ed to my Pi.
**Fix:** Merging them by using bash command "git config pull.rebase false"
**Lesson:** When you make changes on one place, and changes on another place and forget to sync it, remember to sync it!

---

### Failure 5:
**Expected:** Function "get_home()" to have Correct Syntax
**What happened:** Python was very, very confused.
**Cause:** The "with open()" was inside of the parameters' parentheses!
**Fix:** Moving "with open()" from the parameters' parentheses to the body of "get_home()."
**Lesson:** Don't put code where the parameters are supposed to go.

---

### Failure 6:
**Expected:** Index.html to Show Disconnected when I Stopped Uvicorn from Updating
**What happened:** Kept loading forever.
**Cause:** No timeout for the javascript's searching for app.py
**Fix:** Adding AbortController to javascript
**Lesson:** If you don't include a timeout, it will keep searching forever until it finds what it is looking for.

---

## One thing that confused me at first but makes sense now
How to use the AbortController in the javascript section of index.html

---

## One thing I'm still fuzzy on
I don't know.

---

## Current Checklist:

 - [x] Fake telemetry endpoint working at /telemetry
 - [x] Home route working at /
 - [x] Code committed and pushed to GitHub
 - [x] The HTML dashboard page at / that displays and updates telemetry
 - [x] Connection state indicator
 - [ ] Real Phase 1 Pico data replacing fake data

---