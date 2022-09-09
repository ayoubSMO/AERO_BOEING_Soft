import xml.etree.ElementTree as et
import pandas as pd
import numpy as np
import lxml.etree



def xmlToExcel(pathFile, outputName):
    my_tree = et.parse(pathFile)
    my_root = my_tree.getroot()
    doc = lxml.etree.parse(pathFile)
    count = doc.xpath('count(//Table_Row)')
    rows = []
    values = []

    try:
        for i in range(2, int(count + 1)):
            values = []
            # Les attributs du premier élément enfant
            for a in my_root[i]:
                values.append(str(a.text))
            rows.append(values)
            values = []
        
        row =[]
        valu = []

        for i in rows:
            for j in i:
                tmp = j.replace('\n','')
                valu.append(tmp.replace('\t',''))
            row.append(valu)
            valu = []
        
        XML_columns = []
        for a in my_root[1]:
            XML_columns.append(a.text)
            XML_columns = list(map(lambda x:x.strip(),XML_columns))
        
        df = pd.DataFrame(columns = XML_columns)
        for roww in row:
            df = df.append(pd.DataFrame((np.array(roww)).reshape(1,-1), columns=list(df)), ignore_index=True)

        df.to_excel(outputName + ".xlsx")
    except IndexError as e:
        print(e)
        pass