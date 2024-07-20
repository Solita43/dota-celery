# https://www.opendota.com/api-keys
#                   Free Tier	                                Premium Tier
# Price	            Free	                                    $0.01 per 100 calls
# Key Required?	    No	                                        Yes -- requires payment method
# Call Limit	    2000 per day	                            Unlimited
# Rate Limit	    60 calls per minute	                        1200 calls per minute
# Support	        Community support via Discord group	        Priority support from core developers


# You're charged $0.0001 per call, rounded up to the nearest cent.
# Getting an API key requires a linked payment method. We'll automatically charge the card at the beginning of the month for any fees owed.
# 500 errors don't count as usage, since that means we messed up!


# API Documentation
# https://docs.opendota.com/#section/Introduction


# Example Route:
# https://api.opendota.com/api/matches/271145478?api_key=...


import os


api_key=os.environ["OPEN_DOTA_API_KEY"]


# business logic for hero rankings
# grab all hero_id 's
# call /rankings
