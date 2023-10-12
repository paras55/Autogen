from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create assistant agent
assistant = AssistantAgent(name="assistant", llm_config={
                           "config_list": config_list})

# Create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "coding"},
    human_input_mode="NEVER")

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Do a prediction on who will win latest India vs Pakistan match based on past results")
