import pandas as pd
from datetime import datetime
import pickle


json_cols = ['device', 'geoNetwork', 'totals', 'trafficsource']
json_cols_lower = [col.lower() for col in json_cols]
with open('./pickles/field_vals.pkl', 'rb') as f:
    field_vals = pickle.load(f)
    
with open('./pickles/useless_fields.pkl', 'rb') as f:
    useless_fields = pickle.load(f)

with open('./pickles/field_dict.pkl', 'rb') as f:
    field_dict = pickle.load(f)
    
with open('./pickles/channel_groups.pkl', 'rb') as f:
    channel_groups = pickle.load(f)

adwordsClickInfo_keys = ['adNetworkType', 'criteriaParameters', 'gclId', 'isVideoAd', 'page', 'slot', 'targetingCriteria']
objects_dict = {}

#From a SELECT * statement from either table, unwraps the json columns.
def dictUnravel(df, dataset='train'):
    temp = df.copy()
    for column in json_cols:
        fields = set(field_vals[dataset][column].keys()).difference(useless_fields[dataset])
        for field in fields:
            temp[field] = temp[column.lower()].map(lambda row: row[field] if field in row.keys() else None)
    for field in adwordsClickInfo_keys:
        temp[field] = temp['adwordsClickInfo'].map(lambda row: row[field] if field in row.keys() else None)
    numeric_cols = ['pageviews', 'bounces', 'newVisits', 'hits']
    for column in numeric_cols:
        temp[column] = temp[column].astype(float).fillna(0)
    if dataset == 'train':
        temp['transactionRevenue'] = temp['transactionRevenue'].astype('float').fillna(0).map(lambda x: x*1e-6)
    return temp.drop(json_cols_lower + ['adwordsClickInfo'], axis=1)

#changes visit start time into datetime format
def visitFix(df):
    temp = df.copy()
    temp['visitstarttime'] = temp.visitstarttime.map(datetime.fromtimestamp)
    temp.drop(['sessionid', 'visitid'], axis=1, inplace=True)
    return temp
