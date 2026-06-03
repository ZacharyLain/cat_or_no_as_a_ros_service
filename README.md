# cat_or_no_as_a_ros2_service

A ROS2 service for getting cats, sometimes

Combines [NaaS (No-as-a-Service)](https://github.com/hotheadhacker/no-as-a-service) and [CataaS (Cat-as-a-Service)](https://cataas.com/) into CoNaaS (Car-or-No-as-a-Service), and makes it available as a ROS2 service, resulting in a Cat-or-No-as-a-ROS2-Service (CoNaaRS).

```bash
ros2 run cat_or_no_as_a_ros2_service server
```

## Services

Service Name | Type | Description
--- | --- | ---
`/cat_or_no` | cat_or_no_as_a_ros_service/srv/CatOrNo.srv | Get a cat, maybe

## Published Topics

Topic Name | Type | Description
--- | --- | ---
`/cat` | cat_or_no_as_a_ros_service/msg/CatImage.msg | meow
