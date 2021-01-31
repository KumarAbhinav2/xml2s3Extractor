# xml2s3Extractor

1. Downloads the xml from given link

2. From the xml, parses through to the first download link whose file_type is DLTINS and download the zip

3. Extract the xml from the zip.

4. Convert the contents of the xml into a CSV with the following header:

    . *FinInstrmGnlAttrbts.Id*

    . *FinInstrmGnlAttrbts.FullNm*

    . *FinInstrmGnlAttrbts.ClssfctnTp*

    . *FinInstrmGnlAttrbts.CmmdtyDerivInd*

    . *FinInstrmGnlAttrbts.NtnlCcy*

    . *Issr*

5. Store the csv from step 4) in an AWS S3 bucket


# Directions:

Python version: 3.8

Script to initiate: python driver.py


# TODO:


  1: Models are of no use currently, but we can extend further, Record each path and its status, so that we can provide retry in case of failue.
  
  2: We can introduce a message queue for concurrent users scenario
  
  3: Currently , csv file is getting stored in disk which is not efficient , we can introduce streaming here.
  
  4: We can make our s3 upload function async , to improve the efficiency.
  
  5: Ideally i should be clearing the file created but purging is not added in this version.
  
  5: We can have a local db as well to store current status of the files.
