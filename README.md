# Bandwidth Evaluator


This program measure the system bandwidth by downloading a
dummy package from a test server (completely safe) and measuring the download
time. When you launch the program, it will calibrate itself by identifying the
best download server (normally the fastest) and it will use this server until
the program stop. Each hour, the program will take five sample and will
calculate the average download speed (this result will appear in the output
file).

The upload measurement is not used in the program (the
program can do it, but it has been deactivated, because it’s not very useful for
bandwidth speed evaluation, also the speedtest-cli library is not very good for upload speed
measurement)

If the program stop (power loss, for example) you can just
relaunch it, the program will create a new output file (without deleting the
previous one).

This program use the speedtest-cli library to evaluate the bandwidth (reference : https://github.com/sivel/speedtest-cli )

You can use the source code or the windows stand-alone executable


 
