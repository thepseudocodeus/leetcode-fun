# This script is a best-practice example of how to gather structured data from LeetCode's
# public API. It uses a GraphQL query to efficiently fetch problem metadata, including
# tags and difficulty, which are crucial for the Entropy Analyzer.

import json
import time

import requests


def fetch_all_problems():
    """
    Fetches all LeetCode problems from the public GraphQL API.

    This function sends a POST request to the GraphQL endpoint with a specific
    query to get all questions. It handles pagination to ensure all problems
    are retrieved.

    Returns:
        list: A list of dictionaries, where each dictionary represents a problem.
    """
    url = "https://leetcode.com/graphql"
    all_problems = []
    has_next = True
    skip = 0
    limit = 50  # Fetch 50 problems at a time to handle pagination

    # The GraphQL query to fetch problem metadata.
    # We are specifically asking for a list of all questions and their fields.
    query = """
        query problemsetQuestionList($skip: Int, $limit: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList(skip: $skip, limit: $limit, filters: $filters) {
                questions {
                    questionId
                    title
                    titleSlug
                    difficulty
                    topicTags {
                        name
                    }
                    isPaidOnly
                }
                totalNum
            }
        }
    """

    print("Starting data collection from LeetCode...")

    while has_next:
        variables = {"skip": skip, "limit": limit, "filters": {}}

        # Build the payload for the POST request
        payload = {"query": query, "variables": variables}

        try:
            # Send the request and check for a successful response
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()  # Raises an HTTPError if the response was an error

            data = response.json()

            # Extract the problems from the JSON response
            questions_data = data["data"]["problemsetQuestionList"]
            problems_chunk = questions_data["questions"]
            total_problems = questions_data["totalNum"]

            all_problems.extend(problems_chunk)
            print(f"Fetched {len(all_problems)} of {total_problems} problems...")

            # Check if there are more problems to fetch
            if len(all_problems) < total_problems:
                skip += limit
                time.sleep(1)  # Be a good citizen and avoid rate limiting
            else:
                has_next = False

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    print("Data collection complete.")
    return all_problems


def save_to_json(data, filename="leetcode_problems.json"):
    """
    Saves the collected data to a JSON file.

    Args:
        data (list): The list of problem dictionaries to save.
        filename (str): The name of the file to save the data to.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved data to '{filename}'")
    except IOError as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    # Execute the script
    problems = fetch_all_problems()

    if problems:
        # Filter out "premium" problems since we can't access them for analysis
        free_problems = [p for p in problems if not p.get("isPaidOnly")]

        # Save the collected data to a file for later analysis
        save_to_json(free_problems)
