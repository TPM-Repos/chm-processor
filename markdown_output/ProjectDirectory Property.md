Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectDirectory Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : ProjectDirectory Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the fully-qualified path to the directory containing the project on which the specification is based. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ProjectDirectory As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.ProjectDirectory  
  
C#|   
---|---  
      
    
    public string ProjectDirectory {get;}  
  
#### Property Value

The fully-qualified path, or a null reference if the specification context is not loaded.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


