![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectNavigation Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10222.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) : ProjectNavigation Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ProjectNavigation](topic10222.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Count](topic10246.md)| Gets the total number of steps in the navigation (including the start and finish steps).   
![Public Property](dotnetimages/publicProperty.gif)| [FinishStep](topic10247.md)| Gets the final step in the navigation.   
![Public Property](dotnetimages/publicProperty.gif)| [Item](topic10248.md)| Gets the navigation step at the given index.   
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic10249.md)| Gets the project.   
![Public Property](dotnetimages/publicProperty.gif)| [StartStep](topic10250.md)| Gets the first step in the navigation.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [CreateDecision](topic10228.md)| Creates a new decision.   
Public Method| [CreateForm](topic10229.md)| Creates a new form.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetControl](topic10232.md)| Gets a control given its name.   
Public Method| [GetDecisions](topic10233.md)| Gets all of the decisions in the navigation.   
Public Method| [GetForms](topic10234.md)| Gets the project's forms.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetStep](topic10235.md)| Gets the named navigation step.   
Public Method| [GetSteps](topic10236.md)| Gets all of the steps in the navigation.   
Public Method| [TryGetControl](topic10240.md)| Overloaded. Gets a control given its name.   
Public Method| [TryGetStep](topic10243.md)| Overloaded. Gets the named navigation step.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [Dispose](topic10231.md)|   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseNavigationStepCreated](topic10237.md)|   
Protected Method| [RaiseNavigationStepDeleted](topic10238.md)|   
Protected Method| [RaiseNavigationStepNameChanged](topic10239.md)|   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ControlCreated](topic10251.md)| Raised whenever a control is created on any form or dialog.   
![Public Event](dotnetimages/publicEvent.gif)| [ControlDeleted](topic10252.md)| Raised whenever any control is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [ControlNameChanged](topic10253.md)| Raised whenever any control is renamed.   
![Public Event](dotnetimages/publicEvent.gif)| [NavigationStepCreated](topic10254.md)| Raised when a navigation step is created.   
![Public Event](dotnetimages/publicEvent.gif)| [NavigationStepDeleted](topic10255.md)| Raised when a navigation step is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [NavigationStepNameChanged](topic10256.md)| Raised when the name of a navigation step is changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[DriveWorks.Navigation Namespace](topic10114.md)


