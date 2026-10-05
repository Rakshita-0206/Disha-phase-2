# Disha Phase 2 — API Specification & Endpoint Reference

## Base URL
* Local: `http://127.0.0.1:8000`
* Production: `https://jee-college-finder-utmt-asov.onrender.com`

---

## 1. Recommendation Endpoint

### `POST /api/recommend`
Computes ranked college and branch recommendations based on candidate rank and preferences.

#### Request Body Schema
```json
{
  "rank": 6500,
  "rank_type": "JEE_MAIN",
  "seat_type": "OPEN",
  "gender": "Gender-Neutral",
  "home_state": "Madhya Pradesh",
  "interest_tags": ["Coding & software"],
  "institute_types": ["NIT", "IIIT"]
}
```

#### Response Structure
```json
{
  "status": "success",
  "summary": {
    "total_options": 142,
    "safe_count": 58,
    "target_count": 46,
    "reach_count": 38
  },
  "recommendations": [
    {
      "institute_name": "National Institute of Technology, Bhopal",
      "program_name": "Computer Science and Engineering",
      "quota": "HS",
      "seat_type": "OPEN",
      "opening_rank": 4820,
      "closing_rank": 7240,
      "probability": 0.82,
      "tier": "Safe",
      "interest_score": 1.0
    }
  ]
}
```

---

## 2. Statistical Aggregations Endpoint

### `GET /api/stats`
Retrieves precomputed dataset distributions, quota splits, and cutoff percentiles.

#### Query Parameters
* `year` (optional, integer): Dataset year (default: `2025`).
* `category` (optional, string): Reservation category filter (`OPEN`, `OBC-NCL`, `SC`, `ST`, `EWS`).

#### Response Sample
```json
{
  "total_records": 12143,
  "institutes_count": 128,
  "gender_cushion_ratio": 1.24,
  "cse_premium_index": 2.18
}
```

---

## 3. Health & Readiness Probe

### `GET /health`
Returns system status, memory allocation, and active model versions.
```json
{
  "status": "healthy",
  "version": "2.1.0",
  "dataset_loaded": true,
  "records_count": 12143
}
```

### Validation Constraints
* `rank`: Required integer $\ge 1$.
* `seat_type`: Must be one of `OPEN`, `OBC-NCL`, `SC`, `ST`, `EWS`, or associated PwD sub-tiers.
* `rank_type`: Strict enum matching either `JEE_MAIN` or `JEE_ADVANCED`.
* HTTP 422: Returned on malformed payload structure with detailed field-level path pointers.

### Sorting & Ranking Parameters
* Default ordering: Tier priority (`Safe` > `Target` > `Reach`) sorted descending by computed admission probability.
* Tie-breaker: Ordered by descending `interest_score` followed by ascending closing rank delta.

### Localization Support
* Header `Accept-Language`: Supports `en`, `hi`, `gu`, `kn`.
* UI templates dynamically switch label dictionaries without server re-computation.

### Statistical Metrics Schema
* `gender_cushion_ratio`: Ratio of female-only cutoff to gender-neutral cutoff.
* `cse_premium_index`: Ratio of overall branch median closing rank to CSE closing rank.
