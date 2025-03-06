WordDocument Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5885.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : WordDocument Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [WordDocument](topic5885.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [CreateHtmlFile](topic5905.md)| Gets/sets if the document should be exported to HTML after it is generated.   
![Public Property](dotnetimages/publicProperty.gif)| [CreatePdfFile](topic5906.md)| Gets/sets if the document should be exported to PDF after it is generated.   
![Public Property](dotnetimages/publicProperty.gif)| [DocumentNameRule](topic2881.md)| Gets/sets the name of the output file (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentNameValue](topic2882.md)| Gives the resolved name that this document will have. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentPathRule](topic2883.md)| Gets the rule which calculates the relative path for the document. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DocumentPathValue](topic2884.md)| Gets the resolved path offset that this document will have (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [HasDisplayFileRule](topic4391.md)| Gets whether the document has a display file rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [HideHtmlFile](topic5907.md)| Gets/sets if generated HTML files should be hidden from the specification's documents list.   
![Public Property](dotnetimages/publicProperty.gif)| [HidePdfFile](topic5908.md)| Gets/sets if generated PDF files should be hidden from the specification's documents list.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4392.md)| Gets whether the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsHidden](topic2885.md)| Property to determine if the generated document is hidden from the end-user view. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsInitialized](topic4393.md)| Gets whether the document has been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4394.md)| Gets/sets the name of the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic4395.md)| Gets the project to which the document belongs. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SourceFilePath](topic2886.md)| Gets/sets the path to the master file. This is often a relative path. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SupportsPreview](topic4396.md)| Gets whether the document supports generating a preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic4390.md)| Gets/sets the custom data for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [ClearRanges](topic5891.md)| Removes all bookmarks from the list of ranges to be driven.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetRange](topic5894.md)| Get the rule for a driven bookmark.   
Public Method| [GetRangeNames](topic5895.md)| Gets a list of all the driven ranges names.   
Public Method| [GetRangeValues](topic5896.md)| Gets all the ranges resolved values.   
Public Method| [LoadRangesFromFile](topic5899.md)| Matches range information with ranges from file. Creates missing ranges and removes unused ones.   
Public Method| [RangeExists](topic5900.md)| Sees if a given driven bookmark exists with a specific name.   
Public Method| [RemoveRange](topic5901.md)| Removes a bookmark from the list of ranges to be driven.   
Public Method| [SetRange](topic5902.md)| Overloaded. Sets/adds a bookmark to be driven.   
Public Method| [ShouldGenerate](topic2877.md)| Overloaded. Determines whether the document should be generated. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Public Method| [ShouldGeneratePreview](topic2879.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [CalculateRulesCore](topic4367.md)| Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [EvaluateRule](topic4371.md)| Evaluates the specified rule formula into a displayable string. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [GenerateCore](topic5892.md)| Overridden.   
Protected Method| [GeneratePreviewCore](topic5893.md)| Overridden.   
Protected Method| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [InitializeCommon](topic2876.md)|  (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Protected Method| [InitializeExistingCore](topic5897.md)| Overridden.   
Protected Method| [InitializeNewCore](topic5898.md)| Overridden.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic4397.md)| Raised when the document is deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic4398.md)| Raised when the document's name changes. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[DriveWorks Namespace](topic2159.md)


