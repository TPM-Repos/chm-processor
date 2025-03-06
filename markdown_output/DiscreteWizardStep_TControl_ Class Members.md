![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
DiscreteWizardStep<TControl> Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic770.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : DiscreteWizardStep<TControl> Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [DiscreteWizardStep<TControl>](topic770.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [AutoAdvance](topic759.md)| Gets/sets whether the step automatically advanced to the next step as soon as one is available. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Description](topic779.md)| Overridden. Gets the description of the step.   
![Public Property](dotnetimages/publicProperty.gif)| [HideFromNavigation](topic761.md)| Determines whether the step is added to the list of previous steps when it is navigated past. This is useful when a step acts as a transition between one step and another. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Image](topic780.md)| Overridden. Gets the image which represents the step (may return a null reference).   
![Public Property](dotnetimages/publicProperty.gif)| [IsCancelSuppressed](topic763.md)| Gets/sets whether the step suppresses the cancel button on the wizard. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsControlCreated](topic781.md)| Determines whether the control has been created.   
![Public Property](dotnetimages/publicProperty.gif)| [IsPreviousSuppressed](topic764.md)| Gets/sets whether the step suppresses the previous button on the wizard. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic782.md)| Overridden. Gets the title of the step.   
![Public Property](dotnetimages/publicProperty.gif)| [Wizard](topic783.md)| Gets the wizard to which the step belongs.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [GetControl](topic776.md)| Overridden. Gets the control which provides the UI for the step.   
![Public Method](dotnetimages/publicMethod.gif)| [GetControlTyped](topic777.md)| Gets the control.   
![Public Method](dotnetimages/publicMethod.gif)| [GetNextStep](topic778.md)| Overridden. Gets the next step if the state is valid, a null reference if the state is not valid, or [FinishStep](topic766.md) if the wizard's next action is to finish.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnNextStepChanged](topic758.md)| Raises the [NextStepChanged](topic769.md) event. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Activated](topic767.md)| Raised when the step is activated. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Event](dotnetimages/publicEvent.gif)| [Deactivated](topic768.md)| Raised when the step is deactivated. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NextStepChanged](topic769.md)| Raised if the next step has changed, e.g. a different option was chosen, or the state has become valid/invalid. (Inherited from [DriveWorks.Applications.DiscreteWizardStep](topic750.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DiscreteWizardStep<TControl> Class](topic770.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
