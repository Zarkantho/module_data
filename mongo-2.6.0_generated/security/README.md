# Security

MongoDB security code

## Modules

### [Auditing](auditing)
TODO: auditing description

### [Authorization](authorization)
Authorization is the process of determining what a user is allowed to do in the system.  The five main entities in our authorization system are Users, Resources, Actions, Privileges, and Roles.

1. A User is the basic entity that operates on the system. 2. A Resource is something that the system provides that can be acted on by a User. 3. An Action is something that a User can do to a Resource. 4. A Privilege is a set of Actions that can performed on a given Resource. 5. A Role is a set of Priviliges.

Users can be assigned Roles and Privileges, which describe what the user is allowed to do.

Note that some of this code, such as the code to access the User data, is shared by the Authentication module.

### [Authentication](authentication)
Authentication is the way to securely verify the identity of a user. This is distinct from Authorization, which is what actually determines what each user is allowed to do once authenticated.  There are different mechanisms and protocols to perform authentication.  MongoDB has a challenge response protocol built in, but SASL and Kerberos authentication support requires the enterprise module.

### [Authentication Utilities](authentication\_utilities)
Utilities used for authentication

### [Legacy Code](legacy\_code)
Legacy Auth Code

