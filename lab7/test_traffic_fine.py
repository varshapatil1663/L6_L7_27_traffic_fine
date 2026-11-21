
from hypothesis import given, strategies as st
from traffic_fine import parse_ticket_id, total_fines, speed_excess


@given(st.text() | st.none())
def test_parse_ticket_id_no_crash(s):
    try:
        parse_ticket_id(s)
    except Exception as e:
        assert False, f"parse_ticket_id crashed with: {e}"


@given(st.text() | st.none())
def test_total_fines_no_crash(s):
    try:
        total_fines(s)
    except Exception as e:
        assert False, f"total_fines crashed with: {e}"


@given(st.text() | st.none())
def test_speed_excess_no_crash(s):
    try:
        speed_excess(s)
    except Exception as e:
        assert False, f"speed_excess crashed with: {e}"
