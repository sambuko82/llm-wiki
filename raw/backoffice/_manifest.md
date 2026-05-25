---
type: source
title: Backoffice MySQL — Inventory & Extraction Manifest
last_updated: 2026-05-25
sources: [backoffice-mysql]
---

# Backoffice MySQL Inventory

- **DB:** `u1805424_jvto_clone` @ MariaDB 10.11 (Hostinger)
- **Snapshot:** 2026-05-25
- **Total tables:** 210
- **Total rows:** 63,001

## Bucket summary

| Bucket | Count | Treatment |
|---|---|---|
| business | 160 | Full extract → dumps/ + csv/ + wiki summary |
| sensitive | 40 | Full extract local; wiki = aggregate only; customer slice May 2026+ |
| framework | 10 | Skip (Laravel internals) |

## Domain breakdown (business + sensitive)

| Domain | Tables | Rows |
|---|---|---|
| bookings | 27 | 25,162 |
| finance | 21 | 1,962 |
| hotels | 11 | 907 |
| media | 7 | 274 |
| misc | 68 | 11,298 |
| people | 16 | 4,487 |
| products | 28 | 4,970 |
| reviews | 2 | 118 |
| vehicles | 7 | 58 |
| vendors | 2 | 16 |
| whatsapp | 11 | 12,806 |

## Top tables by row count

| Table | Rows | Size KB | Bucket | Domain |
|---|---:|---:|---|---|
| `wa_chats` | 5,547 | 1552 | business | whatsapp |
| `tw_calculation_details` | 5,317 | 1552 | business | misc |
| `book_destination_activities` | 4,294 | 368 | sensitive | bookings |
| `wa_logs` | 3,608 | 2576 | business | whatsapp |
| `booking_itineraries` | 3,595 | 1552 | sensitive | bookings |
| `users` | 3,568 | 1552 | sensitive | people |
| `book_room_hotels` | 3,150 | 256 | sensitive | bookings |
| `wa_itineraries` | 2,985 | 1552 | business | whatsapp |
| `book_others_activities` | 2,577 | 208 | sensitive | bookings |
| `book_hotels` | 2,487 | 192 | sensitive | bookings |
| `availabilities` | 2,400 | 480 | business | misc |
| `book_guide_drivers` | 2,105 | 160 | sensitive | bookings |
| `bookings` | 1,453 | 1552 | sensitive | bookings |
| `booking_details` | 1,451 | 208 | sensitive | bookings |
| `package_include_excludes` | 1,093 | 80 | business | products |
| `book_cars` | 1,065 | 96 | sensitive | bookings |
| `invoice_histories` | 1,002 | 160 | sensitive | finance |
| `user_logs` | 655 | 144 | business | people |
| `book_hotel_meals` | 643 | 80 | sensitive | bookings |
| `wa_chat_summaries` | 640 | 192 | business | whatsapp |
| `package_banners` | 626 | 48 | business | products |
| `discounts` | 623 | 80 | business | misc |
| `migrations` | 567 | 64 | framework | misc |
| `book_car_activities` | 564 | 64 | sensitive | bookings |
| `package_prices` | 556 | 64 | business | products |
| `booking_documents` | 530 | 64 | sensitive | bookings |
| `itinerary_details` | 512 | 96 | business | products |
| `book_crew_activities` | 509 | 64 | sensitive | bookings |
| `booking_payments` | 506 | 80 | sensitive | finance |
| `itineraries` | 368 | 400 | business | products |
| `package_hotels` | 367 | 48 | business | hotels |
| `add_on_packages` | 365 | 48 | business | products |
| `personal_access_tokens` | 364 | 80 | framework | misc |
| `itinerary_meals` | 363 | 48 | business | products |
| `package_destinations` | 358 | 48 | business | products |
| `galleries` | 352 | 96 | business | misc |
| `tw_calculations` | 295 | 48 | business | misc |
| `room_hotels` | 263 | 48 | business | hotels |
| `itinerary_destinations` | 252 | 16 | business | products |
| `book_itineraries` | 249 | 48 | sensitive | bookings |

## All business tables

