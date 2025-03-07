Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CalculateRules() Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [CalculateRules Method](topic4364.md) : CalculateRules() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Calculates the results of the rules that have been defined for the document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overloads Function CalculateRules() As [RuleResults](topic11136.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim value As [RuleResults](topic11136.md)
     
    value = instance.CalculateRules()  
  
C#|   
---|---  
      
    
    protected [RuleResults](topic11136.md) CalculateRules()  
  
#### Return Value

An instance of the [DriveWorks.Specification.RuleResults](topic11136.md) type which has been populated with the rule results.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4364.md)


