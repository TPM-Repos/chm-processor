Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Hidden Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDetails Class](topic4330.md) : Hidden Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the project is hidden from the list of projects that can be specified. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Hidden As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDetails](topic4330.md)
    Dim value As Boolean
     
    instance.Hidden = value
     
    value = instance.Hidden  
  
C#|   
---|---  
      
    
    public bool Hidden {get; set;}  
  
# Remarks

If a project is hidden, it is not displayed in the list of projects that can be specified, but will still be shown in the list of projects that can be specified for a child specification if explicitly chosen.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDetails Class](topic4330.md)   
[ProjectDetails Members](topic4331.md)


