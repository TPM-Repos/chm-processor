![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SupportsEmbedChildSpecifications Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4898.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationSettings Class](topic4885.md) : SupportsEmbedChildSpecifications Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether this project supports embedded child specifications or not. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property SupportsEmbedChildSpecifications As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationSettings](topic4885.md)
    Dim value As Boolean
     
    value = instance.SupportsEmbedChildSpecifications  
  
C#|   
---|---  
      
    
    public bool SupportsEmbedChildSpecifications {get;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This is based off of the project type. E.g. Excel based projects do not support embedded child specifications.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectSpecificationSettings Class](topic4885.md)   
[ProjectSpecificationSettings Members](topic4886.md)

©2024 DriveWorks Ltd. All Rights Reserved.
