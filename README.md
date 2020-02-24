# Wordcrack
Infosec exercise

On my InfoSec course we acquired some password hashes and usernames through an exercise. 
As a bonus exercise that round we were tasked with finding out 10 of the passwords. I 
started off by writing a short python script to test different words from a list to see 
if those were a password. I then modified the script so it would be easy to add tests to it, 
such as adding symbols or numbers, replacing vowels etc. It quickly got quite slow, so I 
added a progress bar with an estimate of the time remaining as well.

I thought this was a really fun exercise, and it was fun to write the script myself, trying 
to make it modular so I could add to it a little bit at a time. Unfortunately, in the end, I 
had to resort to using John the Ripper instead for the last 3 passwords, as it was much faster 
and had built in functions to add combinations of numbers, letters and symbols.
