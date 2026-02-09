url https://api.anthropic.com/v1/messages \
        --header "x-api-key: sk-ant-api03-<INSERT-MY-KEY>" \
        --header "anthropic-version: 2023-06-01" \
        --header "content-type: application/json" \
        --data \
    '{
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'

# Response I got:

{"model":"claude-sonnet-4-20250514","id":"msg_01TsMq3AjTsNxvXt7PP54oQK","type":"message","role":"assistant","content":[{"type":"text","text":"Hello! It's nice to meet you. How are you doing today? Is there anything I can help you with or would you like to chat about?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":0},"output_tokens":34,"service_tier":"standard","inference_geo":"not_available"}}% 
