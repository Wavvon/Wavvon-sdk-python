"""Contains all the data models used in inputs/outputs"""

from .ack_me_events_body import AckMeEventsBody
from .alliance_info import AllianceInfo
from .app_registration import AppRegistration
from .app_registration_commands_item import AppRegistrationCommandsItem
from .attachment import Attachment
from .attest_recovery_rotation_request_body import AttestRecoveryRotationRequestBody
from .badge_payload import BadgePayload
from .begin_webauthn_assertion_body import BeginWebauthnAssertionBody
from .begin_webauthn_assertion_response_200 import BeginWebauthnAssertionResponse200
from .begin_webauthn_assertion_response_200_options import (
    BeginWebauthnAssertionResponse200Options,
)
from .begin_webauthn_registration_body import BeginWebauthnRegistrationBody
from .begin_webauthn_registration_response_200 import (
    BeginWebauthnRegistrationResponse200,
)
from .begin_webauthn_registration_response_200_options import (
    BeginWebauthnRegistrationResponse200Options,
)
from .bot_channel_scope import BotChannelScope
from .cert_payload import CertPayload
from .cert_payload_standing import CertPayloadStanding
from .certification import Certification
from .challenge_prompt import ChallengePrompt
from .challenge_prompt_mode import ChallengePromptMode
from .channel import Channel
from .conversation import Conversation
from .create_admin_banlist_override_body import CreateAdminBanlistOverrideBody
from .create_admin_banlist_override_body_override_type import (
    CreateAdminBanlistOverrideBodyOverrideType,
)
from .create_admin_banlist_override_response_201 import (
    CreateAdminBanlistOverrideResponse201,
)
from .create_admin_banlist_source_body import CreateAdminBanlistSourceBody
from .create_admin_banlist_source_body_policy import CreateAdminBanlistSourceBodyPolicy
from .create_admin_banlist_source_response_201 import (
    CreateAdminBanlistSourceResponse201,
)
from .create_admin_cert_badge_body import CreateAdminCertBadgeBody
from .create_admin_emoji_body import CreateAdminEmojiBody
from .create_admin_outgoing_webhook_body import CreateAdminOutgoingWebhookBody
from .create_admin_outgoing_webhook_response_201 import (
    CreateAdminOutgoingWebhookResponse201,
)
from .create_admin_webhook_body import CreateAdminWebhookBody
from .create_admin_webhook_response_201 import CreateAdminWebhookResponse201
from .create_alliance_body import CreateAllianceBody
from .create_alliance_channel_body import CreateAllianceChannelBody
from .create_alliance_channel_body_forum_remote_write import (
    CreateAllianceChannelBodyForumRemoteWrite,
)
from .create_alliance_channel_body_voice_remote_join import (
    CreateAllianceChannelBodyVoiceRemoteJoin,
)
from .create_alliance_channel_post_body import CreateAllianceChannelPostBody
from .create_alliance_channel_post_reaction_body import (
    CreateAllianceChannelPostReactionBody,
)
from .create_alliance_channel_post_reply_body import CreateAllianceChannelPostReplyBody
from .create_alliance_push_invite_body import CreateAlliancePushInviteBody
from .create_alliance_voice_grant_body import CreateAllianceVoiceGrantBody
from .create_alliance_voice_grant_response_200 import (
    CreateAllianceVoiceGrantResponse200,
)
from .create_alliance_voice_grant_response_200_grant import (
    CreateAllianceVoiceGrantResponse200Grant,
)
from .create_auth_challenge_body import CreateAuthChallengeBody
from .create_auth_challenge_response_200 import CreateAuthChallengeResponse200
from .create_auth_challenge_response_200_scheme import (
    CreateAuthChallengeResponse200Scheme,
)
from .create_auth_device_token_body import CreateAuthDeviceTokenBody
from .create_auth_device_token_response_200 import CreateAuthDeviceTokenResponse200
from .create_channel_ban_body import CreateChannelBanBody
from .create_channel_body import CreateChannelBody
from .create_channel_message_body import CreateChannelMessageBody
from .create_channel_message_reaction_body import CreateChannelMessageReactionBody
from .create_channel_poll_body import CreateChannelPollBody
from .create_channel_poll_body_options_item import CreateChannelPollBodyOptionsItem
from .create_channel_post_body import CreateChannelPostBody
from .create_channel_post_reaction_body import CreateChannelPostReactionBody
from .create_channel_post_reply_body import CreateChannelPostReplyBody
from .create_channel_post_reply_reaction_body import CreateChannelPostReplyReactionBody
from .create_channel_tag_body import CreateChannelTagBody
from .create_channel_voice_mute_body import CreateChannelVoiceMuteBody
from .create_conversation_body import CreateConversationBody
from .create_conversation_member_body import CreateConversationMemberBody
from .create_conversation_message_body import CreateConversationMessageBody
from .create_conversation_message_body_plaintext_signer_cert import (
    CreateConversationMessageBodyPlaintextSignerCert,
)
from .create_event_body import CreateEventBody
from .create_event_slot_body import CreateEventSlotBody
from .create_event_slot_response_201 import CreateEventSlotResponse201
from .create_event_squad_room_body import CreateEventSquadRoomBody
from .create_federation_badge_offer_body import CreateFederationBadgeOfferBody
from .create_federation_dm_member_change_body import CreateFederationDmMemberChangeBody
from .create_federation_dm_member_change_body_signer_cert import (
    CreateFederationDmMemberChangeBodySignerCert,
)
from .create_federation_forum_channel_post_body import (
    CreateFederationForumChannelPostBody,
)
from .create_federation_forum_channel_post_reaction_body import (
    CreateFederationForumChannelPostReactionBody,
)
from .create_federation_forum_channel_post_reply_body import (
    CreateFederationForumChannelPostReplyBody,
)
from .create_friend_body import CreateFriendBody
from .create_invite_body import CreateInviteBody
from .create_moderation_ban_body import CreateModerationBanBody
from .create_moderation_ban_response_201 import CreateModerationBanResponse201
from .create_role_body import CreateRoleBody
from .create_role_category_body import CreateRoleCategoryBody
from .create_soundboard_sound_body import CreateSoundboardSoundBody
from .create_soundboard_sound_response_201 import CreateSoundboardSoundResponse201
from .delete_admin_banlist_sources_body import DeleteAdminBanlistSourcesBody
from .delete_federation_forum_channel_post_body import (
    DeleteFederationForumChannelPostBody,
)
from .delete_federation_forum_channel_post_reply_body import (
    DeleteFederationForumChannelPostReplyBody,
)
from .dm_message import DmMessage
from .error import Error
from .execute_webhook_body import ExecuteWebhookBody
from .execute_webhook_body_embeds import ExecuteWebhookBodyEmbeds
from .execute_webhook_response_200 import ExecuteWebhookResponse200
from .explain_user_permissions_response_200 import ExplainUserPermissionsResponse200
from .explain_user_permissions_response_200_sources_item import (
    ExplainUserPermissionsResponse200SourcesItem,
)
from .explain_user_permissions_response_200_sources_item_kind import (
    ExplainUserPermissionsResponse200SourcesItemKind,
)
from .federation_join_alliance_body import FederationJoinAllianceBody
from .federation_join_alliance_response_200 import FederationJoinAllianceResponse200
from .finish_webauthn_assertion_body import FinishWebauthnAssertionBody
from .finish_webauthn_assertion_body_credential import (
    FinishWebauthnAssertionBodyCredential,
)
from .finish_webauthn_assertion_response_200 import FinishWebauthnAssertionResponse200
from .finish_webauthn_registration_body import FinishWebauthnRegistrationBody
from .finish_webauthn_registration_body_credential import (
    FinishWebauthnRegistrationBodyCredential,
)
from .finish_webauthn_registration_response_200 import (
    FinishWebauthnRegistrationResponse200,
)
from .forum_tag import ForumTag
from .get_admin_settings_banlist_response_200 import GetAdminSettingsBanlistResponse200
from .get_admin_settings_banlist_response_200_sources_item import (
    GetAdminSettingsBanlistResponse200SourcesItem,
)
from .get_admin_settings_pow_response_200 import GetAdminSettingsPowResponse200
from .get_admin_settings_tags_response_200 import GetAdminSettingsTagsResponse200
from .get_channel_my_permissions_response_200 import GetChannelMyPermissionsResponse200
from .get_federation_banlist_response_200 import GetFederationBanlistResponse200
from .get_federation_banlist_response_200_payload import (
    GetFederationBanlistResponse200Payload,
)
from .get_federation_banlist_response_200_payload_entries_item import (
    GetFederationBanlistResponse200PayloadEntriesItem,
)
from .get_federation_listing_response_200 import GetFederationListingResponse200
from .get_health_response_200 import GetHealthResponse200
from .get_join_invite_response_200 import GetJoinInviteResponse200
from .get_moderation_history_response_200 import GetModerationHistoryResponse200
from .get_moderation_history_response_200_entries_item import (
    GetModerationHistoryResponse200EntriesItem,
)
from .get_moderation_history_response_200_entries_item_policy import (
    GetModerationHistoryResponse200EntriesItemPolicy,
)
from .get_poll_response_200 import GetPollResponse200
from .get_poll_response_200_totals import GetPollResponse200Totals
from .get_preview_response_200 import GetPreviewResponse200
from .get_recovery_rotation_request_response_200 import (
    GetRecoveryRotationRequestResponse200,
)
from .get_recovery_rotation_request_response_200_status import (
    GetRecoveryRotationRequestResponse200Status,
)
from .get_user_profile_response_200 import GetUserProfileResponse200
from .get_user_profile_response_200_badges_item import (
    GetUserProfileResponse200BadgesItem,
)
from .get_user_profile_response_200_roles_item import GetUserProfileResponse200RolesItem
from .hub_info import HubInfo
from .hub_info_challenge_mode import HubInfoChallengeMode
from .invite import Invite
from .invite_status import InviteStatus
from .issue_admin_badge_body import IssueAdminBadgeBody
from .issue_admin_badge_response_201 import IssueAdminBadgeResponse201
from .leave_voice_body import LeaveVoiceBody
from .list_admin_audit_log_response_200 import ListAdminAuditLogResponse200
from .list_admin_audit_log_response_200_entries_item import (
    ListAdminAuditLogResponse200EntriesItem,
)
from .list_admin_audit_log_response_200_entries_item_payload import (
    ListAdminAuditLogResponse200EntriesItemPayload,
)
from .list_admin_banlist_entries_response_200_item import (
    ListAdminBanlistEntriesResponse200Item,
)
from .list_admin_banlist_overrides_response_200_item import (
    ListAdminBanlistOverridesResponse200Item,
)
from .list_admin_banlist_overrides_response_200_item_override_type import (
    ListAdminBanlistOverridesResponse200ItemOverrideType,
)
from .list_admin_banlist_sources_response_200_item import (
    ListAdminBanlistSourcesResponse200Item,
)
from .list_admin_banlist_sources_response_200_item_policy import (
    ListAdminBanlistSourcesResponse200ItemPolicy,
)
from .list_admin_certs_response_200_item import ListAdminCertsResponse200Item
from .list_admin_certs_response_200_item_standing import (
    ListAdminCertsResponse200ItemStanding,
)
from .list_admin_outgoing_webhook_deliveries_response_200_item import (
    ListAdminOutgoingWebhookDeliveriesResponse200Item,
)
from .list_admin_outgoing_webhook_subscriptions_response_200 import (
    ListAdminOutgoingWebhookSubscriptionsResponse200,
)
from .list_admin_outgoing_webhook_subscriptions_response_200_subscriptions_item import (
    ListAdminOutgoingWebhookSubscriptionsResponse200SubscriptionsItem,
)
from .list_admin_outgoing_webhooks_response_200_item import (
    ListAdminOutgoingWebhooksResponse200Item,
)
from .list_admin_recovery_pending_response_200_item import (
    ListAdminRecoveryPendingResponse200Item,
)
from .list_admin_reports_response_200_item import ListAdminReportsResponse200Item
from .list_admin_reports_status import ListAdminReportsStatus
from .list_admin_settings_certs_response_200 import ListAdminSettingsCertsResponse200
from .list_admin_settings_certs_response_200_cert_issuer_urls import (
    ListAdminSettingsCertsResponse200CertIssuerUrls,
)
from .list_admin_settings_certs_response_200_cert_mode import (
    ListAdminSettingsCertsResponse200CertMode,
)
from .list_alliance_channel_posts_response_200 import (
    ListAllianceChannelPostsResponse200,
)
from .list_alliance_managers_response_200_item import (
    ListAllianceManagersResponse200Item,
)
from .list_alliance_people_response_200_item import ListAlliancePeopleResponse200Item
from .list_apps_response_200_item import ListAppsResponse200Item
from .list_apps_response_200_item_commands_item import (
    ListAppsResponse200ItemCommandsItem,
)
from .list_apps_response_200_item_game import ListAppsResponse200ItemGame
from .list_badges_response_200_item import ListBadgesResponse200Item
from .list_certs_revocations_response_200_item import (
    ListCertsRevocationsResponse200Item,
)
from .list_channel_bans_response_200_item import ListChannelBansResponse200Item
from .list_channel_permissions_response_200 import ListChannelPermissionsResponse200
from .list_channel_permissions_response_200_roles_item import (
    ListChannelPermissionsResponse200RolesItem,
)
from .list_channel_permissions_response_200_roles_item_overwrites import (
    ListChannelPermissionsResponse200RolesItemOverwrites,
)
from .list_channel_pins_response_200_item import ListChannelPinsResponse200Item
from .list_channel_pins_response_200_item_message import (
    ListChannelPinsResponse200ItemMessage,
)
from .list_channel_polls_response_200_item import ListChannelPollsResponse200Item
from .list_channel_polls_response_200_item_totals import (
    ListChannelPollsResponse200ItemTotals,
)
from .list_channel_posts_response_200 import ListChannelPostsResponse200
from .list_channel_voice_mutes_response_200_item import (
    ListChannelVoiceMutesResponse200Item,
)
from .list_conversation_sender_keys_response_200_item import (
    ListConversationSenderKeysResponse200Item,
)
from .list_emojis_response_200_item import ListEmojisResponse200Item
from .list_event_assignments_response_200_item import (
    ListEventAssignmentsResponse200Item,
)
from .list_event_rsvps_response_200_item import ListEventRsvpsResponse200Item
from .list_events_response_200_item import ListEventsResponse200Item
from .list_events_response_200_item_my_rsvp import ListEventsResponse200ItemMyRsvp
from .list_events_response_200_item_rsvp_counts import (
    ListEventsResponse200ItemRsvpCounts,
)
from .list_federation_badge_revocations_response_200_item import (
    ListFederationBadgeRevocationsResponse200Item,
)
from .list_identity_dm_blocks_response_200 import ListIdentityDmBlocksResponse200
from .list_me_credentials_response_200_item import ListMeCredentialsResponse200Item
from .list_me_devices_response_200_item import ListMeDevicesResponse200Item
from .list_me_events_response_200 import ListMeEventsResponse200
from .list_me_events_response_200_events_item import ListMeEventsResponse200EventsItem
from .list_pending_badges_response_200_item import ListPendingBadgesResponse200Item
from .list_permissions_response_200 import ListPermissionsResponse200
from .list_permissions_response_200_permissions_item import (
    ListPermissionsResponse200PermissionsItem,
)
from .list_permissions_response_200_permissions_item_scope import (
    ListPermissionsResponse200PermissionsItemScope,
)
from .list_recovery_contacts_response_200 import ListRecoveryContactsResponse200
from .list_recovery_contacts_response_200_contacts_item import (
    ListRecoveryContactsResponse200ContactsItem,
)
from .list_recovery_requests_response_200_item import (
    ListRecoveryRequestsResponse200Item,
)
from .list_soundboard_sounds_response_200_item import (
    ListSoundboardSoundsResponse200Item,
)
from .list_unread_channels_response_200_item import ListUnreadChannelsResponse200Item
from .lobby_status import LobbyStatus
from .lobby_status_status import LobbyStatusStatus
from .mark_soundboard_sound_played_body import MarkSoundboardSoundPlayedBody
from .me_info import MeInfo
from .me_info_approval_status import MeInfoApprovalStatus
from .message import Message
from .post_detail import PostDetail
from .post_summary import PostSummary
from .raise_channel_hand_response_201 import RaiseChannelHandResponse201
from .reaction import Reaction
from .redeem_auth_device_token_body import RedeemAuthDeviceTokenBody
from .redeem_auth_device_token_response_200 import RedeemAuthDeviceTokenResponse200
from .reindex_admin_search_response_202 import ReindexAdminSearchResponse202
from .reindex_admin_search_response_202_status import (
    ReindexAdminSearchResponse202Status,
)
from .reply_context import ReplyContext
from .reply_view import ReplyView
from .report_message_body import ReportMessageBody
from .review_admin_report_body import ReviewAdminReportBody
from .review_admin_report_body_action import ReviewAdminReportBodyAction
from .role import Role
from .role_category import RoleCategory
from .rotate_admin_outgoing_webhook_secret_response_200 import (
    RotateAdminOutgoingWebhookSecretResponse200,
)
from .rotate_recovery_key_body import RotateRecoveryKeyBody
from .rotate_recovery_key_body_attestations_item import (
    RotateRecoveryKeyBodyAttestationsItem,
)
from .rotate_recovery_key_response_201 import RotateRecoveryKeyResponse201
from .rotate_recovery_key_response_201_status import RotateRecoveryKeyResponse201Status
from .rsvp_event_body import RsvpEventBody
from .rsvp_event_body_status import RsvpEventBodyStatus
from .search_channel_posts_response_200 import SearchChannelPostsResponse200
from .search_channel_posts_response_200_results_item import (
    SearchChannelPostsResponse200ResultsItem,
)
from .search_response_200_item import SearchResponse200Item
from .set_admin_outgoing_webhook_subscriptions_body import (
    SetAdminOutgoingWebhookSubscriptionsBody,
)
from .set_admin_outgoing_webhook_subscriptions_body_subscriptions_item import (
    SetAdminOutgoingWebhookSubscriptionsBodySubscriptionsItem,
)
from .set_admin_outgoing_webhook_subscriptions_response_200 import (
    SetAdminOutgoingWebhookSubscriptionsResponse200,
)
from .set_alliance_people_visibility_body import SetAlliancePeopleVisibilityBody
from .set_channel_permission_body import SetChannelPermissionBody
from .set_conversation_sender_keys_body import SetConversationSenderKeysBody
from .set_conversation_sender_keys_body_recipients_item import (
    SetConversationSenderKeysBodyRecipientsItem,
)
from .set_conversation_sender_keys_body_signer_cert import (
    SetConversationSenderKeysBodySignerCert,
)
from .set_event_body import SetEventBody
from .set_hub_settings_challenge_body import SetHubSettingsChallengeBody
from .set_hub_settings_challenge_body_challenge_mode import (
    SetHubSettingsChallengeBodyChallengeMode,
)
from .set_hub_settings_lobby_body import SetHubSettingsLobbyBody
from .set_identity_dm_blocks_body import SetIdentityDmBlocksBody
from .set_me_app_commands_body import SetMeAppCommandsBody
from .set_me_app_commands_body_commands_item import SetMeAppCommandsBodyCommandsItem
from .set_me_app_commands_body_commands_item_scope import (
    SetMeAppCommandsBodyCommandsItemScope,
)
from .set_me_app_profile_body import SetMeAppProfileBody
from .set_me_app_profile_body_game import SetMeAppProfileBodyGame
from .set_me_app_subscriptions_body import SetMeAppSubscriptionsBody
from .set_me_app_subscriptions_body_subscriptions_item import (
    SetMeAppSubscriptionsBodySubscriptionsItem,
)
from .set_me_app_subscriptions_response_200 import SetMeAppSubscriptionsResponse200
from .set_recovery_contacts_body import SetRecoveryContactsBody
from .signed_member_change import SignedMemberChange
from .signed_member_change_signer_cert import SignedMemberChangeSignerCert
from .start_screenshare_body import StartScreenshareBody
from .start_screenshare_response_200 import StartScreenshareResponse200
from .stop_screenshare_body import StopScreenshareBody
from .submit_lobby_pow_body import SubmitLobbyPowBody
from .update_admin_banlist_sources_body import UpdateAdminBanlistSourcesBody
from .update_admin_banlist_sources_body_policy import (
    UpdateAdminBanlistSourcesBodyPolicy,
)
from .update_admin_outgoing_webhook_body import UpdateAdminOutgoingWebhookBody
from .update_admin_settings_banlist_body import UpdateAdminSettingsBanlistBody
from .update_admin_settings_certs_body import UpdateAdminSettingsCertsBody
from .update_admin_settings_certs_body_cert_issuer_urls import (
    UpdateAdminSettingsCertsBodyCertIssuerUrls,
)
from .update_admin_settings_certs_body_cert_mode import (
    UpdateAdminSettingsCertsBodyCertMode,
)
from .update_admin_settings_certs_body_cert_require import (
    UpdateAdminSettingsCertsBodyCertRequire,
)
from .update_admin_settings_listing_body import UpdateAdminSettingsListingBody
from .update_admin_settings_moderation_body import UpdateAdminSettingsModerationBody
from .update_admin_settings_pow_body import UpdateAdminSettingsPowBody
from .update_admin_settings_tags_body import UpdateAdminSettingsTagsBody
from .update_channel_message_body import UpdateChannelMessageBody
from .update_channel_post_body import UpdateChannelPostBody
from .update_channel_post_reply_body import UpdateChannelPostReplyBody
from .update_event_slot_body import UpdateEventSlotBody
from .update_event_slot_response_200 import UpdateEventSlotResponse200
from .update_hub_body import UpdateHubBody
from .update_me_body import UpdateMeBody
from .update_me_credential_body import UpdateMeCredentialBody
from .update_role_category_body import UpdateRoleCategoryBody
from .update_tag_body import UpdateTagBody
from .upload_channel_file_body import UploadChannelFileBody
from .upload_channel_file_response_201 import UploadChannelFileResponse201
from .user import User
from .verify_auth_body import VerifyAuthBody
from .verify_auth_body_alliance_voice_grant import VerifyAuthBodyAllianceVoiceGrant
from .verify_auth_body_alliance_voice_grant_payload import (
    VerifyAuthBodyAllianceVoiceGrantPayload,
)
from .verify_auth_body_subkey_cert import VerifyAuthBodySubkeyCert
from .verify_auth_response_200 import VerifyAuthResponse200
from .verify_auth_response_200_scope import VerifyAuthResponse200Scope
from .verify_challenge_body import VerifyChallengeBody
from .vote_poll_body import VotePollBody

