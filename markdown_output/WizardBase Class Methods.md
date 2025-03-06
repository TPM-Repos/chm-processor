WizardBase Class Methods   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : WizardBase Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [WizardBase members](topic1201.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| [ShowHelp](topic1231.md)| Shows the wizards help.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [BeginUpdate](topic1206.md)| Signals the start of updates to wizard navigation. Navigation events will be suppressed until [EndUpdate](topic1210.md) is called.   
Protected Method| [Cancel](topic1207.md)| Cancels the wizard.   
Protected Method| [CancelCore](topic1208.md)| Attempts to cancel the wizard.   
Protected Method| [DisplayHelpTopic](topic1209.md)| Shows the specified help topic.   
Protected Method| [EndUpdate](topic1210.md)| Signals the end of updates to wizard navigation.   
Protected Method| [Finish](topic1211.md)| Finishes the wizard.   
Protected Method| [FinishCore](topic1212.md)| Attempts to complete the wizard.   
Protected Method| [GetHeaderImageFromResource](topic1213.md)| A helper function which gets an image which has been embedded as a resource in the implementing type's assembly.   
Protected Method| [GetInitialStep](topic1214.md)| Gets the initial wizard step.   
Protected Method| [Next](topic1215.md)| Navigates the wizard to the next step.   
Protected Method| [NextCore](topic1216.md)| Attempts navigation to the next wizard step.   
Protected Method| [OnActiveStepChanged](topic1217.md)| Handles the Active Step Changed event.   
Protected Method| [OnCancelInvoked](topic1218.md)| Raises the [CancelInvoked](topic1248.md) event.   
Protected Method| [OnCancelInvoking](topic1219.md)| Raises the [CancelInvoking](topic1249.md) event.   
Protected Method| [OnFinishInvoked](topic1220.md)| Raises the [FinishInvoked](topic1250.md) event.   
Protected Method| [OnFinishInvoking](topic1221.md)| Raises the [FinishInvoking](topic1251.md) event.   
Protected Method| [OnNavigated](topic1222.md)| Raises the [Navigated](topic1252.md) event.   
Protected Method| [OnNavigatedConditional](topic1223.md)| Raises the [Navigated](topic1252.md) event if there is no suppression active; otherwise schedules the event to be raised when the suppression is removed.   
Protected Method| [OnNextInvoked](topic1224.md)| Raises the [NextInvoked](topic1253.md) event.   
Protected Method| [OnNextInvoking](topic1225.md)| Raises the [NextInvoking](topic1254.md) event.   
Protected Method| [OnPreviousInvoked](topic1226.md)| Raises the [PreviousInvoked](topic1255.md) event.   
Protected Method| [OnPreviousInvoking](topic1227.md)| Raises the [PreviousInvoking](topic1256.md) event.   
Protected Method| [Previous](topic1228.md)| Navigates the wizard to the previous step.   
Protected Method| [PreviousCore](topic1229.md)| Attempts navigation to the previous wizard step.   
Protected Method| [PushStep](topic1230.md)| Manual pushes a step on to the list of previous steps. May be useful if GetInitialStep returns a step other than the zeroeth.   
Top

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[DriveWorks.Applications Namespace](topic16.md)


