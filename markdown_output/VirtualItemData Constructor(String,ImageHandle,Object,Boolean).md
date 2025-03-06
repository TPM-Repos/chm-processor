VirtualItemData Constructor(String,ImageHandle,Object,Boolean)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemData Class](topic1154.md) > [VirtualItemData Constructor](topic1160.md) : VirtualItemData Constructor(String,ImageHandle,Object,Boolean)  
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

_shouldHighlight_
    Whether or not to highlight this item in the list.

Glossary Item Box

Initializes a new instance of the [VirtualItemData](topic1154.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _title_ As String, _
       ByVal _imageHandle_ As [ImageHandle](topic854.md), _
       ByVal _tag_ As Object, _
       ByVal _shouldHighlight_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim title As String
    Dim imageHandle As [ImageHandle](topic854.md)
    Dim tag As Object
    Dim shouldHighlight As Boolean
     
    Dim instance As New [VirtualItemData](topic1154.md)(title, imageHandle, tag, shouldHighlight)  
  
C#|   
---|---  
      
    
    public VirtualItemData( 
       string _title_ ,
       [ImageHandle](topic854.md) _imageHandle_ ,
       object _tag_ ,
       bool _shouldHighlight_
    )  
  
#### Parameters

 _title_
    The localized title of the item.
_imageHandle_
    A handle to an image which will be shown with the item.
_tag_
    A tag which can be used to store additional data.
_shouldHighlight_
    Whether or not to highlight this item in the list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemData Class](topic1154.md)   
[VirtualItemData Members](topic1155.md)   
[Overload List](topic1160.md)


