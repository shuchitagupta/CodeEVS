"""

EVS: Python Code for Risk Assessment

Group 4 { Apurba Mondal 	2013128,
         Chanchal Prajapati 2013030,
         Juhi Bhatnagar 	2013044 [Group Leader],
         Mohini Verma 		2013062,
         Prerna Singh 		2013149,
         Protichi Basak 	2013075,
         Ritvik Agarwal 	2013078,
         Saloni Gupta 		2013084,
         Shuchita Gupta 	2013101,
         Siddhant Sharma 	2013160,
         Simran Saxena 		2013104 }

To run, just click on the play button on the upper left side of the screen.
"""

pollutant_mapping = { 0: "Ozone",
                      1: "TSP",
                      2: "CO",
                      3: "SO2",
                      4: "NO2"
                    }

values = { "Ozone": (1.003, 1013),
           "TSP": (1.003, 1013),
           "CO": (1.004, 1013),
           "SO2": (1.004, 1013),
           "NO2": (1.002, 497)
        }


def function_to_call(conc_array, aqi_array):
    pollu_values = []
    for dummy_i in range (0, len(conc_array)):
        pollu = conc_array[dummy_i]
        pollu_rr = relative_risk_calculator(pollu, conc_array[dummy_i], aqi_array[dummy_i])
        pollu_values.extend(pollu_rr)
    return air_risk_calculation(pollu_values)
    

def relative_risk_calculator(pollutant, conc, aqi):
    dummy_a = (conc - aqi) / 10
    dummy_b = (values[pollutant][0]) - 1
    rel_risk = (a * b) + 1
    return rel_risk
    
    
def air_risk_calculation(pollutants_values):
    numerator = 0
    denomenator  = 0
    for dummy_i in range (0, len(pollutants_values)):
        dummy_a = values[pollutant_mapping[dummy_i]][1]
        numerator += (pollutants_values[dummy_i] - 1) * dummy_a 
        denomenator += pollutants_values[dummy_i] * dummy_a
    return numerator / denomenator
    


