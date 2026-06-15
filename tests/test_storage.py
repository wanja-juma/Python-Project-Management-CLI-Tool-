from utils.storage import save_data, load_data

def test_save_and_load(tmp_path):
    file = "test.json"
    data = [{"a": 1}]
    save_data(file, data)
    loaded = load_data(file)
    assert isinstance(loaded, list)