from collections import OrderedDict

fav_ling = OrderedDict()
fav_ling ['jen'] = 'python'
fav_ling ['Sarah'] = 'C'
fav_ling ['Edward'] = 'Ruby'
fav_ling ['Phill'] = 'python'

for name, language in fav_ling.items():
    print(name.title() + 'sua linguagem favorita é ' + language.title() + '!')

print(fav_ling)