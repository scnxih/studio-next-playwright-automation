"""
Store zh-CN input data for build-in steps
"""


class INPUTDATAZH:
    AUTOLIB = "libname AUTOLIB '/segatest/I18N/Autolib';"

    SCATTER_MAP = """
data city_loc (label="内华达'Cities"
               keep="county'县"n "city'城市1"n "city'城市2"n "lat'纬度"n "long'经度"n "countyname'县名"n);
format "county'县"n 4. "city'城市1"n $20. "city'城市2"n $20. "lat'纬度"n 20.3 "long'经度"n 20.3 "countyname'县名"n $20.;
"county'县"n = county;
"city'城市1"n = city;
"city'城市2"n = city2;
"lat'纬度"n = lat;
"long'经度"n = long;
"countyname'县名"n = county_name;
set mapsgfk.uscity_all(where=(state=32));
run;
proc sql;
    create table "city_loc'中"n as
    select * from work.city_loc
    where "county'县"n is not missing;
run;
proc sort data="city_loc'中"n;
  by "city'城市2"n;
run;

data "city_pop'中"n (label='内华达州县城人口');
  length "city'城市1"n $65 "city'城市2"n $55;
  infile datalines dlm=',';
  input "city'城市1"n "population'人口"n "county'县"n;
  label "city'城市1"n            = '县城'
        "city'城市2"n           = '标准化城市名称'
        "population'人口"n = '城市人口'
        "county'县"n          = 'County FIPS Code';
  "city'城市2"n = upcase(compress("city'城市1"n));
cards;
Fallon, 8458, 1
Las Vegas, 623747, 3
Minden, 3180, 5
Elko, 20279, 7
Goldfield, 443, 9
Eureka, 487, 11
Winnemucca, 7887, 13
Battle Mountain, 3276, 15
Pioche, 911, 17
Yerington, 3064, 19
Hawthorne, 3095, 21
Tonopah, 2360 , 23
Lovelock, 1878, 27
Virginia City, 717, 29
Reno, 241445, 31
Ely, 4134, 33
Carson City, 54521, 510
;
proc sort data="city_pop'中"n;
  by "city'城市2"n;
run;

data "city_pop_loc'中"n;
  merge "city_pop'中"n (in=a) "city_loc'中"n;
  by "city'城市2"n;
  if a;
run;
 
data "nevada'内华达"n;
  set mapsgfk.us_counties(where=(state=32)
                          drop=x y
                          rename=(long=x lat=y));
run;

data "county_pop'中"n (label='内华达州各县');
  length "county_name'县名"n $55;
  infile datalines dlm=',';
  "state'州"n=32;
  input "county_name'县名"n "county'县"n "population'县人口"n;
  label "state'州"n             = 'State FIPS Code'
        "county_name'县名"n       = 'County Name'
        "county'县"n            = 'County FIPS Code'
        "population'县人口"n = '2010 Census County Population'
        "group'组"n             = 'Population range';
  /* Add five population ranges as groups to map response data. */
  if      "population'县人口"n > 100000 then "group'组"n='大于 100,000';
  else if "population'县人口"n > 10000  then "group'组"n='10,000 - 100,000';
  else if "population'县人口"n > 5000   then "group'组"n='5,000 - 10,000';
  else if "population'县人口"n > 1000   then "group'组"n='1,000 - 5,000';
  else                                    "group'组"n='小于 1,000';
cards;
Churchill, 1, 24877
Clark, 3, 2069681
Douglas, 5, 47710
Elko, 7, 52766
Esmeralda, 9, 783
Eureka, 11, 1987
Humboldt, 13, 17019
Lander, 15, 5775
Lincoln, 17, 5036
Lyon, 19, 52585
Mineral, 21, 4772
Nye, 23, 43946
Pershing, 27, 6753
Storey, 29, 3987
Washoe, 31, 446903
White Pine, 33, 10030
Carson City, 510, 54521
;
"""

    CANONICAL_CORRELATION = """
data "jobs'中"n;
   input "career'中"n "supervisor'中"n "finance'中"n "variety'中"n "feedback'中"n "autonomy'中"n;
   datalines;
72 26 9 10 11 70
63 76 7 85 22 93
96 31 7 83 63 73
96 98 6 82 75 97
84 94 6 36 77 97
66 10 5 28 24 75
31 40 9 64 23 75
45 14 2 19 15 50
42 18 6 33 13 70
79 74 4 23 14 90
39 12 2 37 13 70
54 35 3 23 74 53
60 75 5 45 58 83
63 45 5 22 67 53
run;
"""
