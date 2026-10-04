"""YOUR test suite — Part B (15 marks).

This file is graded by what it CATCHES, not by how much you write.

After the deadline your suite is run against five secret broken versions of
the Archive. Each contains exactly one realistic bug of a kind we have
discussed in class. You score 3 marks for each broken version your suite
detects — meaning at least one of your tests FAILS against it.

Two rules that decide whether you score at all:

  1. Your suite must PASS COMPLETELY against a correct implementation.
     A suite that fails everything "catches" all five bugs and scores ZERO.

  2. For validate_year you must include all four kinds of test data from
     Session 2: normal, abnormal, extreme, and boundary either side.

Where are the bugs? Where careless code always breaks: the edges. Test
1099/1100 and 1900/1901. Test empty strings and whitespace. Test a field
count that is wrong. Test upper case where you assumed lower.

Run yours with:   pytest tests/test_yours.py -v
"""

import pytest

from archive.errors import MalformedRecordError
from archive.storage import parse_line, load_archive, save_archive
from archive.validation import (
    validate_id,
    validate_title,
    validate_city,
    validate_year,
    validate_condition,
    validate_record,
)
from archive.queries import count_before, find_by_city, oldest, cities_summary


# ====================================================== WORKED EXAMPLE
# The four kinds of test data from Session 2, shown on validate_condition.
# Study the PATTERN here, then apply it yourself to the other fields.
# These five are given. They are not enough to catch anything on their own.

def test_condition_normal():
    """NORMAL — an ordinary accepted value."""
    assert validate_condition("fragile")[0] is True


def test_condition_normal_other():
    """NORMAL — the other accepted values matter too."""
    assert validate_condition("good")[0] is True


def test_condition_abnormal():
    """ABNORMAL — a value of the wrong kind entirely."""
    assert validate_condition("excellent")[0] is False


def test_condition_empty():
    """ABNORMAL — nothing at all is still the wrong kind."""
    assert validate_condition("")[0] is False


def test_condition_case():
    """A rule the brief states: the check is case-insensitive."""
    assert validate_condition("GOOD")[0] is True


# ============================================= NOW DO THIS FOR validate_year
# Required for Part B. The year rules are where the marks are, because the
# year rules are where careless code breaks. Write all four kinds:
#
#   NORMAL     a year from the middle of the range
#   ABNORMAL   something that is not a year at all
#   EXTREME    1100 and 1900 — valid, sitting exactly on the edge
#   BOUNDARY   1099 and 1901 — one step outside, must be rejected
#
# TODO: write them here.


def test_validate_year_normal():
    assert validate_year("1655")[0] is True


def test_validate_year_abnormal():
    assert validate_year("c.1590")[0] is False


def test_validate_year_extreme_low():
    assert validate_year("1100")[0] is True


def test_validate_year_extreme_high():
    assert validate_year("1900")[0] is True


def test_validate_year_boundary_below():
    assert validate_year("1099")[0] is False


def test_validate_year_boundary_above():
    assert validate_year("1901")[0] is False

def test_validate_year_empty():
    assert validate_year("")[0] is False

def test_validate_year_not_numeric():
    assert validate_year("12A4")[0] is False


# ============================================================== your tests
# Everything below is yours. Suggested coverage, in the order the marks are
# easiest to earn:
#
#   validate_id          format, length, case, empty
#   validate_title       whitespace-only, exactly 3 characters, shorter
#   validate_city        known, unknown, different case
#   validate_condition   each valid value, upper case, an invalid one
#   validate_record      a clean record, and one with several faults at once
#   parse_line           5 fields, 4 fields, 6 fields, whitespace around values
#   load_archive         missing file, the clean file, the messy file
#   save_archive         round trip: save then load gives back what you saved
#   queries              empty list, ties, case-insensitive city


GOOD_RECORD = {
    "id": "MS001",
    "title": "Tarikh al-Sudan",
    "city": "Timbuktu",
    "year": "1655",
    "condition": "fragile",
}

SAMPLE = [
    {"id": "MS001", "title": "Tarikh al-Sudan", "city": "Timbuktu", "year": "1655", "condition": "fragile"},
    {"id": "MS002", "title": "Kitab al-Tara'if", "city": "Djenne", "year": "1590", "condition": "good"},
    {"id": "MS003", "title": "Risala fi'l-Nujum", "city": "Timbuktu", "year": "1548", "condition": "fragile"},
]

def test_validate_id_accepts_good_format():
    assert validate_id("MS001")[0] is True


def test_validate_id_rejects_lowercase_prefix():
    assert validate_id("ms001")[0] is False


def test_validate_id_rejects_wrong_length():
    assert validate_id("MS1")[0] is False


def test_validate_id_rejects_non_numeric_suffix():
    assert validate_id("MS00A")[0] is False


def test_validate_id_rejects_empty_string():
    assert validate_id("")[0] is False


def test_validate_title_accepts_normal_string():
    assert validate_title("Tarikh al-Sudan")[0] is True


def test_validate_title_rejects_whitespace_only():
    assert validate_title("   ")[0] is False


def test_validate_title_rejects_too_short_after_strip():
    assert validate_title(" Ab ")[0] is False


def test_validate_title_accepts_exactly_three_characters():
    assert validate_title("abc")[0] is True


def test_validate_city_accepts_known_value_case_insensitive():
    assert validate_city("timbuktu")[0] is True


def test_validate_city_rejects_unknown_city():
    assert validate_city("Kano")[0] is False


def test_validate_city_accepts_other_known_city():
    assert validate_city("Gao")[0] is True

def test_validate_condition_accepts_other_valid_value():
    assert validate_condition("fair")[0] is True


def test_validate_condition_accepts_uppercase():
    assert validate_condition("GOOD")[0] is True


def test_validate_condition_rejects_invalid():
    assert validate_condition("excellent")[0] is False


def test_validate_condition_rejects_empty():
    assert validate_condition("")[0] is False


def test_validate_record_accepts_clean_record():
    assert validate_record(GOOD_RECORD) == []

def test_validate_record_rejects_multiple_faults():
    record_with_faults = {
        "id": "ms001",  # lowercase prefix
        "title": "  ",  # whitespace only
        "city": "UnknownCity",  # unknown city
        "year": "2000",  # out of range
        "condition": "excellent",  # invalid condition
    }
    errors = validate_record(record_with_faults)
    assert len(errors) == 5  # Expecting 5 errors for each field

def test_validate_record_accepts_partial_faults():
    record_with_partial_faults = {
        "id": "MS001",
        "title": "Valid Title",
        "city": "Timbuktu",
        "year": "2000",  # out of range
        "condition": "good",
    }
    errors = validate_record(record_with_partial_faults)
    assert len(errors) == 1  # Only the year should be invalid

