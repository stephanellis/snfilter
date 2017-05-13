# snfilter
Spotter Network Feed filter
snfilter let's you take the gibson ridge feeds from spotternetwork and
filter them down to just the spotters you actually want to see.  This is
particularly helpful for spotter organizations that just want to see their
own spotters during a major severe weather event.

You can see the [spotter network gibson ridge feeds page](http://www.spotternetwork.org/pages/feeds/gibson-ridge)
 for more information.

 When you install this package, you get a command line utility called
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
