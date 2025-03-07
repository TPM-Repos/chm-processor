Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjects() Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [GetProjects Method](topic3212.md) : GetProjects() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all registered projects whether or not the logged-on user has access. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetProjects() As [ProjectDetails()](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim value() As [ProjectDetails](topic4330.md)
     
    value = instance.GetProjects()  
  
C#|   
---|---  
      
    
    public [ProjectDetails[]](topic4330.md) GetProjects()  
  
# Remarks

This method will return a project even if the current user doesn't have access to the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3212.md)


