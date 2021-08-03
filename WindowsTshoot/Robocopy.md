# Robocopy #

## Generic ##

`robocopy <source> <destination> /E /Z /DCOPY:T /COPYALL /R:3 /W:1 /XO  /V /MT:32 /LOG:<file>`

## Details about arguments ##

* source :: Source Directory (drive:\path or \\server\share\path).
* destination :: Destination Dir  (drive:\path or \\server\share\path).
* /E :: copy subdirectories, including Empty ones.
* /ZB :: use restartable mode; if access denied use Backup mode.
* /DCOPY:T :: COPY Directory Timestamps.
* /COPYALL :: COPY ALL file info (equivalent to /COPY:DATSOU).  Copies the Data, Attributes, Timestamps, Ownser, Permissions and Auditing info
* /R:n :: number of Retries on failed copies: default is 1 million but I set this to only retry once.
* /W:n :: Wait time between retries: default is 30 seconds but I set this to 1 second.
* /V :: produce Verbose output, showing skipped files.
* /TEE :: output to console window, as well as the log file.
* /LOG:file :: output status to LOG file (overwrite existing log).
* /XO :: Skip files where destination is same size and date or newer
* /MT:n :: Multithreaded