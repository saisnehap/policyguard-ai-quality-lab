from household import summarize_household

def test_summarize_household():
    data = {"size": 3, "state": "NM", "income": 45000}
    assert summarize_household(data) == "NM: 3 people"

def test_another_summarize_household():
    data = {"state": "AZ", "size": 2}
    assert summarize_household(data) == "AZ: 2 people"

    
    
def test_single_person_household():
    data = {"state": "NM", "size": 1}
    assert summarize_household(data) == "NM: 1 person"

def test_another_single_person_household():
   data = {"state": "CA", "size": 1}
   assert summarize_household(data)== "CA: 1 person"
 