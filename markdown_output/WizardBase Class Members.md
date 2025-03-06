       

 Collapse All Expand All  Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
WizardBase Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1200.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : WizardBase Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [WizardBase](topic1200.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Application](topic1236.md)| Gets the application used to create this wizard.   
![Public Property](dotnetimages/publicProperty.gif)| [IsSizeable](topic1245.md)| Indicates whether the wizard should be resizable.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [ActiveStep](topic1232.md)| Gets the wizards active step.   
![Protected Property](dotnetimages/protectedProperty.gif)| [ActiveStepDescription](topic1233.md)| If the value from the [ActiveStep](topic1232.md) property implements the [IWizardStep](topic648.md) interface then the description is returned from the active step, otherwise the [FallbackStepDescription](topic1237.md) is returned.   
![Protected Property](dotnetimages/protectedProperty.gif)| [ActiveStepImage](topic1234.md)| If the value from the [ActiveStep](topic1232.md) property implements the [IWizardStep](topic648.md) interface then the image is returned from the active step, otherwise the [FallbackStepImage](topic1238.md) is returned.   
![Protected Property](dotnetimages/protectedProperty.gif)| [ActiveStepTitle](topic1235.md)| If the value from the [ActiveStep](topic1232.md) property implements the [IWizardStep](topic648.md) interface then the title is returned from the active step, otherwise the [FallbackStepTitle](topic1239.md) is returned.   
![Protected Property](dotnetimages/protectedProperty.gif)| [FallbackStepDescription](topic1237.md)| Provides the description used for the active step if the value from the [ActiveStep](topic1232.md) property does not implement the [IWizardStep](topic648.md) interface.   
![Protected Property](dotnetimages/protectedProperty.gif)| [FallbackStepImage](topic1238.md)| Provides the image used for the active step if the value from the [ActiveStep](topic1232.md) property does not implement the [IWizardStep](topic648.md) interface.   
![Protected Property](dotnetimages/protectedProperty.gif)| [FallbackStepTitle](topic1239.md)| Provides the title used for the active step if the value from the [ActiveStep](topic1232.md) property does not implement the [IWizardStep](topic648.md) interface.   
![Protected Property](dotnetimages/protectedProperty.gif)| [IsCancelEnabled](topic1240.md)| Gets/Sets the enabled state of the wizards cancel button.   
![Protected Property](dotnetimages/protectedProperty.gif)| [IsFinishEnabled](topic1241.md)| Gets/Sets the enabled state of the wizards finish button.   
![Protected Property](dotnetimages/protectedProperty.gif)| [IsHelpEnabled](topic1242.md)| Determines if the help button is enabled, the default implementation checks to see if the wizard implements the [IHasHelp](topic288.md) interface.   
![Protected Property](dotnetimages/protectedProperty.gif)| [IsNextEnabled](topic1243.md)| Gets/Sets the enabled state of the wizards next button.   
![Protected Property](dotnetimages/protectedProperty.gif)| [IsPreviousEnabled](topic1244.md)| Gets/Sets the enabled state of the wizards previous button.   
![Protected Property](dotnetimages/protectedProperty.gif)| [NavigationDepth](topic1246.md)| Returns the number of steps that have been traversed in the navigation.   
![Protected Property](dotnetimages/protectedProperty.gif)| [WizardTitle](topic1247.md)| Gets the title of the wizard.   
Top

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [ShowHelp](topic1231.md)| Shows the wizards help.   
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [BeginUpdate](topic1206.md)| Signals the start of updates to wizard navigation. Navigation events will be suppressed until [EndUpdate](topic1210.md) is called.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Cancel](topic1207.md)| Cancels the wizard.   
![Protected Method](dotnetimages/protectedMethod.gif)| [CancelCore](topic1208.md)| Attempts to cancel the wizard.   
![Protected Method](dotnetimages/protectedMethod.gif)| [DisplayHelpTopic](topic1209.md)| Shows the specified help topic.   
![Protected Method](dotnetimages/protectedMethod.gif)| [EndUpdate](topic1210.md)| Signals the end of updates to wizard navigation.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Finish](topic1211.md)| Finishes the wizard.   
![Protected Method](dotnetimages/protectedMethod.gif)| [FinishCore](topic1212.md)| Attempts to complete the wizard.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GetHeaderImageFromResource](topic1213.md)| A helper function which gets an image which has been embedded as a resource in the implementing type's assembly.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GetInitialStep](topic1214.md)| Gets the initial wizard step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Next](topic1215.md)| Navigates the wizard to the next step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [NextCore](topic1216.md)| Attempts navigation to the next wizard step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveStepChanged](topic1217.md)| Handles the Active Step Changed event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnCancelInvoked](topic1218.md)| Raises the [CancelInvoked](topic1248.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnCancelInvoking](topic1219.md)| Raises the [CancelInvoking](topic1249.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnFinishInvoked](topic1220.md)| Raises the [FinishInvoked](topic1250.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnFinishInvoking](topic1221.md)| Raises the [FinishInvoking](topic1251.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnNavigated](topic1222.md)| Raises the [Navigated](topic1252.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnNavigatedConditional](topic1223.md)| Raises the [Navigated](topic1252.md) event if there is no suppression active; otherwise schedules the event to be raised when the suppression is removed.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnNextInvoked](topic1224.md)| Raises the [NextInvoked](topic1253.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnNextInvoking](topic1225.md)| Raises the [NextInvoking](topic1254.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnPreviousInvoked](topic1226.md)| Raises the [PreviousInvoked](topic1255.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnPreviousInvoking](topic1227.md)| Raises the [PreviousInvoking](topic1256.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Previous](topic1228.md)| Navigates the wizard to the previous step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [PreviousCore](topic1229.md)| Attempts navigation to the previous wizard step.   
![Protected Method](dotnetimages/protectedMethod.gif)| [PushStep](topic1230.md)| Manual pushes a step on to the list of previous steps. May be useful if GetInitialStep returns a step other than the zeroeth.   
Top

# Protected Events

| Name| Description  
---|---|---  
![Protected Event](dotnetimages/protectedEvent.gif)| [CancelInvoked](topic1248.md)| Raise when the wizard is canceled.   
![Protected Event](dotnetimages/protectedEvent.gif)| [CancelInvoking](topic1249.md)| Raised when wizard cancellation is requested.   
![Protected Event](dotnetimages/protectedEvent.gif)| [FinishInvoked](topic1250.md)| Raised when the wizard is finished.   
![Protected Event](dotnetimages/protectedEvent.gif)| [FinishInvoking](topic1251.md)| Raised when wizard finish is requested.   
![Protected Event](dotnetimages/protectedEvent.gif)| [Navigated](topic1252.md)| Raised when the wizard is navigated.   
![Protected Event](dotnetimages/protectedEvent.gif)| [NextInvoked](topic1253.md)| Raised when the wizard is navigated forward.   
![Protected Event](dotnetimages/protectedEvent.gif)| [NextInvoking](topic1254.md)| Raised when forward navigation is requested in the wizard.   
![Protected Event](dotnetimages/protectedEvent.gif)| [PreviousInvoked](topic1255.md)| Raised when the wizard is navigated backwards.   
![Protected Event](dotnetimages/protectedEvent.gif)| [PreviousInvoking](topic1256.md)| Raised when backwards navigation is requested in the wizard.   
Top

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
