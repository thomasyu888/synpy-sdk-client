# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from synclient.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from synclient.model.accesstype import ACCESSTYPE
from synclient.model.access_approval import AccessApproval
from synclient.model.access_approval_info import AccessApprovalInfo
from synclient.model.access_approval_notification import AccessApprovalNotification
from synclient.model.access_approval_notification_request import AccessApprovalNotificationRequest
from synclient.model.access_approval_notification_response import AccessApprovalNotificationResponse
from synclient.model.access_control_list import AccessControlList
from synclient.model.access_requirement import AccessRequirement
from synclient.model.accessor_group import AccessorGroup
from synclient.model.accessor_group_request import AccessorGroupRequest
from synclient.model.accessor_group_response import AccessorGroupResponse
from synclient.model.activity import Activity
from synclient.model.alias_list import AliasList
from synclient.model.annotations_annotation import AnnotationsAnnotation
from synclient.model.annotations_v2 import AnnotationsV2
from synclient.model.annotations_value import AnnotationsValue
from synclient.model.annotations_value_type import AnnotationsValueType
from synclient.model.approval_state import ApprovalState
from synclient.model.async_job_id import AsyncJobId
from synclient.model.attachment_metadata import AttachmentMetadata
from synclient.model.batch_access_approval_info_request import BatchAccessApprovalInfoRequest
from synclient.model.batch_access_approval_info_response import BatchAccessApprovalInfoResponse
from synclient.model.batch_upload_response import BatchUploadResponse
from synclient.model.bind_schema_to_entity_request import BindSchemaToEntityRequest
from synclient.model.boolean_result import BooleanResult
from synclient.model.bound_object_type import BoundObjectType
from synclient.model.challenge import Challenge
from synclient.model.challenge_paged_results import ChallengePagedResults
from synclient.model.challenge_team import ChallengeTeam
from synclient.model.challenge_team_paged_results import ChallengeTeamPagedResults
from synclient.model.column_model import ColumnModel
from synclient.model.column_type import ColumnType
from synclient.model.count import Count
from synclient.model.create_discussion_reply import CreateDiscussionReply
from synclient.model.create_discussion_thread import CreateDiscussionThread
from synclient.model.csv_table_descriptor import CsvTableDescriptor
from synclient.model.data_type import DataType
from synclient.model.data_type_response import DataTypeResponse
from synclient.model.discussion_reply_bundle import DiscussionReplyBundle
from synclient.model.discussion_thread_bundle import DiscussionThreadBundle
from synclient.model.docker_commit import DockerCommit
from synclient.model.doi import Doi
from synclient.model.doi_all_of import DoiAllOf
from synclient.model.doi_association import DoiAssociation
from synclient.model.doi_creator import DoiCreator
from synclient.model.doi_name_identifier import DoiNameIdentifier
from synclient.model.doi_request import DoiRequest
from synclient.model.doi_resource_type import DoiResourceType
from synclient.model.doi_resource_type_general import DoiResourceTypeGeneral
from synclient.model.doi_response import DoiResponse
from synclient.model.doi_title import DoiTitle
from synclient.model.double_annotation import DoubleAnnotation
from synclient.model.download_from_table_request import DownloadFromTableRequest
from synclient.model.download_from_table_request_all_of import DownloadFromTableRequestAllOf
from synclient.model.download_from_table_result import DownloadFromTableResult
from synclient.model.entity import Entity
from synclient.model.entity_bundle_create_v2 import EntityBundleCreateV2
from synclient.model.entity_bundle_request import EntityBundleRequest
from synclient.model.entity_bundle_v2 import EntityBundleV2
from synclient.model.entity_children_request import EntityChildrenRequest
from synclient.model.entity_children_response import EntityChildrenResponse
from synclient.model.entity_header import EntityHeader
from synclient.model.entity_id import EntityId
from synclient.model.entity_id_list import EntityIdList
from synclient.model.entity_lookup_request import EntityLookupRequest
from synclient.model.entity_path import EntityPath
from synclient.model.entity_thread_count import EntityThreadCount
from synclient.model.entity_thread_counts import EntityThreadCounts
from synclient.model.entity_type import EntityType
from synclient.model.evaluation import Evaluation
from synclient.model.evaluation_round import EvaluationRound
from synclient.model.evaluation_round_limit import EvaluationRoundLimit
from synclient.model.evaluation_round_limit_type import EvaluationRoundLimitType
from synclient.model.evaluation_round_list_request import EvaluationRoundListRequest
from synclient.model.evaluation_round_list_response import EvaluationRoundListResponse
from synclient.model.evaluation_status import EvaluationStatus
from synclient.model.facet_column_request import FacetColumnRequest
from synclient.model.facet_column_result import FacetColumnResult
from synclient.model.facet_type import FacetType
from synclient.model.file_handle import FileHandle
from synclient.model.file_handle_results import FileHandleResults
from synclient.model.file_handle_update_request import FileHandleUpdateRequest
from synclient.model.form_change_request import FormChangeRequest
from synclient.model.form_data import FormData
from synclient.model.form_group import FormGroup
from synclient.model.form_rejection import FormRejection
from synclient.model.forum import Forum
from synclient.model.id_list import IdList
from synclient.model.join_team_signed_token import JoinTeamSignedToken
from synclient.model.json_schema_object_binding import JsonSchemaObjectBinding
from synclient.model.json_schema_version_info import JsonSchemaVersionInfo
from synclient.model.list_request import ListRequest
from synclient.model.list_response import ListResponse
from synclient.model.list_validation_results_request import ListValidationResultsRequest
from synclient.model.list_validation_results_response import ListValidationResultsResponse
from synclient.model.list_wrapper_of_team import ListWrapperOfTeam
from synclient.model.list_wrapper_of_team_member import ListWrapperOfTeamMember
from synclient.model.list_wrapper_of_user_profile import ListWrapperOfUserProfile
from synclient.model.long_annotation import LongAnnotation
from synclient.model.member_submission_eligibility import MemberSubmissionEligibility
from synclient.model.membership_invitation import MembershipInvitation
from synclient.model.membership_request import MembershipRequest
from synclient.model.message_to_user import MessageToUser
from synclient.model.message_url import MessageURL
from synclient.model.name_identifier_scheme import NameIdentifierScheme
from synclient.model.notification_type import NotificationType
from synclient.model.object_type import ObjectType
from synclient.model.object_type_schema import ObjectTypeSchema
from synclient.model.paginated_column_models import PaginatedColumnModels
from synclient.model.paginated_ids import PaginatedIds
from synclient.model.paginated_results_of_access_requirement import PaginatedResultsOfAccessRequirement
from synclient.model.paginated_results_of_discussion_reply_bundle import PaginatedResultsOfDiscussionReplyBundle
from synclient.model.paginated_results_of_discussion_thread_bundle import PaginatedResultsOfDiscussionThreadBundle
from synclient.model.paginated_results_of_docker_commit import PaginatedResultsOfDockerCommit
from synclient.model.paginated_results_of_entity_header import PaginatedResultsOfEntityHeader
from synclient.model.paginated_results_of_evaluation import PaginatedResultsOfEvaluation
from synclient.model.paginated_results_of_membership_invitation import PaginatedResultsOfMembershipInvitation
from synclient.model.paginated_results_of_membership_request import PaginatedResultsOfMembershipRequest
from synclient.model.paginated_results_of_reference import PaginatedResultsOfReference
from synclient.model.paginated_results_of_submission import PaginatedResultsOfSubmission
from synclient.model.paginated_results_of_submission_bundle import PaginatedResultsOfSubmissionBundle
from synclient.model.paginated_results_of_submission_status import PaginatedResultsOfSubmissionStatus
from synclient.model.paginated_results_of_team import PaginatedResultsOfTeam
from synclient.model.paginated_results_of_team_member import PaginatedResultsOfTeamMember
from synclient.model.paginated_results_of_trashed_entity import PaginatedResultsOfTrashedEntity
from synclient.model.paginated_results_of_user_group import PaginatedResultsOfUserGroup
from synclient.model.paginated_results_of_user_profile import PaginatedResultsOfUserProfile
from synclient.model.paginated_results_of_version_info import PaginatedResultsOfVersionInfo
from synclient.model.paginated_team_ids import PaginatedTeamIds
from synclient.model.passing_record import PassingRecord
from synclient.model.query import Query
from synclient.model.query_bundle_request import QueryBundleRequest
from synclient.model.query_next_page_token import QueryNextPageToken
from synclient.model.query_result import QueryResult
from synclient.model.query_result_bundle import QueryResultBundle
from synclient.model.question import Question
from synclient.model.question_response import QuestionResponse
from synclient.model.reference import Reference
from synclient.model.reference_list import ReferenceList
from synclient.model.reply_count import ReplyCount
from synclient.model.resource_access import ResourceAccess
from synclient.model.response_correctness import ResponseCorrectness
from synclient.model.response_message import ResponseMessage
from synclient.model.restrictable_object_descriptor import RestrictableObjectDescriptor
from synclient.model.restrictable_object_type import RestrictableObjectType
from synclient.model.restriction_information_response import RestrictionInformationResponse
from synclient.model.restriction_level import RestrictionLevel
from synclient.model.row_reference import RowReference
from synclient.model.row_reference_set import RowReferenceSet
from synclient.model.row_set import RowSet
from synclient.model.row_table import RowTable
from synclient.model.select_column import SelectColumn
from synclient.model.settings import Settings
from synclient.model.snapshot_request import SnapshotRequest
from synclient.model.snapshot_response import SnapshotResponse
from synclient.model.sort_by import SortBy
from synclient.model.sort_direction import SortDirection
from synclient.model.sort_item import SortItem
from synclient.model.state_enum import StateEnum
from synclient.model.string_annotation import StringAnnotation
from synclient.model.sts_credentials import StsCredentials
from synclient.model.submission_bundle import SubmissionBundle
from synclient.model.submission_contributor import SubmissionContributor
from synclient.model.submission_eligibility import SubmissionEligibility
from synclient.model.submission_model import SubmissionModel
from synclient.model.submission_quota import SubmissionQuota
from synclient.model.submission_status_batch import SubmissionStatusBatch
from synclient.model.submission_status_enum import SubmissionStatusEnum
from synclient.model.submission_status_form import SubmissionStatusForm
from synclient.model.submission_status_model import SubmissionStatusModel
from synclient.model.sum_file_sizes import SumFileSizes
from synclient.model.table_bundle import TableBundle
from synclient.model.table_file_handle_results import TableFileHandleResults
from synclient.model.table_update_request import TableUpdateRequest
from synclient.model.table_update_response import TableUpdateResponse
from synclient.model.table_update_transaction_request import TableUpdateTransactionRequest
from synclient.model.table_update_transaction_response import TableUpdateTransactionResponse
from synclient.model.team import Team
from synclient.model.team_member import TeamMember
from synclient.model.team_membership_status import TeamMembershipStatus
from synclient.model.team_submission_eligibility import TeamSubmissionEligibility
from synclient.model.thread_count import ThreadCount
from synclient.model.trashed_entity import TrashedEntity
from synclient.model.update_reply_message import UpdateReplyMessage
from synclient.model.update_thread_message import UpdateThreadMessage
from synclient.model.update_thread_title import UpdateThreadTitle
from synclient.model.used import Used
from synclient.model.user_bundle import UserBundle
from synclient.model.user_entity_permissions import UserEntityPermissions
from synclient.model.user_group import UserGroup
from synclient.model.user_group_header import UserGroupHeader
from synclient.model.user_group_header_response import UserGroupHeaderResponse
from synclient.model.user_group_header_response_page import UserGroupHeaderResponsePage
from synclient.model.user_preference import UserPreference
from synclient.model.user_profile import UserProfile
from synclient.model.validation_exception import ValidationException
from synclient.model.validation_results import ValidationResults
from synclient.model.validation_summary_statistics import ValidationSummaryStatistics
from synclient.model.verification_state import VerificationState
from synclient.model.verification_state_enum import VerificationStateEnum
from synclient.model.verification_submission import VerificationSubmission
from synclient.model.version_info import VersionInfo
from synclient.model.wiki_page_key import WikiPageKey
