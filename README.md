# iCERT
iCERT Case Status Check

steps to get the cookies from chrome
------------------------------------
- open https://icert.doleta.gov/ in chrome 
- under iCERT CASE STATUS CHECK pass the reCAPTCHA 
- from Chrome menu select More tools -> Developer tools then select Network tap 
- back to iCERT STATUS CHECK write any case number and click the check status button 
- in the right hand side under Name select index.cfm?event=ehRegister.... 
- under Headers tab find request header and find the Cookies value, copy the entire value and use it in the script
