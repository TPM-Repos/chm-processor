Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsCreatorPermitted Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationDetails Class](topic11292.md) : IsCreatorPermitted Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the creator of the specification is permitted to access it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property IsCreatorPermitted As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationDetails](topic11292.md)
    Dim value As Boolean
     
    instance.IsCreatorPermitted = value
     
    value = instance.IsCreatorPermitted  
  
C#|   
---|---  
      
    
    public bool IsCreatorPermitted {get; set;}  
  
# Remarks

In addition to team-based access control lists for specifications, specification flow allows the administrator to configure whether the owner/creator/everyone can see a specification in a given state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationDetails Class](topic11292.md)   
[SpecificationDetails Members](topic11293.md)


