# As input data you have list of strings with information about some location:
#
# "id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"
#
# As output tuple of strings name and population

import re


def max_population(list_info):
    st = ''.join(list_info)
    items = re.findall(r'(\w+_\w+),(\d+)', st)
    max_pop = int(items[0][1])
    index = 0
    for i in items:
        if int(i[1]) > max_pop:
            max_pop = int(i[1])
            index = items.index(i)
    return items[index]
