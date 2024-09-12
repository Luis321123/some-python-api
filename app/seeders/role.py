class Role:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    ADMINISTRATOR = {
        "name": "administrator",
        "description": "The highest level of authorization in the application"
    }


    MEMBER = {
        "name": "member",
        "description": "Role for the usual user who enters to the application like a church follower"
    }
    
    
    SUPERUSER = {
        "name": "superuser",
        "description": "The most highest level of authorization in the application and creation"
    }