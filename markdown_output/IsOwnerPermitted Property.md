Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsOwnerPermitted Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationDetails Class](topic11292.md) : IsOwnerPermitted Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the owner of the specification is permitted to access it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property IsOwnerPermitted As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationDetails](topic11292.md)
    Dim value As Boolean
     
    instance.IsOwnerPermitted = value
     
    value = instance.IsOwnerPermitted  
  
C#|   
---|---  
      
    
    public bool IsOwnerPermitted {get; set;}  
  
# Remarks

In addition to team-based access control lists for specifications, specification flow allows the administrator to configure whether the owner/creator/everyone can see a specification in a given state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationDetails Class](topic11292.md)   
[SpecificationDetails Members](topic11293.md)


