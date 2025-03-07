Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AllocateSpecificationId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : AllocateSpecificationId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Allocates a specification identifier to the specification, by default, uses the next specification identifier from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function AllocateSpecificationId() As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As Integer
     
    value = instance.AllocateSpecificationId()  
  
C#|   
---|---  
      
    
    protected virtual int AllocateSpecificationId()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


