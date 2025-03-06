![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ISettingsManager Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic442.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ISettingsManager Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ISettingsManager](topic442.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [CanRequestElevation](topic462.md)| Returns true if the settings manager is capable of requesting elevation for access to privileged settings.   
![ Property](dotnetimages/Property.gif)| [IsPrivileged](topic463.md)| Gets whether the settings manager has access to settings stored in privileged locations such as HKEY_LOCAL_MACHINE.   
![ Property](dotnetimages/Property.gif)| [IsRedirectionEnabled](topic464.md)| Gets/sets whether machine-level settings are redirected to the user-profile instead.   
![ Property](dotnetimages/Property.gif)| [LocalUserContentFolder](topic465.md)| Gets the fully-qualified path to the local user content folder.   
![ Property](dotnetimages/Property.gif)| [MachineContentFolder](topic466.md)| Gets the fully-qualified path to the machine content folder.   
![ Property](dotnetimages/Property.gif)| [RoamingUserContentFolder](topic467.md)| Gets the fully-qualified path to the roaming user content folder.   
![ Property](dotnetimages/Property.gif)| [SharedContentFolder](topic468.md)| Gets/sets the fully-qualified path to the shared content folder.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [DeleteSetting](topic447.md)| Deletes the specified setting.   
![ Method](dotnetimages/Method.gif)| [DeleteSettingGroup](topic448.md)| Deletes the specified setting group.   
![ Method](dotnetimages/Method.gif)| [GetSetting](topic449.md)| Gets the specified setting.   
![ Method](dotnetimages/Method.gif)| [GetSettingAsByteArray](topic450.md)| Gets the specified setting as a byte array.   
![ Method](dotnetimages/Method.gif)| [GetSettingAsString](topic451.md)| Gets the specified setting as a string.   
![ Method](dotnetimages/Method.gif)| [GetSettingAsStringArray](topic452.md)| Gets the specified setting as a string array.   
![ Method](dotnetimages/Method.gif)| [RequestElevation](topic453.md)| Requests elevation if supported.   
![ Method](dotnetimages/Method.gif)| [SetSetting](topic454.md)| Overloaded. Saves the specified setting.   
![ Method](dotnetimages/Method.gif)| [TryGetSettingAsBoolean](topic460.md)| Gets the specified setting as a boolean.   
![ Method](dotnetimages/Method.gif)| [TryGetSettingAsInteger](topic461.md)| Gets the specified setting as a boolean.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [Elevated](topic469.md)| Raised when the settings manager has been elevated.   
![ Event](dotnetimages/Event.gif)| [SettingValueChanged](topic470.md)| Raised when the value of a setting changes.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[DriveWorks.Applications Namespace](topic16.md)


