Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTransitions Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : GetTransitions Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of transitions with the evaluated result of their conditions. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTransitions() As [AvailableTransition()](topic10796.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value() As [AvailableTransition](topic10796.md)
     
    value = instance.GetTransitions()  
  
C#|   
---|---  
      
    
    public [AvailableTransition[]](topic10796.md) GetTransitions()  
  
#### Return Value

An array of invokable transitions.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


