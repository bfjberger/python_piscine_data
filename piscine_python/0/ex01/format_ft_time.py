import time 
import datetime

date = datetime.date.today()
formatted_date = date.strftime("%b %d %Y")
seconds_since_epoch = time.time()
formatted_seconds = "{:,.4f}".format(seconds_since_epoch)
# Explanation:
# :,.4f indicates:
# ,: Use commas as the thousands separator.
# .4f: Format the number as a floating-point number with 4 decimal places.

scientific_epoch = "{:.2e}".format(seconds_since_epoch)
epoc_str = "Seconds since January 1, 1970: {} or {} in scientific notation".format(formatted_seconds, scientific_epoch)
print(epoc_str)
print(formatted_date)
