---
type: source
title: Backoffice — Master Data Catalog
last_updated: 2026-05-25
sources: [backoffice-mysql]
---

# Backoffice Master Data — Reference Catalogs

Snapshot 2026-05-25. Seeded reference data backing all transactional tables.

## `accounts` — Chart of accounts / financial accounts

Rows: 3

| id | name |
|---|---|
| 1 | admin |
| 2 | sam |
| 3 | JVTO |

## `payment_methods` — Payment method options

Rows: 7

| id | name |
|---|---|
| 1 | Cash |
| 2 | PT JAVA VOLCANO RENDEZVOUS |
| 3 | Debit/Credit Card |
| 4 | EDC |
| 5 | WISE |
| 6 | Bank Transfer |
| 7 | Pay Later |

## `crew_roles` — Crew role catalog

Rows: 14

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| 11 |
| 12 |
| 13 |
| 14 |

## `booking_categories` — Booking category catalog

Rows: 3

| id | name | code |
|---|---|---|
| 1 | Reguler | R |
| 2 | Student | S |
| 3 | Klook | K |

## `vendor_categories` — Vendor categories

Rows: 4

| id | name |
|---|---|
| 1 | Accommodation |
| 2 | Activities |
| 3 | Transportation |
| 4 | Others |

## `activity_categories` — Activity categories

Rows: 7

| id | name | icon |
|---|---|---|
| 1 | Pickup | https://res.klook.com/image/upload/v1667274969/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_location_3x.png |
| 2 | Attraction | https://res.klook.com/image/upload/v1667274968/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_attraction_3x.png |
| 3 | Accommodation | https://res.klook.com/image/upload/v1667274969/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_stay_3x.png |
| 4 | Meals | https://res.klook.com/image/upload/v1667274968/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_dining_3x.png |
| 5 | Transportation | https://res.klook.com/image/upload/v1667274969/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_transport_car_3x.png |
| 6 | Drop Off | https://res.klook.com/image/upload/v1667274969/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_location_3x.png |
| 7 | Services | https://res.klook.com/image/upload/v1667274968/UED%20Team%EF%BC%88for%20DE%20only%EF%BC%89/Exp%20vertical/Itinerary/icon_category_attraction_3x.png |

## `accommodation_categories` — Accommodation categories

Rows: 4

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |

## `price_plans` — Price plans (B2B/B2C/Klook)

Rows: 3

| id | name | icon |
|---|---|---|
| 1 | Basic | basic.png |
| 2 | Reguler | reguler.png |
| 3 | Luxury | luxury.png |

## `price_categories` — Price categories (per-pax tiers)

Rows: 42

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| 11 |
| 12 |
| 13 |
| 14 |
| 15 |
| 16 |
| 17 |
| 18 |
| 19 |
| 20 |
| 21 |
| 22 |
| 23 |
| 24 |
| 25 |
| 26 |
| 27 |
| 28 |
| 29 |
| 30 |
| 31 |
| 32 |
| 33 |
| 34 |
| 35 |
| 36 |
| 37 |
| 38 |
| 39 |
| 40 |
| 41 |
| 42 |

## `services` — Service definitions

Rows: 14

| id |
|---|
| 12 |
| 13 |
| 14 |
| 15 |
| 16 |
| 17 |
| 18 |
| 19 |
| 20 |
| 21 |
| 22 |
| 23 |
| 24 |
| 25 |

## `tags` — Tag catalog

Rows: 4

| id | name | description |
|---|---|---|
| 2 | Invoice | Dokumen invoice |
| 9 | JVTO |  |
| 10 | TWT |  |
| 11 | KLOOK |  |

## `destinations` — Destination master

Rows: 38

