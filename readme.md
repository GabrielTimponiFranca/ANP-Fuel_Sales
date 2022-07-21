# Data Engineering Test from Raízen

This project aims to carry out the ETL process, using data provided by the Brazilian fuel regulatory agency, ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustível).

The ETL process involves downloading the file available on the ANP website, and transforming the data, for loading purposes, two final files were generated, one in CSV format and another in PARQUET format.

Airflow was used for the ETL orchestration process.

At the end, a webapp will be opened with the purpose of viewing the data that was processed throughout this process.

## About test

**Acess the [ANP Fuel Sales ETL Test](https://github.com/raizen-analytics/data-engineering-test/blob/master/TEST.md).**

## Solution

Every script is present in the source folder (src).

**Installation**

```
$ pip install -r requirements.txt
```

**Start ETL process**
To start the process don't forget to check if it is inside the source folder.

```
# If it's in the root folder
$ python src/main.py

# In source folder
$ python main.py
```

**First stage**
The first stage consists of downloading the excel file available on the website of the national oil, natural gas and biofuels agency (ANP)

Acess the [ANP](https://www.gov.br/anp/pt-br/).

File used in test [vendas-combustiveis-m3.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3.xls/@@download/file/vendas-combustiveis-m3.xlsx).

The raw file, downloaded by the script, will be available in the "src/data/raw" folder, in its name, containing the date of the extraction day.
If the folder is not created, the script itself will create the folders, to ensure that there are no errors throughout the process.

**Second stage**
After downloading the raw file, start extracting the data present in pivot tables 1 and 3.

**Third stage**
After extracting the data, they will be exported to two files, one CSV and the other PARQUET, so that they can be used as a query base, both saved in the folder "src/data/csv" and "src/data/parquet" respectively.

**Fourth stage**
After the export process, a web screen will be called up to visualize the data, with the possibility of filters and with interactive graphics.

If you already have a database in PARQUET format, present in the folder "src/data/parquet", just run the webapp script to view the database extracted from the ANP spreadsheet

```
# Run webapp
# If it's in the root folder
$ python src/webapp.py

# In source folder
$ python webapp.py

```
