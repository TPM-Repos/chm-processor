![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationEnvironment Class Properties   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11355.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationEnvironment Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [SpecificationEnvironment members](topic11356.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [AllowIgnoreTaskList](topic11362.md)| Gets/sets whether the user is allowed to ignore the state of the task list when navigating and invoking transitions.   
![Public Property](dotnetimages/publicProperty.gif)| [CanEditCompletedSpecifications](topic11363.md)| Gets/sets whether completed specifications can be edited.   
![Public Property](dotnetimages/publicProperty.gif)| [DocumentGeneration](topic11364.md)| Gets/sets when documents are generated using the default specification flow.   
![Public Property](dotnetimages/publicProperty.gif)| [DriveAppId](topic11365.md)| Gets the optional unique identifier of the DriveApp instance that this specification represents. This has no value if the [SpecificationEnvironment](topic11355.md) is not for a DriveApp.   
![Public Property](dotnetimages/publicProperty.gif)| [IsAsynchronous](topic11366.md)| Gets/sets whether or not to run the specification asynchronously.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDriveApp](topic11367.md)| Gets whether or not the specification is an instance of a DriveApp.   
![Public Property](dotnetimages/publicProperty.gif)| [IsLocked](topic11368.md)| Determines whether the object has been locked.   
![Public Property](dotnetimages/publicProperty.gif)| [OverrideProjectReportingLevel](topic11369.md)| Gets/sets whether the reporting level set on the environment should override the equivalent level set on the project. This is automatically set to true if the reporting level is changed on the environment.   
![Public Property](dotnetimages/publicProperty.gif)| [OverwriteReleasedComponents](topic11370.md)| Gets/sets whether, during the release of components, components that already exist are overwritten or used as-is. Only takes effect if [CanEditCompletedSpecifications](topic11363.md) is enabled.   
![Public Property](dotnetimages/publicProperty.gif)| [ReleaseToAutopilot](topic11371.md)| Gets/sets whether the Release-to-Autopilot setting is enabled.   
![Public Property](dotnetimages/publicProperty.gif)| [ReportingLevel](topic11372.md)| Gets/sets the reporting level to use for specification reporting. Setting this value will automatically change the [OverrideProjectReportingLevel](topic11369.md) to true.   
![Public Property](dotnetimages/publicProperty.gif)| [ServiceProvider](topic11373.md)| Gets/sets the service provider to be used by the specification context and tasks when interaction with the hosting application is required.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationBasePath](topic11374.md)| Gets/sets the base path for specification files (this is usually equivalent to the group's default specification folder).   
![Public Property](dotnetimages/publicProperty.gif)| [TemporaryFolderPath](topic11375.md)| Gets/sets the path to the temporary folder.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
