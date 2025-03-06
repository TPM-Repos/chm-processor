![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemData Constructor(String,ImageHandle,Object)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1161.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemData Class](topic1154.md) > [VirtualItemData Constructor](topic1160.md) : VirtualItemData Constructor(String,ImageHandle,Object)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The localized title of the item.

_imageHandle_
    A handle to an image which will be shown with the item.

_tag_
    A tag which can be used to store additional data.

Glossary Item Box

Initializes a new instance of the [VirtualItemData](topic1154.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _title_ As String, _
       ByVal _imageHandle_ As [ImageHandle](topic854.md), _
       ByVal _tag_ As Object _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim title As String
    Dim imageHandle As [ImageHandle](topic854.md)
    Dim tag As Object
     
    Dim instance As New [VirtualItemData](topic1154.md)(title, imageHandle, tag)  
  
C#|   
---|---  
      
    
    public VirtualItemData( 
       string _title_ ,
       [ImageHandle](topic854.md) _imageHandle_ ,
       object _tag_
    )  
  
#### Parameters

 _title_
    The localized title of the item.
_imageHandle_
    A handle to an image which will be shown with the item.
_tag_
    A tag which can be used to store additional data.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[VirtualItemData Class](topic1154.md)   
[VirtualItemData Members](topic1155.md)   
[Overload List](topic1160.md)

©2024 DriveWorks Ltd. All Rights Reserved.
