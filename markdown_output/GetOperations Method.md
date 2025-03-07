Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetOperations Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : GetOperations Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of transitions with the evaluated result of their conditions. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetOperations() As [AvailableOperation()](topic10787.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value() As [AvailableOperation](topic10787.md)
     
    value = instance.GetOperations()  
  
C#|   
---|---  
      
    
    public [AvailableOperation[]](topic10787.md) GetOperations()  
  
#### Return Value

An array of operations transitions.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


