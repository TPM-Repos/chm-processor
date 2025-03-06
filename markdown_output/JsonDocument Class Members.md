![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
JsonDocument Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3635.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : JsonDocument Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [JsonDocument](topic3635.md).

# ![](dotnetimages/collapse.gif)Public Constructors

| Name| Description  
---|---|---  
![Public Constructor](dotnetimages/publicConstructor.gif)| [JsonDocument Constructor](topic3641.md)| Creates a new instance of the [JsonDocument](topic3635.md) class.   
Top

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentNameRule](topic2881.md)| Gets/sets the name of the output file (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentNameValue](topic2882.md)| Gives the resolved name that this document will have. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentPathRule](topic2883.md)| Gets the rule which calculates the relative path for the document. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentPathValue](topic2884.md)| Gets the resolved path offset that this document will have (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentRootType](topic3656.md)| Gets/Sets the documents root type.   
![Public Property](dotnetimages/publicProperty.gif)| [HasDisplayFileRule](topic4391.md)| Gets whether the document has a display file rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4392.md)| Gets whether the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsHidden](topic2885.md)| Property to determine if the generated document is hidden from the end-user view. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsInitialized](topic4393.md)| Gets whether the document has been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsMinified](topic3657.md)| Gets whether the the generated output should be minified or have indented formatting.   
![Public Property](dotnetimages/publicProperty.gif)| [IsMinifiedRule](topic3658.md)| Gets the rule which calculates whether the generated document should be minified or have indented formatting.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4394.md)| Gets/sets the name of the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic4395.md)| Gets the project to which the document belongs. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SourceFilePath](topic2886.md)| Gets/sets the path to the master file. This is often a relative path. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SupportsPreview](topic4396.md)| Gets whether the document supports generating a preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic4390.md)| Gets/sets the custom data for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddNode](topic3642.md)| Overloaded. Adds a new node to the documents structure.   
![Public Method](dotnetimages/publicMethod.gif)| [CommitChanges](topic3646.md)| Commits any transient rule or node structure changes to the document.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetDocumentRuleIds](topic3649.md)| Returns a Dictionary of rule paths and respective Rule Id.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetProjectDocumentRule](topic3650.md)| Gets the [ProjectDocumentRule](topic4399.md) associated with this Id.   
![Public Method](dotnetimages/publicMethod.gif)| [GetRootNodeData](topic3651.md)| Gets the documents tree structure.   
![Public Method](dotnetimages/publicMethod.gif)| [GetRuleResults](topic3652.md)| Gets a Dictionary of all Rule Ids for this document and their evaluated result.   
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGenerate](topic2877.md)| Overloaded. Determines whether the document should be generated. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGeneratePreview](topic2879.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRulesCore](topic3645.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [EvaluateRule](topic4371.md)| Evaluates the specified rule formula into a displayable string. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GenerateCore](topic3647.md)| Overridden. Generates a new driven advanced xml document.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GeneratePreviewCore](topic3648.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeCommon](topic3653.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeExistingCore](topic3654.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeNewCore](topic3655.md)| Overridden.   
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

[JsonDocument Class](topic3635.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
