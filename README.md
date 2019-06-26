# SDL_mya-MM_code
Solution to standarize the language code for mya-MM among SDL platforms (SDL Trados Studio and WorldServer).

GENERAL

The language code for Burmese in SDL Trados Studio 2017/2019 and SDL WorldServer are not synchronized.
This affects round-tripping FTS content between SDL Trados Studio and WorldServer.
For example, users trying to load a Burmese WSXZ package exported from WorldServer will receive the following error message:
"Invalid language code is detected: mya-MM"

DESCRIPTION

Burma.py processes WSXZ packages exported from WorldServer so these can be imported into SDL Trados Studio.

INSTRUCTIONS

1- Download the Burmese WSXZ file from WorldServer. This will have a file name similar to "tasks_xxx_mya_MM_xliff.wsxz".

2- Execute Burma.py in the same directory.

NOTE: Burma.py will not work with xliff_projects.zip files. Make sure the file extension is WSXZ.
