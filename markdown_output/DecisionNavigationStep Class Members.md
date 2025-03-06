![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
DecisionNavigationStep Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10125.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) : DecisionNavigationStep Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [DecisionNavigationStep](topic10125.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [CanRename](topic10185.md)| Gets a value indicating whether the name of the navigation step can be changed. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Comment](topic10136.md)| Gets/sets the comment associated with the Navigation step's rule.   
![Public Property](dotnetimages/publicProperty.gif)| [ConditionExpression](topic10137.md)| Gets/sets an expression which evaluates to either true or false and ultimately determines which navigation step is activated next.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic10138.md)| Gets the invariant identifier of the rule.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic10186.md)| Gets whether the navigation step has been deleted. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Left](topic10187.md)| Gets the left position of the step in the navigation designer. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic10188.md)| Gets/sets the name of the navigation step. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Navigation](topic10189.md)| Gets the project navigation. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [NextStep](topic10139.md)| Overridden. Overridden to throw an exception if it is attempted to change the next step as a decision's next step is governed by the [ConditionExpression](topic10137.md), [NextStepIfTrue](topic10141.md), and [NextStepIfFalse](topic10140.md) properties.   
![Public Property](dotnetimages/publicProperty.gif)| [NextStepIfFalse](topic10140.md)| Gets the next step to be shown if [ConditionExpression](topic10137.md) evaluates to true.   
![Public Property](dotnetimages/publicProperty.gif)| [NextStepIfTrue](topic10141.md)| Gets the next step to be shown if [ConditionExpression](topic10137.md) evaluates to true.   
![Public Property](dotnetimages/publicProperty.gif)| [OnNextMacroName](topic10191.md)| Gets the name of the macro to be executed when the next step is activated. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [OnNextMacroRule](topic10192.md)| Gets/sets the rule which defines the name of the macro to be executed when the next step is activated. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [OnPreviousMacroName](topic10193.md)| Gets the name of the macro to be executed when the previous step is activated. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [OnPreviousMacroRule](topic10194.md)| Gets/sets the rule which defines the name of the macro to be executed when the previous step is activated. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Top](topic10195.md)| Gets the top position of the step in the navigation designer. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic10183.md)| Deletes the step from the navigation. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetVersionHistory](topic10132.md)| Gets the rule condition rule history for this decision.   
![Public Method](dotnetimages/publicMethod.gif)| [SetRuleAndComment](topic10133.md)| Overloaded. Sets the rule and the comment for the Decision Step.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic10181.md)| Checks to see if the item has been deleted, and if it has, throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) exception. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [ChangeNameCore](topic10182.md)| When overridden by a derived class, changes the name of the navigation step. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic10131.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ConditionExpressionChanged](topic10142.md)| Raised when the value of the [ConditionExpression](topic10137.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic10196.md)| Raised when the navigation step is deleted. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [LeftChanged](topic10197.md)| Raised when the [NavigationStep.Left](topic10187.md) property is changed. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic10198.md)| Raised when the [NavigationStep.Name](topic10188.md) property changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NextMacroNameChanged](topic10199.md)| Raised when the macro to be fired when the next step is activated changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NextMacroRuleChanged](topic10200.md)| Raised when the rule, which determines the macro to be fired when the next step is activated, changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NextStepChanged](topic10201.md)| Raised when the [NavigationStep.NextStep](topic10190.md) property changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NextStepIfFalseChanged](topic10143.md)| Raised when the value of the [NextStepIfFalse](topic10140.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [NextStepIfTrueChanged](topic10144.md)| Raised when the value of the [NextStepIfTrue](topic10141.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [PreviousMacroNameChanged](topic10202.md)| Raised when the macro to be fired when the previous step is activated changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [PreviousMacroRuleChanged](topic10203.md)| Raised when the rule, which determines the macro to be fired when the previous step is activated, changes. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
![Public Event](dotnetimages/publicEvent.gif)| [TopChanged](topic10204.md)| Raised when the [NavigationStep.Left](topic10187.md) property is changed. (Inherited from [DriveWorks.Navigation.NavigationStep](topic10175.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DecisionNavigationStep Class](topic10125.md)   
[DriveWorks.Navigation Namespace](topic10114.md)


