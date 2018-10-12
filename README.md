# google_analytics_kaggle

Terms to look up:
Social Engagement Type (came from social network?)


### Totals

bounces: 1 if bounced, not there if no.  Also implies page views and visits is 1, but these are shown anyway.

pageViews: Page views on store for the session.  1 also means bounce.

visits: 

### Traffic Source

source: Pairs with medium.  
    - Direct visits are those with no referral or organic header.  It is usually assumed that these come from directly typing in the url or from clicking a bookmark, though this is not necessarily the case.  Direct has no medium.
    - Referral is a link followed from another website.  Medium will be the page that directs the traffic.
    - Organic is a search engine search.  Medium will be the search engine used.
    - cpc indicates traffic from Google Adwords
    - cpm indicates traffic from another ad network
    
adwordsClickInfo: Includes yet another dictionary.
    - page: Which page the ad was placed in the google search
    - slot: Where on the page the ad is located
    - isVideoAd: If the ad was a video, bool
    - adNetworkType: Ad network, head and tail results are 'Google Search'
    - gclId:
    - criteriaParameters: Censored
    - targetingCriteria: Appears sometimes, as an empty list to boot.  Need to look further.
    
Campaign: Something to do with ad campaigns targetting specific item categories.

campaignCode: Not included in test set, but there was only one in the training data.  Not sure which campaign it's tied to, don't care for absence in test data.  Should have just included it in columns with no information but just wanted to point out that there is potentially information for the training data, useless for the model.

isTrueDirect: 



### Censored Fields with No Information

These are listed below: criteriaParameters(inside adwordsClickInfo), 