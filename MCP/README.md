
# Town MCP Server

## Overview
The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for package management.

```shell
uv add "mcp[cli]"
```
## Run server
server will be run with sse mode,so you should provide one accessable url for our client.

```shell
mcp dev server.py
```

## What should you do in server.py
Code your tools or replace our methods/tools/resources to control your character.




## System Tools
> all of the tool's description is not the full description of system tools,you can rewrite it in your own way.
> other tools will be support in the future.

#### `generate_wake_up_hour(user: dict) -> list[hour: int]`
- **Description**: Generate the character's wake-up time. 
- **Result**: Must be a int between 0 and 23.

#### `generate_sleep_hour(user: dict) -> list[hour: int]`
- **Description**: Generate the character's sleeping time. if sleep hour is less than wake-up hour, it will be added to the next day.
- **Result**: Must be a int between 0 and 23.


#### `generate_daily_task(user: dict) -> list[task: dict]`
- **Description**: Generate the character's daily tasks from wake-up hour to sleep hour. Each task will last one hour.
- **Task Structure**:
  - `description`: A string used to generate task details.
  - `username`: A list of strings containing the names of all participants. The system will notify the participants. The available participants for the task are provided in the user dictionary (`dict`).

---

#### `generate_task_detail(user: dict, task: str) -> list[task: dict]`
- **Description**: Generate detailed information for a single task.
- **Task Structure**:
  - `duration`: A number of minutes, determining how long the task will take.
  - `description`: A string used to generate the task detail.

---

#### `generate_task_action_destination(map: dict, action: str) -> str`
- **Description**: Generate the destination for a character's task action.
- **Result**: Must be one of the positions in the map. If not, a random position will be selected within the current area.

---

#### `generate_task_action_object(objects: list, action: str) -> str`
- **Description**: Generate what will be use in character's task action.
- **Result**: Must be one object in memery, If not, a random object will be selected within the current area.

---

#### `generate_task_emoji_icon(action: str) -> str`
- **Description**: Generate an emoji icon representing the character's action.
- **Result Length**: Must be 1 or 2 characters.

---

#### `decide_whether_to_talk(from_user: dict) -> bool`
- **Description**: When someone enters your line of sight, decide whether to initiate a conversation.

---

#### `generate_dialogue(from_user: dict, user: dict) -> str`
- **Description**: Generate dialogue between two characters.
- **Result**: Must be a string.

---

#### `voting_for_world_events(event: str) -> bool`
- **Description**: Vote for world events.

---

#### `user_event(event: dict) -> None`
- **Description**: Notify players of user events.