from app.pricing import calculate_total


def test_returns_base_price_when_no_flags_are_used():
    assert calculate_total(100.0) == 108.0


def test_rejects_negative_prices():
    try:
        calculate_total(-1.0)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "non-negative" in str(exc)


def test_rounds_taxed_total_to_two_decimals():
    assert calculate_total(19.995) == 21.59
