Feature: Spin up AWS resources
    In order to automate AWS resource creation
    As a DevOps Engineer
    I want to run python that creates a VPC based on environment data
    Scenario: When I need a new VPC
        Given that the DevOps engineer has rights to execute cloudformation
            And  that their AWS client profiles are configured correctly
            And the default_ipv4_reservation_size is 24
            And ipv4_skip_broadcast_and_network is True
        When User submits a request for an IPBLock
            And the ip_version is IPV4
            And the namespace is msp_customer_namespace
            And the reservation_purpose is nat_for_angry_apples
        Then A new namespace (msp_customer_namespace) is stored with default settings
            And a new reservation (nat_for_angry_apples) is created : 10.0.0.0/24
            And a new allocation is created : 10.0.0.1/32 in nat_for_angry_apples

