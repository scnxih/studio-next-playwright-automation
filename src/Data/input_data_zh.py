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

    # Following tables can be also used for Network Summary step
    CORE_DECOMPOSITION = """
libname mycas cas;
data mycas."LinkSetIn'链接"n;
   input "from'始"n $ "to'终"n $ "community'中"n "weight'中"n "wt'中"n;
   datalines;
A B 1 3 3 
A C 1 2 2
A D 1 1 1
B C 1 5 5
C D 1 7 7
C E 1 2 2
D F . 3 3
F G 2 9 9
F H 2 3 3
F I 2 5 5
G H 2 7 7
G I 2 3 3
I J . 3 3
J K 3 1 2
J L 3 6 6
K L 3 3 3
;
 
data mycas."NodeSetIn'节点"n;
   input "node'中"n $ @@;
   datalines;
A    M   N
;
 
data mycas."NodeSubet'节点子网"n;
   input "node'中"n $ "reachId'中"n;
   datalines;
A 1 
C 2
G 1
J 2
K 2
;
    """

    HIDDEN_MARKOV_MODELS = """
libname mycas cas;
/* The following statements simulate the bivariate vector time series from the previous model to provide test data for the HMM procedure: */
%let pi1 = 0.5;
%let a11 = 0.001;
%let a22 = 0.001;
%let mu1_1 = 1;
%let mu1_2 = 1;
%let sigma1_11 = 1;
%let sigma1_21 = 0;
%let sigma1_22 = 1;
%let mu2_1 = -1;
%let mu2_2 = -1;
%let sigma2_11 = 1;
%let sigma2_21 = 0;
%let sigma2_22 = 1;
%let T = 1000;
%let seed = 1234;
 
data DGPone;
	retain cd1_11 cd1_21 cd1_22 cd2_11 cd2_21 cd2_22;
 
	do "t'中"n=1 to &T.;
		if("t'中"n=1) then
			do;
				/* initial probability distribution */
				p=&pi1.;
 
				/* Cholesky decomposition of sigma1 */
				cd1_11=sqrt(&sigma1_11.);
				cd1_21=&sigma1_21./sqrt(&sigma1_11.);
				cd1_22=sqrt(&sigma1_22.-&sigma1_21.*&sigma1_21./&sigma1_11.);
 
				/* Cholesky decomposition of sigma2 */
				cd2_11=sqrt(&sigma2_11.);
				cd2_21=&sigma2_21./sqrt(&sigma2_11.);
				cd2_22=sqrt(&sigma2_22.-&sigma2_21.*&sigma2_21./&sigma2_11.);
			end;
		else
			do;
				/* transition probability matrix */
				if(lags=1) then
					p=&a11.;
				else
					p=1-&a22.;
			end;
		u=uniform(&seed.);
 
		if(u<=p) then
			s=1;
		else
			s=2;
		e1=normal(&seed.);
		e2=normal(&seed.);
 
		if(s=1) then
			do;
				/* ("x'中"n,"y'中"n) ~ N(mu1, Sigma1) at state 1 */
				"x'中"n=&mu1_1. + cd1_11*e1;
				"y'中"n=&mu1_2. + cd1_21*e1+cd1_22*e2;
			end;
		else
			do;
				/* ("x'中"n,"y'中"n) ~ N(mu2, Sigma2) at state 2 */
				"x'中"n=&mu2_1. + cd2_11*e1;
				"y'中"n=&mu2_2. + cd2_21*e1+cd2_22*e2;
			end;
		output;
		lags=s;
	end;
run;
 
/* In general, the data generating process is unknown. What can be seen is the data set One, but not the data set DGPone. */
data One;
	set DGPone;
	keep "t'中"n "x'中"n "y'中"n;
run;
 
data mycas."One'中"n;
	set One;
run;
    """

    SEGMENTATION = """
libname mycas cas;
 
data mycas."reviews'中"n;
       infile datalines delimiter='|' missover;
       length "text'中"n $300 "category'中"n $20;
       input "text'中"n$ "positive'中"n "category'中"n$ "did'中"n;
       datalines;
    这是有史以来最棒的手机！喜欢它！|1|电子产品|1
    手机电池寿命太短。|0|电子产品|2
    屏幕分辨率较低，但我喜欢这台电视。|1|电子产品|3
    尽管分辨率较低，但电影本身很棒。|1|电影|4
    这部电影的故事很无聊，表演也很差。|0|电影|5
    我在电视上看了这部电影，小屏幕上效果不佳。|0|电影|6
    先看了电影就很喜欢，书甚至更好！|1|书籍|7
    我喜欢这本书里的故事，他们应该把它搬上银幕。|1|书籍|8
    我喜欢这个作者，但这本书浪费时间，不要买。|0|书籍|9
;
    """

    BOOLEAN_RULES = """
libname mycas cas;
 
data mycas."getstart'中"n;
    infile datalines delimiter='|' missover;
    length "text'中"n $150;
    input "text'中"n$ "apple_fruit'中"n "did'中"n$;
    datalines;
美味又香脆的苹果是最受欢迎的水果之一 | 1 |d01
苹果是水果之王。 | 1 |d02
番荔枝或 Sitaphal 是一种甜而多汁的水果 | 1 |d03
苹果是热带地区常见的树种 | 1 |d04
苹果是圆形的，味道很甜 | 1 |d05
热带苹果树结出甜苹果| 1| d06
甜苹果爱好者喜爱富士，因为它是| 1 |d07
这棵苹果树很小 | 1 |d08
Apple Store 商店出售 iPhone x 和 iPhone x Plus。| 0 |d09
查看全球 Apple 电话号码列表。| 0 |d10
查找用户指南的链接并联系 Apple 支持，| 0 |d11
苹果推出 iPhone 画廊来反击三星 Galaxy 产品 | 0 |d12
苹果智能手机 - Verizon Wireless。| 0 |d13
苹果公司这位反复无常的首席执行官，非常愤怒。| 0 |d14
苹果已经升级了这款手机。| 0 |d15
新款 Apple iPhone x 的强大功能。| 0 |d16
苹果 甜美的苹果 iphone。| 0 |d17
苹果将生产汽车 | 0 |d18
苹果也做手表| 0 |d19
苹果也生产电脑| 0 |d20
;
    """
