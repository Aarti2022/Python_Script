#!/bin/bash

# List of URLs 
declare -a urls=("https://fasb.org/" "https://fasb.org/about-us" "https://fasb.org/about-us/standard-setting-process" "https://fasb.org/about-us/post-implementation-review-process" "https://fasb.org/about-us/board-members" "https://fasb.org/standards/accounting-standard-updates" "https://fasb.org/standards/accounting-standard-updated-effective-date" "https://fasb.org/projects/current-projects" "https://fasb.org/projects/recently-completed-projects")

# Loop through URLs
for url in "${urls[@]}"
do
   echo "Generating report for $url"
   # Run Lighthouse and generate HTML report
   Lighthouse "$url" --output html --documents/generatedreport"$(echo $url | sed 's/https\?:\/\///').html"
done

echo "Reports generated successfully!"
