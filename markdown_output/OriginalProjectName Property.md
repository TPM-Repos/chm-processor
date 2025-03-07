Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OriginalProjectName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationDetails Class](topic11292.md) : OriginalProjectName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the name of the project that created the specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property OriginalProjectName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationDetails](topic11292.md)
    Dim value As String
     
    value = instance.OriginalProjectName  
  
C#|   
---|---  
      
    
    public string OriginalProjectName {get;}  
  
# Remarks

The name of the project that is returned is the name of the project as it was when the specification was created, so if the project is renamed, the original project name is the unchanged.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationDetails Class](topic11292.md)   
[SpecificationDetails Members](topic11293.md)


