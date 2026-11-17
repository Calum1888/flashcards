import pytest

from flashcards.__main__ import build_parser


def test_quiz_command_parses_deck():
    args = build_parser().parse_args(["quiz", "python"])
    assert args.command == "quiz"
    assert args.deck == "python"
    assert args.count is None


def test_quiz_command_parses_count_as_int():
    args = build_parser().parse_args(["quiz", "sql", "--count", "5"])
    assert args.count == 5


def test_list_command():
    args = build_parser().parse_args(["list"])
    assert args.command == "list"


def test_add_command_parses_deck():
    args = build_parser().parse_args(["add", "ml"])
    assert args.command == "add"
    assert args.deck == "ml"


def test_count_must_be_an_integer():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["quiz", "python", "--count", "abc"])


def test_command_is_required():
    with pytest.raises(SystemExit):
        build_parser().parse_args([])