| id | name | code | description |
|---|---|---|---|
| 1 | Mount Bromo | 2 | Mount Bromo or in Tenggerese spelled "Brama", also called the Tengger Caldera, is an active volcano in East Java, Indonesia. This mountain has a height of 2,329 meters above sea level and is located in four districts, namely Probolinggo Regency, Pasuruan Regency, Lumajang Regency, and Malang Regency. |
| 2 | Mount Ijen | 1 | Mount Ijen is a volcano located on the border of Banyuwangi Regency and Bondowoso Regency, East Java, Indonesia. This mountain has a height of 2,386 meters above sea level and is located side by side with Mount Merapi. Mount Ijen last erupted in 1999. One of the most famous natural phenomena of Mount Ijen is the blue fire. |
| 3 | Bali |  | Bali is a province in Indonesia whose capital city is Denpasar. The province of Bali is located in the western part of the Nusa Tenggara Islands. At the beginning of Indonesia's independence, this island was included in the Lesser Sunda Province with Singaraja as its capital, and is now divided into 3 provinces, namely Bali, West Nusa Tenggara and East Nusa Tenggara. |
| 4 | Surabaya | 4 | The city of Surabaya (Hanacaraka: ꦏꦹꦛꦯꦹꦫꦨꦪ; Javanese Pegon: اسورابايا, tr. Kutha Surabaya, Javanese pronunciation: [kuʈɔ surɔˈbɔjɔ]. Madura Pegon: , tr. Sorbhâjâh. Chinese: ) is the capital city of East Java Province, Indonesia, as well as a city largest metropolitan area in the province. Surabaya is the second largest city in Indonesia after Jakarta. |
| 5 | Malang City |  | Malang City (pronounced [malaŋ], Javanese: Hanacaraka: ꦩꦭꦁ, Pegon: الاڠ, Osob kiwalan: Ngalam) is a city located in the province of East Java, Indonesia, the second largest city in East Java after Surabaya, and the the 12th largest in Indonesia. |
| 6 | Madakaripura Waterfall |  | Madakaripura Waterfall is a waterfall located in Probolinggo Regency, East Java Province. This 200 meter high waterfall is the highest waterfall on the island of Java and the second highest in Indonesia. This waterfall is one of the waterfalls in the Bromo Tengger Semeru National Park area, precisely on the slopes of Mount Bromo. |
| 7 | Tumpak Sewu Waterfall | 3 | Tumpak Sewu Waterfall or also called Coban Sewu is a waterfall with a height of about 120 meters. This waterfall is bordered by Lumajang Regency and Malang Regency, East Java Province. Tumpak Sewu Waterfall has a water flow that resembles a curtain so it is included in the Tiered waterfall type. |
| 8 | Bromo Area |  | Cemoro Lawang is a settlement located between four areas, namely Probolinggo, Pasuruan, Malang, and Lumajang. Cemoro Lawang is one way to go to Mount Bromo National Park. Located in the village of Ngadisari, on the slopes of the Tengger mountains with an altitude of 2,200 meters above sea level, Sukapura, Probolinggo district. |
| 9 | Papuma Beach |  | Papuma Beach is a beach that has become a tourist spot in Jember Regency, East Java Province, Indonesia. The name Papuma itself is actually an abbreviation of "Malikan White Sand". Papuma Beach is located in Lojejer Village, Wuluhan District, Jember Regency . Papuma beach is one of the most popular and well-known beaches in Jember. |
| 10 | Jember City |  | Jember (Javanese: Hanacaraka: ꦗꦩ꧀ꦧꦼꦂ, Pegon: ) is a district in the province of East Java, Indonesia. The capital city of Jember Regency is Jember City which is located in the middle of the Horseshoe area, East Java Province. Administratively, Jember Regency is divided into 31 sub-districts consisting of 28 sub-districts with 226 villages and 3 sub-districts with 22 urban villages. |
| 11 | Djawatan |  |  |
| 12 | Banyuwangi City |  | Banyuwangi, previously known as Banjoewangi, is the administrative capital of Banyuwangi Regency at the far eastern end of the island of Java, Indonesia.
The town is also known as city of festival as many festivals are held throughout the year. Banyuwangi Regency is a tourist destination, and additional developments have been proposed to encourage international tourism by building necessary infrastructures. |
| 13 | I Gusti Ngurah Rai International Airport - Bali |  |  |
| 14 | Bondowoso City |  | Bondowoso Regency is a landlocked regency in East Java, Indonesia. It covers an area of 1,560.10 km2, and had a population of 736,772 at the 2010 Census[3] and 776,151 at the 2020 Census. The most common languages are Madurese and Javanese, although Madurese is the majority. The nearest large city is Surabaya, approximately five hours' drive away.

The administrative centre of the regency is the provincial town of Bondowoso, after which the regency in named. Common in most provincial towns is a park in the city centre, called "Alun-Alun"; Bondowoso is no exception. In the backdrop of the park is a view of a mountain ("gunung").

