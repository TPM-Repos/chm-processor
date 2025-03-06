![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationStep Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10175.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) : NavigationStep Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [NavigationStep](topic10175.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [CanRename](topic10185.md)| Gets a value indicating whether the name of the navigation step can be changed.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic10186.md)| Gets whether the navigation step has been deleted.   
![Public Property](dotnetimages/publicProperty.gif)| [Left](topic10187.md)| Gets the left position of the step in the navigation designer.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic10188.md)| Gets/sets the name of the navigation step.   
![Public Property](dotnetimages/publicProperty.gif)| [Navigation](topic10189.md)| Gets the project navigation.   
![Public Property](dotnetimages/publicProperty.gif)| [NextStep](topic10190.md)| Gets/sets the navigation step to be activated after this.   
![Public Property](dotnetimages/publicProperty.gif)| [OnNextMacroName](topic10191.md)| Gets the name of the macro to be executed when the next step is activated.   
![Public Property](dotnetimages/publicProperty.gif)| [OnNextMacroRule](topic10192.md)| Gets/sets the rule which defines the name of the macro to be executed when the next step is activated.   
![Public Property](dotnetimages/publicProperty.gif)| [OnPreviousMacroName](topic10193.md)| Gets the name of the macro to be executed when the previous step is activated.   
![Public Property](dotnetimages/publicProperty.gif)| [OnPreviousMacroRule](topic10194.md)| Gets/sets the rule which defines the name of the macro to be executed when the previous step is activated.   
![Public Property](dotnetimages/publicProperty.gif)| [Top](topic10195.md)| Gets the top position of the step in the navigation designer.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic10183.md)| Deletes the step from the navigation.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic10181.md)| Checks to see if the item has been deleted, and if it has, throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) exception.   
![Protected Method](dotnetimages/protectedMethod.gif)| [ChangeNameCore](topic10182.md)| When overridden by a derived class, changes the name of the navigation step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic10184.md)| Performs any derived-type specific deletion.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic10196.md)| Raised when the navigation step is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [LeftChanged](topic10197.md)| Raised when the [Left](topic10187.md) property is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic10198.md)| Raised when the [Name](topic10188.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [NextMacroNameChanged](topic10199.md)| Raised when the macro to be fired when the next step is activated changes.   
![Public Event](dotnetimages/publicEvent.gif)| [NextMacroRuleChanged](topic10200.md)| Raised when the rule, which determines the macro to be fired when the next step is activated, changes.   
![Public Event](dotnetimages/publicEvent.gif)| [NextStepChanged](topic10201.md)| Raised when the [NextStep](topic10190.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [PreviousMacroNameChanged](topic10202.md)| Raised when the macro to be fired when the previous step is activated changes.   
![Public Event](dotnetimages/publicEvent.gif)| [PreviousMacroRuleChanged](topic10203.md)| Raised when the rule, which determines the macro to be fired when the previous step is activated, changes.   
![Public Event](dotnetimages/publicEvent.gif)| [TopChanged](topic10204.md)| Raised when the [Left](topic10187.md) property is changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NavigationStep Class](topic10175.md)   
[DriveWorks.Navigation Namespace](topic10114.md)

©2024 DriveWorks Ltd. All Rights Reserved.
