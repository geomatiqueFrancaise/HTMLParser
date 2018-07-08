"# HTMLParser" 

1) Requirement for running HTMLParser Script :

      Install pip if you have not did it yet :

      1 - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

      2 - python get-pip.py

Those libraries must be installed on your machine :
    
    a) BeautifulSoup4 :
        pip install beautifulsoup4
    b) lxml:
        pip install lxml

2) How to run this Script :

    Once you are in the correct directory :

    Run this command:

    a) python HTML2RSS.py -uf arg1 -t arg2 -att arg3 -v arg4
        
        where :
        

        -uf URLFILE, --urlfile URLFILE : 

                        This is a simple text file that contains http url one
                        by one . If you want to comment you url file, you can
                        do this by adding a "#" at the begining of the line.
                        The script will simply ignore this line.


        -t TAG, --tag TAG : This is the target tag in DOM HTML

        -att ATTRNAME, --AttrName ATTRNAME : This is the target attribute of the above tag

        -v VALUENAME, --ValueName VALUENAME : This is the attribute value of the tag

3) Exceptions:

There is two main exceptions : 

    a) if your url file cannot be open for any raisons (for exe;ple if it does not exist), the command line will print :

            "!!! --------Cannot Open the specified file -----!!!!"

    b) if the url is incorrect or if you do not have access to this url for any raisons, the command line will print :

            "!!!!!  cannot open the url {url}   !!!"
            where url wil show which url the script cannot open
    




       
