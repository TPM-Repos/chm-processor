![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationFlowDefinition Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11387.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationFlowDefinition Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [SpecificationFlowDefinition](topic11387.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [InitialState](topic11398.md)| Gets/sets the initial state of a newly created specification.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDefault](topic11399.md)| Gets whether the current specification-flow is the default specification-flow.   
![Public Property](dotnetimages/publicProperty.gif)| [States](topic11400.md)| Gets the states which have been defined for the specification flow.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Customize](topic11393.md)| Let the definition know it has been customized and therefore the changes need persisting in the project.   
![Public Method](dotnetimages/publicMethod.gif)| [ExportXml](topic11394.md)| Get a copy of the current specification flow XML.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetDefaultSpecificationFlow](topic11395.md)| Gets the XML representing the default specification flow.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [LoadSpecificationFlow](topic11396.md)| Loads in a custom specification flow from XML.   
![Public Method](dotnetimages/publicMethod.gif)| [ResetDefault](topic11397.md)| Resets the specification-flow to the default.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [IsDefaultChanged](topic11401.md)| Raised when the IsDefault property is changed after the specification flow is customized from default or is reset back to default.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationFlowDefinition Class](topic11387.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