Tourist spots include Kawah Ijen, a crater lake. Kawah Ijen is managed jointly by two local governments, Bondowoso Regency and Banyuwangi Regency. In addition to the crater, other tourist destinations in Bondowoso are Tancak Kembar in Pakem and Air Terjun Belawan Sempol. A hike or climb to the crater takes around 1.5 to 3 hours. Other spots are Gunung Merapi and waterfalls. |
| 15 | Juanda International Aiport Surabaya |  |  |
| 16 | Pronojiwo, Lumajang |  |  |
| 17 | Yogyakarta |  |  |
| 18 | Coffee & Cocoa Science Technopark |  |  |
| 19 | Bangsring Underwater |  |  |
| 20 | Timang Beach |  |  |
| 21 | Borobudur Temple |  |  |
| 22 | Prambanan Temple |  |  |
| 23 | Timang Beach |  |  |
| 24 | Prambanan Temple |  |  |
| 25 | Batik Vilage |  |  |
| 26 | Punthuk Setumbu Hill |  |  |
| 27 | Phuntuk Setumbu Hill |  |  |
| 28 | Borobudur Temple |  |  |
| 29 | Taman Sari |  |  |
| 30 | Taman Sari |  |  |
| 31 | Sultan Palace |  |  |
| 32 | Pinus Pengger Forest |  |  |
| 33 | Timang Beach |  |  |
| 34 | Pinus Pengger Forest |  |  |
| 35 | Pinus Pengger Forest |  |  |
| 36 | Jomblang Cave |  |  |
| 37 | Others |  |  |
| 38 | Taman Safari Prigen |  | Taman Safari Indonesia (TSI) Prigen Jatim is a world-class zoo and titled the best conservation site by Indonesian Ministry of Forestry. |

## `areas` — Area master

Rows: 12

| id |
|---|
| 12 |
| 13 |
| 14 |
| 15 |
| 16 |
| 17 |
| 18 |
| 19 |
| 20 |
| 21 |
| 22 |
| 23 |

## `car_configurations` — Car configuration presets

Rows: 24

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| 11 |
| 12 |
| 13 |
| 14 |
| 15 |
| 16 |
| 17 |
| 18 |
| 19 |
| 20 |
| 21 |
| 22 |
| 23 |
| 24 |

## `room_hotel_configurations` — Room/hotel configuration presets

Rows: 182

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| 11 |
| 12 |
| 13 |
| 14 |
| 15 |
| 16 |
| 17 |
| 18 |
| 19 |
| 20 |
| 21 |
| 22 |
| 23 |
| 24 |
| 25 |
| 26 |
| 27 |
| 28 |
| 29 |
| 30 |
| 31 |
| 32 |
| 33 |
| 34 |
| 35 |
| 36 |
| 37 |
| 38 |
| 39 |
| 40 |
| 41 |
| 42 |
| 43 |
| 44 |
| 45 |
| 46 |
| 47 |
| 48 |
| 49 |
| 50 |

*(132 more rows)*

## `attachment_types` — Attachment type catalog

Rows: 7

| id | name |
|---|---|
| 1 | Flight Ticket |
| 2 | Train Ticket |
| 3 | Hotel Voucher |
| 4 | Passport |
| 5 | Student Card |
| 6 | The Window Booking Form |
| 7 | Booking Ticket |

## `file_types` — File type catalog

Rows: 8

| id |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |

## `folder_types` — Folder type catalog

Rows: 12

| id | name |
|---|---|
| 1 | default |
| 2 | bookings |
| 3 | schedules |
| 4 | invoices |
| 5 | expenses |
| 6 | crew_vehicle_assignments |
| 7 | financial_reports |
| 8 | customer_statistics |
| 9 | accommodations |
| 10 | destinations |
| 11 | activities |
| 12 | assets |

## `note_categories` — Note category catalog

Rows: 6

| id | name |
|---|---|
| 1 | General |
| 2 | Important |
| 3 | Follow-up |
| 4 | Completed |
| 5 | In Progress |
| 6 | Special |

## `weather_codes` — Weather code mapping

Rows: 28

