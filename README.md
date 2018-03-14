# iCERT
iCERT Case Status Check

Automating the scanning for the Prevailing wage detirmination status from iCERT website

I started the original code http://www.trackitt.com/usa-discussion-forums/atlanta-perm/664488317/prevailing-wage-processing-time/page/185 #4617

Another member enhanced the script by using the cookies from the browser inside the script

http://www.trackitt.com/usa-discussion-forums/atlanta-perm/664488317/prevailing-wage-processing-time/page/186 #4628

my current version http://www.trackitt.com/usa-discussion-forums/atlanta-perm/664488317/prevailing-wage-processing-time/page/192 #4784

steps to get the cookies from chrome
------------------------------------
- open https://icert.doleta.gov/ in chrome 
- under iCERT CASE STATUS CHECK pass the reCAPTCHA 
- from Chrome menu select More tools -> Developer tools then select Network tap 
- back to iCERT STATUS CHECK write any case number and click the check status button 
- in the right hand side under Name select index.cfm?event=ehRegister.... 
- under Headers tab find request header and find the Cookies value, copy the entire value and use it in the script
