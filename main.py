import json

from jira_tool.setting import jira_api, zephyr_api
from jira_tool.jira_api.create_issue import CreateIssue
from models import Environment, AutomationDescription, User
from automation_body import generate_jira_automation_subtask_body
import asyncio
async def main():
	api = jira_api
	api_key = 'd2VpY2h1bmcuY2hlbmdAaXJvbnl1bi5jb206QVRBVFQzeEZmR0YwZFJ0aXhCa1lqYUZOZkZ5RFZBRHlneXFNVFpDTjg3UjhxTDVQMXRLU3pDRmJQLXQxalRzQk93S2lmcnEzSXNuanRlaklzR20wc2VTZklic2FEakxveXZIQ2VZcXRXRFg3NjY5QUk1cmxRcFFFWUxFRWZsVF9BS2h6YTFjU2YyN1NGYXRKcm5sTW5sbExyWG11NFRIMEJ0R3p4VUs3R05qVTF5ZUotQThQc01JPTk0OEE5MzBB'
	parent_id = "ANC-20312"
	due_date = "2025-02-07"
	environment = Environment.ONLINE_UPGRADE_DOCKER_ENVIRONMENT

	subtasks = [
		generate_jira_automation_subtask_body(parent_id, "Automation - API", AutomationDescription(
			environment,
			"https://drive.google.com/drive/u/2/folders/1cvnu6fJcevsroSdKgTQ63Y8WlBIzm5k3",
			"http://172.16.15.20:8080/job/QA/view/Automation%20-%20Vaidio%20Core/job/vaidio-core-api-automation/job/master/",
		), User.DD, due_date),
		generate_jira_automation_subtask_body(parent_id, "Automation - GUI", AutomationDescription(
			environment,
			"https://drive.google.com/drive/u/2/folders/1r-Cr2WQj5de_CMw40XzOT1IcVJKX4Xfy",
			"http://172.16.15.20:8080/job/QA/view/Automation%20-%20Vaidio%20Core/job/vaidio-core-ui-automation/job/master/",
		), User.WC, due_date),
		generate_jira_automation_subtask_body(parent_id, "Automation - Evaluation", AutomationDescription(
			environment,
			"https://drive.google.com/drive/u/2/folders/1OF8FcglXk-sflsdonCCAazdaGJwppfpQ",
			"http://172.16.15.20:8080/job/QA/view/Automation%20-%20Vaidio%20Core/job/vaidio-core-evaluation/job/master/",
		), User.WC, due_date),
		generate_jira_automation_subtask_body(parent_id, "Automation - GPU Memory Usage Estimation", AutomationDescription(
			environment,
			"https://drive.google.com/drive/u/2/folders/1Rg8BsM2vCqf00HjbtIqhJyqdDqYuWW0W",
			"http://172.16.15.20:8080/job/QA/view/Automation%20-%20Vaidio%20Core/job/gpu-memory-usage-estimation/",
		), User.WC, due_date),
		generate_jira_automation_subtask_body(parent_id, "Automation - Single Engine", AutomationDescription(
			environment,
			"https://drive.google.com/drive/u/2/folders/1NFmjn4A9RQTkbvnhuCRANVJq87_llJ8Y",
			"",
		), User.DD, due_date)
	]
	api.autorization_key = api_key
	# all_type = await jira_api.jira_api.create_issue(payload)
	for subtask in subtasks:
		result = await api.async_call(CreateIssue.params(subtask))
		a = result

if __name__ == "__main__":
	asyncio.run(main())