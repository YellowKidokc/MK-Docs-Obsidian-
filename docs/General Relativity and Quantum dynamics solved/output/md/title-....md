---
category: theophysics-research
date: '2025-09-28'
publish_to:
  production: false
  research: true
  template: false
status: published
tags:
- o
- theophysics
title: '------------------------------------------------------------...'
---
   
;------------------------------------------------------------------------------   
   
; Default Settings    
   
;------------------   
   
; default_api_key  : OpenAI API key - (https://platform.openai.com/account)   
   
;------------------------------------------------------------------------------   
   
[settings]   
   
default_api_key=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   
   
   
   
;------------------------------------------------------------------------------   
   
; Hotkeys     
   
;---------   
   
; ^ = Ctrl, ! = Alt, + = Shift, # = Win    
   
; See: (https://autohotkey.com/docs/Hotkeys.htm)    
   
;   
   
; hotkey_1        : (Required) The hotkey to select the current line and auto-run   
   
; hotkey_1_prompt : (Required) The prompt to use for the hotkey_1   
   
; hotkey_2        : (Required) The hotkey to select the current line and display   
   
;                   the prompt menu   
   
; menu_hotkey     : (Required) The hotkey to display the prompt menu   
   
;------------------------------------------------------------------------------   
   
hotkey_1        = ^+j   
   
hotkey_1_prompt = prompt_spelling   
   
hotkey_2        = ^+k      
   
menu_hotkey     = ^!+k     
   
    
   
;------------------------------------------------------------------------------   
   
; Misc. Settings   
   
;----------------   
   
; default_mode     : (Required) The default mode to use for the prompt   
   
; reload_on_change : (Optional:True/False:Defult True) If true, the script will   
   
;                     reload the settings.ini file if it is changed     
   
; cursor_wait_file : (Optional) The mouse cursor when waiting for response    
   
; debug            : (Optional) Enable writting debug logs to ./debug.log file   
   
; timeout          : (Optional) The number of seconds to wait for a response   
   
;------------------------------------------------------------------------------   
   
default_mode      = mode_chat_completion   
   
reload_on_change  = false   
   
timeout           = 120   
   
;cursor_wait_file = wait-1.ani   
   
;debug=true   
   
   
   
;------------------------------------------------------------------------------   
   
; Popup Menu   
   
;------------   
   
; Prompts to display in listed order in the popup menu     
   
; Values are the prompt name (see prompts section)   
   
; First 10 items are 1-0, then a-z, unless menu_text contains a & character to    
   
; indicate a hotkey   
   
; - = separator   
   
;------------------------------------------------------------------------------   
   
[popup_menu]   
   
prompt_spelling   
   
prompt_writting   
   
prompt_shorter   
   
prompt_longer   
   
prompt_tone_professional   
   
prompt_simplify   
   
   
-   
   
prompt_proof   
   
prompt_summarize   
   
prompt_explain   
   
prompt_items   
   
   
-   
   
prompt_code_optimize   
   
   
-   
   
prompt_continue   
   
   
   
;------------------------------------------------------------------------------   
   
; Prompts   
   
;---------   
   
; prompt           : (Required) The main prompt to prepend before to    
   
;                     the user input   
   
; mode             : (Required) The mode to be used for the prompt    
   
;                     - see modes section   
   
; menu_text        : (Optional) The text to be displayed in the popup  menu   
   
; prompt_system    : (Optional) The system prompt send of system input    
   
;                     for chat completion mode   
   
; prompt_end       : (Optional) Text to append to the end of user input   
   
; replace_selected : (Optional:True/False:Defult True) If true, the response    
   
;                     will be appended to the user input   
   
; response_start   : (Optional:Default "") The text to append between    
   
;                     the user input and the response   
   
; response_end     : (Optional:Default "") The text to append after the   
   
;                     response   
   
; ~mode overrides~ : (Optional) Any mode setting can be overriden for a    
   
;                      specific prompt   
   
; --   
   
;  Note: String values must be enclosed in double quotes and can use \n for    
   
;        new lines   
   
;------------------------------------------------------------------------------   
   
   
   
[prompt_spelling]   
   
prompt_system="I want you to act as an English spelling corrector and grammar improver. I want you to only reply the correction, the improvements and nothing else, do not write explanations. NEVER WRITE ANYTHING THAT IS NOT A CORRECTION OR IMPROVEMENT. NEVER SAY YOU ARE AN IA LANGUAGE MODEL."   
   
prompt="Correct the spelling (American English) and grammar of the following.\nInput: the caat in the hat\nThe cat in the hat.\nInput: The dog is black and white.\nOutput: The dog is black and white.\nInput: "   
   
prompt_end="\nOutput: "   
   
menu_text="Fix spelling && grammar"   
   
temperature=0   
   
   
   
[prompt_writting]   
   
prompt="Improve the writting for clarity and conciseness and correct the spelling (American English) and grammar of the following:\n\n"   
   
menu_text="Rewrite for clarity"   
   
   
   
[prompt_shorter]   
   
prompt="Make the following shorter:\n\n"   
   
menu_text="Make shorter"   
   
   
   
[prompt_longer]   
   
prompt="Make the following longer:\n\n"   
   
menu_text="Make longer"   
   
   
   
[prompt_tone_professional]   
   
prompt="Make the following more professional:\n\n"   
   
menu_text="Change Tone - Professional"   
   
   
   
[prompt_simplify]   
   
prompt="Simplify the following:\n\n"   
   
menu_text="Simplify language"   
   
   
   
[prompt_proof]   
   
prompt_system="I want you act as a English proofreader. I will provide you texts and I would like you to review them for any spelling, grammar, or punctuation errors. Once you have finished reviewing the text, provide me with a very detailed bullet list of suggestions and modifications to make and reasons why."   
   
prompt="My text is the following: "   
   
menu_text="Proofread"   
   
replace_selected=False   
   
response_start="\n\n"   
   
temperature=0   
   
   
   
[prompt_summarize]   
   
prompt="Summarize the following:\n\n"   
   
menu_text="Summarize"   
   
replace_selected=False   
   
response_start="\n"   
   
temperature=0   
   
   
   
[prompt_explain]   
   
prompt="Explain the following:\n\n"   
   
menu_text="Explain this"   
   
replace_selected=False   
   
response_start="\n"   
   
temperature=0   
   
   
   
[prompt_items]   
   
prompt="Summarize as a statement and identify any action items as a bullet list:\n\n"   
   
menu_text="Find action items"   
   
replace_selected=False   
   
response_start="\n"   
   
temperature=0   
   
   
   
[prompt_code_optimize]   
   
prompt_system="You are an assistant to a software engineer. You will be given a code snippet and you will be asked to optimize it for time and space complexity."   
   
prompt="Improve and explain how to optimize the following code:\n\n"   
   
prompt_end=""   
   
menu_text="Code - Optimize"   
   
replace_selected=False   
   
response_start="\n\n>>>>\n"   
   
response_end="\n<<<<\n"   
   
temperature=0   
   
   
   
[prompt_continue]   
   
prompt=""   
   
replace_selected=False   
   
menu_text="Space& - Continue writting"   
   
response_start=" "   
   
   
   
;------------------------------------------------------------------------------   
   
; Modes   
   
;-------   
   
; [mode_<name>]     : (Required) The name of the mode   
   
; endpoint          : (Required) The OpenAI API endpoint   
   
; model             : (Required) The OpenAI model to use   
   
; max_tokens        : (Optional) The maximum number of tokens to generate   
   
; temperature       : (Optional) The temperature of the model   
   
; top_p             : (Optional) The top_p of the model   
   
; frequency_penalty : (Optional) The frequency_penalty of the model   
   
; presence_penalty  : (Optional) The presence_penalty of the model   
   
; best_of           : (Optional) The best_of of the model   
   
; stop              : (Optional) The stop of the model   
   
; --   
   
; Note: Optional values vary depending on the mode and model - see OpenAI API   
   
;------------------------------------------------------------------------------   
   
   
   
; Default mode settings   
   
[mode_chat_completion]   
   
endpoint=[https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions)   
   
model="gpt-3.5-turbo"   
   
max_tokens=3000   
   
temperature=0.2   
   
top_p=1   
   
frequency_penalty=0.0   
   
presence_penalty=0.0   
   
   
   
; Azure mode settings - See: [https://docs.microsoft.com/en-us/azure/openai/quickstart](https://docs.microsoft.com/en-us/azure/openai/quickstart)   
   
[mode_chat_completion_azure]   
   
endpoint=[https://****.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview](https://****.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview)   
   
api_key=***   
   
model="gpt-3.5-turbo"   
   
max_tokens=2000   
   
temperature=0.2   
   
top_p=1   
   
best_of=1   
   
frequency_penalty=0.0   
   
presence_penalty=0.0   
   
stop=["###"]   
   
; See: (https://autohotkey.com/docs/Hotkeys.htm)    
;   
; hotkey_1        : (Required) The hotkey to select the current line and auto-run   
; hotkey_1_prompt : (Required) The prompt to use for the hotkey_1   
; hotkey_2        : (Required) The hotkey to select the current line and display   
;                   the prompt menu   
; menu_hotkey     : (Required) The hotkey to display the prompt menu   
;------------------------------------------------------------------------------   
hotkey_1        = ^+j   
hotkey_1_prompt = prompt_spelling   
hotkey_2        = ^+k      
menu_hotkey     = ^!+k     
    
;------------------------------------------------------------------------------   
; Misc. Settings   
;----------------   
; default_mode     : (Required) The default mode to use for the prompt   
; reload_on_change : (Optional:True/False:Defult True) If true, the script will   
;                     reload the settings.ini file if it is changed     
; cursor_wait_file : (Optional) The mouse cursor when waiting for response    
; debug            : (Optional) Enable writting debug logs to ./debug.log file   
; timeout          : (Optional) The number of seconds to wait for a response   
;------------------------------------------------------------------------------   
default_mode      = mode_chat_completion   
reload_on_change  = false   
timeout           = 120   
;cursor_wait_file = wait-1.ani   
;debug=true   
   
;------------------------------------------------------------------------------   
; Popup Menu   
;------------   
; Prompts to display in listed order in the popup menu     
; Values are the prompt name (see prompts section)   
; First 10 items are 1-0, then a-z, unless menu_text contains a & character to    
; indicate a hotkey   
; - = separator   
;------------------------------------------------------------------------------   
[popup_menu]   
prompt_spelling   
prompt_writting   
prompt_shorter   
prompt_longer   
prompt_tone_professional   
prompt_simplify   
   
-   
prompt_proof   
prompt_summarize   
prompt_explain   
prompt_items   
   
-   
prompt_code_optimize   
   
-   
prompt_continue   
   
;------------------------------------------------------------------------------   
; Prompts   
;---------   
; prompt           : (Required) The main prompt to prepend before to    
;                     the user input   
; mode             : (Required) The mode to be used for the prompt    
;                     - see modes section   
; menu_text        : (Optional) The text to be displayed in the popup  menu   
; prompt_system    : (Optional) The system prompt send of system input    
;                     for chat completion mode   
; prompt_end       : (Optional) Text to append to the end of user input   
; replace_selected : (Optional:True/False:Defult True) If true, the response    
;                     will be appended to the user input   
; response_start   : (Optional:Default "") The text to append between    
;                     the user input and the response   
; response_end     : (Optional:Default "") The text to append after the   
;                     response   
; ~mode overrides~ : (Optional) Any mode setting can be overriden for a    
;                      specific prompt   
; --   
;  Note: String values must be enclosed in double quotes and can use \n for    
;        new lines   
;------------------------------------------------------------------------------   
   
[prompt_spelling]   
prompt_system="I want you to act as an English spelling corrector and grammar improver. I want you to only reply the correction, the improvements and nothing else, do not write explanations. NEVER WRITE ANYTHING THAT IS NOT A CORRECTION OR IMPROVEMENT. NEVER SAY YOU ARE AN IA LANGUAGE MODEL."   
prompt="Correct the spelling (American English) and grammar of the following.\nInput: the caat in the hat\nThe cat in the hat.\nInput: The dog is black and white.\nOutput: The dog is black and white.\nInput: "   
prompt_end="\nOutput: "   
menu_text="Fix spelling && grammar"   
temperature=0   
   
[prompt_writting]   
prompt="Improve the writting for clarity and conciseness and correct the spelling (American English) and grammar of the following:\n\n"   
menu_text="Rewrite for clarity"   
   
[prompt_shorter]   
prompt="Make the following shorter:\n\n"   
menu_text="Make shorter"   
   
[prompt_longer]   
prompt="Make the following longer:\n\n"   
menu_text="Make longer"   
   
[prompt_tone_professional]   
prompt="Make the following more professional:\n\n"   
menu_text="Change Tone - Professional"   
   
[prompt_simplify]   
prompt="Simplify the following:\n\n"   
menu_text="Simplify language"   
   
[prompt_proof]   
prompt_system="I want you act as a English proofreader. I will provide you texts and I would like you to review them for any spelling, grammar, or punctuation errors. Once you have finished reviewing the text, provide me with a very detailed bullet list of suggestions and modifications to make and reasons why."   
prompt="My text is the following: "   
menu_text="Proofread"   
replace_selected=False   
response_start="\n\n"   
temperature=0   
   
[prompt_summarize]   
prompt="Summarize the following:\n\n"   
menu_text="Summarize"   
replace_selected=False   
response_start="\n"   
temperature=0   
   
[prompt_explain]   
prompt="Explain the following:\n\n"   
menu_text="Explain this"   
replace_selected=False   
response_start="\n"   
temperature=0   
   
[prompt_items]   
prompt="Summarize as a statement and identify any action items as a bullet list:\n\n"   
menu_text="Find action items"   
replace_selected=False   
response_start="\n"   
temperature=0   
   
[prompt_code_optimize]   
prompt_system="You are an assistant to a software engineer. You will be given a code snippet and you will be asked to optimize it for time and space complexity."   
prompt="Improve and explain how to optimize the following code:\n\n"   
prompt_end=""   
menu_text="Code - Optimize"   
replace_selected=False   
response_start="\n\n>>>>\n"   
response_end="\n<<<<\n"   
temperature=0   
   
[prompt_continue]   
prompt=""   
replace_selected=False   
menu_text="Space& - Continue writting"   
response_start=" "   
   
;------------------------------------------------------------------------------   
; Modes   
;-------   
; [mode_<name>]     : (Required) The name of the mode   
; endpoint          : (Required) The OpenAI API endpoint   
; model             : (Required) The OpenAI model to use   
; max_tokens        : (Optional) The maximum number of tokens to generate   
; temperature       : (Optional) The temperature of the model   
; top_p             : (Optional) The top_p of the model   
; frequency_penalty : (Optional) The frequency_penalty of the model   
; presence_penalty  : (Optional) The presence_penalty of the model   
; best_of           : (Optional) The best_of of the model   
; stop              : (Optional) The stop of the model   
; --   
; Note: Optional values vary depending on the mode and model - see OpenAI API   
;------------------------------------------------------------------------------   
   
; Default mode settings   
[mode_chat_completion]   
endpoint=[https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions)   
model="gpt-3.5-turbo"   
max_tokens=3000   
temperature=0.2   
top_p=1   
frequency_penalty=0.0   
presence_penalty=0.0   
   
; Azure mode settings - See: [https://docs.microsoft.com/en-us/azure/openai/quickstart](https://docs.microsoft.com/en-us/azure/openai/quickstart)   
[mode_chat_completion_azure]   
endpoint=[https://****.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview](https://****.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview)   
api_key=***   
model="gpt-3.5-turbo"   
max_tokens=2000   
temperature=0.2   
top_p=1   
best_of=1   
frequency_penalty=0.0   
presence_penalty=0.0   
stop=["###"]