from english_detector.main import detect_english


class TestMain:
    text = 'Medium is a social publishing platform with a diverse array of metaverse and gaming-related articles and stories. View this article at medium.com.'

    def test_detect_english_return_value(self: 'TestMain') -> None:
        assert detect_english(self.text)

    def test_detect_english_return_type(self: 'TestMain') -> None:
        assert isinstance(detect_english(self.text), bool)

    def test_detect_english_no_text(self: 'TestMain') -> None:
        assert detect_english(None)
