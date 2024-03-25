operation_parameter_map = {
    '/channels/{channel_id}-PATCH': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/channels/{channel_id}/inbound_messages-POST': {
        'parameters': [
            {
                'name': 'sender'
            },
            {
                'name': 'body'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'delivered_at'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/channels/{channel_id}/outbound_messages-POST': {
        'parameters': [
            {
                'name': 'to'
            },
            {
                'name': 'body'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'sender_name'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'delivered_at'
            },
            {
                'name': 'attachments'
            },
        ]
    },
};