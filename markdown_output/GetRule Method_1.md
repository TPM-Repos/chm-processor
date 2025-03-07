Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRules Class](topic4413.md) : GetRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The identifier which uniquely identifies the rule to retrieve.

Glossary Item Box

Gets the rule with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRule( _
       ByVal _ruleId_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRules](topic4413.md)
    Dim ruleId As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.GetRule(ruleId)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) GetRule( 
       string _ruleId_
    )  
  
#### Parameters

 _ruleId_
    The identifier which uniquely identifies the rule to retrieve.

#### Return Value

The rule with the specified unique identifier.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if the specified rule does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRules Class](topic4413.md)   
[ProjectDocumentRules Members](topic4414.md)


