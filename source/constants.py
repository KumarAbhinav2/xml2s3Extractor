XML_URL = 'https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100'


class XMLConstants:
    URL_TAG = './result/doc/str'
    URL_ATTRIBUTE = 'download_link'
    nmap = {'header': 'urn:iso:std:iso:20022:tech:xsd:head.003.001.01',
            'auth': 'urn:iso:std:iso:20022:tech:xsd:auth.036.001.02'}
    record_tag = 'header:Pyld/auth:Document/auth:FinInstrmRptgRefDataDltaRpt/auth:FinInstrm/auth:TermntdRcrd'
    child1 = 'auth:FinInstrmGnlAttrbts'
    child2 = 'auth:Issr'
    skip_child = 'ShrtNm'


class CSVConstants:
    cols = ['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp',
            'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr']

    output_file = 'source/outputs/output_csv.csv'


class AWSConstants:
    bucket = 's3-simple-exp'