| Table | Rows | Domain |
|---|---:|---|
| `accommodation_categories` | 4 | hotels |
| `accommodations` | 0 | hotels |
| `accounts` | 3 | finance |
| `activities` | 18 | misc |
| `activity_categories` | 7 | products |
| `activity_destination_medias` | 0 | products |
| `activity_destinations` | 0 | products |
| `activity_ends` | 14 | products |
| `activity_starts` | 19 | products |
| `add_on_carts` | 0 | vehicles |
| `add_on_packages` | 365 | products |
| `add_ons` | 160 | misc |
| `agents` | 7 | people |
| `announcements` | 0 | misc |
| `areas` | 12 | misc |
| `article_media` | 0 | media |
| `articles` | 3 | misc |
| `attachment_types` | 7 | media |
| `availabilities` | 2,400 | misc |
| `blogs` | 0 | misc |
| `calculation_detail_others` | 80 | misc |
| `calculation_details` | 169 | misc |
| `calculations` | 27 | misc |
| `car_activities` | 0 | vehicles |
| `car_configurations` | 24 | vehicles |
| `cars` | 27 | vehicles |
| `carts` | 4 | vehicles |
| `categories` | 4 | misc |
| `component_contents` | 0 | misc |
| `components` | 0 | misc |
| `countries` | 244 | misc |
| `crew_reviews` | 0 | people |
| `crew_roles` | 14 | people |
| `currency_exchange` | 0 | misc |
| `destination_activities` | 53 | products |
| `destination_details` | 6 | products |
| `destinations` | 38 | products |
| `discounts` | 623 | misc |
| `document_finders` | 20 | media |
| `durations` | 9 | misc |
| `email_accounts` | 0 | finance |
| `email_providers` | 0 | misc |
| `event_sequences` | 0 | misc |
| `expense_additionals` | 55 | finance |
| `expense_refunds` | 70 | finance |
| `expense_revisions` | 20 | finance |
| `experiences` | 0 | misc |
| `extra_luggages` | 9 | misc |
| `faq_categories` | 12 | misc |
| `faq_subcategories` | 28 | misc |
| `faqs` | 63 | misc |
| `fcm_tokens` | 3 | misc |
| `file_tags` | 0 | media |
| `file_types` | 8 | media |
| `files` | 223 | media |
| `flipbooks` | 5 | bookings |
| `folder_types` | 12 | misc |
| `folders` | 105 | misc |
| `galleries` | 352 | misc |
| `garages` | 1 | misc |
| `gift_cards` | 3 | vehicles |
| `google_bills` | 0 | misc |
| `group_user` | 0 | people |
| `guide_drivers` | 74 | people |
| `hotel_images` | 18 | hotels |
| `hotel_services` | 6 | hotels |
| `hotels` | 67 | hotels |
| `identities_types` | 0 | misc |
| `image_panoramas` | 16 | media |
| `include_excludes` | 58 | misc |
| `item_activities` | 0 | misc |
| `item_activity_categories` | 0 | products |
| `item_calculation_others` | 27 | misc |
| `item_calculations` | 91 | misc |
| `itineraries` | 368 | products |
| `itinerary_destinations` | 252 | products |
| `itinerary_details` | 512 | products |
| `itinerary_invoices` | 86 | finance |
| `itinerary_meals` | 363 | products |
| `itinerary_route_destinations` | 0 | products |
| `itinerary_route_details` | 0 | products |
| `itinerary_routes` | 0 | products |
| `jvto_review_crews` | 111 | people |
| `jvto_reviews` | 118 | reviews |
| `links` | 142 | misc |
| `locations` | 20 | misc |
| `mice_forms` | 5 | misc |
| `note_categories` | 6 | misc |
| `order_channels` | 3 | misc |
| `others_activities` | 129 | misc |
| `package_activities` | 49 | products |
| `package_activity_faqs` | 39 | products |
| `package_activity_packages` | 65 | products |
| `package_banners` | 626 | products |
| `package_categories` | 6 | products |
| `package_destinations` | 358 | products |
| `package_hotels` | 367 | hotels |
| `package_include_excludes` | 1,093 | products |
| `package_meals` | 84 | products |
| `package_prices` | 556 | products |
| `package_transportations` | 7 | products |
| `packages` | 90 | products |
| `pages` | 0 | misc |
| `participants` | 101 | misc |
| `partner_discount_codes` | 0 | misc |
| `partner_discounts` | 0 | misc |
| `password_activations` | 0 | misc |
| `police_escorts` | 3 | misc |
| `pos_transfers` | 25 | misc |
| `price_categories` | 42 | misc |
| `price_maker_location_details` | 135 | misc |
| `price_maker_locations` | 37 | misc |
| `price_maker_price_paxs` | 126 | misc |
| `price_makers` | 9 | misc |
| `price_plans` | 3 | misc |
| `review_guides` | 10 | people |
| `reviews` | 0 | reviews |
| `role_user` | 0 | people |
| `room_configurations` | 0 | hotels |
| `room_hotel_configurations` | 182 | hotels |
| `room_hotels` | 263 | hotels |
| `room_photos` | 0 | hotels |
| `room_types` | 0 | hotels |
| `services` | 14 | misc |
| `tags` | 4 | misc |
| `task_lists` | 0 | misc |
| `tasks` | 0 | misc |
| `transport_bali_pricing` | 36 | misc |
| `trip_expense_items` | 0 | finance |
| `trip_expense_locations` | 0 | finance |
| `trip_expenses` | 0 | finance |
| `tw_calculation_categories` | 9 | misc |
| `tw_calculation_category_codes` | 5 | misc |
| `tw_calculation_details` | 5,317 | misc |
| `tw_calculation_item_details` | 248 | misc |
| `tw_calculation_items` | 23 | misc |
| `tw_calculations` | 295 | misc |
| `user_accommodations` | 4 | people |
| `user_garages` | 2 | people |
| `user_jeeps` | 3 | people |
| `user_logs` | 655 | people |
| `user_partners` | 35 | people |
| `user_police_escorts` | 1 | people |
| `user_tshirts` | 3 | people |
| `vendor_categories` | 4 | vendors |
| `vendors` | 12 | vendors |
| `wa_chat_categories` | 26 | whatsapp |
| `wa_chat_ignores` | 0 | whatsapp |
| `wa_chat_summaries` | 640 | whatsapp |
| `wa_chats` | 5,547 | whatsapp |
| `wa_conversations` | 0 | whatsapp |
| `wa_drafts` | 0 | whatsapp |
| `wa_intent_taxonomy` | 0 | whatsapp |
| `wa_itineraries` | 2,985 | whatsapp |
| `wa_logs` | 3,608 | whatsapp |
| `wa_messages` | 0 | whatsapp |
| `wa_templates` | 0 | whatsapp |
| `weather_codes` | 28 | misc |
| `website_link_categories` | 12 | misc |
| `website_links` | 11 | misc |

