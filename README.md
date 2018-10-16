# Google Analytics Kaggle



## Differences Between Train and Test Data

The training data starts on 8/1/16 and ends 8/1/17.  The test data starts off on 8/2/17. Visitors are unique to each set; there is no opportunity to utilize visitor history, though this forces the model to be more generalizable besides. 

## Dataset Features

Here, we list the features available in the competition data.  Features that are further embedded in json format are discussed in the next section.

channelGrouping: Pairs with medium.  
    - Direct visits are those with no referral or organic header.  It is usually assumed that these come from directly typing in the url or from clicking a bookmark, though this is not necessarily the case.  Direct has no medium.
    - Referral is a link followed from another website.  Medium will be the page that directs the traffic.
    - Organic is a search engine search.  Medium will be the search engine used.
    - Paid Search has mediums including cpc indicating traffic from Google Adwords
    - Display has mediums including cpm indicating traffic from another ad network
    
date: Date of interaction.  Stored as integer in tables, but recognizable as YYYYMMDD

fullVisitorId: Unique identifier of user interacting with site.  Stored as string, too large to store as integers.

sessionId: Combination of visitor id and visit start time timestamp.  Uniquely identifies a row, but contains redundant information in a long string otherwise.
    
socialEngagementType: Only ever 'Not Socially Engaged'.  The site doesn't have information on likes or sharing the site on social media sites.

visitId: Timestamp for the time the visit started.  Redundant information.

visitNumber:  The number of times the visitor has visited the store since first recorded.

visitStartTime: Timestamp for the time the visit started.  Stored as integer.


## JSON Columns

The following features are further embedded in jsons.  We detail the contents here.  The fields that were censored and contain no information are generally omitted unless I decided to rant about it.

### Device

deviceCategory: Tablet, mobile or desktop

isMobile: True or false, not sure if this gives any new information

browser:  Name of the browser used.

operatingSystem:  Nintendo systems and xbox are included, but the Playstation does not seem to be.  There was a browser on the PSVita, but perhaps not since then.

### GeoNetwork

city: Like it sounds.

continent: Like it sounds.

country: Like it sounds.

metro: Large city, mostly in the US.  Sometimes it mentions that the current metro is unavailable in the dataset.

networkDomain: ISP domain name.

region: Lists state in America, province in China, region in Japan, etc.

subContinent: Cardinal direction + continent


### Totals

bounces: 1 if bounced, not there if no.  Also implies page views and visits is 1, but these are shown anyway.

pageViews: Page views on store for the session.  Bounce means 1 pageView, not sure about the other way around.

visits: Sequence of pageViews with no more than 30 minutes between each view.  In this dataset, it's only ever 1.

newVisits: 1 or None.  As opposed to visits, which is just 1.

hits: Number of objects loaded in the session.  Kaggle says different types of hits are usually distinguished, but are grouped together here.

### Traffic Source

adContent: Brief description of the ad if directed from one.
    
adwordsClickInfo: Includes yet another dictionary.
    - page: Which page the ad was placed in the google search
    - slot: Where on the page the ad is located
    - isVideoAd: If the ad was a video, bool
    - adNetworkType: Ad network, head and tail results are 'Google Search'
    - gclId:
    - criteriaParameters: Censored
    - targetingCriteria: Appears sometimes, as an empty list to boot.  Need to look further.
    
campaign: Something to do with ad campaigns targetting specific item categories.

campaignCode: Not included in test set, but there was only one in the training data.  Not sure which campaign it's tied to, don't care for absence in test data.  Should have just included it in columns with no information but just wanted to point out that there is potentially information for the training data, useless for the model.

gclId: 

isTrueDirect: 

keyword: **Check if this is only for organic searches or something**

medium: See channelGrouping above

referralPath: Specific link for the referral appended on the source domain.

source: Site originating the referral.
