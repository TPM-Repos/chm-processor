![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetPreviewResource(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7293.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewResourceHandler Interface](topic7286.md) > [GetPreviewResource Method](topic7292.md) : GetPreviewResource(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The name of the resource to fetch.

Glossary Item Box

Attempts to get a resource from the preview object. This is typically for fetching model data in a JSON format or an image binary. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetPreviewResource( _
       ByVal _key_ As String _
    ) As Task(Of Stream)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPreviewResourceHandler](topic7286.md)
    Dim key As String
    Dim value As Task(Of Stream)
     
    value = instance.GetPreviewResource(key)  
  
C#|   
---|---  
      
    
    Task<Stream> GetPreviewResource( 
       string _key_
    )  
  
#### Parameters

 _key_
    The name of the resource to fetch.

#### Return Value

A stream to the resource or null if nothing was found.

# ![](dotnetimages/collapse.gif)Remarks

The result will be cached if it was a fresh result, and if [EagerLoadResources](topic7291.md) has been called then other new resources will begin loading too.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewResourceHandler Interface](topic7286.md)   
[IPreviewResourceHandler Members](topic7287.md)   
[Overload List](topic7292.md)

©2024 DriveWorks Ltd. All Rights Reserved.
