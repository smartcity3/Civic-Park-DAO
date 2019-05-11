import json
from pathlib import Path

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


def parse_json():
    base_path = Path(__file__).parent.parent
    with open(base_path / 'static/response_campaigns.json') as json_file:
        parsed_json = json.load(json_file)
    return parsed_json


def get_campaign_data_from_response():

    campaign_categories_mapping_to_json = {
        "FAMobility": 12,
        "FASafety": 13,
        "SAEconomic": 14,
        "SARoadsTrans": 15,
        "TArtificialIntelligence": 16,
        "TAutonomousVehicles": 17,
        "TGeospatial": 18,
        "TIoT": 19,
        "TSensors": 20
    }

    response_json = parse_json()

    data = []
    for contract in response_json['contracts']:
        row = {"Name_Of_Community": contract['contractProperties'][3]['value']}
        for category in campaign_categories_mapping_to_json.keys():
            row.update({category: int(contract['contractProperties']
                                      [campaign_categories_mapping_to_json[category]]['value'])})
        data.append(row)

    return data
