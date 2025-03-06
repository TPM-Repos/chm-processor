![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvalidateResource Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7295.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewResourceHandler Interface](topic7286.md) : InvalidateResource Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_resourceName_
    The name of the scene resource.

Glossary Item Box

Invalidates the resource in the event it is changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InvalidateResource( _
       ByVal _resourceName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPreviewResourceHandler](topic7286.md)
    Dim resourceName As String
     
    instance.InvalidateResource(resourceName)  
  
C#|   
---|---  
      
    
    void InvalidateResource( 
       string _resourceName_
    )  
  
#### Parameters

 _resourceName_
    The name of the scene resource.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewResourceHandler Interface](topic7286.md)   
[IPreviewResourceHandler Members](topic7287.md)

©2024 DriveWorks Ltd. All Rights Reserved.
