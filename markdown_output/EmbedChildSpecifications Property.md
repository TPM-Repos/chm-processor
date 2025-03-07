Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EmbedChildSpecifications Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationSettings Class](topic4885.md) : EmbedChildSpecifications Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether child specifications should be saved within this project, rather than being saved to their own directory and being registered as it's own specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property EmbedChildSpecifications As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationSettings](topic4885.md)
    Dim value As Boolean
     
    instance.EmbedChildSpecifications = value
     
    value = instance.EmbedChildSpecifications  
  
C#|   
---|---  
      
    
    public bool EmbedChildSpecifications {get; set;}  
  
# Remarks

This setting only applies if this is the root project and can only be set on .driveprojx projects.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationSettings Class](topic4885.md)   
[ProjectSpecificationSettings Members](topic4886.md)


