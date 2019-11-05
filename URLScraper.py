# URLScraper - scrapes a desired URL of all links and writes them to a new file
# will overwrite the same file if a new name is not given
# Uses BeautifulSoup's Library for scraping pages

def ScrapeNet( filename, urls ) :
    
    from bs4 import BeautifulSoup
    import requests
    
    try :
        filehandle = open(filename,"w")
    except IOError :
        print( "*** URLScraper : Cannot open the file %s" % ( filename ) )
        return
    
    for url in urls :
        
        num_line = 0
        r  = requests.get( "http://" + url )
        data = r.text
        soup = BeautifulSoup( data , features="html5lib")    
        filehandle.write( "%s" % ( "-" * 50 )+"\n" )
        filehandle.write( "All Link Scrapes for '%s'\n" % ( url ) + "-" * 50 + "\n\n" )
        
        for link in soup.find_all( 'a' ):
            num_line += 1
            print( num_line,link.get( 'href' ) )
            filehandle.write( "%3i - %s" % ( num_line, link.get( 'href' )) + '\n' )

ScrapeNet( "links.txt", [ "www.linkedin.com" ] )
