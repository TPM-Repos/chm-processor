Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ReferencedFile Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ReferencedFile Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ReferencedFile members](topic5047.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [ShouldGenerate](topic5055.md)| Overloaded. Overridden. Determines whether the document should be generated.   
Public Method| [ShouldGeneratePreview](topic4386.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
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
Protected Method| [GenerateCore](topic5052.md)| Overridden. When overridden in a derived class, generates the document.   
Protected Method| [GeneratePreviewCore](topic4377.md)| When overridden in a derived class, generates a preview of the document in the specified directory using the given calculated rule results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [InitializeExistingCore](topic5053.md)| Overridden. When overridden in a derived class, performs initialization tasks relevant to an existing document, i.e. during project load.   
Protected Method| [InitializeNewCore](topic5054.md)| Overridden. When overridden in a derived class, performs initialization tasks relevant to a newly created document.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Protected Method| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# See Also

#### Reference

[ReferencedFile Class](topic5046.md)   
[DriveWorks Namespace](topic2159.md)


