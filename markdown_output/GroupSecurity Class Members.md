![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
GroupSecurity Class Members   
See Also Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3282.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : GroupSecurity Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [GroupSecurity](topic3282.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddUserActiveDirectoryId](topic3288.md)| Adds an Azure Active Directory User mapping for the provided DriveWorks User.   
![Public Method](dotnetimages/publicMethod.gif)| [AddUserToTeam](topic3289.md)| Overloaded. Adds the specified user to the given team.   
![Public Method](dotnetimages/publicMethod.gif)| [ClearProjectPermissionsForTeam](topic3292.md)| Overloaded. Clears the list of allowed projects for the specified team.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [CreateTeam](topic3295.md)| Overloaded. Creates a new team with the specified information.   
![Public Method](dotnetimages/publicMethod.gif)| [CreateUser](topic3300.md)| Creates a new user with the specified information.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetProjectPermissionsForTeam](topic3301.md)| Overloaded. Gets the list of project permissions for the specified team.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeamGroupTablePermissionForGroupTable](topic3304.md)| Returns the effective permission that a user has for the specified group data table.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeamGroupTablePermissionsForGroupTable](topic3305.md)| Returns a collection group data table permissions that the specified group data table has.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeamGroupTablePermissionsForTeam](topic3306.md)| Returns a collection permissions that the specified team has for group tables.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeamGroupTablePermissionsForUser](topic3307.md)| Returns a collection of group data table permissions that the specified user has.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeams](topic3308.md)| Gets information about all registered teams.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTeamsForUser](topic3309.md)| Overloaded. Gets all the teams to which the given user belongs.   
![Public Method](dotnetimages/publicMethod.gif)| [GetUserActiveDirectoryMappings](topic3312.md)| Gets a list of mapped Azure Active Directory User Principal ID's for a given DriveWorks User Id.   
![Public Method](dotnetimages/publicMethod.gif)| [GetUserByActiveDirectoryId](topic3313.md)| Get a specific DriveWorks User details that is already registered against an AAD User, if one exists.   
![Public Method](dotnetimages/publicMethod.gif)| [GetUserById](topic3314.md)| Gets a users details from the given ID.   
![Public Method](dotnetimages/publicMethod.gif)| [GetUsers](topic3315.md)| Gets information about all registered users.   
![Public Method](dotnetimages/publicMethod.gif)| [GetUsersInTeam](topic3316.md)| Overloaded. Gets all the users that belong to the specified team.   
![Public Method](dotnetimages/publicMethod.gif)| [RemoveUserActiveDirectoryMapping](topic3319.md)| Removes an Azure Active Directory User mapping from the provided DriveWorks User.   
![Public Method](dotnetimages/publicMethod.gif)| [RemoveUserFromTeam](topic3320.md)| Overloaded. Removes the specified user from the given team.   
![Public Method](dotnetimages/publicMethod.gif)| [SetGroupTablePermissionForTeam](topic3323.md)| Sets the specified permissions for the specified team and group.   
![Public Method](dotnetimages/publicMethod.gif)| [TryAddProjectPermissionToTeam](topic3324.md)| Overloaded. Adds the specified project to the list of projects to which users in the given team have access.   
![Public Method](dotnetimages/publicMethod.gif)| [TryDeleteTeam](topic3327.md)| Deletes the named team.   
![Public Method](dotnetimages/publicMethod.gif)| [TryDeleteUser](topic3328.md)| Deletes the user with the specified login name.   
![Public Method](dotnetimages/publicMethod.gif)| [TryGetTeam](topic3329.md)| Overloaded. Gets the specified team.   
![Public Method](dotnetimages/publicMethod.gif)| [TryGetUser](topic3332.md)| Gets information about the user with the specified login name.   
![Public Method](dotnetimages/publicMethod.gif)| [TryRemoveProjectPermissionFromTeam](topic3333.md)| Overloaded. Removes the specified project from the list of projects to which users in the given team have access.   
![Public Method](dotnetimages/publicMethod.gif)| [TrySetUserPassword](topic3336.md)| Updates an existing user with the specified information.   
![Public Method](dotnetimages/publicMethod.gif)| [TryUpdateTeam](topic3337.md)| Updates the team with the specified details.   
![Public Method](dotnetimages/publicMethod.gif)| [TryUpdateUser](topic3338.md)| Updates an existing user with the specified information.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [TeamCreated](topic3339.md)| Raised when a team is created.   
![Public Event](dotnetimages/publicEvent.gif)| [TeamDeleted](topic3340.md)| Raised when a team is successfully deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [TeamUpdated](topic3341.md)| Raised when a team is successfully updated.   
![Public Event](dotnetimages/publicEvent.gif)| [UserCreated](topic3342.md)| Raised when a user is created.   
![Public Event](dotnetimages/publicEvent.gif)| [UserDeleted](topic3343.md)| Raised when a user is successfully deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [UserUpdated](topic3344.md)| Raised when a user is successfully updated.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
