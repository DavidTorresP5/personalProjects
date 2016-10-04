# pip install savReaderWriter

import pandas as pd
import savReaderWriter as spss

url = 'url/file.sav'
raw_data = spss.SavReader(url, returnHeader=True, rawMode=False)
 
df = pd.DataFrame(list(raw_data)) 
