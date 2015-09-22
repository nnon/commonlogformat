Apache Common/Combined Log Parser
---------------------------------

Parses Apache common/combined web log format records. 

Returns either a dictionary representing the entire record or a list of specified objects. 

To use::

    from clfparser import CLFParser

    test='10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209'
    
    #return dictionary
    clfDict=CLFParser.logDict(test)

    #return list containing host, log time and a datetime object representing the log time
    clfList=CLFParser.logParts(test, '%h %t %time')

Common Log Format
-----------------

Described by::

    "%h %l %u %t \"%r\" %>s %b"

Where:

%h - host
%l - identity
%u - userid
%t - time
%r - request
%>s - status
%b - size

Combined Log Format
-------------------

As Common Log Format with the addition of 2 further fields::

    "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""

Where:

%{Referer}i - HTTP request header referer
%{User-agent}i - HTTP request header user agent

Additional Fields
-----------------

In addition to the standard log fields, clfparser also parses the log time field, *%t*, to create a Python datetime object *%time* and a string object representing the timezone, *timezone*.
