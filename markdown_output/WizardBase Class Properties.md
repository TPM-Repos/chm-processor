       

 Collapse All Expand All  Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
WizardBase Class Properties   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1200.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : WizardBase Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [WizardBase members](topic1201.md).

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

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
