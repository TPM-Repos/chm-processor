![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IFlowNode Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6873.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : IFlowNode Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IFlowNode](topic6873.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [Flow](topic6880.md)| Gets the flow this node is associated with.   
![ Property](dotnetimages/Property.gif)| [Left](topic6881.md)| Gets the left position of this node in the visual editor.   
![ Property](dotnetimages/Property.gif)| [Name](topic6882.md)| Gets the name of the node.   
![ Property](dotnetimages/Property.gif)| [NavigationOutput](topic6883.md)| Gets the navigation output of this node.   
![ Property](dotnetimages/Property.gif)| [Outputs](topic6884.md)| Gets a collection of all outputs of this node.   
![ Property](dotnetimages/Property.gif)| [Top](topic6885.md)| Gets the top position of this node in the visual editor.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [NotifyRequirementsChanged](topic6878.md)| Called whenever the value of any mapped inputs or connections have changed And this node should reevaluate whether it can execute or not.   
![ Method](dotnetimages/Method.gif)| [TryGetOutputEndpoint](topic6879.md)| Attempts to retrieve the output end point with the given name.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [LeftChanged](topic6886.md)| Occurs when the value of the [Left](topic6881.md) property has changed.   
![ Event](dotnetimages/Event.gif)| [TopChanged](topic6887.md)| Occurs when the value of the [Top](topic6885.md) property has changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IFlowNode Interface](topic6873.md)   
[DriveWorks.EventFlow Namespace](topic6871.md)

©2024 DriveWorks Ltd. All Rights Reserved.
