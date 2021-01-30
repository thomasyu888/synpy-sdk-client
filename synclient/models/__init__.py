# coding: utf-8

# flake8: noqa
"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from synclient.models.accesstype import ACCESSTYPE
from synclient.models.access_control_list import AccessControlList
from synclient.models.access_requirement import AccessRequirement
from synclient.models.activity import Activity
from synclient.models.alias_list import AliasList
from synclient.models.annotations_annotation import AnnotationsAnnotation
from synclient.models.annotations_v2 import AnnotationsV2
from synclient.models.annotations_value import AnnotationsValue
from synclient.models.annotations_value_type import AnnotationsValueType
from synclient.models.async_job_id import AsyncJobId
from synclient.models.attachment_metadata import AttachmentMetadata
from synclient.models.batch_upload_response import BatchUploadResponse
from synclient.models.bind_schema_to_entity_request import BindSchemaToEntityRequest
from synclient.models.boolean_result import BooleanResult
from synclient.models.bound_object_type import BoundObjectType
from synclient.models.challenge import Challenge
from synclient.models.challenge_paged_results import ChallengePagedResults
from synclient.models.challenge_team import ChallengeTeam
from synclient.models.challenge_team_paged_results import ChallengeTeamPagedResults
from synclient.models.column_model import ColumnModel
from synclient.models.column_type import ColumnType
from synclient.models.count import Count
from synclient.models.create_discussion_thread import CreateDiscussionThread
from synclient.models.csv_table_descriptor import CsvTableDescriptor
from synclient.models.data_type import DataType
from synclient.models.data_type_response import DataTypeResponse
from synclient.models.discussion_reply_bundle import DiscussionReplyBundle
from synclient.models.discussion_thread_bundle import DiscussionThreadBundle
from synclient.models.docker_commit import DockerCommit
from synclient.models.doi import Doi
from synclient.models.doi_all_of import DoiAllOf
from synclient.models.doi_association import DoiAssociation
from synclient.models.doi_creator import DoiCreator
from synclient.models.doi_name_identifier import DoiNameIdentifier
from synclient.models.doi_request import DoiRequest
from synclient.models.doi_resource_type import DoiResourceType
from synclient.models.doi_resource_type_general import DoiResourceTypeGeneral
from synclient.models.doi_response import DoiResponse
from synclient.models.doi_title import DoiTitle
from synclient.models.double_annotation import DoubleAnnotation
from synclient.models.download_from_table_request import DownloadFromTableRequest
from synclient.models.download_from_table_request_all_of import DownloadFromTableRequestAllOf
from synclient.models.download_from_table_result import DownloadFromTableResult
from synclient.models.entity import Entity
from synclient.models.entity_bundle_create_v2 import EntityBundleCreateV2
from synclient.models.entity_bundle_request import EntityBundleRequest
from synclient.models.entity_bundle_v2 import EntityBundleV2
from synclient.models.entity_children_request import EntityChildrenRequest
from synclient.models.entity_children_response import EntityChildrenResponse
from synclient.models.entity_header import EntityHeader
from synclient.models.entity_id import EntityId
from synclient.models.entity_id_list import EntityIdList
from synclient.models.entity_lookup_request import EntityLookupRequest
from synclient.models.entity_path import EntityPath
from synclient.models.entity_thread_count import EntityThreadCount
from synclient.models.entity_thread_counts import EntityThreadCounts
from synclient.models.entity_type import EntityType
from synclient.models.evaluation import Evaluation
from synclient.models.evaluation_round import EvaluationRound
from synclient.models.evaluation_round_limit import EvaluationRoundLimit
from synclient.models.evaluation_round_limit_type import EvaluationRoundLimitType
from synclient.models.evaluation_round_list_request import EvaluationRoundListRequest
from synclient.models.evaluation_round_list_response import EvaluationRoundListResponse
from synclient.models.evaluation_status import EvaluationStatus
from synclient.models.facet_column_request import FacetColumnRequest
from synclient.models.facet_column_result import FacetColumnResult
from synclient.models.facet_type import FacetType
from synclient.models.file_handle import FileHandle
from synclient.models.file_handle_results import FileHandleResults
from synclient.models.file_handle_update_request import FileHandleUpdateRequest
from synclient.models.form_change_request import FormChangeRequest
from synclient.models.form_data import FormData
from synclient.models.form_group import FormGroup
from synclient.models.form_rejection import FormRejection
from synclient.models.id_list import IdList
from synclient.models.join_team_signed_token import JoinTeamSignedToken
from synclient.models.json_schema_object_binding import JsonSchemaObjectBinding
from synclient.models.json_schema_version_info import JsonSchemaVersionInfo
from synclient.models.list_request import ListRequest
from synclient.models.list_response import ListResponse
from synclient.models.list_validation_results_request import ListValidationResultsRequest
from synclient.models.list_validation_results_response import ListValidationResultsResponse
from synclient.models.list_wrapper_of_team import ListWrapperOfTeam
from synclient.models.list_wrapper_of_team_member import ListWrapperOfTeamMember
from synclient.models.list_wrapper_of_user_profile import ListWrapperOfUserProfile
from synclient.models.long_annotation import LongAnnotation
from synclient.models.member_submission_eligibility import MemberSubmissionEligibility
from synclient.models.membership_invitation import MembershipInvitation
from synclient.models.membership_request import MembershipRequest
from synclient.models.message_to_user import MessageToUser
from synclient.models.message_url import MessageURL
from synclient.models.name_identifier_scheme import NameIdentifierScheme
from synclient.models.object_type import ObjectType
from synclient.models.object_type_schema import ObjectTypeSchema
from synclient.models.paginated_column_models import PaginatedColumnModels
from synclient.models.paginated_ids import PaginatedIds
from synclient.models.paginated_results_of_access_requirement import PaginatedResultsOfAccessRequirement
from synclient.models.paginated_results_of_discussion_reply_bundle import PaginatedResultsOfDiscussionReplyBundle
from synclient.models.paginated_results_of_discussion_thread_bundle import PaginatedResultsOfDiscussionThreadBundle
from synclient.models.paginated_results_of_docker_commit import PaginatedResultsOfDockerCommit
from synclient.models.paginated_results_of_entity_header import PaginatedResultsOfEntityHeader
from synclient.models.paginated_results_of_evaluation import PaginatedResultsOfEvaluation
from synclient.models.paginated_results_of_membership_invitation import PaginatedResultsOfMembershipInvitation
from synclient.models.paginated_results_of_membership_request import PaginatedResultsOfMembershipRequest
from synclient.models.paginated_results_of_submission import PaginatedResultsOfSubmission
from synclient.models.paginated_results_of_submission_bundle import PaginatedResultsOfSubmissionBundle
from synclient.models.paginated_results_of_submission_status import PaginatedResultsOfSubmissionStatus
from synclient.models.paginated_results_of_team import PaginatedResultsOfTeam
from synclient.models.paginated_results_of_team_member import PaginatedResultsOfTeamMember
from synclient.models.paginated_results_of_trashed_entity import PaginatedResultsOfTrashedEntity
from synclient.models.paginated_results_of_user_group import PaginatedResultsOfUserGroup
from synclient.models.paginated_results_of_user_profile import PaginatedResultsOfUserProfile
from synclient.models.paginated_results_of_version_info import PaginatedResultsOfVersionInfo
from synclient.models.paginated_team_ids import PaginatedTeamIds
from synclient.models.passing_record import PassingRecord
from synclient.models.query import Query
from synclient.models.query_bundle_request import QueryBundleRequest
from synclient.models.query_next_page_token import QueryNextPageToken
from synclient.models.query_result import QueryResult
from synclient.models.query_result_bundle import QueryResultBundle
from synclient.models.question import Question
from synclient.models.question_response import QuestionResponse
from synclient.models.reference import Reference
from synclient.models.reference_list import ReferenceList
from synclient.models.reply_count import ReplyCount
from synclient.models.resource_access import ResourceAccess
from synclient.models.response_correctness import ResponseCorrectness
from synclient.models.response_message import ResponseMessage
from synclient.models.restrictable_object_descriptor import RestrictableObjectDescriptor
from synclient.models.restrictable_object_type import RestrictableObjectType
from synclient.models.restriction_information_response import RestrictionInformationResponse
from synclient.models.restriction_level import RestrictionLevel
from synclient.models.row_reference import RowReference
from synclient.models.row_reference_set import RowReferenceSet
from synclient.models.row_set import RowSet
from synclient.models.row_table import RowTable
from synclient.models.select_column import SelectColumn
from synclient.models.settings import Settings
from synclient.models.snapshot_request import SnapshotRequest
from synclient.models.snapshot_response import SnapshotResponse
from synclient.models.sort_by import SortBy
from synclient.models.sort_direction import SortDirection
from synclient.models.sort_item import SortItem
from synclient.models.state_enum import StateEnum
from synclient.models.string_annotation import StringAnnotation
from synclient.models.sts_credentials import StsCredentials
from synclient.models.submission_bundle import SubmissionBundle
from synclient.models.submission_contributor import SubmissionContributor
from synclient.models.submission_eligibility import SubmissionEligibility
from synclient.models.submission_model import SubmissionModel
from synclient.models.submission_quota import SubmissionQuota
from synclient.models.submission_status_batch import SubmissionStatusBatch
from synclient.models.submission_status_enum import SubmissionStatusEnum
from synclient.models.submission_status_form import SubmissionStatusForm
from synclient.models.submission_status_model import SubmissionStatusModel
from synclient.models.sum_file_sizes import SumFileSizes
from synclient.models.table_bundle import TableBundle
from synclient.models.table_file_handle_results import TableFileHandleResults
from synclient.models.table_update_request import TableUpdateRequest
from synclient.models.table_update_response import TableUpdateResponse
from synclient.models.table_update_transaction_request import TableUpdateTransactionRequest
from synclient.models.table_update_transaction_response import TableUpdateTransactionResponse
from synclient.models.team import Team
from synclient.models.team_member import TeamMember
from synclient.models.team_membership_status import TeamMembershipStatus
from synclient.models.team_submission_eligibility import TeamSubmissionEligibility
from synclient.models.trashed_entity import TrashedEntity
from synclient.models.update_thread_message import UpdateThreadMessage
from synclient.models.update_thread_title import UpdateThreadTitle
from synclient.models.used import Used
from synclient.models.user_bundle import UserBundle
from synclient.models.user_entity_permissions import UserEntityPermissions
from synclient.models.user_group import UserGroup
from synclient.models.user_group_header import UserGroupHeader
from synclient.models.user_group_header_response import UserGroupHeaderResponse
from synclient.models.user_group_header_response_page import UserGroupHeaderResponsePage
from synclient.models.user_preference import UserPreference
from synclient.models.user_profile import UserProfile
from synclient.models.validation_exception import ValidationException
from synclient.models.validation_results import ValidationResults
from synclient.models.validation_summary_statistics import ValidationSummaryStatistics
from synclient.models.verification_state import VerificationState
from synclient.models.verification_state_enum import VerificationStateEnum
from synclient.models.verification_submission import VerificationSubmission
from synclient.models.version_info import VersionInfo
from synclient.models.wiki_page_key import WikiPageKey
