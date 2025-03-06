![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EmbedChildSpecifications Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4894.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationSettings Class](topic4885.md) : EmbedChildSpecifications Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether child specifications should be saved within this project, rather than being saved to their own directory and being registered as it's own specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property EmbedChildSpecifications As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationSettings](topic4885.md)
    Dim value As Boolean
     
    instance.EmbedChildSpecifications = value
     
    value = instance.EmbedChildSpecifications  
  
C#|   
---|---  
      
    
    public bool EmbedChildSpecifications {get; set;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This setting only applies if this is the root project and can only be set on .driveprojx projects.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectSpecificationSettings Class](topic4885.md)   
[ProjectSpecificationSettings Members](topic4886.md)

©2024 DriveWorks Ltd. All Rights Reserved.
