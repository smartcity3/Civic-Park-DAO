import requests
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def get_apriori_result(supp, api_endpoint):
    array_of_campaigns = get_json(api_endpoint)
    variables = list(array_of_campaigns[0].keys())
    df = pd.DataFrame([[i.get(j, None) for j in variables] for i in array_of_campaigns], columns=variables)

    
    # Drop non numeric columns
    df.index = df['campaignName']
    df_dropped = df.drop(['campaignName', '$class', 'owner', 'campaignId'], axis=1)
        
    apriori_df = apriori(df_dropped.T, supp, use_colnames=True)
    return apriori_df.to_json(orient='records')

def get_association_rules(supp, api_endpoint):
    frequent_itemsets = pd.read_json(get_apriori_result(supp, api_endpoint), orient='columns')

    associated_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=supp)

    return associated_rules.to_json(orient='records')


def get_json(api_endpoint):
    r = requests.get(api_endpoint)
    return r.json()


def post_json(body, api_endpoint):
    r = requests.post(api_endpoint, json=body)
    return r.json()
