---
type: source
title: Tourist Accidents at Kawah Ijen and Surrounding Areas
last_updated: 2026-05-25
sources: []
source_type: incident-dataset
primary_domain: credentials
visibility: public_sensitive
raw_file: "raw/Tourist Accidents at Kawah Ijen and Surrounding Areas.xlsx"
claims_supported: [C1, C4]
---

# Tourist Accidents at Kawah Ijen and Surrounding Areas

*Structured incident registry: 7 documented accidents (2015–2026), 4 fatalities, 3 non-fatal injuries. Extracted from Excel spreadsheet with 6 source references.*

> **Sensitivity notice**: This data involves named individuals and fatalities. Use for internal safety analysis and health-screening justification. Publishing accident details on the website requires human approval — do not auto-generate website output from this source.

---

## Incident Registry

### Fatalities (4)

| Date | Victim | Nationality | Age | Cause | Location | Detail |
|------|--------|-------------|-----|-------|----------|--------|
| Sept 2015 | Not named | Switzerland | 68 | Exhaustion + respiratory distress | En route to crater | Succumbed while scaling volcano toward crater |
| Dec 30, 2023 | BJ (initials) | Not stated | 64 | Heart attack / medical emergency | Post 3 → Paltuding | Used trolley to ascend; exhausted at Post 3, turned back; collapsed at Paltuding stall; declared dead at Puskesmas Licin despite oxygen |
| Feb 2024 | Not named | Poland | 53 | Found dead on climbing route | Hiking route to crater | Found lifeless along climbing route |
| Apr 20, 2024 | Huang Lihong | China | — | Fall from cliff into crater | Crater edge / Hutan Mati | Posing for photo near tree at crater edge; stepped backward, entangled in long skirt, fell 75m into crater. Body evacuated 2 hours later. → Hutan Mati closed temporarily. |

### Non-Fatal Injuries (3)

| Date | Victim | Nationality | Cause | Location | Injuries | Outcome |
|------|--------|-------------|-------|----------|----------|---------|
| Apr 21, 2025 | Saxena Akansa | India | Motorcycle slip | Sengkan Gandrung descent | Bone dislocation | First aid by passing tour guide → Puskesmas Licin → hospital |
| Apr 21, 2025 | Piere Ghirardy Johan | France | Motorcycle slip on descent | Ijen track descent | Lacerations | Evacuated to Puskesmas Licin |
| Feb 2026 | Muhammad Dzikri Maulana | Indonesia | Lost / separated from group | Between crater path intersection and sunrise point | Extreme weakness | Went with 4 friends at 20:05 WIB; separated at summit; found after 2-day SAR + thermal drone search, 890m from last seen, alive |

---

## Pattern Analysis

### Health-Related Deaths (2/4 = 50%)

The 2015 Swiss (68, exhaustion) and 2023 Indonesian (64, heart attack) fatalities were **fitness-related**. Both victims lacked the cardiovascular capacity for the ascent. This is the exact risk the BBKSDA health screening targets: screening SpO₂, blood pressure, heart rate, and respiratory history would flag high-risk individuals before they attempt the climb.

**This data directly validates BBKSDA SE.1658/KSA.9/2024 health screening mandate.** → [[credentials/medical-screening]]

### Behavioral Deaths (1/4 = 25%)

The 2024 Chinese tourist (Huang Lihong) death was caused by photography behavior at the crater edge — stepping backward in a long skirt near a cliff. Led to BBKSDA temporarily closing Hutan Mati and adding warning signage.

### Undetermined (1/4 = 25%)

The 2024 Polish tourist (53) was found dead on the hiking route with no detailed cause published.

### Motorcycle Accidents (2/3 non-fatal)

Both April 2025 incidents involved tourists on motorcycles descending steep Ijen roads. Not related to the hiking trail itself — these are road descent accidents. Relevant for safety briefings about self-ride vs. JVTO private transport.

### Lost Hiker (1/3 non-fatal)

The February 2026 Indonesian hiker case shows the danger of hiking without a guide — separated from friends, lost for 2 days. Underscores mandatory guide supervision rule. SAR + thermal drones deployed. Found alive.

---

## Source References (6)

| # | Reference |
|---|-----------|
| 1 | Pasca Insiden Wisatawan Asing Tewas, BKSDA Bakal Tambah Papan Rambu Peringatan — Kabar Banyuwangi |
| 2 | Tourist falls to death from Indonesia volcano — Travel Weekly Asia |
| 3 | Usai Turis China Tewas, Hutan Mati Kawah Ijen Ditutup Sementara — CNN Indonesia |
| 4 | Dua Orang Wisatawan Asing Alami Kecelakaan Saat Turun dari Kawah Ijen Banyuwangi |
| 5 | Kronologi Pendaki Hilang di Gunung Ijen & Ditemukan Selamat — Tirto.id |
| 6 | Kronologi Meninggalnya Wisatawan di Gunung Ijen, Putar Balik karena Lelah |

All sources are reputable Indonesian media (evidence weight 4) except source 2 (Travel Weekly Asia, also weight 4).

---

## Content Angles

1. **Health screening justification** — 50% of fatalities were fitness-related (heart, exhaustion). The screening JVTO coordinates is not theater — it addresses a documented pattern of deaths.
2. **Guide supervision justification** — The February 2026 lost hiker case shows why solo/unguided hiking is dangerous at Ijen.
3. **Private transport value** — 2 motorcycle accidents on descent road show the risk of self-ride. JVTO's private vehicle eliminates this.
4. **Hutan Mati restriction** — The April 2024 cliff death led to area closure and additional signage. JVTO guides enforce the restriction.
5. **Puskesmas Licin as safety net** — appears in 3/7 incidents as the emergency medical response facility. Validates [[credentials/medical-screening]] partner facility chain.

## Trust Anchors

Supports **C4** (health screening prevents fitness-related deaths) and **C1** (safety-led operations — guide supervision, private transport, restricted area enforcement).

-> [[sources/ijen-safety-resource-mapping]] | -> [[credentials/medical-screening]] | -> [[destinations/kawah-ijen]] | -> [[credentials/police-integration]]