## All sensitive tables

| Table | Rows | Domain |
|---|---:|---|
| `book_activities` | 48 | bookings |
| `book_add_ons` | 135 | bookings |
| `book_attachments` | 0 | bookings |
| `book_car_activities` | 564 | bookings |
| `book_cars` | 1,065 | bookings |
| `book_crew_activities` | 509 | bookings |
| `book_destination_activities` | 4,294 | bookings |
| `book_guide_drivers` | 2,105 | bookings |
| `book_hotel_meals` | 643 | bookings |
| `book_hotel_service` | 0 | bookings |
| `book_hotels` | 2,487 | bookings |
| `book_itineraries` | 249 | bookings |
| `book_itinerary_details` | 0 | bookings |
| `book_jeeps` | 98 | bookings |
| `book_meals` | 48 | bookings |
| `book_others_activities` | 2,577 | bookings |
| `book_room_hotels` | 3,150 | bookings |
| `book_services` | 146 | bookings |
| `booking_additional_price_bookings` | 4 | bookings |
| `booking_categories` | 3 | bookings |
| `booking_details` | 1,451 | bookings |
| `booking_documents` | 530 | bookings |
| `booking_itineraries` | 3,595 | bookings |
| `booking_payments` | 506 | finance |
| `booking_refund_and_penalties` | 3 | bookings |
| `booking_reviews` | 0 | bookings |
| `bookings` | 1,453 | bookings |
| `debt_payment_details` | 0 | finance |
| `debt_payments` | 0 | finance |
| `identity_cards` | 0 | vehicles |
| `invoice_histories` | 1,002 | finance |
| `invoice_twt_details` | 3 | finance |
| `invoice_twts` | 2 | finance |
| `payment_methods` | 7 | finance |
| `twt_invoice_additionals` | 52 | finance |
| `twt_invoice_bookings` | 49 | finance |
| `twt_invoice_payments` | 22 | finance |
| `twt_invoice_refunds_penalties` | 67 | finance |
| `twt_invoices` | 18 | finance |
| `users` | 3,568 | people |

## All framework tables

| Table | Rows | Domain |
|---|---:|---|
| `cache` | 4 | misc |
| `cache_locks` | 0 | misc |
| `failed_jobs` | 0 | misc |
| `job_batches` | 0 | misc |
| `jobs` | 0 | misc |
| `migrations` | 567 | misc |
| `password_reset_tokens` | 0 | misc |
| `password_resets` | 2 | misc |
| `personal_access_tokens` | 364 | misc |
| `sessions` | 6 | misc |

## Extraction plan

- **Schema dump:** all 210 tables → `raw/backoffice/schema/full-schema.sql` (commit-safe)
- **Data dump:** business + sensitive (non-framework) → `raw/backoffice/dumps/<table>.sql` (gitignored)
- **CSV export:** business + sensitive → `raw/backoffice/csv/<table>.csv` (gitignored)
- **Customer slice:** sensitive tables with `created_at` column → filter `WHERE created_at >= '2026-05-01'` for wiki aggregation only
- **Wiki layer:** aggregate stats only; no email/phone/full name leak; see PII guard in extraction script
