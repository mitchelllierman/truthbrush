import json
import time
from datetime import datetime, timedelta

import logging
from truthbrush import Api

# Set up logging
logging.basicConfig(filename='search_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

api = Api()


results = api.search(searchtype="statuses", query="Maga Hat")

i = 0
# Open a file for writing
with open('corpus.json', 'w') as json_file:
    # Write an opening bracket for the JSON array
    json_file.write('[')

    # Iterate over the results and write each one to the file
    first = True
    try:
        for result in results:
            try:
                if i % 250 == 0:
                    sleep_dur = 350 #seconds
                    finish = datetime.now() + timedelta(seconds=sleep_dur)
                    print(f"Honk shoo mimimi. Come back at {finish}. ")
                    time.sleep(350)
                print(
                    f"{i} | Lm: {api.ratelimit_remaining} | {api.ratelimit_reset}",
                    end="\r", flush=True)
                i += 1
                if not first:
                    json_file.write(',')
                else:
                    first = False
                json.dump(result, json_file, indent=4)
            except Exception as e:
                logging.error(
                    f"An error occurred while processing result {i}: {e}")
        # Write a closing bracket for the JSON array
    finally:
        json_file.write(']')
