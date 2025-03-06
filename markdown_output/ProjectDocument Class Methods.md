![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectDocument Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectDocument Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ProjectDocument members](topic4357.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4368.md)| Deletes the document from the project.   
Public Method| [Generate](topic4372.md)| Generates the document within the context of the active specification.   
Public Method| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [ShouldGenerate](topic4383.md)| Overloaded. Determines whether the document should be generated.   
Public Method| [ShouldGeneratePreview](topic4386.md)| Overloaded. Determines whether the document should be generated during preview.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized.   
Protected Method| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted.   
Protected Method| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document.   
Protected Method| [CalculateRulesCore](topic4367.md)| Calculates the results of the rules that have been defined for the document.   
Protected Method| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project.   
Protected Method| [EvaluateRule](topic4371.md)| Evaluates the specified rule into a displayable string.   
Protected Method| [GenerateCore](topic4373.md)| When overridden in a derived class, generates the document.   
Protected Method| [GeneratePreviewCore](topic4377.md)| When overridden in a derived class, generates a preview of the document in the specified directory using the given calculated rule results.   
Protected Method| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results.   
Protected Method| [InitializeExistingCore](topic4379.md)| When overridden in a derived class, performs initialization tasks relevant to an existing document, i.e. during project load.   
Protected Method| [InitializeNewCore](topic4380.md)| When overridden in a derived class, performs initialization tasks relevant to a newly created document.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification.   
Protected Method| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule.   
Protected Method| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[DriveWorks Namespace](topic2159.md)


