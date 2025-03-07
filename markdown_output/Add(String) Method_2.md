Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRules Class](topic4413.md) > [Add Method](topic4419.md) : Add(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The identifier to give to the rule.

Glossary Item Box

Creates and returns a new rule with a given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _ruleId_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRules](topic4413.md)
    Dim ruleId As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.Add(ruleId)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) Add( 
       string _ruleId_
    )  
  
#### Parameters

 _ruleId_
    The identifier to give to the rule.

#### Return Value

An instance of the [ProjectDocumentRule](topic4399.md) type which provides access to the newly created rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRules Class](topic4413.md)   
[ProjectDocumentRules Members](topic4414.md)   
[Overload List](topic4419.md)


