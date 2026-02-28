from app import app

def test_home_page_loads():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    html = r.get_data(as_text=True)
    assert "Mini Randevu Portalı" in html

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"