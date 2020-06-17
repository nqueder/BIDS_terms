import os,sys
from argparse import ArgumentParser
import pandas as pd
from pyld import jsonld
from os.path import join
import json
import shutil
import tempfile
import urllib.request as ur
from urllib.parse import urlparse
import numpy as np

from add_term import add_term
from table_utils import generate_pdf


def load_available_properties(terms_dict):
    '''
    Takes union of all properties available for current BIDS terms
    :return: list of available properites
    '''

    property_list = []

    # go through each BIDS terms label and get properties
    for label,property_dict in terms_dict.items():
        # then loop through properties and add property if not already added
        for property, value in property_dict.items():
            if property not in property_list:
                # if property isn't in our list add it
                property_list.append(property)

    return property_list


def main(agrv):

    parser = ArgumentParser(description='This tool will allow the user to search across existing BIDS terms allowing for '
                                        'creation of PDF table for the BIDS specification documents. The tool will also'
                                        'allow the user to add new BIDS terms, which will result in JSON-LD files added to '
                                        '"bids_terms_to_pdf_table" Github repository')

    parser.add_argument('-in', dest='in_dir', required=True, help='Path to cloned "bids_terms_to_pdf_table" Github repository')
    parser.add_argument('-out', dest= 'out_dir', required=False, help='Path to output directory: only required if you would like'
                                                                      ' to export a PDF table of BIDS specification terms')

    args = parser.parse_args()

    #Present the user with instructions
    print('instruction... (TO BE ADDED)')

    #Set paths to input and output directory
    path_to_jld = os.path.join(args.in_dir,'BIDS_Terms')
    path_to_out = args.out_dir

    #List all existing BIDS terms JSON-LD files
    bids_terms_ = os.listdir(path_to_jld)

    # all currently available BIDS terms
    bids_terms = []
    # terms selected for pdf table
    selected_terms = []
    # list of term properties selected for inclusion in PDF table
    selected_properties = []
    # term properties available
    available_properties = []
    # dict of all terms
    terms_dict = {}


    #Loop through the terms in bids_terms_ takeout the ".jsonld" extention
    for t in bids_terms_:
        path_to_term = os.path.join(path_to_jld, t)
        with open (path_to_term) as p:
            term_dict = json.load(p)

        terms_dict[t] = term_dict


    while True:
        # print options for the user to select from
        print('1. Select a term')
        print('2. Search terms')
        print('3. Add new term')
        print("4. Create PDF table of selected terms (%s)" % selected_terms)
        print("5. Exit")

        #Allow the user to input a number that correspond to their choice
        num = int(input('Please choose from the following options:'))

        if (num < 1) or (num > 5):
            print("Please select a valid option (1-4)")
            continue

        #if num == 1:

        #if num == 2:

        # adding a new BIDS term
        if num == 3:
            # create new BIDS term and save to new dictionary
            new_term = add_term(bids_terms)

            # add new_term dictionary to existing bids_terms dictionary

            # git fork of main BIDS terms repo into user's github space

            # write new term to JSON-LD file to user's forked github space

                # do a git commit

                # do a git push

            # issue a pull request to main BIDS terms repo



        # adding properties for table creation
        if num == 4:
            num_selectors = 1
            property_list = load_available_properties(bids_terms)
            while True:
                print("Please select which properties to include in the the PDF table:")

                for property in property_list:
                    print("%d. %s" %(num_selectors, property))
                    num_selectors = num_selectors + 1

                print("%d. Done" % num_selectors)
                #Allow the user to input a number that correspond to their choice
                property = int(input('Please choose from the following options:'))

                if (property<1) or (property > (len(property_list))):
                    continue
                # if they selected the "Done" selection then exit this loop
                elif property == num_selectors:
                    break
                # if they selected a property add it to the selected properties list for PDF table
                else:
                    selected_properties.append(property_list[property])


            # create PDF table and exist loop
            # generate_pdf(term_dictionary,selected_properties,file_name)

            # break

        # if the user wants to exit without creating a PDF table
        if num == 5:
            exit(0)
    #Once the user is done then he/she will be allowed
    #pdf = input('Would you like to generate a PDF table of the selected/added terms? [yes/no]:')


    #if pdf == 'no':
        #continue
    #if pdf == 'yes':


if __name__ == "__main__":
   main(sys.argv[1:])
