# test_app.py
import app

def test_main(capfd):
    app.main()
    captured = capfd.readouterr()
    assert "Hello, Jenkins!" in captured.out
