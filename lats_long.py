from geopy.distance import distance,great_circle

manufaturing_country_lat={'Netherlands': 52.5001698, 'India': 22.3511148, 'UK': 54.7023545, 'Germany': 51.0834196,
                          'Switzerland': 46.7985624, 'Not Applicable': 0, 'Japan': 36.5748441, 'Ireland': 52.865196,
                          'USA': 39.7837304, 'France': 46.603354, 'Korea': 36.638392, 'Canada': 61.0666922, 'South Africa': -28.8166236,
                          'China': 35.000074, 'Italy': 42.6384261}

manufaturing_country_long={'Netherlands': 5.7480821, 'India': 78.6677428, 'UK': -3.2765753, 'Germany': 10.4234469,
                           'Switzerland': 8.2319736, 'Not Applicable': 0, 'Japan': 139.2394179, 'Ireland': -7.9794599,
                           'USA': -100.445882, 'France': 1.8883335, 'Korea': 127.6961188, 'Canada': -107.991707, 'South Africa': 24.991639,

                           'China': 104.999927, 'Italy': 12.674297}

def get_manufaturing_country_lat(x):
    for k,v in manufaturing_country_lat.items():
        if k==x:
            return v

def get_manufaturing_country_long(x):
    for k,v in manufaturing_country_long.items():
        if k==x:
            return v


country_lat={'Kenya': 1.4419683, 'Nigeria': 9.6000359,'Botswana': -23.1681782, 'Tanzania': -6.5247123, 'Cameroon': 4.6125522, 'Ethiopia': 10.2116702,
 'Malawi': -13.2687204, 'Rwanda': -1.9646631, 'Guyana': 4.8417097, 'Kyrgyzstan': 41.5089324,
 'Lesotho': -29.6039267, 'Liberia': 5.7499721, 'Senegal': 14.4750607, 'Swaziland': -26.5624806,
 'Benin': 9.5293472, 'Zimbabwe': -18.4554963, 'Haiti': 19.1399952, 'Namibia': -23.2335499, 'Mali': 16.3700359,
 'Angola': -11.8775768, 'Ghana': 8.0300284, 'Uganda': 1.5333554, 'Kazakhstan': 47.2286086, 'Togo': 8.7800265,
 'South Sudan': 7.8699431, 'Sierra Leone': 8.6400349, 'Dominican Republic': 19.0974031, 'Zambia': -14.5189121,
 'Libya': 26.8234472, "Côte d'Ivoire": 7.9897371, 'Guinea': 10.7226226, 'Sudan': 14.5844444, 'Vietnam': 13.2904027,
 'Guatemala': 15.6356088, 'Congo, DRC': -2.9814344, 'Pakistan': 30.3308401, 'Mozambique': -19.302233, 'South Africa': -28.8166236, 'Afghanistan': 33.7680065,
 'Burkina Faso': 12.0753083, 'Burundi': -3.3634357, 'Belize': 16.8259793, 'Lebanon': 33.8750629}

country_long={'Kenya': 38.4313975, 'Nigeria': 7.9999721, 'Botswana': 24.5928742, 'Tanzania': 35.7878438, 'Cameroon': 13.1535811, 'Ethiopia': 38.6521203,
 'Malawi': 33.9301963, 'Rwanda': 30.0644358, 'Guyana': -58.6416891, 'Kyrgyzstan': 74.724091,
 'Lesotho': 28.3350193, 'Liberia': -9.3658524, 'Senegal': -14.4529612, 'Swaziland': 31.3991317,
 'Benin': 2.2584408, 'Zimbabwe': 29.7468414, 'Haiti': -72.3570972, 'Namibia': 17.3231107, 'Mali': -2.2900239,
 'Angola': 17.5691241, 'Ghana': -1.0800271, 'Uganda': 32.2166578, 'Kazakhstan': 65.2093197, 'Togo': 1.0199765,
 'South Sudan': 29.6667897, 'Sierra Leone': -11.8400269, 'Dominican Republic': -70.3028026, 'Zambia': 27.5589884,
 'Libya': 18.1236723, "Côte d'Ivoire": -5.5679458, 'Guinea': -10.7083587, 'Sudan': 29.4917691, 'Vietnam': 108.4265113,
 'Guatemala': -89.8988087, 'Congo, DRC': 23.8222636, 'Pakistan': 71.247499, 'Mozambique': 34.9144977, 'South Africa': 24.991639, 'Afghanistan': 66.2385139,
 'Burkina Faso': -1.6880314, 'Burundi': 29.8870575, 'Belize': -88.7600927, 'Lebanon': 35.843409}

def get_country_lat(x):
    for k,v in country_lat.items():
        if k==x:
            return v

def get_country_long(x):
    for k,v in country_long.items():
        if k==x:
            return v


def cal_distance(manufaturing_country_lat,manufaturing_country_long, country_lat, country_long):
    start_coordinates = (manufaturing_country_lat, manufaturing_country_long)
    end_coordinates = (country_lat, country_lat)

    return great_circle(start_coordinates, end_coordinates).km