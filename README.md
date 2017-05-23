# snfilter
Spotter Network Gibson Ridge feed filter

snfilter helps you filter the gibson ridge feeds from spotternetwork down to
just the spotters you actually want to see.  This is particularly helpful for
spotter organizations that just want to see their own spotters during a major
severe weather event.

You can see the [spotter network gibson ridge feeds page](http://www.spotternetwork.org/pages/feeds/gibson-ridge)
 for more information.

This package can also convert the output to other formats, such as json and
TruVu Max Navigated CSV.  Please note that if you use the output for
commercial purposes, you must contact the spotter network and get permission to
use the data in your broadcast.

Additional formats can be supported.  If you'd like to see a particular output
format, please create an issue in github and I'd consider hacking it in.

To install, use this:

```
pip install snfilter
```

 After installing this package, you get a command line utility called
 snfilter-cli that allows you to filter those feeds in a scheduled task or
 cron job.  Simply pull the feed like this:

 ```
snfilter-cli pull
 ```

 which will pull the feed file down to the current directory and save it to
 grfeed.txt.  Then use the filter command, like this:

 ```
snfilter-cli filter --nameslist "Daniel Shaw,W5ZFQ:Andrew,Ben Holcomb"
 ```

Which will output the filtered feed to stdout.  Use the --help option for more
information on the available options.

Notice the W5ZFQ:Andrew part in the example nameslist option?  That will
translate the name from the feed to what ever is after the : in the filtered
output.

There is a web interface for this tool, which is available [here](https://github.com/stephanellis/snfilterweb).
 A [live instance](https://snf.vortexok.net) of this webapp is available.
