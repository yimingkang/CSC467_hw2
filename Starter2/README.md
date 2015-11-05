CSC467 lab2
===========

Yiming Kang 998676730  

**Please see my github repo for the commit history <git@@github.com:yimingkang/CSC467_hw2.git>**  

Approach:
---------
The first step we took was to code in the gramma rules without any modification or output and see what happens. Bugs were discovered and fixed and tests were added.  

1- Type in the gramma, then `make`  
2- Got shift/reduce and reduce/reduce conflict, fixed the conflicts  
3- Added yTRACE() call when each rule is reduced, this is done via a script (gen\_yTRACE.py)  
4- Improved testing framework (baesd on the one we built for lab1)  

Challenges:
-----------
These are the challenges we found noteworthy (among others):  

1- Dangling else shift/reduce conflict. We decided to give statements with 'else' a higher priority (shift rather than reduce) which is Bison's default  
2- Figuring out `%prec SYMBOL` assigns the given rule the priority or SYMBOL - this is necessary to resolve some of the shift/reduce conflicts  
3- Systematic testing: Since we're implementing parser.y, we cannot actually judge whether an **output** is correct. We can only feed it with files known to be syntactically correct and expect it to pass, and files known to be syntactically invalid to fail.  

Testing:
--------
As mentioned above, we have no good way of knowing if the actual y.output is correct because we defined it. We were however, able to come up with a more elaborate testing framework than simply checking whether a file passes or failes.  

**Test location**: All tests are located in `./tests`. Tests for lab #x are located in `./tests/labx_test`  
**Running tests**: Run `make && make test`. This will first invoke `python gen_yTRACE.py parser.y.bak > parser.y` to generate the actual rules, then compile and run tests  

1- Building upon the testing framework of lab1, we compared the output of compiling sample files periodically (with each commit). Any changes to the ouput can be quickly detected  
2- As mentioned in challenges, we tested whether files known to be correct actually passes and files known to be incorrect actually fails.  
