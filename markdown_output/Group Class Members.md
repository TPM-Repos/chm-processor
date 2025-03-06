![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Group Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2958.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : Group Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [Group](topic2958.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [ActiveSpecificationContexts](topic2986.md)| Gets all active specification contexts that are in a running state.   
![Public Property](dotnetimages/publicProperty.gif)| [CanEditAllSpecifications](topic2987.md)| Gets if the current user has permission to view and edit all specifications.   
![Public Property](dotnetimages/publicProperty.gif)| [CanEditCompletedSpecifications](topic2988.md)| Gets/sets whether completed specifications in the standard specification flow can be edited.   
![Public Property](dotnetimages/publicProperty.gif)| [CanEditDriveApps](topic2989.md)| Gets if the current user has permission to edit DriveApps.   
![Public Property](dotnetimages/publicProperty.gif)| [CanEditGroupSecurity](topic2990.md)| Gets if the current user has permission to edit group security details.   
![Public Property](dotnetimages/publicProperty.gif)| [CapturedComponents](topic2991.md)| Gets an instance of the [GroupCapturedComponents](topic3022.md) type which is responsible for managing the captured component information in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [ConnectionString](topic2992.md)| Gets the connection string which was used to open the group.   
![Public Property](dotnetimages/publicProperty.gif)| [Connectors](topic2993.md)| Gets an instance of [GroupConnectors](topic3097.md) for this group.   
![Public Property](dotnetimages/publicProperty.gif)| [CurrentUser](topic2994.md)| Gets the logged-on user.   
![Public Property](dotnetimages/publicProperty.gif)| [CurrentUserCredentials](topic2995.md)| Gets the credentials that were used to log on to the group.   
![Public Property](dotnetimages/publicProperty.gif)| [CurrentUserIsAllowedCapture](topic2996.md)| Gets whether the logged-on user belongs to at least one team with permission to capture.   
![Public Property](dotnetimages/publicProperty.gif)| [CurrentUserTeams](topic2997.md)| Gets the teams to which the logged-on user belongs.   
![Public Property](dotnetimages/publicProperty.gif)| [DataTables](topic2998.md)| Gets an instance of [GroupDataTables](topic3136.md) for this group.   
![Public Property](dotnetimages/publicProperty.gif)| [DefaultSpecificationFolder](topic2999.md)| Gets/sets the default specification folder.   
![Public Property](dotnetimages/publicProperty.gif)| [GroupContentFolder](topic3000.md)| Gets/sets the group content folder.   
![Public Property](dotnetimages/publicProperty.gif)| [GroupShouldOverrideProjectReportingLevel](topic3001.md)| Gets/sets whether or not the group should override its projects' reporting levels.   
![Public Property](dotnetimages/publicProperty.gif)| [GroupType](topic3002.md)| Gets the groups specified [GroupType](topic2355.md).   
![Public Property](dotnetimages/publicProperty.gif)| [IsClosed](topic3003.md)| Determines whether the group has been closed.   
![Public Property](dotnetimages/publicProperty.gif)| [IsOpen](topic3004.md)| Determines whether the group is open.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3005.md)| Gets the name of the Group.   
![Public Property](dotnetimages/publicProperty.gif)| [OverwriteReleasedComponentData](topic3006.md)| Gets/sets whether released component data gets overwritten or used-as is.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectReportingOverrideLevel](topic3007.md)| Gets/sets the Group's [DriveWorks.Reporting.ReportingLevel](topic10362.md) which will actively override the [DriveWorks.Reporting.ReportingLevel](topic10362.md) set on individual Projects within the Group.   
![Public Property](dotnetimages/publicProperty.gif)| [Projects](topic3008.md)| Gets an instance of the [GroupProjects](topic3190.md) type which is responsible for managing the project information in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [ReleasedComponents](topic3009.md)| Gets an instance of the [GroupReleasedComponents](topic3238.md) which is responsible for managing the released component information in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [Reports](topic3010.md)| Gets an instance of the [GroupReports](topic3272.md) type which is responsible for managing the reports in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [RuleVersionHistory](topic3011.md)| Gets an instance of the **GroupRuleVersionHistory** type which is responsible for managing the rule revisions in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [Security](topic3012.md)| Gets an instance of the [GroupSecurity](topic3282.md) type which is responsible for managing the security information in the group.   
![Public Property](dotnetimages/publicProperty.gif)| [Specifications](topic3013.md)| Gets an instance of the [GroupSpecifications](topic3355.md) type which is responsible for managing the specifications in the group.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddAgentLogEntry](topic2964.md)| Adds an agent log entry.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [DeleteSetting](topic2965.md)| Deletes the named setting from the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetAgentLog](topic2966.md)| Gets the agent message log of an agent.   
![Public Method](dotnetimages/publicMethod.gif)| [GetAgents](topic2967.md)| Gets a list of generated agents in the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetAgentStatus](topic2968.md)| Gets status information of an agent.   
![Public Method](dotnetimages/publicMethod.gif)| [GetAllJobs](topic2969.md)| Gets all pending and currently in progress jobs that the current user has access to, for the specified job type.   
![Public Method](dotnetimages/publicMethod.gif)| [GetConnectedClients](topic2970.md)| Gets details of all current connections to the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetGroupSetting](topic2971.md)| Gets the named setting from the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetGroupSettingAsBoolean](topic2972.md)| Overloaded. Gets the named setting from the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetGroupSettingAsInteger](topic2975.md)| Gets the named setting from the group as an Integer.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [RefreshSecurity](topic2976.md)| Refreshes cached security information.   
![Public Method](dotnetimages/publicMethod.gif)| [RegisterJobQueue](topic2977.md)| Registers a queue of jobs within DriveWorks that need to be processed.   
![Public Method](dotnetimages/publicMethod.gif)| [SendAgentNotification](topic2978.md)| Attempts to send a notification message to the specified agent.   
![Public Method](dotnetimages/publicMethod.gif)| [SendAgentRequest](topic2979.md)| Attempts to send a request message to the specified agent. Then waits for a reply and returns that result.   
![Public Method](dotnetimages/publicMethod.gif)| [SetGroupSetting](topic2980.md)| Overloaded. Saves the named setting to the group.   
![Public Method](dotnetimages/publicMethod.gif)| [StartAgent](topic2984.md)| Starts an agent.   
![Public Method](dotnetimages/publicMethod.gif)| [StopAgent](topic2985.md)| Stops an agent.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [AgentNotificationReceived](topic3014.md)| Raised when a notification is received from another session.   
![Public Event](dotnetimages/publicEvent.gif)| [AgentRequestReceived](topic3015.md)| Raised when a request is received from another session.   
![Public Event](dotnetimages/publicEvent.gif)| [DriveAppAdded](topic3016.md)| Raised when a DriveApp is added.   
![Public Event](dotnetimages/publicEvent.gif)| [DriveAppDeleted](topic3017.md)| Raised when a DriveApp is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [DriveAppEnabledChanged](topic3018.md)| Raised when a DriveApp is enabled/disabled.   
![Public Event](dotnetimages/publicEvent.gif)| [DriveAppSecurityChanged](topic3019.md)| Raised when the security of a DriveApp is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [DriveAppUpdated](topic3020.md)| Raised when a DriveApp is updated.   
![Public Event](dotnetimages/publicEvent.gif)| [SettingChanged](topic3021.md)| Raised when a setting is changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Group Class](topic2958.md)   
[DriveWorks Namespace](topic2159.md)


