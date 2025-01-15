import json
from models import RegressionDescription, User

def generate_jira_regression_subtask_body(
    parent_id: str,
    description: RegressionDescription,
    assignee: User,
    due_date: str):
    return json.dumps({
        "fields": {
            "project": {
                "id": "10000"
            },
            "issuetype": {
                "id": "10003"
            },
            "summary": "Regression Test",
            "parent": {
                "key": parent_id
            },
            "duedate": due_date,
            "assignee": {
                "id": assignee.value
            },
            "description": {
                "content": [
                    {
                        'content': [
                            {
                                "text": 'Whenever a new build is provided by the development team then the Software Testing team validates the build and ensures that no major issue exists.',
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "text": 'The testing team ensures that the build is stable and a detailed level of testing is carried out further. Smoke Testing checks that a no-show stopper defect exists in the build which will prevent the testing team to test the application in detail.',
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "text": 'If testers find that the major critical functionality is broken down at the initial stage itself then the testing team can reject the build and inform accordingly to the development team. Smoke Testing is carried out to a detailed level of any Functional or Regression Testing.',
                                "type": "text"
                            },
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'Test Environment Scope: ',
                                "type": "text"
                            },
                            {
                                "marks": [{'type': 'textColor', 'attrs': {'color': '#36b37e'}}],
                                "text": description.environment.value,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'Test Scope: ',
                                "type": "text"
                            },
                            {
                                "text": description.test_scope,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'Plan: ',
                                "type": "text"
                            },
                            {
                                "text": "Follow Zephyr’s plan.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            }
        }
    })