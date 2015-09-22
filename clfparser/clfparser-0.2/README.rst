=================================
Apache Common/Combined Log Parser
=================================

Parses a single Apache web log format record. The parser wil first attempt to match a *combined* format record, if this fails it will attempt to match a *common* format record. In the event that the record matches neither pattern, a null record will be returned.

To return a dictionary representing the entire record or a list of specified objects call *CLFParser.logDict(record)*, passing a single log record::

    >>> from clfparser import CLFParser
    >>> logRecord='10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209'
    >>> clfDict=CLFParser.logDict(logRecord)
    >>> print clfDict
    {'b': '209', 'h': '10.223.157.186', 'time': datetime.datetime(2009, 7, 15, 14, 58, 59), 'l': '-', 'Referer': '', 
        's': '404', 'r': '"GET /favicon.ico HTTP/1.1"', 'u': '-', 't': '[15/Jul/2009:14:58:59 -0700]', 'timezone': '-0700', 'Useragent': ''}

Note that the returned dictionary keys lack the leading %, this will hopefully be amended in a later release.

To return a subset of the log record as a list, call *CLFParser.logParts(record, formatMask)*. where *formatMask* is a quoted string listing the log items required in the output::

    >>> clfParts=CLFParser.logParts(test,'%h %time')
    >>> print clfParts
    ['10.223.157.186', datetime.datetime(2009, 7, 15, 14, 58, 59)]

Common Log Format
-----------------

Described by::

    '%h %l %u %t "%r" %>s %b'

Where:

- *%h* - host
- *%l* - identity
- *%u* - userid
- *%t* - time
- *%r* - request
- *%>s* - status
- *%b* - size

Combined Log Format
-------------------

As Common Log Format with the addition of 2 further fields::

    '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-agent}i"'

Where:

- *%{Referer}i* - HTTP request header referer
- *%{User-agent}i* - HTTP request header user agent

Additional Fields
-----------------

In addition to the standard log fields, clfparser also parses the log time field, *%t*, to create a Python datetime object *%time* and a string object representing the timezone, *%timezone*.

Installation
------------

Install using **pip**::

    pip install clfparser

To Do
-----

- Amend dictionary key names to reflect the Apache specification (add leading %).
- Performance improvements
- Command line tools
- Identify request resource as an additional data item


