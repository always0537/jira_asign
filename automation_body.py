import json
from models import AutomationDescription, User

def generate_jira_automation_subtask_body(
    parent_id: str,
    summary: str,
    description: "AutomationDescription",
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
            "summary": summary,
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
                                "text": 'Whenever a new build is provided by the development team then the Software Testing team validates the build and ensures that no performance issue exists.',
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
                                "text": 'Follow Jenkins’ plan.',
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'Google Drive: ',
                                "type": "text"
                            },
                            {
                                "marks": [{'attrs': {'href': description.google_driver_url}, 'type': 'link'}],
                                "text": description.google_driver_url,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    },
                    {
                        'content': [
                            {
                                "marks": [{'type': 'strong'}],
                                "text": 'Jenkins: ',
                                "type": "text"
                            },
                            {
                                "marks": [{'attrs': {'href': description.jenkins_url}, 'type': 'link'}],
                                "text": description.jenkins_url,
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
