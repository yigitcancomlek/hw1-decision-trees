import pytest
import pprint
import json
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

def load_json(json_path):
    if not os.path.isfile(json_path):
        return {}
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

@pytest.fixture(scope='function', autouse=True)
def log_test_result(request):
    yield
    test_result = load_json('tests/test_result.json')
    test_passed = not request.node.rep_call.failed
    test_result[request.node.name] = test_passed
    save_json(test_result, 'tests/test_result.json')

@pytest.fixture(scope="function", autouse=True)
def grade_assignment(request):
    test_result = load_json('tests/test_result.json')
    rubric = load_json('tests/rubric.json')
    report = {
        'score': 0,
        'notes': {}
    }
    total = 0.0

    for name, result in test_result.items():
        if rubric[name] == 'required':
            if not result:
                report['score'] = 0
                report['notes'][name] = (
                    f'Failed required test case {name} resulting in a 0.'
                )
                break
        else:
            if result:
                report['score'] += rubric[name]
            total += rubric[name]

    report['score'] = float(report['score'] / total) * 100

    save_json(report, 'tests/report.json')