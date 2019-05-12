import requests

import pandas as pd
from mlxtend.frequent_patterns import apriori


def get_apriori_result(response, supp):

    campaigns_with_categories_array = response
    for row in campaigns_with_categories_array:
        row.pop('Name_Of_Community', None)

    df = pd.DataFrame(campaigns_with_categories_array)
    apriori_df = apriori(df, min_support=supp, use_colnames=True)
    apriori_df['itemsets'] = apriori_df['itemsets'].astype(str).apply(lambda x: x.replace('frozenset({\'', '')).apply(
        lambda x: x.replace('\'})', '')).apply(lambda x: x.replace('\'', ''))
    apriori_df['support'] = apriori_df['support'].apply(lambda x: "{:.2f}".format(x))
    apriori_df.columns = ['Support', 'Set_Of_Categories']

    cleaned_data = [{'Support': apriori_df['Support'][row_index],
                     'Set_Of_Categories': apriori_df['Set_Of_Categories'][row_index]}
                    for row_index in apriori_df['Support'].keys()]

    return cleaned_data


def new_apriori(supp, api_endpoint):
    array_of_campaigns = get_json(api_endpoint)
    variables = list(array_of_campaigns[0].keys())
    df = pd.DataFrame([[i.get(j, None) for j in variables] for i in array_of_campaigns], columns=variables)

    # Drop non numeric columns
    df_dropped = df.drop(['$class', 'owner', 'campaignId'], axis=1)
    df_dropped.index = df_dropped['campaignName']
    df_dropped = df_dropped.drop(['campaignName', 'Sensors'], axis=1)

    df_dropped.astype(int)

    apriori_df = apriori(df_dropped.T, supp, use_colnames=True)

    return apriori_df.to_json(orient='columns')


def get_json(api_endpoint):
    r = requests.get(api_endpoint)
    return r.json()


def post_json(body, api_endpoint):
    r = requests.post(api_endpoint, json=body)
    return r.json()

# def parse_json():
#     base_path = Path(__file__).parent.parent
#     print(base_path)
#     with open(base_path / 'static/response_campaigns.json') as json_file:
#         parsed_json = json.load(json_file)
#     return parsed_json


# def get_campaign_data_from_response():
#
#     campaign_categories_mapping_to_json = {
#         "FAMobility": 12,
#         "FASafety": 13,
#         "SAEconomic": 14,
#         "SARoadsTrans": 15,
#         "TArtificialIntelligence": 16,
#         "TAutonomousVehicles": 17,
#         "TGeospatial": 18,
#         "TIoT": 19,
#         "TSensors": 20
#     }
#
#     response_json = parse_json()
#
#     data = []
#     for contract in response_json['contracts']:
#         row = {"Name_Of_Community": contract['contractProperties'][3]['value']}
#         for category in campaign_categories_mapping_to_json.keys():
#             row.update({category: int(contract['contractProperties']
#                                       [campaign_categories_mapping_to_json[category]]['value'])})
#         data.append(row)
#
#     return data
