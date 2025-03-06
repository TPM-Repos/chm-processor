       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4428.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRules Class](topic4413.md) : TryGetRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The identifier which uniquely identifies the rule to retrieve.

_rule_
    A reference to a variable which will receive the rule.

Glossary Item Box

Gets the rule with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetRule( _
       ByVal _ruleId_ As String, _
       ByRef _rule_ As [ProjectDocumentRule](topic4399.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRules](topic4413.md)
    Dim ruleId As String
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim value As Boolean
     
    value = instance.TryGetRule(ruleId, rule)  
  
C#|   
---|---  
      
    
    public bool TryGetRule( 
       string _ruleId_ ,
       ref [ProjectDocumentRule](topic4399.md) _rule_
    )  
  
#### Parameters

 _ruleId_
    The identifier which uniquely identifies the rule to retrieve.
_rule_
    A reference to a variable which will receive the rule.

#### Return Value

True if the rule is found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRules Class](topic4413.md)   
[ProjectDocumentRules Members](topic4414.md)

©2024 DriveWorks Ltd. All Rights Reserved.
