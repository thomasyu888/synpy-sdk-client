
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.access_approval_services_api import AccessApprovalServicesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from synclient.api.access_approval_services_api import AccessApprovalServicesApi
from synclient.api.access_requirement_services_api import AccessRequirementServicesApi
from synclient.api.activity_services_api import ActivityServicesApi
from synclient.api.certified_user_services_api import CertifiedUserServicesApi
from synclient.api.challenge_services_api import ChallengeServicesApi
from synclient.api.data_access_services_api import DataAccessServicesApi
from synclient.api.discussion_services_api import DiscussionServicesApi
from synclient.api.docker_commit_services_api import DockerCommitServicesApi
from synclient.api.doi_services_api import DoiServicesApi
from synclient.api.entity_bundle_v2_services_api import EntityBundleV2ServicesApi
from synclient.api.entity_services_api import EntityServicesApi
from synclient.api.evaluation_services_api import EvaluationServicesApi
from synclient.api.form_services_api import FormServicesApi
from synclient.api.membership_invitation_services_api import MembershipInvitationServicesApi
from synclient.api.membership_request_services_api import MembershipRequestServicesApi
from synclient.api.message_services_api import MessageServicesApi
from synclient.api.table_services_api import TableServicesApi
from synclient.api.team_services_api import TeamServicesApi
from synclient.api.trash_services_api import TrashServicesApi
from synclient.api.user_profile_services_api import UserProfileServicesApi
