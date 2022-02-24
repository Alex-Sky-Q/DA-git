# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


def convert_list(lst):
  upd_lst = []
  for x in lst:
    if 'M' in x:
      val = int(float(x.strip('M')) * conversion['M'])
    elif 'B' in x:
      val = int(float(x.strip('B')) * conversion['B'])
    else:
      val = 0
    upd_lst.append(val)
  return upd_lst


# test function by updating damages
upd_dam = convert_list(damages)
print(upd_dam)

# 2 
# Create a Table


def create_dict(name, month, year, wind, areas, damage, death):
  dct = {}
  for a, b, c, d, e, f, g in zip(name, month, year, wind, areas, damage, death):
    dct.update({a: {'Name': a, 'Month': b, 'Year': c, 'Max Sustained Wind': d, 'Areas Affected': e, 'Damage': f, 'Deaths': g}})
  return dct
    

# Create and view the hurricanes dictionary
hurr_dict = create_dict(names, months, years, max_sustained_winds, areas_affected, upd_dam, deaths)
print(hurr_dict)

# 3
# Organizing by Year


def hurr_by_year(dct):
  yrd = {}
  for h in dct:
    y = dct.get(h).get('Year')
    val = dct.get(h)
    if y in yrd:
      yrd[y].append(val)
    else:
      yrd.update({y: [val]})
  return yrd


# create a new dictionary of hurricanes with year and key
hurr_year = hurr_by_year(hurr_dict)
print(hurr_year)

# 4
# Counting Damaged Areas


def area_count(dct):
  res = {}
  for n in dct:
    areas = dct.get(n).get('Areas Affected')
    for area in areas:
      if area in res:
        res[area] += 1
      else:
        res.update({area: 1})
  return res


# create dictionary of areas to store the number of hurricanes involved in
dam_areas = area_count(hurr_dict)
print(dam_areas)

# 5 
# Calculating Maximum Hurricane Count


def max_count(dct):
  res_c = max(dct.values())
  res_f = {}
  for k, v in dct.items():
    if v == res_c:
      res_f[k] = v
  print(res_f)


# find most frequently affected area and the number of hurricanes involved in
max_count(dam_areas)

# 6
# Calculating the Deadliest Hurricane


def max_count_dct(dct):
  dth = [v.get('Deaths') for v in dct.values()]
  res_c = max(dth)
  res_f = {}
  for v in dct.values():
    if v.get('Deaths') == res_c:
      res_f[v.get('Name')] = res_c
  return res_f


# find highest mortality hurricane and the number of deaths
print(f'The deadliest hurricane: {max_count_dct(hurr_dict)}')

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# mort_sc_rev = {v:k for k, v in mortality_scale.items()}


def mort_scale(dct):
  mrt = {}
  for h in dct:
    dth = dct.get(h).get('Deaths')
    if dth == mortality_scale[0]:
      ms = list(mortality_scale.keys())[0]
    elif mortality_scale[0] < dth <= mortality_scale[1]:
      ms = list(mortality_scale.keys())[1]
    elif mortality_scale[1] < dth <= mortality_scale[2]:
      ms = list(mortality_scale.keys())[2]
    elif mortality_scale[2] < dth <= mortality_scale[3]:
      ms = list(mortality_scale.keys())[3]
    elif mortality_scale[3] < dth <= mortality_scale[4]:
      ms = list(mortality_scale.keys())[4]
    else:
      ms = list(mortality_scale.keys())[4] + 1  
    val = dct.get(h)
    if ms in mrt:
      mrt[ms].append(val)
    else:
      mrt.update({ms: [val]})
  return mrt


# categorize hurricanes in new dictionary with mortality severity as key
print(mort_scale(hurr_dict))

# 8 Calculating Hurricane Maximum Damage


def max_dam(dct):
  dam = [v.get('Damage') if v.get('Damage') != '-' else 0 for v in dct.values()]
  res_c = max(dam)
  res_f = {}
  for v in dct.values():
    if v.get('Damage') == res_c:
      res_f[v.get('Name')] = res_c
  return res_f


# find highest damage inducing hurricane and its total cost
print(f'The most damage hurricane: {max_dam(hurr_dict)}')

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def dam_scale(dct):
  res = {}
  for h in dct:
    dam = dct.get(h).get('Damage')
    if dam == damage_scale[0]:
      ds = list(damage_scale.keys())[0]
    elif damage_scale[0] < dam <= damage_scale[1]:
      ds = list(damage_scale.keys())[1]
    elif damage_scale[1] < dam <= damage_scale[2]:
      ds = list(damage_scale.keys())[2]
    elif damage_scale[2] < dam <= damage_scale[3]:
      ds = list(damage_scale.keys())[3]
    elif damage_scale[3] < dam <= damage_scale[4]:
      ds = list(damage_scale.keys())[4]
    else:
      ds = list(damage_scale.keys())[4] + 1  
    val = dct.get(h)
    if ds in res:
      res[ds].append(val)
    else:
      res.update({ds: [val]})
  return res


# categorize hurricanes in new dictionary with damage severity as key
print(dam_scale(hurr_dict))
