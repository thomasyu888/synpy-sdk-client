"""Example code to interface with python sdk"""
import synclient
from synclient.api import challenge_services_api
from synclient.api import user_profile_services_api
from synclient.api import entity_services_api


configuration = synclient.Configuration(
    host="https://repo-prod.prod.sagebase.org/repo/v1",
)
# Obtain PAT from synapse by going to "settings"
pat = ''
configuration.access_token = pat

with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = challenge_services_api.ChallengeServicesApi(api_client)
    user_service = user_profile_services_api.UserProfileServicesApi(api_client)
    entity_service = entity_services_api.EntityServicesApi(api_client)
    # obtain own user profile
    userprofile = user_service.get_my_own_user_profile()

    # Example challenge services
    challenge = api_instance.get_challenge(4328)
    challenge_teams = api_instance.list_challenge_teams(4328)
    participants = api_instance.list_participants_in_challenge(4328)
    challenges = api_instance.list_challenges_for_participant(userprofile.owner_id)
