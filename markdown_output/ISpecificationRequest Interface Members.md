![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ISpecificationRequest Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1778.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : ISpecificationRequest Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ISpecificationRequest](topic1778.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [ProjectName](topic1785.md)| Gets/sets the name of the project to specify.   
![ Property](dotnetimages/Property.gif)| [TransitionName](topic1786.md)| Gets the name of the transition to invoke when the specification has been filled in.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [AddChildSpecification](topic1783.md)| Adds and returns a new child specification request.   
![ Method](dotnetimages/Method.gif)| [AddInput](topic1784.md)| Adds an input to be changed in the specification.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [InputsDriven](topic1787.md)| Occurs when the inputs are driven into to the specification.   
![ Event](dotnetimages/Event.gif)| [ProjectNameInvalid](topic1788.md)| Occurs when the specification is being processed and a project with the given name can't be located.   
![ Event](dotnetimages/Event.gif)| [Specifying](topic1789.md)| Occurs when the [ISpecificationRequest](topic1778.md) is being processed by DriveWorks.   
![ Event](dotnetimages/Event.gif)| [TransitionFailed](topic1790.md)| Occurs when the specification is being processed and a transition with the given name is invalid.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)

©2024 DriveWorks Ltd. All Rights Reserved.
