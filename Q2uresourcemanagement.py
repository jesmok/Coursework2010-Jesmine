5# Filename: uresourcemanagement.py
# Author: Jesmine Mok 6c11
# Description: read from RESOURCE.DAT and update to this file

from classes import *

def UPDATERESOURCE():

    try:

        # open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        # open updated resource file for writing ("a" = append, both read and write)
        uresource_file = open("URESOURCE.DAT", "w")
        
        # read heading line from resource file (creation date, number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        # store creation date and number of records
        creation_date = heading_line[0:10]
        num_recs = heading_line[10:]

        # write CreationDate and NoOfRecords to updated resource file
        uresource_file.write(creation_date + num_recs + "\n" )
        
        # read remaining records details
        detail_lines = resource_file.readlines()

        # initialize resource list
        resource_list = []
        
        # loop for number of records
        for record_lines in detail_lines:
            # new record line
            record_lines = record_lines.rstrip("\n")

            # store resource number, title, date acquired, resource type
            resource_no = record_lines[0:5]
            title = record_lines[5:35]
            date_acquired = record_lines[35:41]
            resource_type = record_lines[41:]            
            
            # print resource info
            print("Resource no: " + resource_no)
            print("Title: " + title)
            print("Date Acquired: " + date_acquired)
            print("Resource Type: " + resource_type)
            
            
            # if resource type is MusicCD
            if resource_type == "C":
                # get and validate Artist
                valid_Artist = False
                while not valid_Artist:
                    Artist = input("Please enter Artist: ")
                    if len(Artist) == 0: # presence check
                        print("Please enter something.")
                    elif not len(Artist) <=50: # length check
                        print("Maximum length is 50 characters. Try Again.")
                    else:
                        valid_Artist = True
                
                # get and validate NoOfTracks
                valid_NoOfTracks = False
                while not valid_NoOfTracks:
                    NoOfTracks = input("Please enter number of tracks: ")
                    if len(NoOfTracks) == 0: # presence check
                        print("Please enter something.")
                    elif not NoOfTracks.isdigit(): # datatype check
                        print("No negative numbers or characters allowed. Try again.")
                    elif not (0 < (int(NoOfTracks)) < 21): # range check
                        print("Check your number of tracks again.")
                    else:
                        valid_NoOfTracks = True

                # create new MusicCD object and add to resource list
                resource_list.append(MusicCd(resource_no, title, date_acquired, resource_type, Artist, NoOfTracks))
                 
            # else resource type is FilmDVD
            else:
                # get and validate Director
                valid_Director = False
                while not valid_Director:
                    Director = input("Please enter Director: ")
                    if len(Director) == 0: # presence check
                        print("Please enter something.")
                    elif not len(Director) <=50: #length check
                        print("Maximum length is 50 characters. Try Again.")
                    else:
                        valid_Director = True
                        
                # get and validate Running Time
                valid_RunningTime = False
                while not valid_RunningTime:
                    RunningTime = input("Please enter Running Time: ")
                    if len(RunningTime) == 0: #presence check
                        print("Please enter something.")
                    elif not RunningTime.isdigit(): #datatype check
                        print("No negative numbers or characters allowed. Try Again.")
                    elif not (0 < (int(RunningTime)) < 300): # range check
                        print("Check you Running Time again.")
                    else:
                        valid_RunningTime = True

                # create new FilmDvd object and add to resource list
                resource_list.append(FilmDvd(resource_no, title, date_acquired, resource_type, Director, RunningTime))

            print(resource_list)

        # write resource info and extra details to updated resource file
        for resource in resource_list:
            uresource_file.write(resource.display() + "\n")
                
                                             
        # close file
        resource_file.close()
        uresource_file.close()

    except IOError:

        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")


# main program
if __name__ == "__main__":
    UPDATERESOURCE()

