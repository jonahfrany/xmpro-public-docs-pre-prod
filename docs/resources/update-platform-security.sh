#!/bin/bash

# Get the current date in the format "DD Mon YY"
current_date=$(date +'%d %b %y')
echo "DS_SAST score is: "$DS_SAST
echo "DS_DAST score is: "$DS_DAST

# Define the updated table content
updated_table="<table><thead><tr><th width=\"242\">Product</th><th data-type=\"number\">SAST Score</th><th>DAST Score</th><th>Date</th><th data-hidden></th></tr></thead><tbody><tr><td>Subscription Manager</td><td>91</td><td>96</td><td>11 Dec 23</td><td></td></tr><tr><td>App Designer</td><td>81</td><td>96</td><td>11 Dec 23</td><td></td></tr><tr><td>Data Stream Designer</td><td>$DS_SAST</td><td>$DS_DAST</td><td>$current_date</td><td></td></tr><tr><td>XMPro AI</td><td>98</td><td>Not Available</td><td>11 Dec 23</td><td></td></tr></tbody></table>"

# Replace the existing table content in readme.md
sed -i 's|<table>.*<\/table>|'"$updated_table"'|' platform-security.md

# Optional: Display a success message
echo "platform-security.md updated successfully!"
