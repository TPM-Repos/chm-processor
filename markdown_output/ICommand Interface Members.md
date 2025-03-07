Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ICommand Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic77.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ICommand Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ICommand](topic77.md).

# Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [Application](topic86.md)| Gets the application to which the command belongs.   
![ Property](dotnetimages/Property.gif)| [IsAvailable](topic87.md)| Gets whether the command is available.   
![ Property](dotnetimages/Property.gif)| [IsEnabled](topic88.md)| Gets/sets whether the command is enabled.   
![ Property](dotnetimages/Property.gif)| [IsValid](topic89.md)| Gets whether the command is valid in the current application state.   
![ Property](dotnetimages/Property.gif)| [Manager](topic90.md)| Gets the command manager which is managing the command.   
![ Property](dotnetimages/Property.gif)| [Name](topic91.md)| Gets the culture invariant name of the command.   
![ Property](dotnetimages/Property.gif)| [StateFilter](topic92.md)| Gets the filter which determines in which application states the command is visible.   
Top

# Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [GetImage](topic82.md)| Gets the context-specific image which represents the command.   
![ Method](dotnetimages/Method.gif)| [GetTitle](topic83.md)| Gets the context-specific title of the command.   
![ Method](dotnetimages/Method.gif)| [Invoke](topic84.md)| Invokes the operation represented by the command.   
![ Method](dotnetimages/Method.gif)| [ValidateContext](topic85.md)| Validates the specified context is suitable for the command.   
Top

# Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [AfterInvoke](topic93.md)| Raised after the command has been invoked.   
![ Event](dotnetimages/Event.gif)| [BeforeInvoke](topic94.md)| Raised when the command is about to be invoked.   
![ Event](dotnetimages/Event.gif)| [Invoking](topic95.md)| Raised when the command is being invoked.   
![ Event](dotnetimages/Event.gif)| [IsAvailableChanged](topic96.md)| Raised when the [IsAvailable](topic87.md) property changes.   
![ Event](dotnetimages/Event.gif)| [IsEnabledChanged](topic97.md)| Raised when the [IsEnabled](topic88.md) property changes.   
![ Event](dotnetimages/Event.gif)| [IsValidChanged](topic98.md)| Raised when the [IsValid](topic89.md) property changes.   
Top

# See Also

#### Reference

[ICommand Interface](topic77.md)   
[DriveWorks.Applications Namespace](topic16.md)


