# Donwload and visualize ISIC

## Introduction

Little tool to select data from ISIC and visualize and download.

## Getting Started

Required packages:
- Pandas
- Tqdm
- Seaborn

Download isic-cli package at: [Link to executable](https://github.com/ImageMarkup/isic-cli/releases/tag/v9.1.0)

If no metadata.csv is downloaded, download it in the directory of the isic executable with

    isic.exe metadata download -o output_file

## Usage

The first part of the script is for loading of metadata and visualization, the rest downloads the images.