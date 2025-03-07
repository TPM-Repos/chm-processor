Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Errors Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [IParseResult Interface](topic10526.md) : Errors Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all the error nodes found in the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Errors As [IRuleError()](topic10534.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IParseResult](topic10526.md)
    Dim value() As [IRuleError](topic10534.md)
     
    value = instance.Errors  
  
C#|   
---|---  
      
    
    [IRuleError[]](topic10534.md) Errors {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IParseResult Interface](topic10526.md)   
[IParseResult Members](topic10527.md)


