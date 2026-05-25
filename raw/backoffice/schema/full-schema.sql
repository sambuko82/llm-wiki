-- Backoffice schema dump
-- Source: u1805424_jvto_clone @ MariaDB 10.11 (Hostinger)
-- Generated: 2026-05-25T16:15:49.240471Z
-- Tables: 210
-- No data — schema only — safe to commit

SET FOREIGN_KEY_CHECKS=0;

-- ---- accommodation_categories (4 rows, business) ----
DROP TABLE IF EXISTS `accommodation_categories`;
CREATE TABLE `accommodation_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `category_code` varchar(255) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- accommodations (0 rows, business) ----
DROP TABLE IF EXISTS `accommodations`;
CREATE TABLE `accommodations` (
  `accommodation_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `category_id` bigint(20) unsigned NOT NULL,
  `accommodation_name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`accommodation_id`),
  KEY `accommodations_category_id_foreign` (`category_id`),
  CONSTRAINT `accommodations_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `accommodation_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- accounts (3 rows, business) ----
DROP TABLE IF EXISTS `accounts`;
CREATE TABLE `accounts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) DEFAULT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activities (18 rows, business) ----
DROP TABLE IF EXISTS `activities`;
CREATE TABLE `activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `activity_code` varchar(255) NOT NULL,
  `activity_category_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `notes` text DEFAULT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `hotel_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activities_activity_category_id_foreign` (`activity_category_id`),
  KEY `activities_destination_id_foreign` (`destination_id`),
  KEY `activities_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `activities_activity_category_id_foreign` FOREIGN KEY (`activity_category_id`) REFERENCES `activity_categories` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activities_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activities_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activity_categories (7 rows, business) ----
DROP TABLE IF EXISTS `activity_categories`;
CREATE TABLE `activity_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `icon` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activity_destination_medias (0 rows, business) ----
DROP TABLE IF EXISTS `activity_destination_medias`;
CREATE TABLE `activity_destination_medias` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `activity_destination_id` bigint(20) unsigned NOT NULL,
  `url` varchar(255) NOT NULL,
  `type` enum('image','video') NOT NULL,
  `alt_text` varchar(255) DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_destination_medias_activity_destination_id_foreign` (`activity_destination_id`),
  CONSTRAINT `activity_destination_medias_activity_destination_id_foreign` FOREIGN KEY (`activity_destination_id`) REFERENCES `activity_destinations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activity_destinations (0 rows, business) ----
DROP TABLE IF EXISTS `activity_destinations`;
CREATE TABLE `activity_destinations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `activity_code` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `activity_category_id` bigint(20) unsigned NOT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `from_destination_id` bigint(20) unsigned DEFAULT NULL,
  `to_destination_id` bigint(20) unsigned DEFAULT NULL,
  `duration_hours` int(11) DEFAULT NULL,
  `difficulty_level` varchar(255) DEFAULT NULL,
  `physical_requirements` text DEFAULT NULL,
  `health_advisories` text DEFAULT NULL,
  `required_gear` text DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `best_time_to_visit` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_destinations_activity_category_id_foreign` (`activity_category_id`),
  KEY `activity_destinations_destination_id_foreign` (`destination_id`),
  KEY `activity_destinations_from_destination_id_foreign` (`from_destination_id`),
  KEY `activity_destinations_to_destination_id_foreign` (`to_destination_id`),
  CONSTRAINT `activity_destinations_activity_category_id_foreign` FOREIGN KEY (`activity_category_id`) REFERENCES `activity_categories` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activity_destinations_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activity_destinations_from_destination_id_foreign` FOREIGN KEY (`from_destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activity_destinations_to_destination_id_foreign` FOREIGN KEY (`to_destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activity_ends (14 rows, business) ----
DROP TABLE IF EXISTS `activity_ends`;
CREATE TABLE `activity_ends` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `d` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- activity_starts (19 rows, business) ----
DROP TABLE IF EXISTS `activity_starts`;
CREATE TABLE `activity_starts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `b` enum('0','1') NOT NULL DEFAULT '0',
  `l` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_starts_destination_id_foreign` (`destination_id`),
  CONSTRAINT `activity_starts_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- add_on_carts (0 rows, business) ----
DROP TABLE IF EXISTS `add_on_carts`;
CREATE TABLE `add_on_carts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cart_id` bigint(20) unsigned NOT NULL,
  `add_on_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `add_on_carts_cart_id_foreign` (`cart_id`),
  KEY `add_on_carts_add_on_id_foreign` (`add_on_id`),
  CONSTRAINT `add_on_carts_add_on_id_foreign` FOREIGN KEY (`add_on_id`) REFERENCES `add_ons` (`id`),
  CONSTRAINT `add_on_carts_cart_id_foreign` FOREIGN KEY (`cart_id`) REFERENCES `carts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- add_on_packages (365 rows, business) ----
DROP TABLE IF EXISTS `add_on_packages`;
CREATE TABLE `add_on_packages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `add_on_id` bigint(20) unsigned NOT NULL,
  `package_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `add_on_packages_add_on_id_foreign` (`add_on_id`),
  KEY `add_on_packages_package_id_foreign` (`package_id`),
  CONSTRAINT `add_on_packages_add_on_id_foreign` FOREIGN KEY (`add_on_id`) REFERENCES `add_ons` (`id`),
  CONSTRAINT `add_on_packages_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=399 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- add_ons (160 rows, business) ----
DROP TABLE IF EXISTS `add_ons`;
CREATE TABLE `add_ons` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `add_on` varchar(255) NOT NULL,
  `is_transport` enum('0','1') NOT NULL DEFAULT '0',
  `type_transport` enum('small','medium','big') DEFAULT NULL,
  `desc` text DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `price` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=197 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- agents (7 rows, business) ----
DROP TABLE IF EXISTS `agents`;
CREATE TABLE `agents` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(255) DEFAULT NULL,
  `booking_code` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `long_name` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `icon` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agents_username_unique` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- announcements (0 rows, business) ----
DROP TABLE IF EXISTS `announcements`;
CREATE TABLE `announcements` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `subtitle` varchar(255) DEFAULT NULL,
  `cover` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- areas (12 rows, business) ----
DROP TABLE IF EXISTS `areas`;
CREATE TABLE `areas` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `area_name` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `color` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `is_start` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- article_media (0 rows, business) ----
DROP TABLE IF EXISTS `article_media`;
CREATE TABLE `article_media` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` bigint(20) unsigned NOT NULL,
  `media_url` varchar(255) NOT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `alt_text` varchar(255) DEFAULT NULL,
  `type` varchar(255) NOT NULL DEFAULT 'image',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_media_article_id_foreign` (`article_id`),
  CONSTRAINT `article_media_article_id_foreign` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- articles (3 rows, business) ----
DROP TABLE IF EXISTS `articles`;
CREATE TABLE `articles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `summary` text DEFAULT NULL,
  `content` longtext NOT NULL,
  `featured_image` varchar(255) DEFAULT NULL,
  `meta_title` varchar(255) DEFAULT NULL,
  `meta_description` varchar(255) DEFAULT NULL,
  `canonical_url` varchar(255) DEFAULT NULL,
  `tags` longtext DEFAULT NULL,
  `status` enum('draft','published') NOT NULL DEFAULT 'draft',
  `published_at` timestamp NULL DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `articles_slug_unique` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- attachment_types (7 rows, business) ----
DROP TABLE IF EXISTS `attachment_types`;
CREATE TABLE `attachment_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- availabilities (2400 rows, business) ----
DROP TABLE IF EXISTS `availabilities`;
CREATE TABLE `availabilities` (
  `id` char(36) NOT NULL,
  `product_id` char(36) NOT NULL,
  `option_id` varchar(255) NOT NULL,
  `local_date` date DEFAULT NULL,
  `local_date_time_start` datetime DEFAULT NULL,
  `local_date_time_end` datetime DEFAULT NULL,
  `all_day` tinyint(1) NOT NULL DEFAULT 1,
  `status` varchar(255) NOT NULL DEFAULT 'FREESALE',
  `available` tinyint(1) NOT NULL,
  `vacancies` int(11) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  `max_units` int(11) DEFAULT NULL,
  `utc_cutoff_at` datetime DEFAULT NULL,
  `opening_hours` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`opening_hours`)),
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- blogs (0 rows, business) ----
DROP TABLE IF EXISTS `blogs`;
CREATE TABLE `blogs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `banner` varchar(255) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `status` enum('publish','draft') NOT NULL,
  `views` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_activities (48 rows, sensitive) ----
DROP TABLE IF EXISTS `book_activities`;
CREATE TABLE `book_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `day` int(11) NOT NULL,
  `date` date NOT NULL,
  `activity` longtext DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_activities_booking_id_foreign` (`booking_id`),
  CONSTRAINT `book_activities_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_add_ons (135 rows, sensitive) ----
DROP TABLE IF EXISTS `book_add_ons`;
CREATE TABLE `book_add_ons` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `add_on_package_id` bigint(20) unsigned DEFAULT NULL,
  `add_on_id` bigint(20) unsigned DEFAULT NULL,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `price` double NOT NULL,
  `price_expense` double NOT NULL DEFAULT 0,
  `qty` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_add_ons_add_on_package_id_foreign` (`add_on_package_id`),
  KEY `book_add_ons_booking_id_foreign` (`booking_id`),
  KEY `book_add_ons_add_on_id_foreign` (`add_on_id`),
  KEY `idx_book_add_ons_booking_id` (`booking_id`),
  CONSTRAINT `book_add_ons_add_on_id_foreign` FOREIGN KEY (`add_on_id`) REFERENCES `add_ons` (`id`),
  CONSTRAINT `book_add_ons_add_on_package_id_foreign` FOREIGN KEY (`add_on_package_id`) REFERENCES `add_on_packages` (`id`),
  CONSTRAINT `book_add_ons_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=562 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_attachments (0 rows, sensitive) ----
DROP TABLE IF EXISTS `book_attachments`;
CREATE TABLE `book_attachments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `attachment` text DEFAULT NULL,
  `note` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_attachments_booking_id_foreign` (`booking_id`),
  CONSTRAINT `book_attachments_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `book_attachments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_car_activities (564 rows, sensitive) ----
DROP TABLE IF EXISTS `book_car_activities`;
CREATE TABLE `book_car_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `car_id` bigint(20) unsigned NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `status_paid` enum('paid','unpaid') DEFAULT NULL,
  `driver_txt` varchar(255) DEFAULT NULL,
  `note_txt` varchar(255) DEFAULT NULL,
  `paid_date` timestamp NULL DEFAULT NULL,
  `is_debt` enum('0','1') DEFAULT NULL,
  `debt_payment_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_car_activities_booking_id_foreign` (`booking_id`),
  KEY `book_car_activities_car_id_foreign` (`car_id`),
  KEY `book_car_activities_debt_payment_id_foreign` (`debt_payment_id`),
  KEY `idx_book_car_activities_booking_id` (`booking_id`),
  CONSTRAINT `book_car_activities_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_car_activities_car_id_foreign` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_car_activities_debt_payment_id_foreign` FOREIGN KEY (`debt_payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=1085 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_cars (1065 rows, sensitive) ----
DROP TABLE IF EXISTS `book_cars`;
CREATE TABLE `book_cars` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `car_id` bigint(20) unsigned DEFAULT NULL,
  `quantity` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `driver_id` bigint(20) unsigned DEFAULT NULL,
  `total_rent` int(11) DEFAULT NULL,
  `total_fuel` int(11) DEFAULT NULL,
  `total_fee_driver` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_cars_booking_id_foreign` (`booking_id`),
  KEY `book_cars_car_id_foreign` (`car_id`),
  CONSTRAINT `book_cars_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `book_cars_car_id_foreign` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3919 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_crew_activities (509 rows, sensitive) ----
