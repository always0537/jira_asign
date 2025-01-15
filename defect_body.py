import json
from models import DefectDescription, User
def generate_jira_defect_subtask_body(
    parent_id: str,
    description: DefectDescription,
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
            "summary": 'Defect Verification',
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
                                "text": 'Bug Fix Verification is a process of verifying if the bug was fixed or not. So at first, a tester re-tests the application and then checks whether new bugs appeared after the previous bug was fixed.',
                                "type": "text"
                            }
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
                                "text": 'Plan: ',
                                "type": "text"
                            },
                            {
                                "text": 'Please follow the assigned Jira.',
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'JQL: ',
                                "type": "text"
                            },
                            {
                                "text": f"ANC AND status != Closed AND fixVersion = {description.fix_version} AND assignee = {assignee.value}",
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