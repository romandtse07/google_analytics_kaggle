# Google Analytics Kaggle

## Abstract

Data from a [Google Analytics Kaggle Competition](https://www.kaggle.com/c/ga-customer-revenue-prediction) is analyzed first for insights into business drivers, then for creating a model with predictive power in guessing how much a visitor will spend given Google Analytics data.  User aggregated features including true directs(used in an average form) and overall bounce rate are given to a Random Forest Regressor, along with several other feature columns.  Though the scores obtained are within order of magnitude relative to previously posted kernels, the results are found unsatisfactory, especially in the context that it should make useful predictions.  Current progress in other efforts are briefly described, including a combination of classification and regression.  More importantly, the difference between customers who spend very little and customers that spend nothing at all should be examined in great detail: if we consider that a majority of the store revenue comes from customers that only have less than even two transactions, we should be wary that whatever model we choose is sensitive to these subtle differences.  The work performed thus far has been biased towards separating top spenders and non-customers, but perhaps an analysis in this direction is the wrong approach for even thinking about the problem.

The original premise of the project was tailored to the competition before it was discovered that the test data revenue was available through the Google Analytics demo account.  The revised version of the problem, in which we predict only on customers with past data available, is arguably more relevant, but the project must be revised to reflect this.

## Project Structure

The project is currently divided into three notebooks.  Files that can be reviewed are numbered in order.  Several variables and functions repeatedly called on are stored in helpers.py.  The data was originally downloaded from the Kaggle site before relocating into a local database.  In order to reproduce the work, there must be an equivalent database made in the user's computer.


## Differences Between Train and Test Data

The training data starts on 8/1/16 and ends 8/1/17.  The test data starts off on 8/2/17. Roughly 7,000 users appear in both training and test sets. 

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

The following features are further embedded in jsons.  We detail the contents here.  The fields that were censored and contain no information are generally omitted.

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

transactionRevenue: Only available on the training data.  Units are recorded in 10^6 units of whatever monetary unit the site records.

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

isTrueDirect: True if either the channel grouping is direct or the same parameters are passed between this session and the last.

keyword: Keyword for searches, organic or paid

medium: See channelGrouping above

referralPath: Specific link for the referral appended on the source domain.

source: Site originating the referral.
