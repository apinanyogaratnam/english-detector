from english_detector.main import detect_english


class TestMain:
    def test_detect_english_return_value(self: 'TestMain') -> None:
        assert detect_english('this is english')

    def test_detect_english_return_type(self: 'TestMain') -> None:
        assert isinstance(detect_english('this is english'), bool)

    def test_detect_english_with_score(self: 'TestMain') -> None:
        assert detect_english('this is english', 0.98)
