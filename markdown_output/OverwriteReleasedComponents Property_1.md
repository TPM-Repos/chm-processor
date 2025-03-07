Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OverwriteReleasedComponents Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseEnvironment Class](topic6379.md) : OverwriteReleasedComponents Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether, during the release of components, components that already exist are overwritten or used as-is. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property OverwriteReleasedComponents As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseEnvironment](topic6379.md)
    Dim value As Boolean
     
    instance.OverwriteReleasedComponents = value
     
    value = instance.OverwriteReleasedComponents  
  
C#|   
---|---  
      
    
    public bool OverwriteReleasedComponents {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseEnvironment Class](topic6379.md)   
[ReleaseEnvironment Members](topic6380.md)