DROP TABLE IF EXISTS `book_crew_activities`;
CREATE TABLE `book_crew_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `crew_role_id` bigint(20) unsigned NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `status_paid` enum('paid','unpaid') DEFAULT NULL,
  `paid_date` timestamp NULL DEFAULT NULL,
  `is_debt` enum('0','1') DEFAULT NULL,
  `debt_payment_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_crew_activities_booking_id_foreign` (`booking_id`),
  KEY `book_crew_activities_crew_role_id_foreign` (`crew_role_id`),
  KEY `book_crew_activities_debt_payment_id_foreign` (`debt_payment_id`),
  KEY `idx_book_crew_activities_booking_id` (`booking_id`),
  CONSTRAINT `book_crew_activities_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_crew_activities_crew_role_id_foreign` FOREIGN KEY (`crew_role_id`) REFERENCES `crew_roles` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_crew_activities_debt_payment_id_foreign` FOREIGN KEY (`debt_payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_destination_activities (4294 rows, sensitive) ----
DROP TABLE IF EXISTS `book_destination_activities`;
CREATE TABLE `book_destination_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `destination_activity_id` bigint(20) unsigned NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `status_paid` enum('paid','unpaid') DEFAULT NULL,
  `paid_date` datetime DEFAULT NULL,
  `is_debt` enum('0','1') DEFAULT NULL,
  `debt_payment_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_destination_activities_destination_activity_id_foreign` (`destination_activity_id`),
  KEY `book_destination_activities_destination_id_foreign` (`destination_id`),
  KEY `book_destination_activities_booking_id_foreign` (`booking_id`),
  KEY `book_destination_activities_debt_payment_id_foreign` (`debt_payment_id`),
  KEY `idx_book_destination_activities_booking_id` (`booking_id`),
  CONSTRAINT `book_destination_activities_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_destination_activities_debt_payment_id_foreign` FOREIGN KEY (`debt_payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE SET NULL,
  CONSTRAINT `book_destination_activities_destination_activity_id_foreign` FOREIGN KEY (`destination_activity_id`) REFERENCES `destination_activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_destination_activities_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6463 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_guide_drivers (2105 rows, sensitive) ----
DROP TABLE IF EXISTS `book_guide_drivers`;
CREATE TABLE `book_guide_drivers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `guide_id` bigint(20) unsigned DEFAULT NULL,
  `type` enum('guide','driver') DEFAULT NULL,
  `guide_type` enum('ijen_only','escort') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `duration` int(11) DEFAULT NULL COMMENT 'Duration in days',
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `guide_ijen` enum('0','1') NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `book_guide_drivers_booking_id_foreign` (`booking_id`),
  KEY `book_guide_drivers_guide_id_foreign` (`guide_id`),
  CONSTRAINT `book_guide_drivers_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `book_guide_drivers_guide_id_foreign` FOREIGN KEY (`guide_id`) REFERENCES `guide_drivers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5489 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_hotel_meals (643 rows, sensitive) ----
DROP TABLE IF EXISTS `book_hotel_meals`;
CREATE TABLE `book_hotel_meals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `book_hotel_id` bigint(20) unsigned NOT NULL,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `meals` enum('breakfast','lunch','dinner') NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_hotel_meals_booking_id_foreign` (`booking_id`),
  KEY `book_hotel_meals_book_hotel_id_foreign` (`book_hotel_id`),
  KEY `book_hotel_meals_hotel_id_foreign` (`hotel_id`),
  KEY `idx_book_hotel_meals_booking_id` (`booking_id`),
  KEY `idx_book_hotel_meals_book_hotel_id` (`book_hotel_id`),
  CONSTRAINT `book_hotel_meals_book_hotel_id_foreign` FOREIGN KEY (`book_hotel_id`) REFERENCES `book_hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_hotel_meals_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_hotel_meals_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=898 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_hotel_service (0 rows, sensitive) ----
DROP TABLE IF EXISTS `book_hotel_service`;
CREATE TABLE `book_hotel_service` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `book_room_hotel_id` bigint(20) unsigned DEFAULT NULL,
  `hotel_service_id` bigint(20) unsigned DEFAULT NULL,
  `qty` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_hotel_service_book_room_hotel_id_foreign` (`book_room_hotel_id`),
  KEY `book_hotel_service_hotel_service_id_foreign` (`hotel_service_id`),
  CONSTRAINT `book_hotel_service_book_room_hotel_id_foreign` FOREIGN KEY (`book_room_hotel_id`) REFERENCES `book_room_hotels` (`id`),
  CONSTRAINT `book_hotel_service_hotel_service_id_foreign` FOREIGN KEY (`hotel_service_id`) REFERENCES `hotel_services` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_hotels (2487 rows, sensitive) ----
DROP TABLE IF EXISTS `book_hotels`;
CREATE TABLE `book_hotels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `booking_itinerary_id` bigint(20) unsigned NOT NULL,
  `hotel_id` bigint(20) unsigned DEFAULT NULL,
  `b` enum('0','1') NOT NULL,
  `l` enum('0','1') NOT NULL,
  `d` enum('0','1') NOT NULL,
  `remarks` text DEFAULT NULL,
  `status` enum('0','1') DEFAULT '1' COMMENT '0=reject, 1=approve',
  `reject_msg` varchar(255) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `is_paid` enum('0','1') NOT NULL DEFAULT '0',
  `paid_at` timestamp NULL DEFAULT NULL,
  `is_debt` enum('0','1') DEFAULT NULL,
  `debt_payment_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_hotels_booking_id_foreign` (`booking_id`),
  KEY `book_hotels_hotel_id_foreign` (`hotel_id`),
  KEY `book_hotels_booking_itinerary_id_foreign` (`booking_itinerary_id`),
  KEY `book_hotels_debt_payment_id_foreign` (`debt_payment_id`),
  KEY `idx_book_hotels_booking_id` (`booking_id`),
  CONSTRAINT `book_hotels_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `book_hotels_booking_itinerary_id_foreign` FOREIGN KEY (`booking_itinerary_id`) REFERENCES `booking_itineraries` (`id`),
  CONSTRAINT `book_hotels_debt_payment_id_foreign` FOREIGN KEY (`debt_payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE SET NULL,
  CONSTRAINT `book_hotels_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5061 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_itineraries (249 rows, sensitive) ----
DROP TABLE IF EXISTS `book_itineraries`;
CREATE TABLE `book_itineraries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `day` int(11) NOT NULL,
  `date` date NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `start_area_id` bigint(20) unsigned DEFAULT NULL,
  `end_area_id` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_itineraries_booking_id_foreign` (`booking_id`),
  CONSTRAINT `book_itineraries_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=849 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_itinerary_details (0 rows, sensitive) ----
DROP TABLE IF EXISTS `book_itinerary_details`;
CREATE TABLE `book_itinerary_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `book_itinerary_id` bigint(20) unsigned DEFAULT NULL,
  `area_id` bigint(20) unsigned DEFAULT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `is_start` tinyint(1) DEFAULT NULL COMMENT 'Jika start maka 1, jika end maka null atau 0 dan is end nya 1',
  `is_end` tinyint(1) DEFAULT NULL COMMENT 'Jika end maka 1, jika start maka null atau 0 dan is start nya 1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_itinerary_details_book_itinerary_id_foreign` (`book_itinerary_id`),
  KEY `book_itinerary_details_area_id_foreign` (`area_id`),
  KEY `book_itinerary_details_destination_id_foreign` (`destination_id`),
  CONSTRAINT `book_itinerary_details_area_id_foreign` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `book_itinerary_details_book_itinerary_id_foreign` FOREIGN KEY (`book_itinerary_id`) REFERENCES `book_itineraries` (`id`),
  CONSTRAINT `book_itinerary_details_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_jeeps (98 rows, sensitive) ----
DROP TABLE IF EXISTS `book_jeeps`;
CREATE TABLE `book_jeeps` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `hotel_id` bigint(20) unsigned DEFAULT NULL,
  `hotel_check_in` date DEFAULT NULL,
  `qty_jeep` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_jeeps_booking_id_foreign` (`booking_id`),
  KEY `book_jeeps_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `book_jeeps_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `book_jeeps_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_meals (48 rows, sensitive) ----
DROP TABLE IF EXISTS `book_meals`;
CREATE TABLE `book_meals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `day` int(11) NOT NULL,
  `date` date NOT NULL,
  `breakfast` enum('0','1') NOT NULL DEFAULT '0',
  `lunch` enum('0','1') NOT NULL DEFAULT '0',
  `dinner` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_meals_booking_id_foreign` (`booking_id`),
  CONSTRAINT `book_meals_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_others_activities (2577 rows, sensitive) ----
DROP TABLE IF EXISTS `book_others_activities`;
CREATE TABLE `book_others_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `others_activity_id` bigint(20) unsigned NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `status_paid` enum('paid','unpaid') DEFAULT NULL,
  `paid_date` datetime DEFAULT NULL,
  `is_debt` enum('0','1') DEFAULT NULL,
  `debt_payment_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_others_activities_others_activity_id_foreign` (`others_activity_id`),
  KEY `book_others_activities_booking_id_foreign` (`booking_id`),
  KEY `book_others_activities_debt_payment_id_foreign` (`debt_payment_id`),
  KEY `idx_book_others_activities_booking_id` (`booking_id`),
  CONSTRAINT `book_others_activities_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_others_activities_debt_payment_id_foreign` FOREIGN KEY (`debt_payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE SET NULL,
  CONSTRAINT `book_others_activities_others_activity_id_foreign` FOREIGN KEY (`others_activity_id`) REFERENCES `others_activities` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_room_hotels (3150 rows, sensitive) ----
DROP TABLE IF EXISTS `book_room_hotels`;
CREATE TABLE `book_room_hotels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `booking_itinerary_id` bigint(20) unsigned DEFAULT NULL,
  `book_hotel_id` bigint(20) unsigned DEFAULT NULL,
  `room_hotel_id` bigint(20) unsigned NOT NULL,
  `check_in` date DEFAULT NULL,
  `check_out` date DEFAULT NULL,
  `quantity` tinyint(3) unsigned NOT NULL,
  `day` tinyint(3) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `hotel_id` bigint(20) unsigned DEFAULT NULL,
  `double` int(11) DEFAULT NULL,
  `twin` int(11) DEFAULT NULL,
  `extra_bed` int(11) DEFAULT NULL,
  `capsule` int(11) DEFAULT NULL,
  `subtotal` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_room_hotels_booking_id_foreign` (`booking_id`),
  KEY `book_room_hotels_room_hotel_id_foreign` (`room_hotel_id`),
  KEY `book_room_hotels_booking_itinerary_id_foreign` (`booking_itinerary_id`),
  KEY `book_room_hotels_book_hotel_id_foreign` (`book_hotel_id`),
  KEY `idx_book_room_hotels_book_hotel_id` (`book_hotel_id`),
  CONSTRAINT `book_room_hotels_book_hotel_id_foreign` FOREIGN KEY (`book_hotel_id`) REFERENCES `book_hotels` (`id`),
  CONSTRAINT `book_room_hotels_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `book_room_hotels_booking_itinerary_id_foreign` FOREIGN KEY (`booking_itinerary_id`) REFERENCES `booking_itineraries` (`id`),
  CONSTRAINT `book_room_hotels_room_hotel_id_foreign` FOREIGN KEY (`room_hotel_id`) REFERENCES `room_hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9649 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- book_services (146 rows, sensitive) ----
DROP TABLE IF EXISTS `book_services`;
CREATE TABLE `book_services` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `service_id` bigint(20) unsigned DEFAULT NULL,
  `other_service` varchar(255) DEFAULT NULL COMMENT 'For other service which not listed on services',
  `day` int(10) unsigned NOT NULL,
  `date` date NOT NULL,
  `qty` int(11) DEFAULT NULL,
  `note` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `guide_ijen_id` bigint(20) unsigned DEFAULT NULL,
  `subtotal` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_services_booking_id_foreign` (`booking_id`),
  KEY `book_services_service_id_foreign` (`service_id`),
  KEY `book_services_guide_ijen_id_foreign` (`guide_ijen_id`),
  CONSTRAINT `book_services_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `book_services_guide_ijen_id_foreign` FOREIGN KEY (`guide_ijen_id`) REFERENCES `guide_drivers` (`id`),
  CONSTRAINT `book_services_service_id_foreign` FOREIGN KEY (`service_id`) REFERENCES `services` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=450 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_additional_price_bookings (4 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_additional_price_bookings`;
CREATE TABLE `booking_additional_price_bookings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) NOT NULL,
  `quantity` double NOT NULL,
  `price` double NOT NULL,
  `subtotal` double NOT NULL,
  `attachment` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_additional_price_bookings_booking_id_foreign` (`booking_id`),
  CONSTRAINT `booking_additional_price_bookings_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_categories (3 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_categories`;
CREATE TABLE `booking_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `agent_id` bigint(20) unsigned NOT NULL,
  `is_transport` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_categories_agent_id_foreign` (`agent_id`),
  CONSTRAINT `booking_categories_agent_id_foreign` FOREIGN KEY (`agent_id`) REFERENCES `agents` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_details (1451 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_details`;
CREATE TABLE `booking_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned DEFAULT NULL,
  `price_plan_id` bigint(20) unsigned DEFAULT NULL,
  `booking_id` bigint(20) unsigned NOT NULL,
  `travel_date_start` date NOT NULL,
  `travel_date_end` date NOT NULL,
  `pax` int(11) NOT NULL,
  `xss` int(10) unsigned DEFAULT NULL,
  `xxs` int(11) DEFAULT 0,
  `xs` int(11) DEFAULT 0,
  `s` int(11) NOT NULL,
  `m` int(11) NOT NULL,
  `l` int(11) NOT NULL,
  `xl` int(11) NOT NULL,
  `xxl` int(11) NOT NULL,
  `xxxl` int(11) DEFAULT 0,
  `custom_tshirt` varchar(255) DEFAULT NULL,
  `custom_tshirt_note` varchar(255) DEFAULT NULL,
  `status` enum('0','1','2','3') NOT NULL DEFAULT '0',
  `total` double NOT NULL,
  `request_schedule` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `klook_unit_items` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`klook_unit_items`)),
  PRIMARY KEY (`id`),
  KEY `booking_details_booking_id_foreign` (`booking_id`),
  KEY `booking_details_package_id_foreign` (`package_id`),
  KEY `booking_details_price_plan_id_foreign` (`price_plan_id`),
  CONSTRAINT `booking_details_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `booking_details_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `booking_details_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3388 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_documents (530 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_documents`;
CREATE TABLE `booking_documents` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `attachment_type_id` bigint(20) unsigned NOT NULL,
  `file` varchar(255) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `note` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_documents_booking_id_foreign` (`booking_id`),
  KEY `booking_documents_user_id_foreign` (`user_id`),
  KEY `booking_documents_attachment_type_id_foreign` (`attachment_type_id`),
  CONSTRAINT `booking_documents_attachment_type_id_foreign` FOREIGN KEY (`attachment_type_id`) REFERENCES `attachment_types` (`id`),
  CONSTRAINT `booking_documents_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `booking_documents_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=599 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_itineraries (3595 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_itineraries`;
CREATE TABLE `booking_itineraries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `day` tinyint(4) NOT NULL,
  `activity_start_id` bigint(20) unsigned DEFAULT NULL,
  `activity_end_id` bigint(20) unsigned DEFAULT NULL,
  `itinerary` varchar(255) NOT NULL,
  `activity` text DEFAULT NULL,
  `b` enum('0','1') DEFAULT NULL,
  `l` enum('0','1') DEFAULT NULL,
  `d` enum('0','1') DEFAULT NULL,
  `accommodation` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_itineraries_activity_start_id_foreign` (`activity_start_id`),
  KEY `booking_itineraries_activity_end_id_foreign` (`activity_end_id`),
  CONSTRAINT `booking_itineraries_activity_end_id_foreign` FOREIGN KEY (`activity_end_id`) REFERENCES `activity_ends` (`id`),
  CONSTRAINT `booking_itineraries_activity_start_id_foreign` FOREIGN KEY (`activity_start_id`) REFERENCES `activity_starts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6893 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_payments (506 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_payments`;
CREATE TABLE `booking_payments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `nominal` double NOT NULL,
  `payment_method_id` bigint(20) unsigned NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `proof_file` varchar(255) DEFAULT NULL,
  `is_paid` enum('0','1') NOT NULL DEFAULT '1',
  `paid_at` datetime DEFAULT NULL,
  `is_add_on` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_payments_booking_id_foreign` (`booking_id`),
  KEY `booking_payments_payment_method_id_foreign` (`payment_method_id`),
  KEY `idx_booking_payments_booking_id` (`booking_id`),
  CONSTRAINT `booking_payments_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `booking_payments_payment_method_id_foreign` FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=612 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_refund_and_penalties (3 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_refund_and_penalties`;
CREATE TABLE `booking_refund_and_penalties` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) NOT NULL,
  `quantity` double NOT NULL,
  `price` double NOT NULL,
  `subtotal` double NOT NULL,
  `attachment` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_refund_and_penalties_booking_id_foreign` (`booking_id`),
  CONSTRAINT `booking_refund_and_penalties_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- booking_reviews (0 rows, sensitive) ----
DROP TABLE IF EXISTS `booking_reviews`;
CREATE TABLE `booking_reviews` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `trip_rate` tinyint(4) DEFAULT NULL,
  `package_rate` tinyint(4) DEFAULT NULL,
  `package_feedback` text DEFAULT NULL,
  `crew_feedback` text DEFAULT NULL,
  `know_from` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_reviews_booking_id_foreign` (`booking_id`),
  CONSTRAINT `booking_reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- bookings (1453 rows, sensitive) ----
DROP TABLE IF EXISTS `bookings`;
CREATE TABLE `bookings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `klook_uuid` varchar(255) DEFAULT NULL,
  `trip_name` varchar(255) DEFAULT NULL,
  `booking_code_app` varchar(255) DEFAULT NULL,
  `booking_code` varchar(255) DEFAULT NULL,
  `custom_code` varchar(255) DEFAULT NULL,
  `invoice_code_origin` varchar(255) DEFAULT NULL,
  `booking_category_id` bigint(20) unsigned DEFAULT NULL,
  `channel_tag` enum('klook','gyg','viator') DEFAULT NULL COMMENT 'Manual override for KLOOK bookings: null = auto-detect by invoice_code_origin prefix',
  `booking_date` date DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `hotel_id_transport` bigint(20) unsigned DEFAULT NULL,
  `booking_numb` varchar(255) DEFAULT NULL,
  `booking_from` varchar(255) DEFAULT NULL,
  `inclusion` text DEFAULT NULL,
  `exclusion` text DEFAULT NULL,
  `no_st` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  `travel_date_start` date DEFAULT NULL,
  `travel_date_end` date DEFAULT NULL,
  `total_pax` double NOT NULL,
  `is_trip_participants` enum('0','1') NOT NULL DEFAULT '0',
  `car_type` varchar(255) DEFAULT NULL,
  `numb_of_car` tinyint(4) DEFAULT NULL,
  `dp` double NOT NULL,
  `dp_no_idr` double NOT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `add_on_total` double NOT NULL DEFAULT 0,
  `discount_id` bigint(20) unsigned DEFAULT NULL,
  `discount_type` enum('percent','nominal') DEFAULT NULL,
  `referral_code` varchar(255) DEFAULT NULL COMMENT 'referral code from referrer',
  `discount_percent` tinyint(4) DEFAULT NULL COMMENT 'discount in percentage',
  `discount` double DEFAULT NULL,
  `grand_total_before_disc` double DEFAULT NULL,
  `deposit` enum('dp','attachment') DEFAULT NULL,
  `grand_total` double NOT NULL,
  `is_buy_isic` enum('0','1') NOT NULL DEFAULT '0',
  `is_buy_isic_complete_form` enum('0','1') NOT NULL DEFAULT '0',
  `payment_status` enum('pending','approved') NOT NULL DEFAULT 'pending',
  `debt` double DEFAULT NULL,
  `balance` double DEFAULT NULL,
  `payment` int(11) DEFAULT NULL,
  `status` enum('booked','pending pay later','reject pay later','pending wise','reject wise','finished') DEFAULT NULL,
  `type` enum('online','offline') DEFAULT NULL,
  `payment_method` enum('pay later','paypal','wise','cc') DEFAULT NULL,
  `payment_link` varchar(255) DEFAULT NULL,
  `outstanding_payment_method` enum('cash','cc','wise','edc') DEFAULT NULL,
  `outstanding_payment_link` varchar(255) DEFAULT NULL,
  `outstanding_payment_amount` double DEFAULT NULL,
  `outstanding_payment_fees` double DEFAULT NULL,
  `meeting_point` varchar(255) DEFAULT NULL,
  `meeting_point_arrival` varchar(255) DEFAULT NULL,
  `meeting_point_value` varchar(255) DEFAULT NULL,
  `surabaya_hotel` varchar(255) DEFAULT NULL,
  `special_requirements` varchar(255) DEFAULT NULL,
  `flight_ticket` varchar(255) DEFAULT NULL,
  `remarks` text DEFAULT NULL,
  `terminal_flight_code` varchar(255) DEFAULT NULL,
  `flight_from` varchar(255) DEFAULT NULL,
  `flight_to` varchar(255) DEFAULT NULL,
  `departure` varchar(255) DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `pickup_note` varchar(255) DEFAULT NULL,
  `pickup` varchar(255) DEFAULT NULL,
  `ticket_type_number` varchar(255) DEFAULT NULL,
  `pickup_time` time DEFAULT NULL,
  `drop` varchar(255) DEFAULT NULL,
  `drop_point` varchar(255) DEFAULT NULL,
  `drop_point_arrival` varchar(255) DEFAULT NULL,
  `drop_point_value` varchar(255) DEFAULT NULL,
  `drop_time` time DEFAULT NULL,
  `student_card` varchar(255) DEFAULT NULL,
  `cost` double DEFAULT NULL,
  `margin` double DEFAULT NULL,
  `mr_sam` double DEFAULT NULL,
  `reject_pay_later_msg` text DEFAULT NULL,
  `whatsapp_sended` tinyint(1) NOT NULL DEFAULT 0,
  `media_link` text DEFAULT NULL,
  `is_window` enum('0','1') DEFAULT '0',
  `url` varchar(255) DEFAULT NULL,
  `is_police_escort` enum('0','1') DEFAULT '0',
  `police_escort_pickup_date` datetime DEFAULT NULL,
  `police_escort_route` varchar(255) DEFAULT NULL,
  `url_name` varchar(255) DEFAULT NULL,
  `pickup_sign` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `recalculated_at` timestamp NULL DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `surat_tugas_file` longtext DEFAULT NULL,
  `note` text DEFAULT NULL,
  `agent_id` bigint(20) unsigned DEFAULT NULL,
  `package_duration` int(11) DEFAULT NULL COMMENT 'Package duration in days',
  `template_package_id` bigint(20) unsigned DEFAULT NULL,
  `bromo_hotel_id` bigint(20) unsigned DEFAULT NULL,
  `bromo_hotel_checkin` date DEFAULT NULL,
  `qty_jeep` tinyint(4) DEFAULT NULL,
  `is_share_media` enum('0','1') NOT NULL DEFAULT '1',
  `is_shuttle` enum('0','1') NOT NULL DEFAULT '0',
  `at_bondowoso` date DEFAULT NULL,
  `at_bromo` date DEFAULT NULL,
  `is_send_wa` enum('0','1') NOT NULL DEFAULT '0' COMMENT 'send wa during the trip or not',
  `wa_status_trip_information` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_schedule_trip_information` datetime DEFAULT NULL,
  `wa_status_trip_media` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_schedule_trip_media` datetime DEFAULT NULL,
  `wa_status_trip_media_crew` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_schedule_trip_media_crew` datetime DEFAULT NULL,
  `wa_status_reminder_crew` enum('0','1','00') NOT NULL DEFAULT '0',
  `wa_schedule_reminder_crew` datetime DEFAULT NULL,
  `wa_status_trip_itinerary_crew` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_status_at_bondowoso_crew` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_status_at_bromo_crew` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `wa_schedule_payment_content` text DEFAULT NULL,
  `wa_status_reminder_payment` enum('0','1') NOT NULL DEFAULT '0',
  `expense_file` varchar(255) DEFAULT NULL,
  `expense_file_internal` varchar(255) DEFAULT NULL,
  `expense_total` double DEFAULT NULL,
  `expense_internal_total` double NOT NULL DEFAULT 0,
  `total_expense_paid` decimal(10,2) NOT NULL DEFAULT 0.00,
  `total_expense_crew` decimal(15,2) NOT NULL DEFAULT 0.00,
  `total_expense_balance` decimal(15,2) NOT NULL DEFAULT 0.00,
  `total_expense_debt` decimal(15,2) NOT NULL DEFAULT 0.00,
  `total_expense_debt_paid` int(11) NOT NULL DEFAULT 0,
  `payment_proof_expense` varchar(255) DEFAULT NULL,
  `income` double NOT NULL DEFAULT 0,
  `is_invoiced_twt` enum('0','1') NOT NULL DEFAULT '0',
  `date_paid_invoiced_twt` datetime DEFAULT NULL,
  `klook_product_id` varchar(255) DEFAULT NULL,
  `klook_option_id` varchar(255) DEFAULT NULL,
  `klook_availability_id` varchar(255) DEFAULT NULL,
  `klook_expiration_minutes` int(11) DEFAULT NULL,
  `klook_supplier_reference` varchar(255) DEFAULT NULL,
  `klook_reseller_reference` varchar(255) DEFAULT NULL,
  `klook_utc_expires_at` timestamp NULL DEFAULT NULL,
  `klook_booking_status` varchar(255) DEFAULT 'ON_HOLD',
  `cancellable` tinyint(1) NOT NULL DEFAULT 1,
  `cancellation` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`cancellation`)),
  `refund` varchar(255) DEFAULT NULL,
  `utc_cancelled_at` datetime DEFAULT NULL,
  `is_vendor_paid` enum('0','1') NOT NULL DEFAULT '0',
  `is_vendor_paid_date` timestamp NULL DEFAULT NULL,
  `is_vendor_paid_reference` varchar(255) DEFAULT NULL,
  `is_vendor_paid_payment_method_id` bigint(20) unsigned DEFAULT NULL,
  `note_category_id` bigint(20) unsigned DEFAULT NULL,
  `is_next` enum('0','1') NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `bookings_user_id_foreign` (`user_id`),
  KEY `bookings_discount_id_foreign` (`discount_id`),
  KEY `bookings_agent_id_foreign` (`agent_id`),
  KEY `bookings_bromo_hotel_id_foreign` (`bromo_hotel_id`),
  KEY `bookings_booking_category_id_foreign` (`booking_category_id`),
  KEY `bookings_hotel_id_transport_foreign` (`hotel_id_transport`),
  KEY `bookings_template_package_id_foreign` (`template_package_id`),
  KEY `bookings_is_vendor_paid_payment_method_id_foreign` (`is_vendor_paid_payment_method_id`),
  KEY `bookings_note_category_id_foreign` (`note_category_id`),
  KEY `idx_bookings_recalculated_at` (`recalculated_at`),
  KEY `idx_bookings_agent_id` (`agent_id`),
  KEY `idx_bookings_booking_category_id` (`booking_category_id`),
  KEY `idx_bookings_travel_date_start` (`travel_date_start`),
  KEY `idx_bookings_travel_date_end` (`travel_date_end`),
  KEY `idx_bookings_booking_date` (`booking_date`),
  CONSTRAINT `bookings_agent_id_foreign` FOREIGN KEY (`agent_id`) REFERENCES `agents` (`id`),
  CONSTRAINT `bookings_booking_category_id_foreign` FOREIGN KEY (`booking_category_id`) REFERENCES `booking_categories` (`id`),
  CONSTRAINT `bookings_bromo_hotel_id_foreign` FOREIGN KEY (`bromo_hotel_id`) REFERENCES `hotels` (`id`),
  CONSTRAINT `bookings_discount_id_foreign` FOREIGN KEY (`discount_id`) REFERENCES `discounts` (`id`),
  CONSTRAINT `bookings_hotel_id_transport_foreign` FOREIGN KEY (`hotel_id_transport`) REFERENCES `hotels` (`id`),
  CONSTRAINT `bookings_is_vendor_paid_payment_method_id_foreign` FOREIGN KEY (`is_vendor_paid_payment_method_id`) REFERENCES `payment_methods` (`id`) ON DELETE SET NULL,
  CONSTRAINT `bookings_note_category_id_foreign` FOREIGN KEY (`note_category_id`) REFERENCES `note_categories` (`id`) ON DELETE SET NULL,
  CONSTRAINT `bookings_template_package_id_foreign` FOREIGN KEY (`template_package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `bookings_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3317 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- cache (4 rows, framework) ----
DROP TABLE IF EXISTS `cache`;
CREATE TABLE `cache` (
  `key` varchar(255) NOT NULL,
  `value` mediumtext NOT NULL,
  `expiration` int(11) NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- cache_locks (0 rows, framework) ----
DROP TABLE IF EXISTS `cache_locks`;
CREATE TABLE `cache_locks` (
  `key` varchar(255) NOT NULL,
  `owner` varchar(255) NOT NULL,
  `expiration` int(11) NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- calculation_detail_others (80 rows, business) ----
DROP TABLE IF EXISTS `calculation_detail_others`;
CREATE TABLE `calculation_detail_others` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `calculation_id` bigint(20) unsigned NOT NULL,
  `item_id` bigint(20) unsigned NOT NULL,
  `qty` double NOT NULL,
  `amount` double DEFAULT NULL,
  `rent` double DEFAULT NULL,
  `fuel` double DEFAULT NULL,
  `driver` double DEFAULT NULL,
  `subtotal` double NOT NULL,
  `type` enum('transport','other') NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calculation_detail_others_calculation_id_foreign` (`calculation_id`),
  KEY `calculation_detail_others_item_id_foreign` (`item_id`),
  CONSTRAINT `calculation_detail_others_calculation_id_foreign` FOREIGN KEY (`calculation_id`) REFERENCES `calculations` (`id`),
  CONSTRAINT `calculation_detail_others_item_id_foreign` FOREIGN KEY (`item_id`) REFERENCES `item_calculation_others` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- calculation_details (169 rows, business) ----
DROP TABLE IF EXISTS `calculation_details`;
CREATE TABLE `calculation_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `calculation_id` bigint(20) unsigned NOT NULL,
  `item_id` bigint(20) unsigned NOT NULL,
  `amount` double NOT NULL,
  `qty` double NOT NULL,
  `subtotal` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calculation_details_calculation_id_foreign` (`calculation_id`),
  KEY `calculation_details_item_id_foreign` (`item_id`),
  CONSTRAINT `calculation_details_calculation_id_foreign` FOREIGN KEY (`calculation_id`) REFERENCES `calculations` (`id`),
  CONSTRAINT `calculation_details_item_id_foreign` FOREIGN KEY (`item_id`) REFERENCES `item_calculations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- calculations (27 rows, business) ----
DROP TABLE IF EXISTS `calculations`;
CREATE TABLE `calculations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `booking_total` double NOT NULL DEFAULT 0,
  `calculation_total` double NOT NULL,
  `profit` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calculations_booking_id_foreign` (`booking_id`),
  CONSTRAINT `calculations_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- car_activities (0 rows, business) ----
DROP TABLE IF EXISTS `car_activities`;
CREATE TABLE `car_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `car_id` bigint(20) unsigned NOT NULL,
  `car_activity_code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `formula` varchar(255) NOT NULL,
  `price` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `car_activities_car_id_foreign` (`car_id`),
  CONSTRAINT `car_activities_car_id_foreign` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- car_configurations (24 rows, business) ----
DROP TABLE IF EXISTS `car_configurations`;
CREATE TABLE `car_configurations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `car_id` bigint(20) unsigned NOT NULL,
  `pax` tinyint(3) unsigned NOT NULL,
  `price` double NOT NULL,
  `crew_jvto_role_id` bigint(20) unsigned DEFAULT NULL,
  `crew_twt_role_id` bigint(20) unsigned DEFAULT NULL,
  `crew_klook_role_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `car_configurations_car_id_foreign` (`car_id`),
  KEY `car_configurations_crew_jvto_role_id_foreign` (`crew_jvto_role_id`),
  KEY `car_configurations_crew_twt_role_id_foreign` (`crew_twt_role_id`),
  KEY `car_configurations_crew_klook_role_id_foreign` (`crew_klook_role_id`),
  CONSTRAINT `car_configurations_car_id_foreign` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`) ON DELETE CASCADE,
  CONSTRAINT `car_configurations_crew_jvto_role_id_foreign` FOREIGN KEY (`crew_jvto_role_id`) REFERENCES `crew_roles` (`id`) ON DELETE SET NULL,
  CONSTRAINT `car_configurations_crew_klook_role_id_foreign` FOREIGN KEY (`crew_klook_role_id`) REFERENCES `crew_roles` (`id`) ON DELETE SET NULL,
  CONSTRAINT `car_configurations_crew_twt_role_id_foreign` FOREIGN KEY (`crew_twt_role_id`) REFERENCES `crew_roles` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- cars (27 rows, business) ----
DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `car_code` varchar(255) NOT NULL,
  `vendor_id` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `car_name` varchar(255) DEFAULT NULL,
  `garage_id` bigint(20) unsigned DEFAULT NULL,
  `banner` varchar(255) DEFAULT NULL,
  `start_pax` tinyint(4) DEFAULT NULL,
  `end_pax` tinyint(4) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `price_twt` decimal(10,2) DEFAULT NULL,
  `fuel` double DEFAULT NULL,
  `driver` double DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `interior` varchar(255) DEFAULT NULL,
  `interior_3d` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `is_publish` enum('0','1') NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `cars_garage_id_foreign` (`garage_id`),
  KEY `cars_vendor_id_foreign` (`vendor_id`),
  CONSTRAINT `cars_garage_id_foreign` FOREIGN KEY (`garage_id`) REFERENCES `garages` (`id`),
  CONSTRAINT `cars_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- carts (4 rows, business) ----
DROP TABLE IF EXISTS `carts`;
CREATE TABLE `carts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `package_price_id` bigint(20) unsigned NOT NULL,
  `package_id` bigint(20) unsigned NOT NULL,
  `travel_date` date NOT NULL,
  `pax` int(11) NOT NULL,
  `s` int(11) DEFAULT 0,
  `m` int(11) DEFAULT 0,
  `l` int(11) DEFAULT 0,
  `xl` int(11) DEFAULT 0,
  `xxl` int(11) DEFAULT 0,
  `total` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `carts_user_id_foreign` (`user_id`),
  KEY `carts_package_price_id_foreign` (`package_price_id`),
  KEY `carts_package_id_foreign` (`package_id`),
  CONSTRAINT `carts_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `carts_package_price_id_foreign` FOREIGN KEY (`package_price_id`) REFERENCES `package_prices` (`id`),
  CONSTRAINT `carts_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- categories (4 rows, business) ----
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `color` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- component_contents (0 rows, business) ----
DROP TABLE IF EXISTS `component_contents`;
CREATE TABLE `component_contents` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `component_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `page_name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `component_contents_component_id_foreign` (`component_id`),
  CONSTRAINT `component_contents_component_id_foreign` FOREIGN KEY (`component_id`) REFERENCES `components` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- components (0 rows, business) ----
DROP TABLE IF EXISTS `components`;
CREATE TABLE `components` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `key` varchar(255) NOT NULL,
  `component_name` varchar(255) NOT NULL,
  `preview` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- countries (244 rows, business) ----
DROP TABLE IF EXISTS `countries`;
CREATE TABLE `countries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `short_name` varchar(255) NOT NULL,
  `long_name` varchar(255) NOT NULL,
  `dial_code` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- crew_reviews (0 rows, business) ----
DROP TABLE IF EXISTS `crew_reviews`;
CREATE TABLE `crew_reviews` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_review_id` bigint(20) unsigned NOT NULL,
  `booking_id` bigint(20) unsigned NOT NULL,
  `crew_id` bigint(20) unsigned NOT NULL,
  `rate` tinyint(4) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `crew_reviews_booking_review_id_foreign` (`booking_review_id`),
  KEY `crew_reviews_booking_id_foreign` (`booking_id`),
  KEY `crew_reviews_crew_id_foreign` (`crew_id`),
  CONSTRAINT `crew_reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `crew_reviews_booking_review_id_foreign` FOREIGN KEY (`booking_review_id`) REFERENCES `booking_reviews` (`id`),
  CONSTRAINT `crew_reviews_crew_id_foreign` FOREIGN KEY (`crew_id`) REFERENCES `guide_drivers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- crew_roles (14 rows, business) ----
DROP TABLE IF EXISTS `crew_roles`;
CREATE TABLE `crew_roles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `crew_role_code` varchar(255) NOT NULL,
  `vendor_id` bigint(20) unsigned DEFAULT NULL,
  `order_channel_id` bigint(20) unsigned NOT NULL,
  `role` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `formula` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  `rate_twt` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `crew_roles_order_channel_id_foreign` (`order_channel_id`),
  KEY `crew_roles_vendor_id_foreign` (`vendor_id`),
  CONSTRAINT `crew_roles_order_channel_id_foreign` FOREIGN KEY (`order_channel_id`) REFERENCES `order_channels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `crew_roles_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- currency_exchange (0 rows, business) ----
DROP TABLE IF EXISTS `currency_exchange`;
CREATE TABLE `currency_exchange` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `currency_code` varchar(255) NOT NULL,
  `conversion_rates` double(12,8) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- debt_payment_details (0 rows, sensitive) ----
DROP TABLE IF EXISTS `debt_payment_details`;
CREATE TABLE `debt_payment_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `payment_id` bigint(20) unsigned NOT NULL,
  `booking_id` bigint(20) unsigned NOT NULL,
  `item_id` bigint(20) unsigned NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `item_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`item_data`)),
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `debt_payment_details_booking_id_foreign` (`booking_id`),
  KEY `debt_payment_details_payment_id_booking_id_index` (`payment_id`,`booking_id`),
  KEY `debt_payment_details_item_id_index` (`item_id`),
  CONSTRAINT `debt_payment_details_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `debt_payment_details_payment_id_foreign` FOREIGN KEY (`payment_id`) REFERENCES `debt_payments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- debt_payments (0 rows, sensitive) ----
DROP TABLE IF EXISTS `debt_payments`;
CREATE TABLE `debt_payments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `payment_number` varchar(255) NOT NULL,
  `vendor_id` bigint(20) unsigned NOT NULL,
  `item_type` enum('hotel','activity','bromo','car','others') NOT NULL,
  `payment_date` date NOT NULL,
  `payment_method_id` bigint(20) unsigned NOT NULL,
  `payment_proof` varchar(255) DEFAULT NULL,
  `note` text DEFAULT NULL,
  `total_amount` decimal(12,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `debt_payments_payment_method_id_foreign` (`payment_method_id`),
  KEY `debt_payments_payment_number_index` (`payment_number`),
  KEY `debt_payments_vendor_id_item_type_index` (`vendor_id`,`item_type`),
  KEY `debt_payments_payment_date_index` (`payment_date`),
  CONSTRAINT `debt_payments_payment_method_id_foreign` FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods` (`id`),
  CONSTRAINT `debt_payments_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- destination_activities (53 rows, business) ----
DROP TABLE IF EXISTS `destination_activities`;
CREATE TABLE `destination_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `destination_activity_code` varchar(255) NOT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `vendor_id` bigint(20) unsigned DEFAULT NULL,
  `activity_id` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `formula` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT 0.00,
  `is_twt` enum('0','1') NOT NULL DEFAULT '0',
  `is_default_jvto` enum('0','1') NOT NULL DEFAULT '0',
  `is_default_klook` enum('0','1') NOT NULL DEFAULT '0',
  `is_default_twt` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `destination_activities_destination_id_foreign` (`destination_id`),
  KEY `destination_activities_activity_id_foreign` (`activity_id`),
  KEY `destination_activities_vendor_id_foreign` (`vendor_id`),
  CONSTRAINT `destination_activities_activity_id_foreign` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `destination_activities_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `destination_activities_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- destination_details (6 rows, business) ----
DROP TABLE IF EXISTS `destination_details`;
CREATE TABLE `destination_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `destination_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `weather_by_season` varchar(255) DEFAULT NULL,
  `rainfall_intensity` varchar(255) DEFAULT NULL,
  `trail_details` varchar(255) DEFAULT NULL,
  `required_gear` varchar(255) DEFAULT NULL,
  `difficulty_level` varchar(255) DEFAULT NULL,
  `environmental_factors` varchar(255) DEFAULT NULL,
  `physical_requirements` varchar(255) DEFAULT NULL,
  `main_attractions` varchar(255) DEFAULT NULL,
  `best_time_to_visit` varchar(255) DEFAULT NULL,
  `tips_for_visitors` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `destination_details_destination_id_foreign` (`destination_id`),
  CONSTRAINT `destination_details_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- destinations (38 rows, business) ----
DROP TABLE IF EXISTS `destinations`;
CREATE TABLE `destinations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `destination_code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `overview` text DEFAULT NULL,
  `activity_id` bigint(20) unsigned DEFAULT NULL,
  `difficulty` varchar(255) DEFAULT NULL,
  `highlight` text DEFAULT NULL,
  `trek_details` text DEFAULT NULL,
  `health_safety` text DEFAULT NULL,
  `requirements` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `long` double DEFAULT NULL,
  `length` double DEFAULT NULL,
  `elevation_gain` double DEFAULT NULL,
  `route_type` varchar(255) DEFAULT NULL,
  `img_map` varchar(255) DEFAULT NULL,
  `trek_video` varchar(255) DEFAULT NULL,
  `tags` text DEFAULT NULL,
  `alltrails_map` text DEFAULT NULL,
  `gallery_id` bigint(20) unsigned NOT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `url` text NOT NULL,
  `calculation_order` tinyint(4) DEFAULT NULL,
  `is_publish` enum('0','1') NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `area_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `destinations_gallery_id_foreign` (`gallery_id`),
  KEY `destinations_activity_id_foreign` (`activity_id`),
  CONSTRAINT `destinations_activity_id_foreign` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`id`) ON DELETE SET NULL,
  CONSTRAINT `destinations_gallery_id_foreign` FOREIGN KEY (`gallery_id`) REFERENCES `galleries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- discounts (623 rows, business) ----
DROP TABLE IF EXISTS `discounts`;
CREATE TABLE `discounts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `gift_card_id` bigint(20) unsigned DEFAULT NULL,
  `disc` double NOT NULL,
  `type` enum('percent','nominal','per_pax') NOT NULL DEFAULT 'percent',
  `email` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `valid_until` date DEFAULT NULL,
  `verification_code` varchar(255) DEFAULT NULL,
  `is_verif` enum('0','1') NOT NULL DEFAULT '1',
  `is_used` enum('0','1') NOT NULL DEFAULT '0',
  `is_isic` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `discounts_user_id_foreign` (`user_id`),
  KEY `discounts_booking_id_foreign` (`booking_id`),
  KEY `discounts_gift_card_id_foreign` (`gift_card_id`),
  CONSTRAINT `discounts_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `discounts_gift_card_id_foreign` FOREIGN KEY (`gift_card_id`) REFERENCES `gift_cards` (`id`),
  CONSTRAINT `discounts_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=641 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- document_finders (20 rows, business) ----
DROP TABLE IF EXISTS `document_finders`;
CREATE TABLE `document_finders` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `url` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- durations (9 rows, business) ----
DROP TABLE IF EXISTS `durations`;
CREATE TABLE `durations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `day` tinyint(4) NOT NULL,
  `night` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- email_accounts (0 rows, business) ----
DROP TABLE IF EXISTS `email_accounts`;
CREATE TABLE `email_accounts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `from_name` varchar(255) DEFAULT NULL,
  `reply_to_mail` varchar(255) DEFAULT NULL,
  `reply_to_name` varchar(255) DEFAULT NULL,
  `provider_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `email_accounts_provider_id_foreign` (`provider_id`),
  CONSTRAINT `email_accounts_provider_id_foreign` FOREIGN KEY (`provider_id`) REFERENCES `email_providers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- email_providers (0 rows, business) ----
DROP TABLE IF EXISTS `email_providers`;
CREATE TABLE `email_providers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `host` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `encryption` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- event_sequences (0 rows, business) ----
DROP TABLE IF EXISTS `event_sequences`;
CREATE TABLE `event_sequences` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `no` int(11) NOT NULL,
  `start_time` time DEFAULT NULL,
  `itinerary_id` bigint(20) unsigned NOT NULL,
  `activity_destination_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_sequences_itinerary_id_foreign` (`itinerary_id`),
  KEY `event_sequences_activity_destination_id_foreign` (`activity_destination_id`),
  CONSTRAINT `event_sequences_activity_destination_id_foreign` FOREIGN KEY (`activity_destination_id`) REFERENCES `activity_destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `event_sequences_itinerary_id_foreign` FOREIGN KEY (`itinerary_id`) REFERENCES `itineraries` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- expense_additionals (55 rows, business) ----
DROP TABLE IF EXISTS `expense_additionals`;
CREATE TABLE `expense_additionals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(12,2) NOT NULL,
  `qty` int(11) NOT NULL,
  `subtotal` decimal(12,2) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `bill` varchar(255) DEFAULT NULL,
  `request_date` date DEFAULT NULL,
  `request_by` varchar(255) DEFAULT NULL,
  `submit_date` date DEFAULT NULL,
  `submit_by` bigint(20) unsigned DEFAULT NULL,
  `status` enum('pending','submitted','invoiced') NOT NULL DEFAULT 'pending',
  `approved_by` bigint(20) unsigned DEFAULT NULL,
  `approved_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `expense_additionals_booking_id_foreign` (`booking_id`),
  KEY `expense_additionals_submit_by_foreign` (`submit_by`),
  KEY `expense_additionals_approved_by_foreign` (`approved_by`),
  KEY `idx_expense_additionals_booking_status` (`booking_id`,`status`),
  CONSTRAINT `expense_additionals_approved_by_foreign` FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `expense_additionals_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `expense_additionals_submit_by_foreign` FOREIGN KEY (`submit_by`) REFERENCES `guide_drivers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- expense_refunds (70 rows, business) ----
DROP TABLE IF EXISTS `expense_refunds`;
CREATE TABLE `expense_refunds` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `type` enum('refund','penalty') NOT NULL DEFAULT 'refund',
  `item` varchar(255) NOT NULL,
  `refund_to` enum('office','customer') DEFAULT NULL,
  `proof_image` varchar(255) DEFAULT NULL,
  `item_id` varchar(255) DEFAULT NULL,
  `item_value` varchar(255) DEFAULT NULL,
  `item_source` varchar(255) DEFAULT NULL,
  `price` decimal(12,2) NOT NULL,
  `qty` int(11) NOT NULL,
  `subtotal` decimal(12,2) NOT NULL,
  `status` enum('pending','invoiced') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `expense_refunds_booking_id_foreign` (`booking_id`),
  CONSTRAINT `expense_refunds_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- expense_revisions (20 rows, business) ----
DROP TABLE IF EXISTS `expense_revisions`;
CREATE TABLE `expense_revisions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) DEFAULT NULL,
  `item_id` varchar(255) DEFAULT NULL,
  `item_value` varchar(255) DEFAULT NULL,
  `item_source` varchar(255) DEFAULT NULL,
  `qty` tinyint(4) NOT NULL,
  `price_before` decimal(12,2) NOT NULL,
  `price_after` decimal(12,2) NOT NULL,
  `total` decimal(12,2) NOT NULL,
  `status` enum('pending','approved','rejected') NOT NULL DEFAULT 'pending',
  `reason` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `expense_revisions_booking_id_foreign` (`booking_id`),
  CONSTRAINT `expense_revisions_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- experiences (0 rows, business) ----
DROP TABLE IF EXISTS `experiences`;
CREATE TABLE `experiences` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `background` varchar(255) DEFAULT NULL,
  `icon` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- extra_luggages (9 rows, business) ----
DROP TABLE IF EXISTS `extra_luggages`;
CREATE TABLE `extra_luggages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `price_maker_id` bigint(20) unsigned DEFAULT NULL,
  `extra_luggage` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `extra_luggages_price_maker_id_foreign` (`price_maker_id`),
  CONSTRAINT `extra_luggages_price_maker_id_foreign` FOREIGN KEY (`price_maker_id`) REFERENCES `price_makers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- failed_jobs (0 rows, framework) ----
DROP TABLE IF EXISTS `failed_jobs`;
CREATE TABLE `failed_jobs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(255) NOT NULL,
  `connection` text NOT NULL,
  `queue` text NOT NULL,
  `payload` longtext NOT NULL,
  `exception` longtext NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- faq_categories (12 rows, business) ----
DROP TABLE IF EXISTS `faq_categories`;
CREATE TABLE `faq_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `icon` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- faq_subcategories (28 rows, business) ----
DROP TABLE IF EXISTS `faq_subcategories`;
CREATE TABLE `faq_subcategories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `faq_category_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `faq_subcategories_faq_category_id_foreign` (`faq_category_id`),
  CONSTRAINT `faq_subcategories_faq_category_id_foreign` FOREIGN KEY (`faq_category_id`) REFERENCES `faq_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- faqs (63 rows, business) ----
DROP TABLE IF EXISTS `faqs`;
CREATE TABLE `faqs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `faq_category_id` bigint(20) unsigned NOT NULL,
  `faq_subcategory_id` bigint(20) unsigned DEFAULT NULL,
  `question` varchar(255) NOT NULL,
  `answer` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `faqs_faq_category_id_foreign` (`faq_category_id`),
  KEY `faqs_faq_subcategory_id_foreign` (`faq_subcategory_id`),
  CONSTRAINT `faqs_faq_category_id_foreign` FOREIGN KEY (`faq_category_id`) REFERENCES `faq_categories` (`id`) ON DELETE CASCADE,
  CONSTRAINT `faqs_faq_subcategory_id_foreign` FOREIGN KEY (`faq_subcategory_id`) REFERENCES `faq_subcategories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- fcm_tokens (3 rows, business) ----
DROP TABLE IF EXISTS `fcm_tokens`;
CREATE TABLE `fcm_tokens` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  `token` text NOT NULL,
  `device_type` varchar(255) NOT NULL DEFAULT 'web',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fcm_tokens_user_id_foreign` (`user_id`),
  CONSTRAINT `fcm_tokens_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- file_tags (0 rows, business) ----
DROP TABLE IF EXISTS `file_tags`;
CREATE TABLE `file_tags` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `file_id` bigint(20) unsigned NOT NULL,
  `tag_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_tags_file_id_tag_id_unique` (`file_id`,`tag_id`),
  KEY `file_tags_file_id_index` (`file_id`),
  KEY `file_tags_tag_id_index` (`tag_id`),
  CONSTRAINT `file_tags_file_id_foreign` FOREIGN KEY (`file_id`) REFERENCES `files` (`id`) ON DELETE CASCADE,
  CONSTRAINT `file_tags_tag_id_foreign` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- file_types (8 rows, business) ----
DROP TABLE IF EXISTS `file_types`;
CREATE TABLE `file_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `extension` varchar(20) NOT NULL,
  `icon_name` varchar(100) NOT NULL,
  `icon_color` varchar(50) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- files (223 rows, business) ----
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `original_name` varchar(255) NOT NULL,
  `folder_id` bigint(20) unsigned NOT NULL,
  `file_type_id` bigint(20) unsigned DEFAULT NULL,
  `size` bigint(20) NOT NULL,
  `path` varchar(1000) NOT NULL,
  `mime_type` varchar(100) DEFAULT NULL,
  `metadata` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`metadata`)),
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `files_folder_id_foreign` (`folder_id`),
  KEY `files_file_type_id_foreign` (`file_type_id`),
  CONSTRAINT `files_file_type_id_foreign` FOREIGN KEY (`file_type_id`) REFERENCES `file_types` (`id`),
  CONSTRAINT `files_folder_id_foreign` FOREIGN KEY (`folder_id`) REFERENCES `folders` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- flipbooks (5 rows, business) ----
DROP TABLE IF EXISTS `flipbooks`;
CREATE TABLE `flipbooks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `pdf` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flipbooks_slug_unique` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- folder_types (12 rows, business) ----
DROP TABLE IF EXISTS `folder_types`;
CREATE TABLE `folder_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `icon_name` varchar(100) NOT NULL,
  `icon_color` varchar(50) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- folders (105 rows, business) ----
DROP TABLE IF EXISTS `folders`;
CREATE TABLE `folders` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `parent_id` bigint(20) unsigned DEFAULT NULL,
  `folder_type_id` bigint(20) unsigned DEFAULT NULL,
  `path` varchar(1000) NOT NULL,
  `is_system_folder` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `folders_name_parent_id_unique` (`name`,`parent_id`),
  KEY `folders_parent_id_foreign` (`parent_id`),
  KEY `folders_folder_type_id_foreign` (`folder_type_id`),
  CONSTRAINT `folders_folder_type_id_foreign` FOREIGN KEY (`folder_type_id`) REFERENCES `folder_types` (`id`),
  CONSTRAINT `folders_parent_id_foreign` FOREIGN KEY (`parent_id`) REFERENCES `folders` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- galleries (352 rows, business) ----
DROP TABLE IF EXISTS `galleries`;
CREATE TABLE `galleries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `image` varchar(255) NOT NULL,
  `og_image` varchar(255) DEFAULT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `caption` varchar(255) NOT NULL,
  `alt_text` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `galleries_destination_id_foreign` (`destination_id`),
  CONSTRAINT `galleries_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=353 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- garages (1 rows, business) ----
DROP TABLE IF EXISTS `garages`;
CREATE TABLE `garages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `background` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- gift_cards (3 rows, business) ----
DROP TABLE IF EXISTS `gift_cards`;
CREATE TABLE `gift_cards` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- google_bills (0 rows, business) ----
DROP TABLE IF EXISTS `google_bills`;
CREATE TABLE `google_bills` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `month` tinyint(3) unsigned NOT NULL COMMENT '1-12',
  `year` smallint(5) unsigned NOT NULL,
  `google_cloud` bigint(20) NOT NULL DEFAULT 0,
  `google_ads` bigint(20) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `google_bills_month_year_unique` (`month`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- group_user (0 rows, business) ----
DROP TABLE IF EXISTS `group_user`;
CREATE TABLE `group_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- guide_drivers (74 rows, business) ----
DROP TABLE IF EXISTS `guide_drivers`;
CREATE TABLE `guide_drivers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `crew_level` enum('green','yellow','red') DEFAULT NULL,
  `crew_id` tinyint(4) DEFAULT NULL,
  `garage_id` bigint(20) unsigned DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `device_token` longtext DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `is_driver` tinyint(1) NOT NULL DEFAULT 0,
  `is_ijen` tinyint(1) NOT NULL DEFAULT 0,
  `crew_photo` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `star` double DEFAULT NULL,
  `guide_license` varchar(255) DEFAULT NULL,
  `driver_license` varchar(255) DEFAULT NULL,
  `ktp` varchar(255) DEFAULT NULL,
  `id_card` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `rank` tinyint(4) DEFAULT NULL,
  `tags` varchar(255) NOT NULL,
  `new_role` varchar(255) DEFAULT NULL COMMENT 'kolom untuk kategori role baru',
  `rate` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `guide_drivers_email_unique` (`email`),
  KEY `guide_drivers_garage_id_foreign` (`garage_id`),
  CONSTRAINT `guide_drivers_garage_id_foreign` FOREIGN KEY (`garage_id`) REFERENCES `garages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- hotel_images (18 rows, business) ----
DROP TABLE IF EXISTS `hotel_images`;
CREATE TABLE `hotel_images` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `image` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hotel_images_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `hotel_images_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- hotel_services (6 rows, business) ----
DROP TABLE IF EXISTS `hotel_services`;
CREATE TABLE `hotel_services` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `service` varchar(255) NOT NULL,
  `rate` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hotel_services_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `hotel_services_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- hotels (67 rows, business) ----
DROP TABLE IF EXISTS `hotels`;
CREATE TABLE `hotels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_code` varchar(255) NOT NULL,
  `vendor_id` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `short_name` varchar(255) DEFAULT NULL,
  `booking_code` varchar(255) DEFAULT NULL,
  `short_description` text DEFAULT NULL,
  `rating` decimal(3,2) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `facilities` longtext DEFAULT NULL,
  `address` text DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `banner` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `group_wa_id` varchar(255) DEFAULT NULL,
  `map_url` text DEFAULT NULL,
  `url` text NOT NULL DEFAULT '#',
  `lunch_rate` double DEFAULT NULL,
  `lunch_rate_twt` decimal(10,2) DEFAULT NULL,
  `dinner_rate` double DEFAULT NULL,
  `dinner_rate_twt` decimal(10,2) DEFAULT NULL,
  `is_publish` enum('0','1') NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `area_id` bigint(20) unsigned DEFAULT NULL,
  `area2_id` bigint(20) unsigned DEFAULT NULL,
  `double_rate` int(11) DEFAULT NULL,
  `twin_rate` int(11) DEFAULT NULL,
  `extra_bed_rate` int(11) DEFAULT NULL,
  `capsule_rate` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hotels_area_id_foreign` (`area_id`),
  KEY `hotels_area2_id_foreign` (`area2_id`),
  KEY `hotels_destination_id_foreign` (`destination_id`),
  KEY `hotels_vendor_id_foreign` (`vendor_id`),
  CONSTRAINT `hotels_area2_id_foreign` FOREIGN KEY (`area2_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `hotels_area_id_foreign` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `hotels_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`),
  CONSTRAINT `hotels_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- identities_types (0 rows, business) ----
DROP TABLE IF EXISTS `identities_types`;
CREATE TABLE `identities_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- identity_cards (0 rows, sensitive) ----
DROP TABLE IF EXISTS `identity_cards`;
CREATE TABLE `identity_cards` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `guide_driver_id` bigint(20) unsigned NOT NULL,
  `identity_type_id` bigint(20) unsigned NOT NULL,
  `front_file` varchar(255) NOT NULL,
  `back_file` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `identity_cards_guide_driver_id_foreign` (`guide_driver_id`),
  KEY `identity_cards_identity_type_id_foreign` (`identity_type_id`),
  CONSTRAINT `identity_cards_guide_driver_id_foreign` FOREIGN KEY (`guide_driver_id`) REFERENCES `guide_drivers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `identity_cards_identity_type_id_foreign` FOREIGN KEY (`identity_type_id`) REFERENCES `identities_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- image_panoramas (16 rows, business) ----
DROP TABLE IF EXISTS `image_panoramas`;
CREATE TABLE `image_panoramas` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `destination_id` bigint(20) unsigned NOT NULL,
  `image` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `image_panoramas_destination_id_foreign` (`destination_id`),
  CONSTRAINT `image_panoramas_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- include_excludes (58 rows, business) ----
DROP TABLE IF EXISTS `include_excludes`;
CREATE TABLE `include_excludes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `description` text NOT NULL,
  `type` enum('in','ex') NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- invoice_histories (1002 rows, sensitive) ----
DROP TABLE IF EXISTS `invoice_histories`;
CREATE TABLE `invoice_histories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `description` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  `qty` tinyint(4) NOT NULL,
  `line_total` double NOT NULL,
  `type` varchar(255) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_histories_booking_id_foreign` (`booking_id`),
  CONSTRAINT `invoice_histories_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1864 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- invoice_twt_details (3 rows, sensitive) ----
DROP TABLE IF EXISTS `invoice_twt_details`;
CREATE TABLE `invoice_twt_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_twt_id` bigint(20) unsigned NOT NULL,
  `booking_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_twt_details_invoice_twt_id_foreign` (`invoice_twt_id`),
  KEY `invoice_twt_details_booking_id_foreign` (`booking_id`),
  CONSTRAINT `invoice_twt_details_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoice_twt_details_invoice_twt_id_foreign` FOREIGN KEY (`invoice_twt_id`) REFERENCES `invoice_twts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- invoice_twts (2 rows, sensitive) ----
DROP TABLE IF EXISTS `invoice_twts`;
CREATE TABLE `invoice_twts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_no` varchar(255) NOT NULL,
  `invoice_date` date NOT NULL,
  `status` enum('Paid','Unpaid') NOT NULL,
  `total` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- item_activities (0 rows, business) ----
DROP TABLE IF EXISTS `item_activities`;
CREATE TABLE `item_activities` (
  `activity_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `category_id` bigint(20) unsigned NOT NULL,
  `activity_name` varchar(255) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `rate` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`activity_id`),
  KEY `item_activities_category_id_foreign` (`category_id`),
  CONSTRAINT `item_activities_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `item_activity_categories` (`category_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- item_activity_categories (0 rows, business) ----
DROP TABLE IF EXISTS `item_activity_categories`;
CREATE TABLE `item_activity_categories` (
  `category_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `category_code` varchar(50) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- item_calculation_others (27 rows, business) ----
DROP TABLE IF EXISTS `item_calculation_others`;
CREATE TABLE `item_calculation_others` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `item` varchar(255) NOT NULL,
  `rent` double DEFAULT NULL,
  `fuel` double DEFAULT NULL,
  `driver` double DEFAULT NULL,
  `qty` double DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `subtotal` double DEFAULT NULL,
  `type` enum('transport','other') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- item_calculations (91 rows, business) ----
DROP TABLE IF EXISTS `item_calculations`;
CREATE TABLE `item_calculations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `destination_id` bigint(20) unsigned DEFAULT NULL,
  `item` varchar(255) DEFAULT NULL,
  `qty` double DEFAULT NULL,
  `amount` double(15,2) DEFAULT NULL,
  `subtotal` double DEFAULT NULL,
  `parent_id` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `item_calculations_destination_id_foreign` (`destination_id`),
  CONSTRAINT `item_calculations_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itineraries (368 rows, business) ----
DROP TABLE IF EXISTS `itineraries`;
CREATE TABLE `itineraries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `day` tinyint(4) NOT NULL,
  `activity_start_id` bigint(20) unsigned DEFAULT NULL,
  `activity_end_id` bigint(20) unsigned DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `activity` text NOT NULL,
  `physical_demand` text DEFAULT NULL,
  `travel_logistic` text DEFAULT NULL,
  `short_activity` text DEFAULT NULL,
  `guide_book` longtext DEFAULT NULL,
  `b` enum('0','1') NOT NULL,
  `l` enum('0','1') NOT NULL,
  `d` enum('0','1') NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itineraries_package_id_foreign` (`package_id`),
  KEY `itineraries_activity_start_id_foreign` (`activity_start_id`),
  KEY `itineraries_activity_end_id_foreign` (`activity_end_id`),
  CONSTRAINT `itineraries_activity_end_id_foreign` FOREIGN KEY (`activity_end_id`) REFERENCES `activity_ends` (`id`),
  CONSTRAINT `itineraries_activity_start_id_foreign` FOREIGN KEY (`activity_start_id`) REFERENCES `activity_starts` (`id`),
  CONSTRAINT `itineraries_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=376 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_destinations (252 rows, business) ----
DROP TABLE IF EXISTS `itinerary_destinations`;
CREATE TABLE `itinerary_destinations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `itinerary_id` bigint(20) unsigned NOT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `second_destination_id` bigint(20) unsigned DEFAULT NULL,
  `activity_id` bigint(20) unsigned DEFAULT NULL,
  `second_activity_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_destinations_package_id_foreign` (`package_id`),
  KEY `itinerary_destinations_itinerary_id_foreign` (`itinerary_id`),
  KEY `itinerary_destinations_destination_id_foreign` (`destination_id`),
  KEY `itinerary_destinations_second_destination_id_foreign` (`second_destination_id`),
  KEY `itinerary_destinations_activity_id_foreign` (`activity_id`),
  KEY `itinerary_destinations_second_activity_id_foreign` (`second_activity_id`),
  CONSTRAINT `itinerary_destinations_activity_id_foreign` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_destinations_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`),
  CONSTRAINT `itinerary_destinations_itinerary_id_foreign` FOREIGN KEY (`itinerary_id`) REFERENCES `itineraries` (`id`),
  CONSTRAINT `itinerary_destinations_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `itinerary_destinations_second_activity_id_foreign` FOREIGN KEY (`second_activity_id`) REFERENCES `activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_destinations_second_destination_id_foreign` FOREIGN KEY (`second_destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=314 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_details (512 rows, business) ----
DROP TABLE IF EXISTS `itinerary_details`;
CREATE TABLE `itinerary_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `itinerary_id` bigint(20) unsigned NOT NULL,
  `no` int(11) NOT NULL,
  `time` varchar(255) DEFAULT NULL,
  `activity_id` bigint(20) unsigned DEFAULT NULL,
  `location_id` bigint(20) unsigned DEFAULT NULL,
  `notes` text DEFAULT NULL,
  `care_tip_for_tomorrow` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_details_itinerary_id_foreign` (`itinerary_id`),
  KEY `itinerary_details_activity_id_foreign` (`activity_id`),
  KEY `itinerary_details_location_id_foreign` (`location_id`),
  CONSTRAINT `itinerary_details_activity_id_foreign` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_details_itinerary_id_foreign` FOREIGN KEY (`itinerary_id`) REFERENCES `itineraries` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_details_location_id_foreign` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=630 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_invoices (86 rows, business) ----
DROP TABLE IF EXISTS `itinerary_invoices`;
CREATE TABLE `itinerary_invoices` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `day` tinyint(4) DEFAULT NULL,
  `activity` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_invoices_booking_id_foreign` (`booking_id`),
  CONSTRAINT `itinerary_invoices_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_meals (363 rows, business) ----
DROP TABLE IF EXISTS `itinerary_meals`;
CREATE TABLE `itinerary_meals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `itinerary_id` bigint(20) unsigned NOT NULL,
  `price_plan_id` bigint(20) unsigned NOT NULL,
  `breakfast` enum('0','1') NOT NULL DEFAULT '0',
  `lunch` enum('0','1') NOT NULL DEFAULT '0',
  `dinner` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_meals_itinerary_id_foreign` (`itinerary_id`),
  KEY `itinerary_meals_price_plan_id_foreign` (`price_plan_id`),
  CONSTRAINT `itinerary_meals_itinerary_id_foreign` FOREIGN KEY (`itinerary_id`) REFERENCES `itineraries` (`id`),
  CONSTRAINT `itinerary_meals_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=395 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_route_destinations (0 rows, business) ----
DROP TABLE IF EXISTS `itinerary_route_destinations`;
CREATE TABLE `itinerary_route_destinations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `itinerary_route_id` bigint(20) unsigned NOT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_route_destinations_itinerary_route_id_foreign` (`itinerary_route_id`),
  KEY `itinerary_route_destinations_destination_id_foreign` (`destination_id`),
  CONSTRAINT `itinerary_route_destinations_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_route_destinations_itinerary_route_id_foreign` FOREIGN KEY (`itinerary_route_id`) REFERENCES `itinerary_routes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_route_details (0 rows, business) ----
DROP TABLE IF EXISTS `itinerary_route_details`;
CREATE TABLE `itinerary_route_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `itinerary_route_id` bigint(20) unsigned NOT NULL,
  `time` time DEFAULT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `activity_category_id` bigint(20) unsigned NOT NULL,
  `activity` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_route_details_itinerary_route_id_foreign` (`itinerary_route_id`),
  KEY `itinerary_route_details_destination_id_foreign` (`destination_id`),
  KEY `itinerary_route_details_activity_category_id_foreign` (`activity_category_id`),
  CONSTRAINT `itinerary_route_details_activity_category_id_foreign` FOREIGN KEY (`activity_category_id`) REFERENCES `activity_categories` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_route_details_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_route_details_itinerary_route_id_foreign` FOREIGN KEY (`itinerary_route_id`) REFERENCES `itinerary_routes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- itinerary_routes (0 rows, business) ----
DROP TABLE IF EXISTS `itinerary_routes`;
CREATE TABLE `itinerary_routes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `route` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `pro_tips` text DEFAULT NULL,
  `start_destination_id` bigint(20) unsigned NOT NULL,
  `end_destination_id` bigint(20) unsigned NOT NULL,
  `breakfast` enum('yes','no') NOT NULL DEFAULT 'no',
  `lunch` enum('yes','no') NOT NULL DEFAULT 'no',
  `dinner` enum('yes','no') NOT NULL DEFAULT 'no',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itinerary_routes_start_destination_id_foreign` (`start_destination_id`),
  KEY `itinerary_routes_end_destination_id_foreign` (`end_destination_id`),
  CONSTRAINT `itinerary_routes_end_destination_id_foreign` FOREIGN KEY (`end_destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `itinerary_routes_start_destination_id_foreign` FOREIGN KEY (`start_destination_id`) REFERENCES `destinations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- job_batches (0 rows, framework) ----
DROP TABLE IF EXISTS `job_batches`;
CREATE TABLE `job_batches` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `total_jobs` int(11) NOT NULL,
  `pending_jobs` int(11) NOT NULL,
  `failed_jobs` int(11) NOT NULL,
  `failed_job_ids` longtext NOT NULL,
  `options` mediumtext DEFAULT NULL,
  `cancelled_at` int(11) DEFAULT NULL,
  `created_at` int(11) NOT NULL,
  `finished_at` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- jobs (0 rows, framework) ----
DROP TABLE IF EXISTS `jobs`;
CREATE TABLE `jobs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `queue` varchar(255) NOT NULL,
  `payload` longtext NOT NULL,
  `attempts` tinyint(3) unsigned NOT NULL,
  `reserved_at` int(10) unsigned DEFAULT NULL,
  `available_at` int(10) unsigned NOT NULL,
  `created_at` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_queue_index` (`queue`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- jvto_review_crews (111 rows, business) ----
DROP TABLE IF EXISTS `jvto_review_crews`;
CREATE TABLE `jvto_review_crews` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `jvto_review_id` bigint(20) unsigned NOT NULL,
  `crew_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jvto_review_crews_jvto_review_id_crew_id_unique` (`jvto_review_id`,`crew_id`),
  KEY `jvto_review_crews_crew_id_foreign` (`crew_id`),
  CONSTRAINT `jvto_review_crews_crew_id_foreign` FOREIGN KEY (`crew_id`) REFERENCES `guide_drivers` (`id`) ON DELETE CASCADE,
  CONSTRAINT `jvto_review_crews_jvto_review_id_foreign` FOREIGN KEY (`jvto_review_id`) REFERENCES `jvto_reviews` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- jvto_reviews (118 rows, business) ----
DROP TABLE IF EXISTS `jvto_reviews`;
CREATE TABLE `jvto_reviews` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) NOT NULL,
  `profile_photo` varchar(255) DEFAULT NULL,
  `platform` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `star` tinyint(4) DEFAULT NULL,
  `review` text NOT NULL,
  `photos` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=344 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- links (142 rows, business) ----
DROP TABLE IF EXISTS `links`;
CREATE TABLE `links` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `short_url` varchar(255) NOT NULL,
  `file` longtext NOT NULL,
  `type` enum('file','link') NOT NULL,
  `is_publish` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=321 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- locations (20 rows, business) ----
DROP TABLE IF EXISTS `locations`;
CREATE TABLE `locations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `map` text DEFAULT NULL,
  `images` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- mice_forms (5 rows, business) ----
DROP TABLE IF EXISTS `mice_forms`;
CREATE TABLE `mice_forms` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `company_website` varchar(255) DEFAULT NULL,
  `company_location` varchar(255) DEFAULT NULL,
  `attendees` varchar(255) DEFAULT NULL,
  `destinations` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `details` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- migrations (567 rows, framework) ----
DROP TABLE IF EXISTS `migrations`;
CREATE TABLE `migrations` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=600 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- note_categories (6 rows, business) ----
DROP TABLE IF EXISTS `note_categories`;
CREATE TABLE `note_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- order_channels (3 rows, business) ----
DROP TABLE IF EXISTS `order_channels`;
CREATE TABLE `order_channels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- others_activities (129 rows, business) ----
DROP TABLE IF EXISTS `others_activities`;
CREATE TABLE `others_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `other_activity_code` varchar(255) NOT NULL,
  `vendor_id` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `formula` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT 0.00,
  `is_twt` enum('0','1') NOT NULL DEFAULT '0',
  `is_default` enum('0','1') NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `others_activities_vendor_id_foreign` (`vendor_id`),
  CONSTRAINT `others_activities_vendor_id_foreign` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_activities (49 rows, business) ----
DROP TABLE IF EXISTS `package_activities`;
CREATE TABLE `package_activities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `long_name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `highlights` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `package_id` bigint(20) unsigned DEFAULT NULL,
  `is_single` enum('0','1') NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `package_activities_package_id_foreign` (`package_id`),
  CONSTRAINT `package_activities_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_activity_faqs (39 rows, business) ----
DROP TABLE IF EXISTS `package_activity_faqs`;
CREATE TABLE `package_activity_faqs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_activity_id` bigint(20) unsigned NOT NULL,
  `question` varchar(255) NOT NULL,
  `answer` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_activity_faqs_package_activity_id_foreign` (`package_activity_id`),
  CONSTRAINT `package_activity_faqs_package_activity_id_foreign` FOREIGN KEY (`package_activity_id`) REFERENCES `package_activities` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_activity_packages (65 rows, business) ----
DROP TABLE IF EXISTS `package_activity_packages`;
CREATE TABLE `package_activity_packages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `package_activity_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_activity_packages_package_id_foreign` (`package_id`),
  KEY `package_activity_packages_package_activity_id_foreign` (`package_activity_id`),
  CONSTRAINT `package_activity_packages_package_activity_id_foreign` FOREIGN KEY (`package_activity_id`) REFERENCES `package_activities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `package_activity_packages_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_banners (626 rows, business) ----
DROP TABLE IF EXISTS `package_banners`;
CREATE TABLE `package_banners` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `gallery_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_banners_package_id_foreign` (`package_id`),
  KEY `package_banners_gallery_id_foreign` (`gallery_id`),
  CONSTRAINT `package_banners_gallery_id_foreign` FOREIGN KEY (`gallery_id`) REFERENCES `galleries` (`id`),
  CONSTRAINT `package_banners_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1397 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_categories (6 rows, business) ----
DROP TABLE IF EXISTS `package_categories`;
CREATE TABLE `package_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `banner` varchar(255) NOT NULL,
  `banner_full` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_destinations (358 rows, business) ----
DROP TABLE IF EXISTS `package_destinations`;
CREATE TABLE `package_destinations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `destination_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_destinations_package_id_foreign` (`package_id`),
  KEY `package_destinations_destination_id_foreign` (`destination_id`),
  CONSTRAINT `package_destinations_destination_id_foreign` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`id`),
  CONSTRAINT `package_destinations_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=468 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_hotels (367 rows, business) ----
DROP TABLE IF EXISTS `package_hotels`;
CREATE TABLE `package_hotels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `price_plan_id` bigint(20) unsigned DEFAULT NULL,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `room_name` varchar(255) DEFAULT NULL,
  `day` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_hotels_package_id_foreign` (`package_id`),
  KEY `package_hotels_hotel_id_foreign` (`hotel_id`),
  KEY `package_hotels_price_plan_id_foreign` (`price_plan_id`),
  CONSTRAINT `package_hotels_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`),
  CONSTRAINT `package_hotels_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `package_hotels_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=400 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_include_excludes (1093 rows, business) ----
DROP TABLE IF EXISTS `package_include_excludes`;
CREATE TABLE `package_include_excludes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `include_exclude_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_include_excludes_package_id_foreign` (`package_id`),
  KEY `package_include_excludes_include_exclude_id_foreign` (`include_exclude_id`),
  CONSTRAINT `package_include_excludes_include_exclude_id_foreign` FOREIGN KEY (`include_exclude_id`) REFERENCES `include_excludes` (`id`),
  CONSTRAINT `package_include_excludes_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_meals (84 rows, business) ----
DROP TABLE IF EXISTS `package_meals`;
CREATE TABLE `package_meals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `price_plan_id` bigint(20) unsigned NOT NULL,
  `breakfast` tinyint(4) NOT NULL,
  `lunch` tinyint(4) NOT NULL,
  `dinner` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_meals_package_id_foreign` (`package_id`),
  KEY `package_meals_price_plan_id_foreign` (`price_plan_id`),
  CONSTRAINT `package_meals_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `package_meals_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_prices (556 rows, business) ----
DROP TABLE IF EXISTS `package_prices`;
CREATE TABLE `package_prices` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `price_plan_id` bigint(20) unsigned DEFAULT NULL,
  `price_category_id` bigint(20) unsigned NOT NULL,
  `price` double NOT NULL,
  `price_before_disc` double NOT NULL DEFAULT 0,
  `disc_percent` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `klook_retail_price` decimal(10,2) DEFAULT NULL,
  `klook_net_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_prices_package_id_foreign` (`package_id`),
  KEY `package_prices_price_category_id_foreign` (`price_category_id`),
  KEY `package_prices_price_plan_id_foreign` (`price_plan_id`),
  CONSTRAINT `package_prices_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `package_prices_price_category_id_foreign` FOREIGN KEY (`price_category_id`) REFERENCES `price_categories` (`id`),
  CONSTRAINT `package_prices_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=971 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- package_transportations (7 rows, business) ----
DROP TABLE IF EXISTS `package_transportations`;
CREATE TABLE `package_transportations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `price_plan_id` bigint(20) unsigned NOT NULL,
  `transportation_id` bigint(20) unsigned NOT NULL,
  `start_pax` tinyint(4) NOT NULL,
  `end_pax` tinyint(4) NOT NULL COMMENT '0 = Above',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `package_transportations_price_plan_id_foreign` (`price_plan_id`),
  KEY `package_transportations_transportation_id_foreign` (`transportation_id`),
  CONSTRAINT `package_transportations_price_plan_id_foreign` FOREIGN KEY (`price_plan_id`) REFERENCES `price_plans` (`id`),
  CONSTRAINT `package_transportations_transportation_id_foreign` FOREIGN KEY (`transportation_id`) REFERENCES `cars` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- packages (90 rows, business) ----
DROP TABLE IF EXISTS `packages`;
CREATE TABLE `packages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_code` varchar(255) NOT NULL,
  `uuid` char(36) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `new_name` varchar(255) DEFAULT NULL,
  `number` tinyint(4) DEFAULT NULL,
  `duration_id` bigint(20) unsigned NOT NULL,
  `category_id` bigint(20) unsigned NOT NULL,
  `package_activity_id` bigint(20) unsigned DEFAULT NULL,
  `package_category_id` bigint(20) unsigned DEFAULT NULL,
  `day_ijen` tinyint(4) DEFAULT NULL,
  `start_destination_id` bigint(20) unsigned DEFAULT NULL,
  `end_destination_id` bigint(20) unsigned DEFAULT NULL,
  `id_url` int(11) DEFAULT NULL,
  `package_platform` varchar(255) NOT NULL DEFAULT 'website',
  `overview` text NOT NULL,
  `key_highlights` text DEFAULT NULL,
  `ideal_arrival` varchar(255) DEFAULT NULL,
  `physicality` text DEFAULT NULL,
  `suitable_for` varchar(255) DEFAULT NULL,
  `short_description` text DEFAULT NULL,
  `block_description` text DEFAULT NULL,
  `meta_description` text DEFAULT NULL,
  `other_information` text NOT NULL,
  `nature_and_adventure` int(11) DEFAULT NULL,
  `relax_and_leisure` int(11) DEFAULT NULL,
  `cultural_heritage_and_local_life` int(11) DEFAULT NULL,
  `monuments_and_history` int(11) DEFAULT NULL,
  `photography_and_scenic_views` int(11) DEFAULT NULL,
  `accessibility_and_family_friendly` int(11) DEFAULT NULL,
  `departure` text DEFAULT NULL,
  `return` text DEFAULT NULL,
  `review_rating` double NOT NULL,
  `review_total` int(11) NOT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `url` text NOT NULL,
  `guide_book` text DEFAULT NULL,
  `is_publish` enum('0','1') NOT NULL DEFAULT '1',
  `b` tinyint(4) NOT NULL,
  `l` tinyint(4) NOT NULL,
  `d` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `experience_id` bigint(20) unsigned DEFAULT NULL,
  `google_merchant_product_id` varchar(255) DEFAULT NULL,
  `meta_catalogue_id` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `new_slug` varchar(255) DEFAULT NULL COMMENT 'Slug yang sesuai dengan database postgre, tidak pengaruh ke link paket',
  PRIMARY KEY (`id`),
  KEY `packages_duration_id_foreign` (`duration_id`),
  KEY `packages_category_id_foreign` (`category_id`),
  KEY `packages_start_destination_id_foreign` (`start_destination_id`),
  KEY `packages_end_destination_id_foreign` (`end_destination_id`),
  KEY `packages_package_activity_id_foreign` (`package_activity_id`),
  KEY `packages_experience_id_foreign` (`experience_id`),
  KEY `packages_package_category_id_foreign` (`package_category_id`),
  CONSTRAINT `packages_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `packages_duration_id_foreign` FOREIGN KEY (`duration_id`) REFERENCES `durations` (`id`),
  CONSTRAINT `packages_end_destination_id_foreign` FOREIGN KEY (`end_destination_id`) REFERENCES `destinations` (`id`),
  CONSTRAINT `packages_experience_id_foreign` FOREIGN KEY (`experience_id`) REFERENCES `experiences` (`id`) ON DELETE SET NULL,
  CONSTRAINT `packages_package_activity_id_foreign` FOREIGN KEY (`package_activity_id`) REFERENCES `package_activities` (`id`),
  CONSTRAINT `packages_package_category_id_foreign` FOREIGN KEY (`package_category_id`) REFERENCES `package_categories` (`id`) ON DELETE SET NULL,
  CONSTRAINT `packages_start_destination_id_foreign` FOREIGN KEY (`start_destination_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- pages (0 rows, business) ----
DROP TABLE IF EXISTS `pages`;
CREATE TABLE `pages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `page_name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `meta_title` varchar(255) DEFAULT NULL,
  `meta_description` text DEFAULT NULL,
  `schema_markup` text DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pages_slug_unique` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- participants (101 rows, business) ----
DROP TABLE IF EXISTS `participants`;
CREATE TABLE `participants` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `flight_number` varchar(255) DEFAULT NULL,
  `passport_number` varchar(255) NOT NULL,
  `tshirt_size` varchar(255) NOT NULL,
  `dietary_restriction` text DEFAULT NULL,
  `car_number` varchar(255) DEFAULT NULL,
  `seat_number` varchar(255) DEFAULT NULL,
  `room_number` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `participants_booking_id_foreign` (`booking_id`),
  CONSTRAINT `participants_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- partner_discount_codes (0 rows, business) ----
DROP TABLE IF EXISTS `partner_discount_codes`;
CREATE TABLE `partner_discount_codes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `partner_discount_id` bigint(20) unsigned NOT NULL,
  `discount_id` bigint(20) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `partner_discount_codes_partner_discount_id_foreign` (`partner_discount_id`),
  KEY `partner_discount_codes_discount_id_foreign` (`discount_id`),
  CONSTRAINT `partner_discount_codes_discount_id_foreign` FOREIGN KEY (`discount_id`) REFERENCES `discounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `partner_discount_codes_partner_discount_id_foreign` FOREIGN KEY (`partner_discount_id`) REFERENCES `partner_discounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- partner_discounts (0 rows, business) ----
DROP TABLE IF EXISTS `partner_discounts`;
CREATE TABLE `partner_discounts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `partner_discounts_username_unique` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- password_activations (0 rows, business) ----
DROP TABLE IF EXISTS `password_activations`;
CREATE TABLE `password_activations` (
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  KEY `password_activations_email_index` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- password_reset_tokens (0 rows, framework) ----
DROP TABLE IF EXISTS `password_reset_tokens`;
CREATE TABLE `password_reset_tokens` (
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- password_resets (2 rows, framework) ----
DROP TABLE IF EXISTS `password_resets`;
CREATE TABLE `password_resets` (
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  KEY `password_resets_email_index` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- payment_methods (7 rows, sensitive) ----
DROP TABLE IF EXISTS `payment_methods`;
CREATE TABLE `payment_methods` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `number` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- personal_access_tokens (364 rows, framework) ----
DROP TABLE IF EXISTS `personal_access_tokens`;
CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tokenable_type` varchar(255) NOT NULL,
  `tokenable_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `token` varchar(64) NOT NULL,
  `abilities` text DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=365 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- police_escorts (3 rows, business) ----
DROP TABLE IF EXISTS `police_escorts`;
CREATE TABLE `police_escorts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `start` longtext DEFAULT NULL,
  `finish` longtext DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `date` date DEFAULT NULL,
  `police_escort_type` enum('Polpar','Police Escort') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `police_escorts_booking_id_foreign` (`booking_id`),
  CONSTRAINT `police_escorts_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- pos_transfers (25 rows, business) ----
DROP TABLE IF EXISTS `pos_transfers`;
CREATE TABLE `pos_transfers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `rekening_number` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_categories (42 rows, business) ----
DROP TABLE IF EXISTS `price_categories`;
CREATE TABLE `price_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) DEFAULT NULL,
  `temp_text` varchar(255) NOT NULL,
  `start` tinyint(4) NOT NULL,
  `end` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_maker_location_details (135 rows, business) ----
DROP TABLE IF EXISTS `price_maker_location_details`;
CREATE TABLE `price_maker_location_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `price_maker_id` bigint(20) unsigned DEFAULT NULL,
  `price_maker_location_id` bigint(20) unsigned DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `rate` double DEFAULT NULL,
  `quantity_formula` varchar(255) DEFAULT NULL,
  `amount_formula` varchar(255) DEFAULT NULL,
  `pos_transfer_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `price_maker_location_details_price_maker_id_foreign` (`price_maker_id`),
  KEY `price_maker_location_details_price_maker_location_id_foreign` (`price_maker_location_id`),
  KEY `price_maker_location_details_pos_transfer_id_foreign` (`pos_transfer_id`),
  CONSTRAINT `price_maker_location_details_pos_transfer_id_foreign` FOREIGN KEY (`pos_transfer_id`) REFERENCES `pos_transfers` (`id`),
  CONSTRAINT `price_maker_location_details_price_maker_id_foreign` FOREIGN KEY (`price_maker_id`) REFERENCES `price_makers` (`id`),
  CONSTRAINT `price_maker_location_details_price_maker_location_id_foreign` FOREIGN KEY (`price_maker_location_id`) REFERENCES `price_maker_locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_maker_locations (37 rows, business) ----
DROP TABLE IF EXISTS `price_maker_locations`;
CREATE TABLE `price_maker_locations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `caption` varchar(255) DEFAULT NULL,
  `price_maker_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `price_maker_locations_price_maker_id_foreign` (`price_maker_id`),
  CONSTRAINT `price_maker_locations_price_maker_id_foreign` FOREIGN KEY (`price_maker_id`) REFERENCES `price_makers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_maker_price_paxs (126 rows, business) ----
DROP TABLE IF EXISTS `price_maker_price_paxs`;
CREATE TABLE `price_maker_price_paxs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `price_maker_id` bigint(20) unsigned DEFAULT NULL,
  `pax` tinyint(4) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `hpp_per_pax` double DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `price_maker_price_paxs_price_maker_id_foreign` (`price_maker_id`),
  CONSTRAINT `price_maker_price_paxs_price_maker_id_foreign` FOREIGN KEY (`price_maker_id`) REFERENCES `price_makers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_makers (9 rows, business) ----
DROP TABLE IF EXISTS `price_makers`;
CREATE TABLE `price_makers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_name` varchar(255) NOT NULL,
  `category_id` bigint(20) unsigned DEFAULT NULL,
  `duration_id` bigint(20) unsigned DEFAULT NULL,
  `is_edit` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `price_makers_duration_id_foreign` (`duration_id`),
  KEY `price_makers_category_id_foreign` (`category_id`),
  CONSTRAINT `price_makers_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `price_makers_duration_id_foreign` FOREIGN KEY (`duration_id`) REFERENCES `durations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- price_plans (3 rows, business) ----
DROP TABLE IF EXISTS `price_plans`;
CREATE TABLE `price_plans` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `background` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `icon` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- review_guides (10 rows, business) ----
DROP TABLE IF EXISTS `review_guides`;
CREATE TABLE `review_guides` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `guide_id` bigint(20) unsigned NOT NULL,
  `star` tinyint(4) DEFAULT NULL,
  `review` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `review_guides_booking_id_foreign` (`booking_id`),
  KEY `review_guides_guide_id_foreign` (`guide_id`),
  CONSTRAINT `review_guides_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `review_guides_guide_id_foreign` FOREIGN KEY (`guide_id`) REFERENCES `guide_drivers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- reviews (0 rows, business) ----
DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `package_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `date` date NOT NULL,
  `star` tinyint(4) NOT NULL,
  `review` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reviews_package_id_foreign` (`package_id`),
  KEY `reviews_user_id_foreign` (`user_id`),
  KEY `reviews_booking_id_foreign` (`booking_id`),
  CONSTRAINT `reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `reviews_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`),
  CONSTRAINT `reviews_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- role_user (0 rows, business) ----
DROP TABLE IF EXISTS `role_user`;
CREATE TABLE `role_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `role_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- room_configurations (0 rows, business) ----
DROP TABLE IF EXISTS `room_configurations`;
CREATE TABLE `room_configurations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `package_id` bigint(20) unsigned NOT NULL,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `room_hotel_id` bigint(20) unsigned NOT NULL,
  `group_size` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_configurations_package_id_foreign` (`package_id`),
  KEY `room_configurations_hotel_id_foreign` (`hotel_id`),
  KEY `room_configurations_room_hotel_id_foreign` (`room_hotel_id`),
  CONSTRAINT `room_configurations_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `room_configurations_package_id_foreign` FOREIGN KEY (`package_id`) REFERENCES `packages` (`id`) ON DELETE CASCADE,
  CONSTRAINT `room_configurations_room_hotel_id_foreign` FOREIGN KEY (`room_hotel_id`) REFERENCES `room_hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- room_hotel_configurations (182 rows, business) ----
DROP TABLE IF EXISTS `room_hotel_configurations`;
CREATE TABLE `room_hotel_configurations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `room_id` bigint(20) unsigned NOT NULL,
  `pax` tinyint(3) unsigned NOT NULL,
  `qty` tinyint(3) unsigned NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_hotel_configurations_hotel_id_foreign` (`hotel_id`),
  KEY `room_hotel_configurations_room_id_foreign` (`room_id`),
  CONSTRAINT `room_hotel_configurations_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `room_hotel_configurations_room_id_foreign` FOREIGN KEY (`room_id`) REFERENCES `room_hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- room_hotels (263 rows, business) ----
DROP TABLE IF EXISTS `room_hotels`;
CREATE TABLE `room_hotels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `room_hotel_code` varchar(255) NOT NULL,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `room_name` varchar(255) NOT NULL,
  `code` tinyint(4) DEFAULT NULL,
  `room_type` varchar(255) DEFAULT NULL,
  `photo` longtext DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `rate` int(11) DEFAULT NULL,
  `rate_twt` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_hotels_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `room_hotels_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=267 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- room_photos (0 rows, business) ----
DROP TABLE IF EXISTS `room_photos`;
CREATE TABLE `room_photos` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `room_hotel_id` bigint(20) unsigned NOT NULL,
  `photo` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_photos_hotel_id_foreign` (`hotel_id`),
  KEY `room_photos_room_hotel_id_foreign` (`room_hotel_id`),
  CONSTRAINT `room_photos_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `room_photos_room_hotel_id_foreign` FOREIGN KEY (`room_hotel_id`) REFERENCES `room_hotels` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- room_types (0 rows, business) ----
DROP TABLE IF EXISTS `room_types`;
CREATE TABLE `room_types` (
  `room_type_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `accommodation_id` bigint(20) unsigned NOT NULL,
  `room_type` varchar(255) NOT NULL,
  `rate_per_night` int(11) NOT NULL,
  `include_breakfast` tinyint(1) NOT NULL DEFAULT 0,
  `include_dinner` tinyint(1) NOT NULL DEFAULT 0,
  `extra_bed_option` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`room_type_id`),
  KEY `room_types_accommodation_id_foreign` (`accommodation_id`),
  CONSTRAINT `room_types_accommodation_id_foreign` FOREIGN KEY (`accommodation_id`) REFERENCES `accommodations` (`accommodation_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- services (14 rows, business) ----
DROP TABLE IF EXISTS `services`;
CREATE TABLE `services` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `service` varchar(100) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `area_id` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `services_area_id_foreign` (`area_id`),
  CONSTRAINT `services_area_id_foreign` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- sessions (6 rows, framework) ----
DROP TABLE IF EXISTS `sessions`;
CREATE TABLE `sessions` (
  `id` varchar(255) NOT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` text DEFAULT NULL,
  `payload` longtext NOT NULL,
  `last_activity` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sessions_user_id_index` (`user_id`),
  KEY `sessions_last_activity_index` (`last_activity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tags (4 rows, business) ----
DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `color` varchar(50) NOT NULL DEFAULT '#3B82F6',
  `description` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tags_name_unique` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- task_lists (0 rows, business) ----
DROP TABLE IF EXISTS `task_lists`;
CREATE TABLE `task_lists` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) unsigned NOT NULL,
  `list_text` text NOT NULL,
  `is_completed` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `task_lists_task_id_foreign` (`task_id`),
  CONSTRAINT `task_lists_task_id_foreign` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tasks (0 rows, business) ----
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- transport_bali_pricing (36 rows, business) ----
DROP TABLE IF EXISTS `transport_bali_pricing`;
CREATE TABLE `transport_bali_pricing` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `start_location` varchar(255) NOT NULL,
  `destination` varchar(255) NOT NULL,
  `avanza_price` decimal(10,2) DEFAULT NULL,
  `elf_short_price` decimal(10,2) DEFAULT NULL,
  `elf_long_price` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- trip_expense_items (0 rows, business) ----
DROP TABLE IF EXISTS `trip_expense_items`;
CREATE TABLE `trip_expense_items` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `trip_expense_location_id` bigint(20) unsigned NOT NULL,
  `price_maker_location_detail_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  `quantity` double NOT NULL,
  `amount` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `trip_expense_items_trip_expense_location_id_foreign` (`trip_expense_location_id`),
  KEY `trip_expense_items_price_maker_location_detail_id_foreign` (`price_maker_location_detail_id`),
  CONSTRAINT `trip_expense_items_price_maker_location_detail_id_foreign` FOREIGN KEY (`price_maker_location_detail_id`) REFERENCES `price_maker_location_details` (`id`),
  CONSTRAINT `trip_expense_items_trip_expense_location_id_foreign` FOREIGN KEY (`trip_expense_location_id`) REFERENCES `trip_expense_locations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- trip_expense_locations (0 rows, business) ----
DROP TABLE IF EXISTS `trip_expense_locations`;
CREATE TABLE `trip_expense_locations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `trip_expense_id` bigint(20) unsigned NOT NULL,
  `price_maker_location_id` bigint(20) unsigned NOT NULL,
  `location` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `trip_expense_locations_trip_expense_id_foreign` (`trip_expense_id`),
  KEY `trip_expense_locations_price_maker_location_id_foreign` (`price_maker_location_id`),
  CONSTRAINT `trip_expense_locations_price_maker_location_id_foreign` FOREIGN KEY (`price_maker_location_id`) REFERENCES `price_maker_locations` (`id`),
  CONSTRAINT `trip_expense_locations_trip_expense_id_foreign` FOREIGN KEY (`trip_expense_id`) REFERENCES `trip_expenses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- trip_expenses (0 rows, business) ----
DROP TABLE IF EXISTS `trip_expenses`;
CREATE TABLE `trip_expenses` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `price_maker_id` bigint(20) unsigned NOT NULL,
  `total` double NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `trip_expenses_booking_id_foreign` (`booking_id`),
  KEY `trip_expenses_price_maker_id_foreign` (`price_maker_id`),
  CONSTRAINT `trip_expenses_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `trip_expenses_price_maker_id_foreign` FOREIGN KEY (`price_maker_id`) REFERENCES `price_makers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculation_categories (9 rows, business) ----
DROP TABLE IF EXISTS `tw_calculation_categories`;
CREATE TABLE `tw_calculation_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `category` varchar(255) NOT NULL,
  `no` tinyint(4) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculation_category_codes (5 rows, business) ----
DROP TABLE IF EXISTS `tw_calculation_category_codes`;
CREATE TABLE `tw_calculation_category_codes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculation_details (5317 rows, business) ----
DROP TABLE IF EXISTS `tw_calculation_details`;
CREATE TABLE `tw_calculation_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tw_calculation_id` bigint(20) unsigned NOT NULL,
  `tw_calculation_category_id` bigint(20) unsigned NOT NULL,
  `tw_calculation_item_id` bigint(20) unsigned NOT NULL,
  `tw_calculation_item_detail_id` bigint(20) unsigned NOT NULL,
  `quantity` double NOT NULL,
  `rate` double NOT NULL,
  `amount` double NOT NULL,
  `is_paid` enum('0','1') NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tw_calculation_details_tw_calculation_item_detail_id_foreign` (`tw_calculation_item_detail_id`),
  KEY `tw_calculation_details_tw_calculation_item_id_foreign` (`tw_calculation_item_id`),
  KEY `tw_calculation_details_tw_calculation_category_id_foreign` (`tw_calculation_category_id`),
  KEY `tw_calculation_details_tw_calculation_id_foreign` (`tw_calculation_id`),
  CONSTRAINT `tw_calculation_details_tw_calculation_category_id_foreign` FOREIGN KEY (`tw_calculation_category_id`) REFERENCES `tw_calculation_categories` (`id`),
  CONSTRAINT `tw_calculation_details_tw_calculation_id_foreign` FOREIGN KEY (`tw_calculation_id`) REFERENCES `tw_calculations` (`id`),
  CONSTRAINT `tw_calculation_details_tw_calculation_item_detail_id_foreign` FOREIGN KEY (`tw_calculation_item_detail_id`) REFERENCES `tw_calculation_item_details` (`id`),
  CONSTRAINT `tw_calculation_details_tw_calculation_item_id_foreign` FOREIGN KEY (`tw_calculation_item_id`) REFERENCES `tw_calculation_items` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5615 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculation_item_details (248 rows, business) ----
DROP TABLE IF EXISTS `tw_calculation_item_details`;
CREATE TABLE `tw_calculation_item_details` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tw_calculation_item_id` bigint(20) unsigned NOT NULL,
  `pos_transfer_id` bigint(20) unsigned DEFAULT NULL,
  `no` tinyint(4) NOT NULL,
  `agent_code` bigint(20) NOT NULL,
  `category_code` bigint(20) unsigned DEFAULT NULL,
  `code` bigint(20) NOT NULL,
  `item` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `quantity` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  `is_check` enum('0','1') NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `destination_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tw_calculation_item_details_tw_calculation_item_id_foreign` (`tw_calculation_item_id`),
  KEY `tw_calculation_item_details_pos_transfer_id_foreign` (`pos_transfer_id`),
  KEY `tw_calculation_item_details_category_code_foreign` (`category_code`),
  CONSTRAINT `tw_calculation_item_details_category_code_foreign` FOREIGN KEY (`category_code`) REFERENCES `tw_calculation_category_codes` (`id`),
  CONSTRAINT `tw_calculation_item_details_pos_transfer_id_foreign` FOREIGN KEY (`pos_transfer_id`) REFERENCES `pos_transfers` (`id`),
  CONSTRAINT `tw_calculation_item_details_tw_calculation_item_id_foreign` FOREIGN KEY (`tw_calculation_item_id`) REFERENCES `tw_calculation_items` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculation_items (23 rows, business) ----
DROP TABLE IF EXISTS `tw_calculation_items`;
CREATE TABLE `tw_calculation_items` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `no` tinyint(4) NOT NULL,
  `tw_calculation_category_id` bigint(20) unsigned NOT NULL,
  `item` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tw_calculation_items_tw_calculation_category_id_foreign` (`tw_calculation_category_id`),
  CONSTRAINT `tw_calculation_items_tw_calculation_category_id_foreign` FOREIGN KEY (`tw_calculation_category_id`) REFERENCES `tw_calculation_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- tw_calculations (295 rows, business) ----
DROP TABLE IF EXISTS `tw_calculations`;
CREATE TABLE `tw_calculations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned DEFAULT NULL,
  `customer` varchar(255) DEFAULT NULL,
  `agent_id` bigint(20) unsigned NOT NULL DEFAULT 1,
  `date_start` date NOT NULL,
  `duration` tinyint(4) DEFAULT NULL,
  `pax` tinyint(4) DEFAULT NULL,
  `total` double NOT NULL DEFAULT 0,
  `paid` double NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tw_calculations_agent_id_foreign` (`agent_id`),
  KEY `tw_calculations_booking_id_foreign` (`booking_id`),
  CONSTRAINT `tw_calculations_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=315 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- twt_invoice_additionals (52 rows, sensitive) ----
DROP TABLE IF EXISTS `twt_invoice_additionals`;
CREATE TABLE `twt_invoice_additionals` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_id` bigint(20) unsigned NOT NULL,
  `expense_additional_id` bigint(20) unsigned NOT NULL,
  `total_amount` decimal(15,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `twt_invoice_additionals_invoice_id_foreign` (`invoice_id`),
  KEY `twt_invoice_additionals_expense_additional_id_foreign` (`expense_additional_id`),
  CONSTRAINT `twt_invoice_additionals_expense_additional_id_foreign` FOREIGN KEY (`expense_additional_id`) REFERENCES `expense_additionals` (`id`),
  CONSTRAINT `twt_invoice_additionals_invoice_id_foreign` FOREIGN KEY (`invoice_id`) REFERENCES `twt_invoices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- twt_invoice_bookings (49 rows, sensitive) ----
DROP TABLE IF EXISTS `twt_invoice_bookings`;
CREATE TABLE `twt_invoice_bookings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_id` bigint(20) unsigned NOT NULL,
  `booking_id` bigint(20) unsigned NOT NULL,
  `total_amount` decimal(15,2) NOT NULL,
  `notes` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `twt_invoice_bookings_invoice_id_foreign` (`invoice_id`),
  KEY `twt_invoice_bookings_booking_id_foreign` (`booking_id`),
  CONSTRAINT `twt_invoice_bookings_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `twt_invoice_bookings_invoice_id_foreign` FOREIGN KEY (`invoice_id`) REFERENCES `twt_invoices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- twt_invoice_payments (22 rows, sensitive) ----
DROP TABLE IF EXISTS `twt_invoice_payments`;
CREATE TABLE `twt_invoice_payments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_id` bigint(20) unsigned NOT NULL,
  `payment_date` date NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `transaction_reference` varchar(100) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `twt_invoice_payments_invoice_id_foreign` (`invoice_id`),
  CONSTRAINT `twt_invoice_payments_invoice_id_foreign` FOREIGN KEY (`invoice_id`) REFERENCES `twt_invoices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- twt_invoice_refunds_penalties (67 rows, sensitive) ----
DROP TABLE IF EXISTS `twt_invoice_refunds_penalties`;
CREATE TABLE `twt_invoice_refunds_penalties` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_id` bigint(20) unsigned NOT NULL,
  `expense_refund_id` bigint(20) unsigned NOT NULL,
  `total_amount` decimal(15,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `twt_invoice_refunds_penalties_invoice_id_foreign` (`invoice_id`),
  KEY `twt_invoice_refunds_penalties_expense_refund_id_foreign` (`expense_refund_id`),
  CONSTRAINT `twt_invoice_refunds_penalties_expense_refund_id_foreign` FOREIGN KEY (`expense_refund_id`) REFERENCES `expense_refunds` (`id`),
  CONSTRAINT `twt_invoice_refunds_penalties_invoice_id_foreign` FOREIGN KEY (`invoice_id`) REFERENCES `twt_invoices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- twt_invoices (18 rows, sensitive) ----
DROP TABLE IF EXISTS `twt_invoices`;
CREATE TABLE `twt_invoices` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invoice_number` varchar(50) NOT NULL,
  `invoice_date` date NOT NULL,
  `agent_id` bigint(20) unsigned NOT NULL,
  `total_bookings` decimal(15,2) NOT NULL DEFAULT 0.00,
  `total_additionals` decimal(15,2) NOT NULL DEFAULT 0.00,
  `total_refunds_penalties` decimal(15,2) NOT NULL DEFAULT 0.00,
  `grand_total` decimal(15,2) NOT NULL DEFAULT 0.00,
  `payment` decimal(15,2) NOT NULL DEFAULT 0.00,
  `balance` decimal(15,2) NOT NULL DEFAULT 0.00,
  `status` enum('unpaid','paid_partially','paid') NOT NULL DEFAULT 'unpaid',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `twt_invoices_invoice_number_unique` (`invoice_number`),
  KEY `twt_invoices_agent_id_foreign` (`agent_id`),
  CONSTRAINT `twt_invoices_agent_id_foreign` FOREIGN KEY (`agent_id`) REFERENCES `agents` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_accommodations (4 rows, business) ----
DROP TABLE IF EXISTS `user_accommodations`;
CREATE TABLE `user_accommodations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `hotel_id` bigint(20) unsigned NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_accommodations_hotel_id_foreign` (`hotel_id`),
  CONSTRAINT `user_accommodations_hotel_id_foreign` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_garages (2 rows, business) ----
DROP TABLE IF EXISTS `user_garages`;
CREATE TABLE `user_garages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_jeeps (3 rows, business) ----
DROP TABLE IF EXISTS `user_jeeps`;
CREATE TABLE `user_jeeps` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_logs (655 rows, business) ----
DROP TABLE IF EXISTS `user_logs`;
CREATE TABLE `user_logs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `log` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_logs_booking_id_foreign` (`booking_id`),
  KEY `user_logs_user_id_foreign` (`user_id`),
  CONSTRAINT `user_logs_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_logs_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=718 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_partners (35 rows, business) ----
DROP TABLE IF EXISTS `user_partners`;
CREATE TABLE `user_partners` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `updated_password` enum('0','1') NOT NULL DEFAULT '0',
  `app_type` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `otp` int(11) DEFAULT NULL,
  `status` enum('0','1') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_police_escorts (1 rows, business) ----
DROP TABLE IF EXISTS `user_police_escorts`;
CREATE TABLE `user_police_escorts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- user_tshirts (3 rows, business) ----
DROP TABLE IF EXISTS `user_tshirts`;
CREATE TABLE `user_tshirts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fcm_token` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- users (3568 rows, sensitive) ----
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `country_id` bigint(20) unsigned DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `google_id` varchar(255) DEFAULT NULL,
  `facebook_id` varchar(255) DEFAULT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `referral_code` varchar(255) DEFAULT NULL,
  `used` tinyint(4) DEFAULT NULL COMMENT 'How many the referral code used',
  `reward_type` enum('nominal','percentage') DEFAULT NULL,
  `reward_amount` decimal(15,2) DEFAULT 0.00,
  `discount_type` enum('nominal','percentage') DEFAULT NULL COMMENT 'discount type for new cust who use the referral code from the referrer',
  `discount_amount` decimal(15,2) DEFAULT 0.00 COMMENT 'discount amount for new cust who use the referral code from the referrer',
  `super` tinyint(1) NOT NULL DEFAULT 0,
  `preferences` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`preferences`)),
  `last_login` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_country_id_foreign` (`country_id`),
  CONSTRAINT `users_country_id_foreign` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3680 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- vendor_categories (4 rows, business) ----
DROP TABLE IF EXISTS `vendor_categories`;
CREATE TABLE `vendor_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- vendors (12 rows, business) ----
DROP TABLE IF EXISTS `vendors`;
CREATE TABLE `vendors` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `vendor_category_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `rekening_number` varchar(255) DEFAULT NULL,
  `rekening_person` varchar(255) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vendors_vendor_category_id_foreign` (`vendor_category_id`),
  CONSTRAINT `vendors_vendor_category_id_foreign` FOREIGN KEY (`vendor_category_id`) REFERENCES `vendor_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_chat_categories (26 rows, business) ----
DROP TABLE IF EXISTS `wa_chat_categories`;
CREATE TABLE `wa_chat_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wa_chat_categories_name_unique` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_chat_ignores (0 rows, business) ----
DROP TABLE IF EXISTS `wa_chat_ignores`;
CREATE TABLE `wa_chat_ignores` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `phone` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wa_chat_ignores_phone_unique` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_chat_summaries (640 rows, business) ----
DROP TABLE IF EXISTS `wa_chat_summaries`;
CREATE TABLE `wa_chat_summaries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `category_id` bigint(20) unsigned NOT NULL,
  `date` date NOT NULL,
  `summary` text NOT NULL,
  `chat_count` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_chat_summaries_user_id_foreign` (`user_id`),
  KEY `wa_chat_summaries_category_id_foreign` (`category_id`),
  CONSTRAINT `wa_chat_summaries_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `wa_chat_categories` (`id`),
  CONSTRAINT `wa_chat_summaries_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=641 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_chats (5547 rows, business) ----
DROP TABLE IF EXISTS `wa_chats`;
CREATE TABLE `wa_chats` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `message` text NOT NULL,
  `is_from_me` enum('0','1') NOT NULL COMMENT '0 = from user, 1 = from me',
  `has_media` enum('0','1') NOT NULL DEFAULT '0',
  `media_mime` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_chats_user_id_foreign` (`user_id`),
  CONSTRAINT `wa_chats_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5548 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_conversations (0 rows, business) ----
DROP TABLE IF EXISTS `wa_conversations`;
CREATE TABLE `wa_conversations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `contact_phone` varchar(30) NOT NULL COMMENT 'E.164 normalized, e.g. 628123456789',
  `contact_name` varchar(255) DEFAULT NULL COMMENT 'From WA profile or DB lookup',
  `jvto_number_key` varchar(100) NOT NULL COMMENT 'WA Pro CRM number_key identifying which JVTO number received',
  `inbox` enum('customer','b2b_partner','internal_ops') NOT NULL COMMENT 'Rules engine Step 2',
  `channel` enum('jvto_inquiry','jvto_post_booking','jvto_returning','klook','window','vendor_crew') NOT NULL COMMENT 'Rules engine Step 3',
  `state` varchar(50) NOT NULL COMMENT 'Per-channel state machine from Step 4, e.g. cold, quoted, klook_pre_tour',
  `booking_id` bigint(20) unsigned DEFAULT NULL COMMENT 'bookings.id — context thread for jvto_post_booking',
  `klook_booking_id` bigint(20) unsigned DEFAULT NULL COMMENT 'klook_bookings.id — context thread for klook channel',
  `language_detected` varchar(5) DEFAULT NULL COMMENT 'en, id, ms, de, fr',
  `last_inbound_at` timestamp NULL DEFAULT NULL,
  `last_outbound_at` timestamp NULL DEFAULT NULL,
  `sla_due_at` timestamp NULL DEFAULT NULL COMMENT 'Response deadline per SLA table in rules engine',
  `sla_breached` tinyint(1) NOT NULL DEFAULT 0,
  `pii_jurisdiction` enum('eu','other') NOT NULL DEFAULT 'other' COMMENT 'EU = mandatory GDPR redaction in wa_messages',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_conversations_contact_phone_index` (`contact_phone`),
  KEY `wa_conversations_contact_phone_jvto_number_key_index` (`contact_phone`,`jvto_number_key`),
  KEY `wa_conversations_channel_index` (`channel`),
  KEY `wa_conversations_state_index` (`state`),
  KEY `wa_conversations_sla_due_at_index` (`sla_due_at`),
  KEY `wa_conversations_last_inbound_at_index` (`last_inbound_at`),
  KEY `wa_conversations_sla_breached_channel_index` (`sla_breached`,`channel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_drafts (0 rows, business) ----
DROP TABLE IF EXISTS `wa_drafts`;
CREATE TABLE `wa_drafts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `conversation_id` bigint(20) unsigned NOT NULL,
  `trigger_message_id` bigint(20) unsigned NOT NULL,
  `body_draft` text NOT NULL COMMENT 'AI-generated draft text',
  `body_final` text DEFAULT NULL COMMENT 'Text after Inan/Sam edits — null if approved without changes',
  `status` enum('pending','approved','edited','rejected','expired','sent') NOT NULL DEFAULT 'pending',
  `tone_profile` varchar(50) NOT NULL COMMENT 'Brand voice applied: jvto_formal, post_booking_warm, klook_servicedesk, b2b_peer, ops_brief',
  `intent_slug` varchar(100) DEFAULT NULL COMMENT 'Intent this draft addresses',
  `template_id` bigint(20) unsigned DEFAULT NULL COMMENT 'wa_templates.id — base template used if any',
  `reviewed_by` varchar(20) DEFAULT NULL COMMENT 'inan or sam',
  `reviewed_at` timestamp NULL DEFAULT NULL,
  `sent_at` timestamp NULL DEFAULT NULL,
  `sent_message_id` bigint(20) unsigned DEFAULT NULL COMMENT 'wa_messages.id of the outbound message created on send',
  `reject_reason` text DEFAULT NULL,
  `expires_at` timestamp NOT NULL COMMENT 'Draft auto-expires if not reviewed — application sets 24h default',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_drafts_conversation_id_index` (`conversation_id`),
  KEY `wa_drafts_status_index` (`status`),
  KEY `wa_drafts_expires_at_index` (`expires_at`),
  KEY `wa_drafts_status_expires_at_index` (`status`,`expires_at`),
  KEY `wa_drafts_trigger_message_id_index` (`trigger_message_id`),
  KEY `wa_drafts_reviewed_by_index` (`reviewed_by`),
  CONSTRAINT `wa_drafts_conversation_id_foreign` FOREIGN KEY (`conversation_id`) REFERENCES `wa_conversations` (`id`) ON DELETE CASCADE,
  CONSTRAINT `wa_drafts_trigger_message_id_foreign` FOREIGN KEY (`trigger_message_id`) REFERENCES `wa_messages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_intent_taxonomy (0 rows, business) ----
DROP TABLE IF EXISTS `wa_intent_taxonomy`;
CREATE TABLE `wa_intent_taxonomy` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `inbox` enum('customer','b2b_partner','internal_ops','any') NOT NULL,
  `channel` varchar(50) NOT NULL COMMENT 'klook, jvto_inquiry, window, vendor_crew, * for any',
  `label` varchar(255) NOT NULL,
  `description` text DEFAULT NULL COMMENT 'Example messages for classifier grounding',
  `default_action` varchar(100) NOT NULL COMMENT 'auto_ack, auto_reply, draft_for_inan, escalate_inan, etc.',
  `min_confidence_auto` decimal(4,3) NOT NULL DEFAULT 0.850 COMMENT 'Threshold for auto_reply vs draft_for_inan',
  `risk_level` enum('low','medium','high') NOT NULL DEFAULT 'medium',
  `requires_human` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'True = always escalate, no auto action ever',
  `auto_reply_enabled` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Phase 5 gate: only true after >=70% draft approval rate sustained',
  `reject_rate_7d` decimal(5,2) DEFAULT NULL COMMENT 'Auto-computed: % drafts rejected past 7 days',
  `approval_rate_7d` decimal(5,2) DEFAULT NULL COMMENT 'Auto-computed: % drafts approved without edit past 7 days',
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wa_intent_taxonomy_slug_unique` (`slug`),
  KEY `wa_intent_taxonomy_inbox_channel_index` (`inbox`,`channel`),
  KEY `wa_intent_taxonomy_is_active_index` (`is_active`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_itineraries (2985 rows, business) ----
DROP TABLE IF EXISTS `wa_itineraries`;
CREATE TABLE `wa_itineraries` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `day` tinyint(4) NOT NULL,
  `message` longtext NOT NULL,
  `guide_book` longtext DEFAULT NULL,
  `status_guide_book` enum('0','1','00') NOT NULL DEFAULT '0',
  `status` enum('0','00','1') NOT NULL DEFAULT '0' COMMENT '0:Belum,00:Gagal,1:Sukses',
  `schedule` datetime NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_itineraries_booking_id_foreign` (`booking_id`),
  KEY `wa_itineraries_user_id_foreign` (`user_id`),
  CONSTRAINT `wa_itineraries_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `wa_itineraries_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7044 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_logs (3608 rows, business) ----
DROP TABLE IF EXISTS `wa_logs`;
CREATE TABLE `wa_logs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `message` longtext NOT NULL,
  `status` enum('0','1') NOT NULL,
  `error` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wa_logs_booking_id_foreign` (`booking_id`),
  KEY `wa_logs_user_id_foreign` (`user_id`),
  CONSTRAINT `wa_logs_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `wa_logs_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3621 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_messages (0 rows, business) ----
DROP TABLE IF EXISTS `wa_messages`;
CREATE TABLE `wa_messages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `conversation_id` bigint(20) unsigned NOT NULL,
  `wa_external_id` varchar(255) DEFAULT NULL COMMENT 'WA Pro CRM message ID — used for deduplication on webhook retries',
  `direction` enum('in','out') NOT NULL,
  `body` text DEFAULT NULL COMMENT 'Null for media-only messages',
  `body_redacted` text DEFAULT NULL COMMENT 'GDPR-redacted version for EU customers (pii_jurisdiction=eu)',
  `type` enum('text','image','audio','document','video','sticker','location') NOT NULL DEFAULT 'text',
  `media_url` varchar(500) DEFAULT NULL,
  `intent_classified` varchar(100) DEFAULT NULL COMMENT 'wa_intent_taxonomy.slug',
  `intent_confidence` decimal(4,3) DEFAULT NULL COMMENT '0.000–1.000',
  `risk_level` enum('low','medium','high') DEFAULT NULL,
  `urgency` enum('low','medium','high') DEFAULT NULL,
  `language_detected` varchar(5) DEFAULT NULL,
  `sender_type` enum('customer','ai','inan','sam','system') DEFAULT NULL COMMENT 'Populated for outbound messages',
  `action_taken` varchar(100) DEFAULT NULL COMMENT 'Rules engine action executed: auto_ack, draft_for_inan, escalate_inan, etc.',
  `hard_rule_triggered` varchar(100) DEFAULT NULL COMMENT 'Name of hard rule that blocked action, if any',
  `pii_redacted` tinyint(1) NOT NULL DEFAULT 0,
  `wa_timestamp` timestamp NOT NULL COMMENT 'Timestamp from WA Pro CRM webhook — not DB insert time',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wa_messages_wa_external_id_unique` (`wa_external_id`),
  KEY `wa_messages_conversation_id_index` (`conversation_id`),
  KEY `wa_messages_conversation_id_direction_index` (`conversation_id`,`direction`),
  KEY `wa_messages_intent_classified_index` (`intent_classified`),
  KEY `wa_messages_wa_timestamp_index` (`wa_timestamp`),
  KEY `wa_messages_direction_sender_type_index` (`direction`,`sender_type`),
  KEY `wa_messages_action_taken_index` (`action_taken`),
  CONSTRAINT `wa_messages_conversation_id_foreign` FOREIGN KEY (`conversation_id`) REFERENCES `wa_conversations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- wa_templates (0 rows, business) ----
DROP TABLE IF EXISTS `wa_templates`;
CREATE TABLE `wa_templates` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL COMMENT 'Internal identifier e.g. ack_off_hours_jvto_inquiry_en',
  `intent_slug` varchar(100) DEFAULT NULL COMMENT 'wa_intent_taxonomy.slug — null for generic templates',
  `language` enum('en','id','ms','de','fr','other') NOT NULL,
  `channel` varchar(50) DEFAULT NULL COMMENT 'klook, jvto_inquiry, * — null means universal',
  `body_md` text NOT NULL COMMENT 'Template body with {variable} placeholders',
  `variables` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'Array of required variable names e.g. ["name","tour_date","pickup_time"]' CHECK (json_valid(`variables`)),
  `tone_profile` varchar(50) DEFAULT NULL COMMENT 'Brand voice reference: jvto_formal, post_booking_warm, klook_servicedesk, b2b_peer, ops_brief',
  `approved_by` varchar(20) NOT NULL COMMENT 'sam or inan',
  `approved_at` timestamp NULL DEFAULT NULL,
  `version` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT 'Increment on revision',
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wa_templates_name_unique` (`name`),
  KEY `wa_templates_intent_slug_index` (`intent_slug`),
  KEY `wa_templates_language_channel_index` (`language`,`channel`),
  KEY `wa_templates_is_active_index` (`is_active`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- weather_codes (28 rows, business) ----
DROP TABLE IF EXISTS `weather_codes`;
CREATE TABLE `weather_codes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- website_link_categories (12 rows, business) ----
DROP TABLE IF EXISTS `website_link_categories`;
CREATE TABLE `website_link_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- website_links (11 rows, business) ----
DROP TABLE IF EXISTS `website_links`;
CREATE TABLE `website_links` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `link_category_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `header` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `schema` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `website_links_link_category_id_foreign` (`link_category_id`),
  CONSTRAINT `website_links_link_category_id_foreign` FOREIGN KEY (`link_category_id`) REFERENCES `website_link_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS=1;