| id | code | description |
|---|---|---|
| 1 | 0 | Clear sky |
| 2 | 1 | Mainly clear |
| 3 | 2 | Partly cloudy |
| 4 | 3 | Overcast |
| 5 | 45 | Fog  |
| 6 | 48 | Depositing rime fog |
| 7 | 51 | Light Drizzle |
| 8 | 53 | Moderate Drizzle |
| 9 | 55 | Dense intensity Drizzle |
| 10 | 56 | Light Freezing Drizzle |
| 11 | 57 | Dense intensity Freezing Drizzle |
| 12 | 61 | Slight Rain |
| 13 | 63 | Moderet Rain |
| 14 | 65 | Heavy Intensity Rain |
| 15 | 66 | Light Freezing Rain |
| 16 | 67 | Heavy Intensity Freezing Rain |
| 17 | 71 | Slight Snow Fall |
| 18 | 73 | Moderate Snow Fall |
| 19 | 75 | heavy Intensity Snow Fall |
| 20 | 77 | Snow Grains |
| 21 | 80 | Slight Rain Showers |
| 22 | 81 | Moderate Rain Showers |
| 23 | 82 | Violent Rain Ahowers |
| 24 | 85 | Snow Showers Alight  |
| 25 | 86 | Heavy |
| 26 | 95 | Slight or moderate Thunderstorm |
| 27 | 96 | Thunderstorm with slight |
| 28 | 99 | Heavy hail |

## `wa_chat_categories` — WhatsApp intent taxonomy

Rows: 26

| id | name | description |
|---|---|---|
| 1 | Dukungan Teknis | Percakapan terkait masalah teknis dan solusi yang diberikan. |
| 2 | Perencanaan Perjalanan | Percakapan terkait rencana perjalanan dan jadwal tur |
| 3 | Percakapan Kosong | Percakapan yang tidak mengandung pesan atau informasi penting. |
| 4 | Masalah Pembayaran | Percakapan terkait masalah atau kendala dalam proses pembayaran |
| 5 | Kendala Pembayaran | Percakapan terkait masalah atau kendala dalam proses pembayaran |
| 6 | Jadwal Perjalanan | Informasi mengenai jadwal perjalanan atau itinerary |
| 7 | Konfirmasi Jadwal | Percakapan terkait konfirmasi jadwal perjalanan atau aktivitas. |
| 12 | Informasi Perjalanan | Percakapan terkait detail dan persiapan perjalanan |
| 13 | Konfirmasi Booking | Percakapan terkait konfirmasi dan detail booking tur |
| 14 | Koordinator Lokasi | Percakapan terkait koordinasi lokasi dan pertemuan dengan tamu. |
| 15 | Hadiah dan Promo | Percakapan terkait pemberian hadiah, promo, atau voucher kepada pelanggan. |
| 16 | Umpan Balik Klien | Percakapan terkait umpan balik atau testimoni dari klien mengenai layanan. |
| 17 | Panduan Drone | Percakapan terkait permintaan informasi tentang lokasi dan aturan menerbangkan drone. |
| 18 | Undangan Gathering | Percakapan terkait undangan untuk menghadiri gathering atau pertemuan. |
| 19 | Pesanan Produk | Percakapan terkait pemesanan dan detail produk yang dipesan. |
| 20 | Permintaan Informasi | Percakapan terkait permintaan informasi atau pencarian data tertentu. |
| 21 | Daftar Pesanan | Percakapan terkait daftar pesanan atau informasi pelanggan. |
| 22 | Penawaran Kerja Sama | Percakapan terkait penawaran kerja sama atau kolaborasi bisnis yang tidak biasa. |
| 23 | Berbagi Dokumen | Percakapan terkait berbagi dokumen atau tautan ke dokumen. |
| 24 | Permintaan Produk | Percakapan terkait permintaan spesifikasi atau modifikasi produk. |
| 25 | Permintaan Desain | Percakapan terkait permintaan dan revisi desain untuk keperluan tertentu. |
| 26 | Pengembalian Dana | Percakapan terkait permintaan pengembalian dana atau sisa operasional. |
| 27 | Permintaan Khusus | Percakapan terkait permintaan khusus dari pelanggan. |
| 28 | Pilihan Menu | Percakapan terkait penawaran menu makanan dan minuman. |
| 29 | Pelunasan Produk | Percakapan terkait pelunasan pembayaran untuk produk tertentu. |
| 30 | Insiden Perjalanan | Percakapan terkait insiden atau kecelakaan yang terjadi selama perjalanan. |

## Cross-references
- [[sources/backoffice-schema]] — full table schema
- [[sources/backoffice-finance]] — uses `accounts`, `payment_methods`
- [[sources/backoffice-bookings-ops]] — uses `booking_categories`
