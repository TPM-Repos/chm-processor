![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Email Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2768.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : Email Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [Email](topic2768.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [AttachmentRule](topic2782.md)| The rule for the attachment segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [BccRule](topic2783.md)| The rule for the BCC segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [BodyText](topic2784.md)| Gets the body text with all rules visible.   
![Public Property](dotnetimages/publicProperty.gif)| [CcRule](topic2785.md)| The rule for the CC segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [FinalBodyText](topic2786.md)| Gets body text with resolved formulae.   
![Public Property](dotnetimages/publicProperty.gif)| [HasDisplayFileRule](topic4391.md)| Gets whether the document has a display file rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4392.md)| Gets whether the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsInitialized](topic4393.md)| Gets whether the document has been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4394.md)| Gets/sets the name of the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [PreventOutlookNewlineRemoval](topic2787.md)| Prevent Outlook from automatically removing newlines in text emails.   
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic4395.md)| Gets the project to which the document belongs. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ReceiverRule](topic2788.md)| The rule for the receiver segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [SendAsHTML](topic2789.md)| Gets/sets whether or not the email's body is HTML.   
![Public Property](dotnetimages/publicProperty.gif)| [SenderRule](topic2790.md)| The rule for the sender segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [SubjectRule](topic2791.md)| The rule for the subject segment of the email.   
![Public Property](dotnetimages/publicProperty.gif)| [SupportsPreview](topic4396.md)| Gets whether the document supports generating a preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [TagsRule](topic2792.md)| The rule for a set of tags that are associated with this email.   
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic4390.md)| Gets/sets the custom data for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GenerateTestEmail](topic2775.md)| Generates and sends a test email.   
![Public Method](dotnetimages/publicMethod.gif)| [GetDetails](topic2776.md)| Gets all of the document information cached into an object that can be edited and commited to update this document.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetResults](topic2777.md)| Calculates the email's rules and returns the results   
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGenerate](topic2780.md)| Overloaded. Overridden. Determines whether the document should be generated.   
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGeneratePreview](topic4386.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRulesCore](topic4367.md)| Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [EvaluateRule](topic4371.md)| Evaluates the specified rule formula into a displayable string. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GenerateCore](topic2774.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GeneratePreviewCore](topic4377.md)| When overridden in a derived class, generates a preview of the document in the specified directory using the given calculated rule results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeExistingCore](topic2778.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeNewCore](topic2779.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic4397.md)| Raised when the document is deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic4398.md)| Raised when the document's name changes. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Email Class](topic2768.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
