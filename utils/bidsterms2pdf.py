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

    #Create a new list to save
    bids_terms = []

    #Loop through the terms in bids_terms_ takeout the ".jsonld" extention
    for t in bids_terms_:
        t = t[:-7]
        bids_terms.append(t)


    # print options for the user to select from
    print('1. Select a term')
    print('2. Search terms')
    print('3. Add new term')

    #Allow the user to input a number that correspond to their choice
    num = int(input('Please choose from the following options:'))


    #if num == '1':

    #if num == '2':

    #if num == '3':


    #Once the user is done then he/she will be allowed
    pdf = input('Would you like to generate a PDF table of the selected/added terms? [yes/no]:')


    #if pdf == 'no':
        #continue
    #if pdf == 'yes':


if __name__ == "__main__":
   main(sys.argv[1:])
