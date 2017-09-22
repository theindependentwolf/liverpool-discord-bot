###################################################################################################################################################
#
#       File Name       :   download_fixtures.py
#
#       Description     :   Downloads liverpool fixtures in csv and converts it to csv format
#
#
#       Revision History
#       _______________________________________________________________________________________________________________________________________
#
#       No.     Author              Date                Version             Comments
#       _______________________________________________________________________________________________________________________________________
#
#       1       Aniruth Oblah       Sep 02, 2017        1.0                 Initial Version
#
# 
#################################################################################################################################################

import wget
import os
import errno

def remove_old_file(filename):
    """
    Remove file if it already exists
    """
    os.remove(filename) if os.path.exists(filename) else None


def download_fixtures(url):
    """
    Downloads the ics calendar file from the Liverpool website
    """
    liverpool_fixtures = wget.download(url) 
    print("{} downloaded".format(liverpool_fixtures))


def convert_to_csv(filename):
    """
    Convert file to CSV
    """
    fp = open(filename, 'r')
    liverpool_fixtures_string = fp.read()
    liverpool_fixtures_list = liverpool_fixtures_string.split("BEGIN:VEVENT")
    liverpool_fixtures_list.pop(0)
    fp_csv = open('fixtures.csv', 'w')
    fixture_lines = "" 
    for line in liverpool_fixtures_list:
        fields = line.split("\n")
        for field in fields:
            if "DTSTART" in field:
                fixture_lines += field.replace("DTSTART;TZID=Europe/London:","")
                fixture_lines += ","
            if "SUMMARY" in field:
                fixture_lines += field.replace("SUMMARY:","")
        fixture_lines += "\n"
    fp_csv.write(fixture_lines)
    fp_csv.close()
    fp.close() 

def main():
    """
    Calls the various functions for download and conversion to csv
    """
    filename = "fixturelist.ics"
    url = "http://www.liverpoolfc.com/ical/first-team/2017+-+2018/" + filename
    remove_old_file(filename)
    download_fixtures(url)
    convert_to_csv(filename)

        


if __name__ == "__main__":
    main()
