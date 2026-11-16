from calculator import add

def test_add():
    assert add(2,3) ==5


def test_total_fee(fees):
    assert sum (fees) == 297


def test_write_file(tmp_path):
    output = tmp_path / "result.txt"
    output.write_text("5", encoding="utf-8")
    assert output.read_text(encoding="utf-8") == "5"


    