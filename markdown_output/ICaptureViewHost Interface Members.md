![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ICaptureViewHost Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13363.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : ICaptureViewHost Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ICaptureViewHost](topic13363.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [Application](topic13374.md)| Gets a reference to the current application.   
![ Property](dotnetimages/Property.gif)| [ComponentManager](topic13375.md)| Gets the [IComponentManager](topic13385.md) of the host.   
![ Property](dotnetimages/Property.gif)| [DisplayManager](topic13376.md)| Gets the **DriveWorks.Applications.Implementation.Configuration.UIDisplayManager** of the host.   
![ Property](dotnetimages/Property.gif)| [ExceptionHandler](topic13377.md)| Gets the [DriveWorks.Applications.IExceptionHandler](topic207.md) of the host.   
![ Property](dotnetimages/Property.gif)| [FileFormatManager](topic13378.md)| Gets the [FileFormatManager](topic13378.md) of the host.   
![ Property](dotnetimages/Property.gif)| [LibraryManager](topic13379.md)| Gets the [DriveWorks.Applications.Extensibility.ILibraryManager](topic2079.md) of the host.   
![ Property](dotnetimages/Property.gif)| [SelectionSuppressed](topic13380.md)| Gets/sets whether selection is currently suppressed.   
![ Property](dotnetimages/Property.gif)| [ServiceManager](topic13381.md)| Gets the service manager of the host.   
![ Property](dotnetimages/Property.gif)| [SolidWorksState](topic13382.md)| Gets the current state of SolidWorks.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [Disable](topic13368.md)| Disables the host ready for a specification.   
![ Method](dotnetimages/Method.gif)| [Enable](topic13369.md)| Re-enables the host after a specification has completed.   
![ Method](dotnetimages/Method.gif)| [OpenDocumentInSolidWorks](topic13370.md)| Opens the component with the given path in SolidWorks.   
![ Method](dotnetimages/Method.gif)| [RebuildComponentManager](topic13371.md)| Notifies DriveWorks that the component manager needs rebuilding as changes have been made to the group which were outside of the component manager's control.   
![ Method](dotnetimages/Method.gif)| [ReloadSolidWorksState](topic13372.md)| Reloads the SolidWorks state.   
![ Method](dotnetimages/Method.gif)| [ShowHelp](topic13373.md)| Shows the help for the given topic name.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [ComponentManagerRebuilt](topic13383.md)| Raised when the [ComponentManager](topic13375.md) has been rebuilt.   
![ Event](dotnetimages/Event.gif)| [Disconnecting](topic13384.md)| Raised when the host is disconnecting.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICaptureViewHost Interface](topic13363.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