__all__ = (
    "AckMeEventsBody",
    "AllianceInfo",
    "AppRegistration",
    "AppRegistrationCommandsItem",
    "Attachment",
    "AttestRecoveryRotationRequestBody",
    "BadgePayload",
    "BeginWebauthnAssertionBody",
    "BeginWebauthnAssertionResponse200",
    "BeginWebauthnAssertionResponse200Options",
    "BeginWebauthnRegistrationBody",
    "BeginWebauthnRegistrationResponse200",
    "BeginWebauthnRegistrationResponse200Options",
    "BotChannelScope",
    "CertPayload",
    "CertPayloadStanding",
    "Certification",
    "ChallengePrompt",
    "ChallengePromptMode",
    "Channel",
    "Conversation",
    "CreateAdminBanlistOverrideBody",
    "CreateAdminBanlistOverrideBodyOverrideType",
    "CreateAdminBanlistOverrideResponse201",
    "CreateAdminBanlistSourceBody",
    "CreateAdminBanlistSourceBodyPolicy",
    "CreateAdminBanlistSourceResponse201",
    "CreateAdminCertBadgeBody",
    "CreateAdminEmojiBody",
    "CreateAdminOutgoingWebhookBody",
    "CreateAdminOutgoingWebhookResponse201",
    "CreateAdminWebhookBody",
    "CreateAdminWebhookResponse201",
    "CreateAllianceBody",
    "CreateAllianceChannelBody",
    "CreateAllianceChannelBodyForumRemoteWrite",
    "CreateAllianceChannelBodyVoiceRemoteJoin",
    "CreateAllianceChannelPostBody",
    "CreateAllianceChannelPostReactionBody",
    "CreateAllianceChannelPostReplyBody",
    "CreateAlliancePushInviteBody",
    "CreateAllianceVoiceGrantBody",
    "CreateAllianceVoiceGrantResponse200",
    "CreateAllianceVoiceGrantResponse200Grant",
    "CreateAuthChallengeBody",
    "CreateAuthChallengeResponse200",
    "CreateAuthChallengeResponse200Scheme",
    "CreateAuthDeviceTokenBody",
    "CreateAuthDeviceTokenResponse200",
    "CreateChannelBanBody",
    "CreateChannelBody",
    "CreateChannelMessageBody",
    "CreateChannelMessageReactionBody",
    "CreateChannelPollBody",
    "CreateChannelPollBodyOptionsItem",
    "CreateChannelPostBody",
    "CreateChannelPostReactionBody",
    "CreateChannelPostReplyBody",
    "CreateChannelPostReplyReactionBody",
    "CreateChannelTagBody",
    "CreateChannelVoiceMuteBody",
    "CreateConversationBody",
    "CreateConversationMemberBody",
    "CreateConversationMessageBody",
    "CreateConversationMessageBodyPlaintextSignerCert",
    "CreateEventBody",
    "CreateEventSlotBody",
    "CreateEventSlotResponse201",
    "CreateEventSquadRoomBody",
    "CreateFederationBadgeOfferBody",
    "CreateFederationDmMemberChangeBody",
    "CreateFederationDmMemberChangeBodySignerCert",
    "CreateFederationForumChannelPostBody",
    "CreateFederationForumChannelPostReactionBody",
    "CreateFederationForumChannelPostReplyBody",
    "CreateFriendBody",
    "CreateInviteBody",
    "CreateModerationBanBody",
    "CreateModerationBanResponse201",
    "CreateRoleBody",
    "CreateRoleCategoryBody",
    "CreateSoundboardSoundBody",
    "CreateSoundboardSoundResponse201",
    "DeleteAdminBanlistSourcesBody",
    "DeleteFederationForumChannelPostBody",
    "DeleteFederationForumChannelPostReplyBody",
    "DmMessage",
    "Error",
    "ExecuteWebhookBody",
    "ExecuteWebhookBodyEmbeds",
    "ExecuteWebhookResponse200",
    "ExplainUserPermissionsResponse200",
    "ExplainUserPermissionsResponse200SourcesItem",
    "ExplainUserPermissionsResponse200SourcesItemKind",
    "FederationJoinAllianceBody",
    "FederationJoinAllianceResponse200",
    "FinishWebauthnAssertionBody",
    "FinishWebauthnAssertionBodyCredential",
    "FinishWebauthnAssertionResponse200",
    "FinishWebauthnRegistrationBody",
    "FinishWebauthnRegistrationBodyCredential",
    "FinishWebauthnRegistrationResponse200",
    "ForumTag",
    "GetAdminSettingsBanlistResponse200",
    "GetAdminSettingsBanlistResponse200SourcesItem",
    "GetAdminSettingsPowResponse200",
    "GetAdminSettingsTagsResponse200",
    "GetChannelMyPermissionsResponse200",
    "GetFederationBanlistResponse200",
    "GetFederationBanlistResponse200Payload",
    "GetFederationBanlistResponse200PayloadEntriesItem",
    "GetFederationListingResponse200",
    "GetHealthResponse200",
    "GetJoinInviteResponse200",
    "GetModerationHistoryResponse200",
    "GetModerationHistoryResponse200EntriesItem",
    "GetModerationHistoryResponse200EntriesItemPolicy",
    "GetPollResponse200",
    "GetPollResponse200Totals",
    "GetPreviewResponse200",
    "GetRecoveryRotationRequestResponse200",
    "GetRecoveryRotationRequestResponse200Status",
    "GetUserProfileResponse200",
    "GetUserProfileResponse200BadgesItem",
    "GetUserProfileResponse200RolesItem",
    "HubInfo",
    "HubInfoChallengeMode",
    "Invite",
    "InviteStatus",
    "IssueAdminBadgeBody",
    "IssueAdminBadgeResponse201",
    "LeaveVoiceBody",
    "ListAdminAuditLogResponse200",
    "ListAdminAuditLogResponse200EntriesItem",
    "ListAdminAuditLogResponse200EntriesItemPayload",
    "ListAdminBanlistEntriesResponse200Item",
    "ListAdminBanlistOverridesResponse200Item",
    "ListAdminBanlistOverridesResponse200ItemOverrideType",
    "ListAdminBanlistSourcesResponse200Item",
    "ListAdminBanlistSourcesResponse200ItemPolicy",
    "ListAdminCertsResponse200Item",
    "ListAdminCertsResponse200ItemStanding",
    "ListAdminOutgoingWebhookDeliveriesResponse200Item",
    "ListAdminOutgoingWebhookSubscriptionsResponse200",
    "ListAdminOutgoingWebhookSubscriptionsResponse200SubscriptionsItem",
    "ListAdminOutgoingWebhooksResponse200Item",
    "ListAdminRecoveryPendingResponse200Item",
    "ListAdminReportsResponse200Item",
    "ListAdminReportsStatus",
    "ListAdminSettingsCertsResponse200",
    "ListAdminSettingsCertsResponse200CertIssuerUrls",
    "ListAdminSettingsCertsResponse200CertMode",
    "ListAllianceChannelPostsResponse200",
    "ListAllianceManagersResponse200Item",
    "ListAlliancePeopleResponse200Item",
    "ListAppsResponse200Item",
    "ListAppsResponse200ItemCommandsItem",
    "ListAppsResponse200ItemGame",
    "ListBadgesResponse200Item",
    "ListCertsRevocationsResponse200Item",
    "ListChannelBansResponse200Item",
    "ListChannelPermissionsResponse200",
    "ListChannelPermissionsResponse200RolesItem",
    "ListChannelPermissionsResponse200RolesItemOverwrites",
    "ListChannelPinsResponse200Item",
    "ListChannelPinsResponse200ItemMessage",
    "ListChannelPollsResponse200Item",
    "ListChannelPollsResponse200ItemTotals",
    "ListChannelPostsResponse200",
    "ListChannelVoiceMutesResponse200Item",
    "ListConversationSenderKeysResponse200Item",
    "ListEmojisResponse200Item",
    "ListEventAssignmentsResponse200Item",
    "ListEventRsvpsResponse200Item",
    "ListEventsResponse200Item",
    "ListEventsResponse200ItemMyRsvp",
    "ListEventsResponse200ItemRsvpCounts",
    "ListFederationBadgeRevocationsResponse200Item",
    "ListIdentityDmBlocksResponse200",
    "ListMeCredentialsResponse200Item",
    "ListMeDevicesResponse200Item",
    "ListMeEventsResponse200",
    "ListMeEventsResponse200EventsItem",
    "ListPendingBadgesResponse200Item",
    "ListPermissionsResponse200",
    "ListPermissionsResponse200PermissionsItem",
    "ListPermissionsResponse200PermissionsItemScope",
    "ListRecoveryContactsResponse200",
    "ListRecoveryContactsResponse200ContactsItem",
    "ListRecoveryRequestsResponse200Item",
    "ListSoundboardSoundsResponse200Item",
    "ListUnreadChannelsResponse200Item",
    "LobbyStatus",
    "LobbyStatusStatus",
    "MarkSoundboardSoundPlayedBody",
    "MeInfo",
    "MeInfoApprovalStatus",
    "Message",
    "PostDetail",
    "PostSummary",
    "RaiseChannelHandResponse201",
    "Reaction",
    "RedeemAuthDeviceTokenBody",
    "RedeemAuthDeviceTokenResponse200",
    "ReindexAdminSearchResponse202",
    "ReindexAdminSearchResponse202Status",
    "ReplyContext",
    "ReplyView",
    "ReportMessageBody",
    "ReviewAdminReportBody",
    "ReviewAdminReportBodyAction",
    "Role",
    "RoleCategory",
    "RotateAdminOutgoingWebhookSecretResponse200",
    "RotateRecoveryKeyBody",
    "RotateRecoveryKeyBodyAttestationsItem",
    "RotateRecoveryKeyResponse201",
    "RotateRecoveryKeyResponse201Status",
    "RsvpEventBody",
    "RsvpEventBodyStatus",
    "SearchChannelPostsResponse200",
    "SearchChannelPostsResponse200ResultsItem",
    "SearchResponse200Item",
    "SetAdminOutgoingWebhookSubscriptionsBody",
    "SetAdminOutgoingWebhookSubscriptionsBodySubscriptionsItem",
    "SetAdminOutgoingWebhookSubscriptionsResponse200",
    "SetAlliancePeopleVisibilityBody",
    "SetChannelPermissionBody",
    "SetConversationSenderKeysBody",
    "SetConversationSenderKeysBodyRecipientsItem",
    "SetConversationSenderKeysBodySignerCert",
    "SetEventBody",
    "SetHubSettingsChallengeBody",
    "SetHubSettingsChallengeBodyChallengeMode",
    "SetHubSettingsLobbyBody",
    "SetIdentityDmBlocksBody",
    "SetMeAppCommandsBody",
    "SetMeAppCommandsBodyCommandsItem",
    "SetMeAppCommandsBodyCommandsItemScope",
    "SetMeAppProfileBody",
    "SetMeAppProfileBodyGame",
    "SetMeAppSubscriptionsBody",
    "SetMeAppSubscriptionsBodySubscriptionsItem",
    "SetMeAppSubscriptionsResponse200",
    "SetRecoveryContactsBody",
    "SignedMemberChange",
    "SignedMemberChangeSignerCert",
    "StartScreenshareBody",
    "StartScreenshareResponse200",
    "StopScreenshareBody",
    "SubmitLobbyPowBody",
    "UpdateAdminBanlistSourcesBody",
    "UpdateAdminBanlistSourcesBodyPolicy",
    "UpdateAdminOutgoingWebhookBody",
    "UpdateAdminSettingsBanlistBody",
    "UpdateAdminSettingsCertsBody",
    "UpdateAdminSettingsCertsBodyCertIssuerUrls",
    "UpdateAdminSettingsCertsBodyCertMode",
    "UpdateAdminSettingsCertsBodyCertRequire",
    "UpdateAdminSettingsListingBody",
    "UpdateAdminSettingsModerationBody",
    "UpdateAdminSettingsPowBody",
    "UpdateAdminSettingsTagsBody",
    "UpdateChannelMessageBody",
    "UpdateChannelPostBody",
    "UpdateChannelPostReplyBody",
    "UpdateEventSlotBody",
    "UpdateEventSlotResponse200",
    "UpdateHubBody",
    "UpdateMeBody",
    "UpdateMeCredentialBody",
    "UpdateRoleCategoryBody",
    "UpdateTagBody",
    "UploadChannelFileBody",
    "UploadChannelFileResponse201",
    "User",
    "VerifyAuthBody",
    "VerifyAuthBodyAllianceVoiceGrant",
    "VerifyAuthBodyAllianceVoiceGrantPayload",
    "VerifyAuthBodySubkeyCert",
    "VerifyAuthResponse200",
    "VerifyAuthResponse200Scope",
    "VerifyChallengeBody",
    "VotePollBody",
)
