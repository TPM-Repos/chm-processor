Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Deployed Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDetails Class](topic4330.md) : Deployed Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the project is deployed so that it can be used by ordinary users. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Deployed As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDetails](topic4330.md)
    Dim value As Boolean
     
    instance.Deployed = value
     
    value = instance.Deployed  
  
C#|   
---|---  
      
    
    public bool Deployed {get; set;}  
  
# Remarks

If a project is not deployed, only administrative users can see and specify the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDetails Class](topic4330.md)   
[ProjectDetails Members](topic4331.md)


