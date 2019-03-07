# coding=utf-8
import argparse
import PyPDF2 as pdflib
from PyPDF2 import PdfFileWriter, PdfFileReader

import os
import sys
import logging


import configparser
import csv

# from config import config

logging.getLogger().setLevel(logging.INFO)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output folder", action="store",
                        default='./output/', type=str, dest="output")

    parser.add_argument("-t", "--template", help="",
                        action="store", default='template.tex', dest="template")
    parser.add_argument("-c", help="config file", action="store",
                        default='config.csv', type=str, dest="config")
    parser.add_argument(nargs=argparse.REMAINDER, dest="file")
    return parser


def load_template(path):
    template = ''
    with open(path) as fd:
        template = fd.read()
    print(template)
    return template


def load_config(path):
    config = []
    with open(path, 'r',encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='\'')
        for row in data:
            if row[0] =='':
                config.append(None)
            else:
                config.append(row)
    print(config)
    return config

    # config = configparser.ConfigParser()
    # config.read(path, encoding='utf-8')
    # figures = config['figure']
    # print(figures)
    # for key, value in figures.items():
    #     if value.lower == 'none':
    #         figures[key] = None
    # return figures

    # config = []
    # with open(path) as fd:
    #     for line in fd:
    #         line = line.strip()
    #         if line.startswith('#'):
    #             continue
    #         if line.lower() =='none':
    #             config.append(None)
    #         else:
    #             config.append(line)
    # print(config)
    # return config


def split(path, template, config, output='output/'):
    """
    split pdf file, and output multiple new pdf files.
    """
    # if inpath==outpath:
    #     raise Exception('input and output can not be the same!')

    if os.path.exists(output):
        if not os.path.isdir(output):
            raise Exception('must be a folder path')
    else:
        os.makedirs(output)

    pages = []
    with open(path, 'rb') as pdf:
        reader = PdfFileReader(pdf)

        for i, item in zip(range(reader.getNumPages()), config):
            if item is None:
                continue

            (name, caption) = item
            path = '{}/{}.pdf'.format(output, name)

            print(template % (path, name, caption))
            print('-'*10)

            writer = PdfFileWriter()
            page = reader.getPage(i)

            writer.addPage(page)
            with open('{}'.format(path), 'wb') as figure:
                writer.write(figure)


def main():
    sys.argv.append('testcase.pdf')

    parser = get_parser()
    args = parser.parse_args()
    print(args)

    input = args.file[0]
    template = args.template
    config = args.config
    output = args.output

    config = load_config(config)
    template = load_template(template)

    split(input, template, config)


if __name__ == "__main__":
    main()