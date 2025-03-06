![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
JsonDocument Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : JsonDocument Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [JsonDocument members](topic3636.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [AddNode](topic3642.md)| Overloaded. Adds a new node to the documents structure.   
Public Method| [CommitChanges](topic3646.md)| Commits any transient rule or node structure changes to the document.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [GetDocumentRuleIds](topic3649.md)| Returns a Dictionary of rule paths and respective Rule Id.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetProjectDocumentRule](topic3650.md)| Gets the [ProjectDocumentRule](topic4399.md) associated with this Id.   
Public Method| [GetRootNodeData](topic3651.md)| Gets the documents tree structure.   
Public Method| [GetRuleResults](topic3652.md)| Gets a Dictionary of all Rule Ids for this document and their evaluated result.   
Public Method| [ShouldGenerate](topic2877.md)| Overloaded. Determines whether the document should be generated. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Public Method| [ShouldGeneratePreview](topic2879.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.FileDocumentBase](topic2870.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [CalculateRulesCore](topic3645.md)| Overridden.   
Protected Method| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [EvaluateRule](topic4371.md)| Evaluates the specified rule formula into a displayable string. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [GenerateCore](topic3647.md)| Overridden. Generates a new driven advanced xml document.   
Protected Method| [GeneratePreviewCore](topic3648.md)| Overridden.   
Protected Method| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [InitializeCommon](topic3653.md)| Overridden.   
Protected Method| [InitializeExistingCore](topic3654.md)| Overridden.   
Protected Method| [InitializeNewCore](topic3655.md)| Overridden.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JsonDocument Class](topic3635.md)   
[DriveWorks Namespace](topic2159.md)


