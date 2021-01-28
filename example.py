import synclient

configuration = synclient.Configuration(
    host="https://repo-prod.prod.sagebase.org/repo/v1",
)
# Obtain PAT from synapse under settings
pat = ''
configuration.access_token = pat


with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.ChallengeServicesApi(api_client)

challenge = api_instance.get_challenge(2797)

challenge_teams = api_instance.list_challenge_teams(2797)
participants = api_instance.list_participants_in_challenge(2797)
challenges = api_instance.list_challenges_for_participant(3324230)
