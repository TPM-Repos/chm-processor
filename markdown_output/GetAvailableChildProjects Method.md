Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAvailableChildProjects Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ChildSpecificationList Class](topic7547.md) : GetAvailableChildProjects Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the available projects that can be used to create child specifications for this definition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetAvailableChildProjects() As [ProjectDetails()](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ChildSpecificationList](topic7547.md)
    Dim value() As [ProjectDetails](topic4330.md)
     
    value = instance.GetAvailableChildProjects()  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [ProjectDetails[]](topic4330.md) GetAvailableChildProjects()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ChildSpecificationList Class](topic7547.md)   
[ChildSpecificationList Members](topic7548.md)


