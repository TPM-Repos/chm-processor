Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
References Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [IParseResult Interface](topic10526.md) : References Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all of the reference nodes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property References As [IRuleNode()](topic10542.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IParseResult](topic10526.md)
    Dim value() As [IRuleNode](topic10542.md)
     
    value = instance.References  
  
C#|   
---|---  
      
    
    [IRuleNode[]](topic10542.md) References {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IParseResult Interface](topic10526.md)   
[IParseResult Members](topic10527.md)


