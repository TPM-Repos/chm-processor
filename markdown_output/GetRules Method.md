Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRules Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : GetRules Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleIds_
    The Id's of the rules to retrieve.

Glossary Item Box

Retrieves the rules of the specified rule Id's. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetRules( _
       ByVal ParamArray _ruleIds_() As String _
    ) As [ProjectDocumentRule()](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim ruleIds() As String
    Dim value() As [ProjectDocumentRule](topic4399.md)
     
    value = instance.GetRules(ruleIds)  
  
C#|   
---|---  
      
    
    [ProjectDocumentRule[]](topic4399.md) GetRules( 
       params string[] _ruleIds_
    )  
  
#### Parameters

 _ruleIds_
    The Id's of the rules to retrieve.

#### Return Value

The rules stored with the specified rule Id's.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


