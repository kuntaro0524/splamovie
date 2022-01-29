#!/bin/bash
mkv_files=`find ~/Movies/ -name '*mkv'`

for mkv_file in $mkv_files
do
/Users/kuntaro/kundev/splamovie/extract_deaths_movie.py $mkv_file
done
