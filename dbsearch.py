import testdblib
import sys

search_type = sys.argv[1]
search_term = sys.argv[2]


if search_type == "name":
    name_search = testdblib.db_find_by_name(search_term)
elif search_type == "company":
    company_search = testdblib.db_find_by_company(search_term)
elif search_type == "twitter":
    twitter_search = testdblib.db_find_by_twitter(search_term)
else:
    print 'It doesn't look like you entered a valid search term!'
