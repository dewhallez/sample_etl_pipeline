from scripts.generate_data import generate_data

def test_generate_data_shape():
    df = generate_data(100)
    assert df.shape[0] == 100
    assert 'sale_id' in df.columns

def test_generate_data_values():
    df = generate_data(10)
    assert (df['price'] > 0).all()
    assert df['year'].between(2000, 2025).all()
