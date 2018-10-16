import pandas as pd
from datetime import datetime
import pickle


json_cols = ['device', 'geoNetwork', 'totals', 'trafficsource']
json_cols_lower = [col.lower() for col in json_cols]
with open('./pickles/field_vals.pkl', 'rb') as f:
    field_vals = pickle.load(f)
    
with open('./pickles/useless_fields.pkl', 'rb') as f:
    useless_fields = pickle.load(f)
    
adwordsClickInfo_keys = ['adNetworkType', 'criteriaParameters', 'gclId', 'isVideoAd', 'page', 'slot', 'targetingCriteria']

def dictUnravel(df):
    temp = df.copy()
    for column in json_cols:
        fields = set(field_vals['train'][column].keys()).difference(useless_fields['train'])
        for field in fields:
            temp[field] = temp[column.lower()].map(lambda row: row[field] if field in row.keys() else None)
    for field in adwordsClickInfo_keys:
        temp[field] = temp['adwordsClickInfo'].map(lambda row: row[field] if field in row.keys() else None)
    numeric_cols = ['pageviews', 'transactionRevenue', 'bounces', 'newVisits', 'hits']
    for column in numeric_cols:
        temp[column] = temp[column].astype(float).fillna(0)
    return temp.drop(json_cols_lower + ['adwordsClickInfo'], axis=1)

def visitFix(df):
    temp = df.copy()
    temp['visitstarttime'] = temp.visitstarttime.map(datetime.fromtimestamp)
    temp.drop(['sessionid', 'visitid'], axis=1, inplace=True)
    return temp