Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IWizard Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic613.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : IWizard Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IWizard](topic613.md).

# Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [ActiveStep](topic623.md)| Gets the Windows Forms control representing the active step.   
![ Property](dotnetimages/Property.gif)| [ActiveStepDescription](topic624.md)| Gets the description of the active step.   
![ Property](dotnetimages/Property.gif)| [ActiveStepImage](topic625.md)| Gets the image which represents the active step.   
![ Property](dotnetimages/Property.gif)| [ActiveStepTitle](topic626.md)| Gets the title of the active step.   
![ Property](dotnetimages/Property.gif)| [IsCancelEnabled](topic627.md)| Gets whether the Cancel button is enabled.   
![ Property](dotnetimages/Property.gif)| [IsFinishEnabled](topic628.md)| Gets whether the Finish button is enabled.   
![ Property](dotnetimages/Property.gif)| [IsHelpEnabled](topic629.md)| Gets whether help is enabled.   
![ Property](dotnetimages/Property.gif)| [IsNextEnabled](topic630.md)| Gets whether the Next button is enabled.   
![ Property](dotnetimages/Property.gif)| [IsPreviousEnabled](topic631.md)| Gets whether the Previous button is enabled.   
![ Property](dotnetimages/Property.gif)| [WizardTitle](topic632.md)| Gets the title of the wizard.   
Top

# Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [Cancel](topic618.md)| Cancels the wizard.   
![ Method](dotnetimages/Method.gif)| [Finish](topic619.md)| Finishes the wizard.   
![ Method](dotnetimages/Method.gif)| [Next](topic620.md)| Navigates to the next step.   
![ Method](dotnetimages/Method.gif)| [Previous](topic621.md)| Navigates to the previous step.   
![ Method](dotnetimages/Method.gif)| [ShowHelp](topic622.md)| Shows the help for the wizard.   
Top

# Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [CancelInvoked](topic633.md)| Raised by the wizard when the cancel action has been invoked.   
![ Event](dotnetimages/Event.gif)| [CancelInvoking](topic634.md)| Raised by the wizard when the cancel action is being invoked.   
![ Event](dotnetimages/Event.gif)| [FinishInvoked](topic635.md)| Raised by the wizard when the finish action has been invoked.   
![ Event](dotnetimages/Event.gif)| [FinishInvoking](topic636.md)| Raised by the wizard when the finish action is being invoked.   
![ Event](dotnetimages/Event.gif)| [Navigated](topic637.md)| Raised by the wizard when some action on the active step has changed the navigation, e.g. if validation has determined the user can no longer select Next, or if the wizard wants to manually switch to another step.   
![ Event](dotnetimages/Event.gif)| [NextInvoked](topic638.md)| Raised by the wizard when the next action has been invoked.   
![ Event](dotnetimages/Event.gif)| [NextInvoking](topic639.md)| Raised by the wizard when the next action is being invoked.   
![ Event](dotnetimages/Event.gif)| [PreviousInvoked](topic640.md)| Raised by the wizard when the previous action has been invoked.   
![ Event](dotnetimages/Event.gif)| [PreviousInvoking](topic641.md)| Raised by the wizard when the previous action is being invoked.   
Top

# See Also

#### Reference

[IWizard Interface](topic613.md)   
[DriveWorks.Applications Namespace](topic16.md)


