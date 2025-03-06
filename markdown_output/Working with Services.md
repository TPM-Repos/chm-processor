![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Working with Services   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5.md)  
  
Glossary Item Box

# Introduction

Services are an important concept when programming against DriveWorks applications because different applications have different capabilities and services provide an easy way of discovering these capabilities.

Services are requested from the service manager on an application, for example:

Request Specification Service | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    Dim specificationService As ISpecificationService = application.ServiceManager.GetService(Of ISpecificationService)()
      
  
If you're writing a plugin, the application is provided to you via your [Initialize Method](topic2009.md).

# Important Services

Some important services are shown below:

Type |  Description |  Provided By  
---|---|---  
[IGenerationService](topic15147.md) |  Provides support for working with model generation events. |  Autopilot, SolidWorks Integration  
[IGroupService](topic251.md) |  Provides support for working with the active group. |  Administrator, User, Autopilot, Live, SolidWorks Integration  
[IProjectService](topic382.md) |  Provides support for working with the active project. |  Administrator  
[ISettingsManager](topic442.md) |  Provides support for accessing settings. |  Administrator, User, Autopilot, Live, SolidWorks Integration  
[ISolidWorksService](DriveWorks.SolidWorks~DriveWorks.SolidWorks.Extensibility.ISolidWorksService.md) |  Provides support for connecting to the SolidWorks instance being used by a DriveWorks application. |  Autopilot, SolidWorks Integration  
[ISpecificationAutomation](DriveWorks.Applications.Autopilot.Extensibility~DriveWorks.Applications.Autopilot.Extensibility.ISpecificationAutomation.md) |  Provides support for automating the creation of specifications based on data from external systems. |  Autopilot  
[ISpecificationService](topic489.md) |  Provides support for working with specifications. |  Administrator, User, Autopilot, Live, SolidWorks Integration  
  

