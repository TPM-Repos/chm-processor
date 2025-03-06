Remove Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRules Class](topic4413.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The unique identifier of the rule to remove.

Glossary Item Box

Removes the rule with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _ruleId_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRules](topic4413.md)
    Dim ruleId As String
    Dim value As Boolean
     
    value = instance.Remove(ruleId)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       string _ruleId_
    )  
  
#### Parameters

 _ruleId_
    The unique identifier of the rule to remove.

#### Return Value

True if a rule with the specified identifier was found and removed, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRules Class](topic4413.md)   
[ProjectDocumentRules Members](topic4414.md)


